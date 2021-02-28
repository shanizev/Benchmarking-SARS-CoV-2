# Benchmarking the ability of common docking programs to correctly reproduce and score binding modes in SARS-CoV-2 protease Mpro

## For the initial coordinates:  
The initial coordiantes can be found in data/initial coordinates/

1.	**Split PDB to chains:** Run python script split_pdb_to_chain.py in the PDB initial coordinates directory. This script will split to different chain (A/B etc.) and to the diffrent ligands, and write them to different files. (maybe the previous script was better..) 
2.	Run python script extract_symmetry.py on all the PDB initial coordinates directory. This script will create *dat file that CHARMM will read in step 3.

## For the proteins structures:  
Goal: Creating the homodimer containing two protomers, and adding hydrogens to the the structure. 

4.	 **Determine the protonation state of HIS** Run bash script step1_fixpdb.sh, this script will run the pdbfix.pl (perl script) that should be in the same directory. The pdbfix.pl will modify the HIS to the corrects protonation state (and ILE (CD1->CD))
5.	 **Creating input files for CHARMM** Run bash step2_createinput.sh . this script will call the createinput_symmetry.sh script and create inputs file for all structures for CHARMM. 
 Note: Some structures was as homodimer initiallty. for these dtructures we read to charmm both chains. 
7.	 **Running CHARMM.** The input should be the prepared PDB file for CHARMM (without ligands, water molecules and solvent, and with fixed HIS and ILE). The output will be the prepared proteins (with hydrogens and as a dimer structure) 
	 
## For the ligands structures:  
7. **Adding hydrogen to ligands using obabel** run addingH_obabel.sh, define your input files directory and output files directory
8. Rename HETATM to ATOM for all ligands using hetatmtoatom.sh
9. **Adding numbers to hydrogens** running run_pdb_lig_fix.csh (./run_pdb_lig_fix.csh). This script will run a python script in the parent folder, pay attention to tmp file 
10. **Replace the residue number to 1.** (first install the pdbtools (pip install pdb-tools), then run the pdb_reres.sh script (./pdb_reres.sh) in the PDB directory) (not in the folder)

## Create parameters to the ligands using CGenFF


## Docking:
1. EnzyDock
2. Glide
