#!/bin/bash

awk 'NR == 1 || FNR > 1' *.csv > original.csv

# diff original.csv ../ex03/hh_positions.csv 