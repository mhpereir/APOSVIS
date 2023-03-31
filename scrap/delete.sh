#!/bin/bash
for SNAPNUM in {0..127}
do
mysql -u mhpereir -pXXXXXX -e "use apostle" -e  "DROP TABLE IF EXISTS SNAP_V1_LR_GAS_"$SNAPNUM";"
echo DROP TABLE IF EXISTS SNAP_V1_LR_GAS_"$SNAPNUM"
done



