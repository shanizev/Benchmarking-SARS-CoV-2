# Benchmarking the ability of common docking programs to correctly reproduce and score binding modes in SARS-CoV-2 protease Mpro

## For the initial coordinates:  
The initial coordiantes is in data/initial coordinates/

1.	Run python script split_pdb_to_chain.py in the PDB initial coordinates directory. This script will split to different chain (A/B etc.) and to the diffrent ligands, and write them to different files. (maybe the previous script was better..) 
2.	Run python script extract_symmetry.py on all the PDB initial coordinates directory. This script will create *dat file that CHARMM will read in step 3.

## For the proteins structures:  
goal: adding the dimer to the monomer, and adding hydrogens to the structure
4. **Determine the protonation state of HIS and ILE** Run bash script step1_fixpdb.sh, this script will run the pdbfix.pl (Perl script) that should be in the same directory. The pdbfix.pl will modify the HIS to the corrects protonation state and change for all ILE (CD1->CD). 
5. **Creating input files for CHARMM**Run bash step2_createinput.sh . this script will call the ## script and create inputs file for CHARMM. 
6. **Running CHARMM.** The input should be the prepared pdb file (without ligands, water molecules and solvent, and with fixed HIS and ILE). The output will be the prepared proteins (with hydrogens and as dimer structure) 
	 
## For the ligands structures:  
7. **Adding hydrogen to ligands using obabel** running addingH_obabel.sh, define your input files directory and output files directory
8. Rename HETATM to ATOM for all ligands using hetatmtoatom.sh
9. **Adding numbers to hydrogens** running run_pdb_lig_fix.csh (./run_pdb_lig_fix.csh). This script will run a python script in the parent folder, pay attention to tmp file 
10. **Replace the residue number to 1.** (first install the pdbtools (pip install pdb-tools), then run the pdb_reres.sh script (./pdb_reres.sh) in the PDB directory) (not in the folder)

## Create parameters to the ligands using CGenFF


## Docking:
