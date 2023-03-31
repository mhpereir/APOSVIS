from django import forms

class SubmitForm(forms.Form):
    vol         = forms.CharField(max_length=2, label='Volume', required=False, initial='V1')
    res         = forms.CharField(max_length=2, label='Resolution', required=False, initial='LR')
    snapnum     = forms.IntegerField(label='SnapNum', required=False, initial='125')
    grpid       = forms.IntegerField(label='GroupID', required=False, initial='1')
    subgrpid    = forms.IntegerField(label='SubGroupID', required=False, initial='0')
    showwhich   = forms.CharField(max_length=8, label='Show', required=False, initial='All')

    ptype       = forms.CharField(max_length=5, label='Particle Type', required=False, initial='Gas')
    boxsize     = forms.FloatField(label='Box Size', required=False, initial='100')
    boxsizeunit = forms.CharField(max_length=5, label='Units of Box Size', required=False, initial='kpc')
    zmin        = forms.FloatField(label='Colorbar Min', required=False, initial='')
    zmax        = forms.FloatField(label='Colorbar Max', required=False, initial='')

    orien       = forms.CharField(max_length=8, label='Orientation', required=False, initial='Face-on')

    timelapse_flag = forms.BooleanField(required=False)
    snapinit       = forms.IntegerField(label='SnapInit', required=False, initial='120')
    snapfinal      = forms.IntegerField(label='SnapFinal', required=False, initial='127')
