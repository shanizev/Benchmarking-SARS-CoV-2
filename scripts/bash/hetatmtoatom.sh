#this script change HETATM to ATOM

#define here your output directory 
pdb_output_ligand='/home/qnt/shani/charmm/workspace/covid-19/mm/pdb/ligands_with_H/'

for pdbfile in $pdb_output_ligand*pdb
do
PDB=$(echo "${pdbfile##*/}")
sed -i 's/HETATM/ATOM  /g' $pdb_output_ligand$PDB
done 
