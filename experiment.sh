#!/bin/bash

gens=20
pop=30

if [ ! $(ls -d resp/) ]; then
    mkdir resp
fi;


for file in $( ls random_3_sat/* ); do

    inst=$(basename $file)
    inst=${inst%%.*}

    echo $inst...

    for opt in "--chaos 0.2 --search reckless --steps 1" "--chaos 0.2" "--uniforme 0.2"; do

        echo "-- Abordagem: "$opt >> $inst

        for i in $(seq 30); do
            python3 main.py $file $pop $gens $opt -v >> $inst
        done;

    done;

    mv $inst resp

done;