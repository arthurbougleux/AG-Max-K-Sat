#!/bin/bash

gens=20
out="lots.csv"

for file in $( ls resp/* ); do

    python3 collect.py $file $gens > $( basename $file ).csv
done;