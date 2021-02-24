#!/bin/csh

# Use script to rename hydrogens that were added using obabel to all pdb files
# # Run from directory with pdb files
setenv TMPDIR .
foreach w ( *.pdb )
   set v = `basename $w .pdb`
     echo "pdb_lig_fix.py on file " $w
       ../pdb_lig_fix.py $w ../ligands_fixed_num_H/${v}_final.pdb
       end


