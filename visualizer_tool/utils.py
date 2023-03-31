import numpy as np

from django.apps import apps

from .models import *
from .plot_utils import *

class DataHandler:

    def get_group_selected(self, group_model, fofid, snapnum):
        result = group_model.objects.filter(fofid=fofid, snapnum=snapnum).values('m200','r200', 'cop_x', 'cop_y', 'cop_z')
        return result
    
    def get_subgroup_selected(self, subgroup_model, fofid, subid, snapnum):
        result = subgroup_model.objects.filter(fofid=fofid, subid=subid, snapnum=snapnum).values('cop_x', 'cop_y', 'cop_z')
        return result

#<------------------------------------------------------------------------------->#

    def get_particle_selected(self, snap_model, ptype, fofid):
        if ptype.upper() == 'DM':
            pdata = snap_model.objects.filter(fofid=fofid).values_list('cop_x', 'cop_y', 'cop_z')
            cols  = ['cop_x', 'cop_y', 'cop_z']
        elif ptype.upper() == 'GAS':
            pdata = snap_model.objects.filter(fofid=fofid).values_list('cop_x', 'cop_y', 'cop_z', 'mass', 'hsml')
            cols = ['cop_x', 'cop_y', 'cop_z', 'mass', 'hsml']
        elif ptype.upper() == 'STAR':
            pdata = snap_model.objects.filter(fofid=fofid).values_list('cop_x', 'cop_y', 'cop_z', 'mass')
            cols = ['cop_x', 'cop_y', 'cop_z', 'mass']
        else:
            print('Unregonized ptype')

        return pdata, cols


#<------------------------------------------------------------------------------->#

    def get_particle_selected_both(self, snap_model, ptype, fofid, subid):
        if ptype.upper() == 'DM':
            pdata = snap_model.objects.filter(fofid=fofid, subid=subid).values_list('cop_x', 'cop_y', 'cop_z')
            cols  = ['cop_x', 'cop_y', 'cop_z']
        elif ptype.upper() == 'GAS':
            pdata = snap_model.objects.filter(fofid=fofid, subid=subid).values_list('cop_x', 'cop_y', 'cop_z', 'mass', 'hsml')
            cols = ['cop_x', 'cop_y', 'cop_z', 'mass', 'hsml']
        elif ptype.upper() == 'STAR':
            pdata = snap_model.objects.filter(fofid=fofid, subid=subid).values_list('cop_x', 'cop_y', 'cop_z', 'mass')
            cols = ['cop_x', 'cop_y', 'cop_z', 'mass']
        else:
            print('Unregonized ptype')

        return pdata, cols


#<------------------------------------------------------------------------------->#

    def get_particle_all(self, snap_model, ptype, center, extent):

        x1 = center[0] - extent
        x2 = center[0] + extent

        y1 = center[1] - extent
        y2 = center[1] + extent

        z1 = center[2] - extent
        z2 = center[2] + extent

        if ptype.upper() == 'DM':
            pdata = snap_model.objects.filter(cop_x__gt=x1, cop_x__lt=x2, cop_y__gt=y1, cop_y__lt=y2, cop_z__gt=z1, cop_z__lt=z2).values_list('cop_x', 'cop_y', 'cop_z')
            cols  = ['cop_x', 'cop_y', 'cop_z']
        elif ptype.upper() == 'GAS':
            pdata = snap_model.objects.filter(cop_x__gt=x1, cop_x__lt=x2, cop_y__gt=y1, cop_y__lt=y2, cop_z__gt=z1, cop_z__lt=z2).values_list('cop_x', 'cop_y', 'cop_z', 'mass', 'hsml')
            cols = ['cop_x', 'cop_y', 'cop_z', 'mass', 'hsml']
        elif ptype.upper() == 'STAR':
            pdata = snap_model.objects.filter(cop_x__gt=x1, cop_x__lt=x2, cop_y__gt=y1, cop_y__lt=y2, cop_z__gt=z1, cop_z__lt=z2).values_list('cop_x', 'cop_y', 'cop_z', 'mass')
            cols = ['cop_x', 'cop_y', 'cop_z', 'mass']
        else:
            print('Unregonized ptype')

        return pdata, cols


#<------------------------------------------------------------------------------->#

    def find_center(self, grpdata, subgrpdata, form):
        '''
        find coordinates of Halo/Subhalo on which to center the plot
        '''
        if form['subgrpid'] == "":
            grpdata_list = list(grpdata)
            center = np.array([grpdata_list[0]['cop_x'], subgrpdata_list[0]['cop_y'], subgrpdata_list[0]['cop_z']])
            grpdata_list = None
        elif form['subgrpid'] >= 0:
            subgrpdata_list = list(subgrpdata)
            center = np.array([subgrpdata_list[0]['cop_x'], subgrpdata_list[0]['cop_y'], subgrpdata_list[0]['cop_z']])
            subgrpdata_list = None
        else:
            print('invalid SUBGROUP? ERROR AT FINDING CENTER')
            center = np.array([0, 0, 0])

        return center
    
    def find_extent(self, grpdata, form):
        '''
        find the distance from center which will be included in the plot
        '''
        if form['boxsizeunit'] == 'RVir' and form['subgrpid'] >= 0:
            print('Invalid units. SubHalos don\'t have virial radius.')
            unit = grpdata[0]['r200'] #units of Mpc
        elif form['boxsizeunit'] == 'RVir' and form['subgrpid'] == '':
            unit = grpdata[0]['r200'] #units of Mpc
        elif form['boxsizeunit'] == 'Mpc':
            unit = 1
        elif form['boxsizeunit'] == 'kpc':
            unit = 1/1000
        else:
            print('Unrecognized value of Units of Box Size')
            unit = 1

        return form['boxsize'] * unit

#<------------------------------------------------------------------------------->#

    def find_snaps_to_plot(self, form):

        snap_0     = form['snapnum']
        snap_init  = form['snapinit']
        snap_final = form['snapfinal']

        #snap_range = range(snap_init, snap_final+1)

        subgrp_model = apps.get_model('visualizer_tool', 'SUBGROUP_{}_{}'.format(form['vol'].upper(), 
                                                                                 form['res'].upper()))
        
        tree_model   = apps.get_model('visualizer_tool', 'MERGERTABLE_{}_{}'.format(form['vol'].upper(), 
                                                                                    form['res'].upper()))

        try:
            subgroups = subgrp_model.objects.filter(snapnum=snap_0, fofid=form['grpid'], subid=form['subgrpid']).values_list('subfid')
            subf_id_0 = list(subgroups)[0][0]
        except ValueError:
            print('This object is not a valid SubHalo')
            return None
            
        try:
            tree_0 = tree_model.objects.filter(subfid=subf_id_0, snapnum=snap_0).values_list('progid',
                                                                                                'nodeid',
                                                                                                    'descid')
            prog_id_0, node_id_0, desc_id_0 = list(tree_0)[0]
        except ValueError:
            print('This object does not exist in the merger tree')
            return None

        
        prog_id_list    = []
        desc_id_list    = []

        snap_prog_list = []
        snap_desc_list = []
        
        if snap_final > snap_0:
            '''
            FINDING ALL DESCENDENTS:
            identify subf_id via the subgroups table of our subhalo in snap_0
            match desc_id to node_id of snap_0 + 1
            make list of snap_num, subf_id
            '''

            snap_desc_range = np.arange(snap_0+1, snap_final+1,1)
            node_look_for = desc_id_0
            for snap_iter in snap_desc_range:
                
                if node_look_for == -1:
                    break
                
                try:
                    temp_query = tree_model.objects.filter(nodeid=node_look_for, snapnum=snap_iter).values_list('descid', 'subfid')
                    node_look_for, new_subfid = list(temp_query)[0]

                    desc_id_list.append(new_subfid)
                    snap_desc_list.append(snap_iter)
                except IndexError:
                    break


            pass
        elif snap_final == snap_0:
            pass
        else:
            print('Invalid SNAPFINAL')

        if snap_init < snap_0:
            '''
            FINDING ALL PROGENITORS:
            identify subf_id via the subgroups table of our subhalo in snap_0
            match id_main_prog to node_id of snap_0 - 1
            make list of snap_num, subf_id
            '''

            snap_prog_range = np.arange(snap_0-1, snap_init-1, -1).astype(int)
            node_look_for   = prog_id_0
            for snap_iter in snap_prog_range:
                
                if node_look_for == -1:
                    break
                
                try:
                    temp_query = tree_model.objects.filter(nodeid=node_look_for, snapnum=snap_iter).values_list('progid', 'subfid')
                    node_look_for, new_subfid = list(temp_query)[0]

                    prog_id_list.append(new_subfid)
                    snap_prog_list.append(snap_iter)
                except IndexError:
                    break

            
            snap_prog_list = snap_prog_list[::-1]
            prog_id_list   = prog_id_list[::-1]

        elif snap_init == snap_0:
            pass
        else:
            print('Invalid SNAPINIT')
        
        temp_query = None

        final_snap_list  = list(snap_prog_list) + [snap_0] + list(snap_desc_list)
        final_subid_list = list(prog_id_list) + [subf_id_0] + list(desc_id_list)


        grpid_list    = []
        subgrpid_list = []
        snap_list     = []
        for snap_iter, subid_iter in zip(final_snap_list, final_subid_list):
            try:
                temp_query = subgrp_model.objects.filter(snapnum=snap_iter, subfid=subid_iter).values_list('fofid', 'subid')
                grp_t,subgrp_t = list(temp_query)[0]

                grpid_list.append(grp_t)
                subgrpid_list.append(subgrp_t)
                snap_list.append(snap_iter)
            except:
                pass
                #print(snap_iter, subid_iter, len(temp_query))
                #break

        return grpid_list, subgrpid_list, final_snap_list
    
