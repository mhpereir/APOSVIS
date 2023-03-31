#!/bin/bash
for SNAPNUM in {0..127}
do
mysql -u mhpereir -pXXXXXX --local_infile=1 -e "use apostle" -e  "
      LOAD DATA LOCAL INFILE '/home/mwilson/Projects/APOSVIS/scrap/SNAPSHOTS_LR_STAR/SNAPSHOT_STAR_V1_LR_"$SNAPNUM".csv'
      INTO TABLE SNAP_V1_LR_STAR_"$SNAPNUM"
      FIELDS TERMINATED BY ',' 
      IGNORE 1 LINES
      (FOFID, SUBID, PID, COP_X, COP_Y, COP_Z, MASS);"

done



