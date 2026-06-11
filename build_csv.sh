#!/bin/bash

gens=10
out="lots.csv"

for file in $( ls resp_10gens/* ); do

    python3 collect.py $file $gens > $( basename $file ).csv
done;