#<------------------------------------------------------------------------------->#

    def make_single_plot(self, form):
        
        grp_model    = apps.get_model('visualizer_tool', 'GROUP_{}_{}'.format(form['vol'].upper(),
                                                                               form['res'].upper()))
        subgrp_model = apps.get_model('visualizer_tool', 'SUBGROUP_{}_{}'.format(form['vol'].upper(), 
                                                                                 form['res'].upper()))
        snap_model   = apps.get_model('visualizer_tool', 'SNAP_{}_{}_{}_{}'.format(form['vol'].upper(),
                                                                           form['res'].upper(),
                                                                           form['ptype'].upper(),
                                                                           form['snapnum']))

        grpdata    = self.get_group_selected(grp_model, form['grpid'], form['snapnum'])
        subgrpdata = self.get_subgroup_selected(subgrp_model, form['grpid'], form['subgrpid'], form['snapnum'])

        center     = self.find_center(grpdata, subgrpdata, form)
        extent     = self.find_extent(grpdata, form)

        if form['showwhich'].upper() == 'GROUP':
            pdata, cols_name = self.get_particle_selected(snap_model, form['ptype'], form['grpid'])
            pdata = np.asarray(pdata)

        elif form['showwhich'].upper() == 'SUBGROUP':
            pdata, cols_name = self.get_particle_selected_both(snap_model, form['ptype'], form['grpid'], form['subgrpid'])
            pdata = np.asarray(pdata)

        elif form['showwhich'].upper() == 'ALL':
            pdata, cols_name = self.get_particle_all(snap_model, form['ptype'], center, extent * np.sqrt(2))
            pdata = np.asarray(pdata)


        xyz = np.array([pdata[:,0], pdata[:,1], pdata[:,2]])

        xyz_g = np.copy(xyz)

        # if form['showwhich'] == 'SubGroup' and form['ptype'] == 'Gas':
        #     xyz_g = xyz
        # else:
        #     pdata_g, cols_name = self.get_particle_selected_both(form['ptype'], form['grpid'], form['subgrpid'])
        #     pdata_g = np.asarray(pdata_g)

        #     xyz_g = np.array([pdata_g[:,0], pdata_g[:,1], pdata_g[:,2]])



        R_matrix = None
        center, xyz, R_matrix = align_data(center, xyz_g, xyz, R_matrix)

        if form['ptype'].upper() == 'GAS':
            other_inputs = [pdata[:,3], pdata[:,4]]
        elif form['ptype'].upper() == 'STAR':
            other_inputs = [pdata[:,3], np.ones(len(pdata[:,0]))*.0001]
        elif form['ptype'].upper() == 'DM':
            other_inputs = [np.zeros(len(pdata[:,0]))+10, np.empty(0)]
        else:
            print('invalid ptype..')

        if form['orien'].upper() == 'FACE-ON':
            img, cmap = plot_sph(extent, roll=0, p=0, t=0, 
                                center=center, 
                                xyz=xyz, 
                                other_inputs=other_inputs, 
                                ptype=form['ptype'])
            
        elif form['orien'].upper() == 'EDGE-ON':
            img, cmap = plot_sph(extent, roll=90, p=0, t=0, 
                            center=center, 
                            xyz=xyz, 
                            other_inputs=other_inputs, 
                            ptype=form['ptype'])

        else:
            print('Unexpected Orientation')

        animation_frame = None
        context = make_context(self, img, form['zmin'], form['zmax'], cmap, animation_frame)

        return context
    

