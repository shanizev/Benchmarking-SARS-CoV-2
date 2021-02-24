#!/bin/bash

##this script run the crateinput.sh in order to create input file for CHARMM 

#Here define your PDB directory
pdb_dir_input='/home/qnt/shani/charmm/workspace/covid-19/mm/pdb/proteins_charmmfixed/'


for pdbfile in $pdb_dir_input*pdb
do
sh createinput_symmetry.sh $pdbfile

done

