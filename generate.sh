#!/bin/bash

k=3
INST_DIR=random_3_sat

if [ ! $(ls -d $INST_DIR/) ]; then 
    mkdir $INST_DIR
fi;

for n in $(seq 100 50 1000); do

    m=$(echo "scale=0; ($n * 4.26) / 1" | bc )

    name=rand_${n}_${m}.cnf
    python3 gen.py $name $n $m $k
    mv $name $INST_DIR

done;