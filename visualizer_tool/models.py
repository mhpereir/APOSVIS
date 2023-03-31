from django.db import models

class GROUP_V1_LR(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    snapnum = models.IntegerField(db_column='SNAPNUM')  
    m200 = models.FloatField(db_column='M200')  
    r200 = models.FloatField(db_column='R200')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'GROUP_V1_LR'
        unique_together = (('fofid', 'snapnum'),)


class GROUP_V1_MR(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    snapnum = models.IntegerField(db_column='SNAPNUM')  
    m200 = models.FloatField(db_column='M200')  
    r200 = models.FloatField(db_column='R200')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'GROUP_V1_MR'
        unique_together = (('fofid', 'snapnum'),)


class MERGERTABLE_V1_LR(models.Model):
    subfid = models.IntegerField(db_column='SUBFID', primary_key=True)  
    snapnum = models.IntegerField(db_column='SNAPNUM')  
    descid = models.BigIntegerField(db_column='DESCID')  
    nodeid = models.BigIntegerField(db_column='NODEID')  
    progid = models.BigIntegerField(db_column='PROGID')  

    class Meta:
        managed = False
        db_table = 'MERGERTABLE_V1_LR'
        unique_together = (('subfid', 'snapnum', 'nodeid'),)


class SNAP_V1_LR_DM_0(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_0'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_1(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_1'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_10(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_10'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_100(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_100'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_101(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_101'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_102(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_102'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_103(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_103'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_104(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_104'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_105(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_105'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_106(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_106'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_107(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_107'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_108(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_108'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_109(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_109'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_11(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_11'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_110(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_110'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_111(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_111'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_112(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_112'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_113(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_113'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_114(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_114'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_115(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_115'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_116(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_116'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_117(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_117'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_118(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_118'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_119(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_119'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_12(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_12'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_120(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_120'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_121(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_121'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_122(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_122'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_123(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_123'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_124(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_124'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_125(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_125'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_126(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_126'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_127(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_127'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_13(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_13'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_14(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_14'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_15(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_15'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_16(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_16'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_17(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_17'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_18(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_18'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_19(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_19'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_2(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_2'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_20(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_20'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_21(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_21'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_22(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_22'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_23(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_23'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_24(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_24'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_25(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_25'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_26(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_26'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_27(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_27'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_28(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_28'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_29(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_29'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_3(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_3'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_30(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_30'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_31(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_31'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_32(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_32'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_33(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_33'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_34(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_34'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_35(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_35'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_36(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_36'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_37(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_37'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_38(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_38'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_39(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_39'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_4(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_4'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_40(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_40'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_41(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_41'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_42(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_42'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_43(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_43'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_44(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_44'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_45(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_45'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_46(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_46'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_47(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_47'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_48(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_48'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_49(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_49'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_5(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_5'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_50(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_50'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_51(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_51'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_52(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_52'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_53(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_53'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_54(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_54'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_55(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_55'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_56(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_56'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_57(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_57'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_58(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_58'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_59(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_59'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_6(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_6'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_60(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_60'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_61(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_61'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_62(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_62'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_63(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_63'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_64(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_64'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_65(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_65'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_66(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_66'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_67(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_67'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_68(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_68'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_69(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_69'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_7(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_7'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_70(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_70'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_71(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_71'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_72(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_72'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_73(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_73'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_74(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_74'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_75(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_75'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_76(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_76'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_77(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_77'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_78(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_78'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_79(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_79'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_8(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_8'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_80(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_80'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_81(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_81'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_82(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_82'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_83(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_83'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_84(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_84'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_85(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_85'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_86(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_86'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_87(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_87'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_88(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_88'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_89(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_89'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_9(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_9'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_90(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_90'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_91(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_91'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_92(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_92'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_93(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_93'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_94(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_94'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_95(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_95'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_96(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_96'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_97(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_97'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_98(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_98'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_DM_99(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_DM_99'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_0(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_0'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_1(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_1'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_10(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_10'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_100(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_100'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_101(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_101'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_102(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_102'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_103(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_103'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_104(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_104'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_105(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_105'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_106(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_106'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_107(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_107'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_108(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_108'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_109(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_109'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_11(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_11'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_110(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_110'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_111(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_111'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_112(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_112'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_113(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_113'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_114(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_114'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_115(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_115'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_116(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_116'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_117(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_117'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_118(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_118'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_119(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_119'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_12(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_12'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_120(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_120'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_121(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_121'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_122(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_122'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_123(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_123'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_124(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_124'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_125(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_125'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_126(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_126'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_127(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_127'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_13(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_13'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_14(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_14'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_15(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_15'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_16(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_16'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_17(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_17'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_18(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_18'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_19(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_19'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_2(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_2'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_20(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_20'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_21(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_21'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_22(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_22'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_23(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_23'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_24(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_24'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_25(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_25'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_26(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_26'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_27(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_27'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_28(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_28'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_29(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_29'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_3(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_3'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_30(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_30'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_31(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_31'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_32(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_32'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_33(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_33'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_34(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_34'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_35(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_35'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_36(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_36'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_37(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_37'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_38(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_38'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_39(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_39'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_4(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_4'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_40(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_40'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_41(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_41'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_42(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_42'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_43(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_43'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_44(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_44'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_45(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_45'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_46(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_46'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_47(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_47'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_48(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_48'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_49(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_49'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_5(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_5'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_50(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_50'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_51(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_51'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_52(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_52'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_53(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_53'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_54(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_54'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_55(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_55'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_56(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_56'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_57(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_57'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_58(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_58'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_59(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_59'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_6(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_6'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_60(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_60'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_61(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_61'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_62(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_62'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_63(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_63'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_64(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_64'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_65(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_65'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_66(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_66'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_67(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_67'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_68(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_68'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_69(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_69'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_7(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_7'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_70(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_70'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_71(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_71'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_72(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_72'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_73(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_73'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_74(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_74'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_75(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_75'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_76(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_76'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_77(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_77'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_78(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_78'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_79(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_79'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_8(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_8'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_80(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_80'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_81(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_81'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_82(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_82'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_83(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_83'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_84(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_84'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_85(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_85'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_86(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_86'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_87(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_87'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_88(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_88'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_89(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_89'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_9(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_9'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_90(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_90'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_91(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_91'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_92(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_92'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_93(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_93'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_94(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_94'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_95(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_95'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_96(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_96'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_97(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_97'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_98(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_98'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_GAS_99(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_GAS_99'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_0(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_0'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_1(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_1'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_10(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_10'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_100(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_100'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_101(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_101'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_102(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_102'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_103(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_103'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_104(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_104'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_105(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_105'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_106(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_106'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_107(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_107'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_108(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_108'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_109(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_109'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_11(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_11'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_110(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_110'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_111(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_111'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_112(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_112'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_113(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_113'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_114(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_114'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_115(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_115'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_116(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_116'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_117(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_117'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_118(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_118'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_119(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_119'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_12(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_12'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_120(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_120'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_121(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_121'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_122(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_122'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_123(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_123'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_124(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_124'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_125(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_125'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_126(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_126'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_127(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_127'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_13(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_13'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_14(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_14'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_15(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_15'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_16(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_16'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_17(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_17'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_18(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_18'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_19(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_19'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_2(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_2'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_20(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_20'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_21(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_21'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_22(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_22'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_23(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_23'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_24(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_24'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_25(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_25'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_26(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_26'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_27(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_27'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_28(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_28'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_29(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_29'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_3(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_3'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_30(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_30'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_31(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_31'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_32(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_32'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_33(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_33'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_34(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_34'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_35(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_35'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_36(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_36'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_37(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_37'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_38(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_38'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_39(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_39'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_4(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_4'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_40(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_40'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_41(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_41'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_42(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_42'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_43(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_43'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_44(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_44'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_45(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_45'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_46(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_46'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_47(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_47'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_48(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_48'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_49(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_49'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_5(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_5'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_50(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_50'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_51(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_51'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_52(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_52'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_53(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_53'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_54(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_54'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_55(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_55'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_56(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_56'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_57(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_57'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_58(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_58'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_59(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_59'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_6(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_6'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_60(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_60'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_61(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_61'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_62(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_62'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_63(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_63'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_64(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_64'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_65(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_65'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_66(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_66'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_67(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_67'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_68(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_68'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_69(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_69'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_7(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_7'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_70(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_70'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_71(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_71'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_72(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_72'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_73(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_73'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_74(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_74'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_75(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_75'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_76(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_76'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_77(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_77'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_78(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_78'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_79(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_79'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_8(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_8'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_80(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_80'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_81(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_81'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_82(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_82'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_83(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_83'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_84(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_84'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_85(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_85'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_86(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_86'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_87(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_87'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_88(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_88'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_89(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_89'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_9(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_9'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_90(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_90'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_91(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_91'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_92(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_92'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_93(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_93'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_94(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_94'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_95(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_95'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_96(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_96'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_97(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_97'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_98(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_98'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_LR_STAR_99(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_LR_STAR_99'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_MR_DM_127(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_MR_DM_127'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_MR_GAS_127(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  
    hsml = models.FloatField(db_column='HSML')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_MR_GAS_127'
        unique_together = (('fofid', 'subid', 'pid'),)


class SNAP_V1_MR_STAR_127(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    pid = models.BigIntegerField(db_column='PID')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  
    mass = models.FloatField(db_column='MASS')  

    class Meta:
        managed = False
        db_table = 'SNAP_V1_MR_STAR_127'
        unique_together = (('fofid', 'subid', 'pid'),)


class SUBGROUP_V1_LR(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    snapnum = models.IntegerField(db_column='SNAPNUM')  
    subfid = models.IntegerField(db_column='SUBFID')
    mdm = models.FloatField(db_column='Mdm')  
    mgas = models.FloatField(db_column='Mgas')  
    mstar = models.FloatField(db_column='Mstar')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SUBGROUP_V1_LR'
        unique_together = (('fofid', 'subid', 'snapnum'),)


class SUBGROUP_V1_MR(models.Model):
    fofid = models.IntegerField(db_column='FOFID', primary_key=True)  
    subid = models.IntegerField(db_column='SUBID')  
    snapnum = models.IntegerField(db_column='SNAPNUM')  
    subfid = models.IntegerField(db_column='SUBFID')
    mdm = models.FloatField(db_column='Mdm')  
    mgas = models.FloatField(db_column='Mgas')  
    mstar = models.FloatField(db_column='Mstar')  
    cop_x = models.FloatField(db_column='COP_X')  
    cop_y = models.FloatField(db_column='COP_Y')  
    cop_z = models.FloatField(db_column='COP_Z')  

    class Meta:
        managed = False
        db_table = 'SUBGROUP_V1_MR'
        unique_together = (('fofid', 'subid', 'snapnum'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
