#!/bin/bash

###create input files for running charmm 


PDB=`basename $1`
#echo $string
#PDB=$(echo "${string##*/}")  ##remove the / in order to get just the pdb
#IDPDB=$(echo "$PDB" | cut -f 1 -d '.') # remove the .pdb            
REFPDB=`basename $2`
#echo $string2

cat > /home/qnt/shani/modeller/workspace/covid_models/$PDB/script2_$PDB.py << EOF
# Step 2: prepare an alignment of all template structures and the
#         target sequence
#
# Align all of the best template structures detected in the previous step
# and compare them. Then align the target sequence with this block of
# aligned structures to generate an alignment suitable for modeling.
#this script write alignmet file and family.mat 

from modeller import *

env = environ()
#env.io.atom_files_directory = ['../atom_files']

# Create an alignment of the 'A' chains of 1clf, 1dur, 1fca and 2fdn
aln = alignment(env)
pdb = '$PDB' #for just one structures
#for multiple structure 
#for pdb in ('7kyu'):
m = model(env, file=pdb)
aln.append_model(m, atom_files=pdb, align_codes=pdb)

# Structurally align all four templates and compare them
aln.malign()
aln.malign3d()
aln.compare_structures()
aln.id_table(matrix_file='family.mat')
env.dendrogram(matrix_file='family.mat', cluster_cut=-1.0)

# Align the target sequence to the previously-aligned structures
align_block = len(aln)
aln.append(file='$REFPDB.seq') #full sequence of the target protein (need to be prepared) 
aln.align2d(align_block=align_block, max_gap_length=50)
aln.write(file='alignment1.ali')




#, ('6xb1', 'A'),
                    # ('6xb0', 'A'),('6xkh', 'A'),('7awu','A'),('7cx9','A'),('7arf','A')): #6xkf is missing because it dimer

 


        

		

            
EOF
        