#<------------------------------------------------------------------------------->#
#<------------------------------------------------------------------------------->#

    def make_timelapse_plot(self, form, timelapse_list):
        
        grp_list, subgrp_list, snap_list = timelapse_list[0], timelapse_list[1], timelapse_list[2]


        grp_model    = apps.get_model('visualizer_tool', 'GROUP_{}_{}'.format(form['vol'].upper(),
                                                                               form['res'].upper()))
        subgrp_model = apps.get_model('visualizer_tool', 'SUBGROUP_{}_{}'.format(form['vol'].upper(), 
                                                                                 form['res'].upper()))
        
        R_matrix = None

        for grpid, subgrpid, snapnum in zip(grp_list, subgrp_list, snap_list):

            snap_model   = apps.get_model('visualizer_tool', 'SNAP_{}_{}_{}_{}'.format(form['vol'].upper(),
                                                                            form['res'].upper(),
                                                                            form['ptype'].upper(),
                                                                            snapnum))

            grpdata    = self.get_group_selected(grp_model, grpid, snapnum)
            subgrpdata = self.get_subgroup_selected(subgrp_model, grpid, subgrpid, snapnum)

            center     = self.find_center(grpdata, subgrpdata, form)
            extent     = self.find_extent(grpdata, form)

            if form['showwhich'].upper() == 'GROUP':
                pdata, cols_name = self.get_particle_selected(snap_model, form['ptype'], grpid)
                pdata = np.asarray(pdata)

            elif form['showwhich'].upper() == 'SUBGROUP':
                pdata, cols_name = self.get_particle_selected_both(snap_model, form['ptype'], grpid, subgrpid)
                pdata = np.asarray(pdata)

            elif form['showwhich'].upper() == 'ALL':
                pdata, cols_name = self.get_particle_all(snap_model, form['ptype'], center, extent * np.sqrt(2))
                pdata = np.asarray(pdata)


            xyz = np.array([pdata[:,0], pdata[:,1], pdata[:,2]])

            xyz_g = np.copy(xyz)

            # if form['showwhich'] == 'SubGroup' and form['ptype'] == 'Gas':
            #     xyz_g = xyz
            # else:
            #     pdata_g, cols_name = self.get_particle_selected_both(form['ptype'], form['grpid'], form['subgrpid'])
            #     pdata_g = np.asarray(pdata_g)

            #     xyz_g = np.array([pdata_g[:,0], pdata_g[:,1], pdata_g[:,2]])

            try:
                R_matrix[0]
                center, xyz, _        = align_data(center, xyz_g, xyz, R_matrix)
                _ = None
            except:
                center, xyz, R_matrix = align_data(center, xyz_g, xyz, R_matrix)
                
            
            if form['ptype'].upper() == 'GAS':
                other_inputs = [pdata[:,3], pdata[:,4]]
            elif form['ptype'].upper() == 'STAR':
                other_inputs = [pdata[:,3], np.ones(len(pdata[:,0]))*.0001]
            elif form['ptype'].upper() == 'DM':
                other_inputs = [np.zeros(len(pdata[:,0]))+10, np.empty(0)]
            else:
                print('invalid ptype..')

            if form['orien'].upper() == 'FACE-ON':
                img_frame, cmap = plot_sph(extent, roll=0, p=0, t=0, 
                                center=center, 
                                xyz=xyz, 
                                other_inputs=other_inputs, 
                                ptype=form['ptype'])
                
            elif form['orien'].upper() == 'EDGE-ON':
                img_frame, cmap = plot_sph(extent, roll=90, p=0, t=0, 
                            center=center, 
                            xyz=xyz, 
                            other_inputs=other_inputs, 
                            ptype=form['ptype'])
            else:
                print('Unexpected Orientation')

            try:
                n = len(img_frame)
                print(n)
                img_stack = np.concatenate( (img_stack, img_frame.reshape(1,n,n)), axis=0)
            except:
                n = len(img_frame)
                print(n)
                img_stack = img_frame.reshape(1,n,n)

        animation_frame = 0
        context = make_context(self, img_stack, form['zmin'], form['zmax'], cmap, animation_frame)

        return context


#<------------------------------------------------------------------------------->#

    def plot_main(self, form):
        '''
        Landing function for Data Handler.
        Decides which snapshots to plot.
        '''
        
        if form['timelapse_flag'] == False:
            context = self.make_single_plot(form)
        else:
            '''
            identify snapshots to plot
            find FOFID, SUBID, SNAPNUM of PROG and DESC within SNAPINIT SNAPFINAL
            '''

            timelapse_list = self.find_snaps_to_plot(form)

            context = self.make_timelapse_plot(form, timelapse_list)

            pass

        return context