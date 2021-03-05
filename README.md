# Benchmarking the ability of common docking programs to correctly reproduce and score binding modes in SARS-CoV-2 protease Mpro

## For the initial coordinates:  
The original, initial PDB coordinates can be found in data/initial coordinates/

1.	**Split PDB to chains:** Run python script split_pdb_to_chain.py in the PDB initial coordinates directory. This script will split to different chains (A/B) and the different ligands, and write them to separate files.
2.	Run python script extract_symmetry.py on all the PDB initial coordinates directory. This script will create *dat file that CHARMM will read in step 3, when generating dimers from monomers ans symmetry information.

## For the protein structures:  
Goal: Creating the homodimer containing two protomers, and adding hydrogens to the structure. 

4.	 **Determine the protonation state of HIS** Run bash script step1_fixpdb.sh, this script will run the pdbfix.pl (perl script) that should be in the same directory. The pdbfix.pl will modify the HIS to the presumed correct protonation state (and changing ILE (CD1->CD))
5.	 **Creating input files for CHARMM** Run bash step2_createinput.sh. this script will call the createinput_symmetry.sh script and create input files for all structures for CHARMM. 
 Note: Some structures are homodimers initially. For these dtructures we read both chains directly with CHARMM. 
7.	 **Running CHARMM.** The input should be the prepared PDB file for CHARMM (without ligands, water molecules and solvent, and with fixed HIS and ILE). The output will be the prepared proteins (with hydrogens and as a dimer structure) 
	 
## For the ligand structures:  
7. **Adding hydrogens to ligands using obabel** run addingH_obabel.sh, define input files directory and output files directory.
8. Rename HETATM to ATOM for all ligands using hetatmtoatom.sh
9. **Adding numbers to hydrogens** running run_pdb_lig_fix.csh (./run_pdb_lig_fix.csh). This script will run a python script in the parent folder, pay attention to tmp file.
10. **Rename the residue number to 1.** (first install the pdbtools (pip install pdb-tools), then run the pdb_reres.sh script (./pdb_reres.sh) in the PDB directory) (not in the folder)

## Create parameters for the ligands using CGenFF (https://mackerell.umaryland.edu/ff_dev.shtml#cgenff)


## Docking:
1. EnzyDock
2. Glide
3. DOCK
4. AutoDock
5. AutoDock Vina
6. FRED
