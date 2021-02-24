# Benchmarking the ability of common docking programs to correctly reproduce and score binding modes in SARS-CoV-2 protease Mpro

## For the initial coordinates:  
1.	Run python script split_pdb_to_chain.py in the PDB initial coordinates directory. This script will split to different chain and to ligands, and write them to different files.
2.	Run python script extract_symmetry.py in the PDB initial coordinates directory. This script will create *dat file that CHARMM will read in step #.

## For the proteins structures:  
The proteins structures is without hydrogens so we want to add them with CHARMM program.

1. **Determine the protonation state of HIS and ILE** 
Run bash script step1_fixpdb.sh, this script will run the pdbfix.pl (Perl script) that should be in the same directory. The pdbfix.pl will modify the HIS to the corrects protonation state and change for all ILE (CD1->CD). 
2. **Creating input files for CHARMM**
Run bash step2_createinput.sh . this script will call the ## script and create inputs file for CHARMM. 
	 
