import sphviewer
from sphviewer.tools import QuickView
from sphviewer.tools import cmaps

import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.patches as patches
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

from scipy.optimize import leastsq
from scipy.spatial.transform import Rotation

from matplotlib import cm
from matplotlib.colors import LogNorm

from plotly.offline import plot
import plotly.express as px

import numpy as np

def align_data(ctr_midpoint, xyz_g, xyz, R_matrix):
    
    try:
        R_matrix[0]
    
    except:

        sol, n_norm = find_plane(xyz_g.T)

        n_prep  = np.array([0,0,1])
        v_x     = np.cross(n_prep, n_norm)
        sin_the = np.linalg.norm(v_x)
        cos_the = np.dot(n_prep, n_norm)

        V_x = np.matrix([[ 0     , -v_x[2],  v_x[1]],
                        [ v_x[2], 0      , -v_x[0]],
                        [-v_x[1], v_x[0] ,  0     ]])

        R_matrix = np.identity(3) + V_x + V_x**2 * (1-cos_the)/sin_the**2
        R_matrix = R_matrix.T

    ctr_mdp_rot = np.asarray(np.dot(R_matrix, ctr_midpoint.T))[0]

    xyz_rot  = np.asarray(np.dot(R_matrix, xyz))

    return ctr_mdp_rot, xyz_rot, R_matrix


#<------------------------------------------------------------------------------->#

def plot_sph(ext, roll, p, t, center, xyz, other_inputs, ptype):
    ##plotting

    print('running plotting routine')

    extent = [-ext,ext,-ext,ext]
    x_res  = 500
    y_res  = x_res
    r      = 'infinity'
    
    r_matrix_x           = np.matrix(Rotation.from_rotvec(np.deg2rad([roll,0,0])).as_dcm())
    r_matrix_y           = np.matrix(Rotation.from_rotvec(np.deg2rad([0,p,0])).as_dcm())
    r_matrix_z           = np.matrix(Rotation.from_rotvec(np.deg2rad([0,0,-t])).as_dcm())
    
    center  = np.asarray(np.dot(r_matrix_z, center.T))[0]
    center  = np.asarray(np.dot(r_matrix_y, center.T))[0]
    center  = np.asarray(np.dot(r_matrix_x, center.T))[0]
    
    xyz      = np.asarray(np.dot(r_matrix_z, xyz))
    xyz      = np.asarray(np.dot(r_matrix_y, xyz))
    xyz      = np.asarray(np.dot(r_matrix_x, xyz))
    
    mass = other_inputs[0]
    hsml = other_inputs[1]
    

    if ptype.upper() == 'GAS':

        cmap = 'twilight'
        #range_color = [0.5, 1.0]
        
        img       = QuickView(xyz.T, mass=np.log10(mass), hsml=hsml, r='infinity',
                            x=center[0],y=center[1],z=center[2], plot=False, 
                            xsize=x_res, ysize=y_res, extent=extent) #, p=p, roll=roll, t=t,
        
    elif ptype.upper() == 'DM':
    
        cmap = 'magma'
        #range_color = [0.0, 1.0]

        img       = QuickView(xyz.T, mass=np.log10(mass), r='infinity',
                            x=center[0],y=center[1],z=center[2], plot=False, 
                            xsize=x_res, ysize=y_res, extent=extent) #, p=p, roll=roll, t=t,

    elif ptype.upper() == 'STAR':
        
        cmap = 'ice'
        #range_color = [0.0, 1.0]

        img       = QuickView(xyz.T, mass=np.log10(mass), hsml=hsml, r='infinity',
                            x=center[0],y=center[1],z=center[2], plot=False, 
                            xsize=x_res, ysize=y_res, extent=extent) #, p=p, roll=roll, t=t,

    return img.get_image(), cmap


#<------------------------------------------------------------------------------->#

def make_context(self, img_stack, zmin, zmax, cmap, animation_frame):

    if animation_frame == None:

        if zmin == '' or zmax == '':
            fig = px.imshow(img_stack, origin='lower', 
                            color_continuous_scale=cmap, 
                            labels={'x':'', 'y':''}, width=800, height=800)
        else:
            fig = px.imshow(img_stack, origin='lower', 
                            color_continuous_scale=cmap, 
                            labels={'x':'', 'y':''}, width=800, height=800, zmin=zmin, zmax=zmax)
            
    else:
        if zmin == '' or zmax == '':
            fig = px.imshow(img_stack, origin='lower', 
                            color_continuous_scale=cmap, 
                            labels={'x':'', 'y':''}, width=800, height=800, animation_frame=animation_frame)
        else:
            fig = px.imshow(img_stack, origin='lower', 
                            color_continuous_scale=cmap, 
                            labels={'x':'', 'y':''}, width=800, height=800, zmin=zmin, zmax=zmax, animation_frame=animation_frame)

    fig.update_layout(
        xaxis_tickvals=np.empty(0),
        yaxis_tickvals=np.empty(0)
    )

    gantt_plot = plot(fig, output_type='div')
    context = {'plot_div': gantt_plot}


    return context


#<------------------------------------------------------------------------------->#

def f_min(X,p):
    plane_xyz = p[0:3]
    distance = (plane_xyz*X).sum(axis=1) + p[3]
    return distance / np.linalg.norm(plane_xyz)

def residuals(params, signal, X):
    return f_min(X, params)

def find_plane(xyz_g):
    # Inital guess of the plane
    p0 = [-16, -9,  -18, 1795] #V1
    
    sol = leastsq(residuals, p0, args=(None, xyz_g))[0]
    
    n_norm = sol[0:3]/np.linalg.norm(sol[0:3])
    
    return sol, n_norm


#<------------------------------------------------------------------------------->#

def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=100):
    new_cmap = colors.LinearSegmentedColormap.from_list(
        'trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name, a=minval, b=maxval),
        cmap(np.linspace(minval, maxval, n)))
    return new_cmap

