##this scipt adding hydrogens with babel command, input file-ligands without H, output files ligands with H 

#define your input and output directory 
pdb_input_ligand='/home/qnt/shani/charmm/workspace/covid-19/mm/pdb/ligands_withoutH/'
pdb_output_ligand='/home/qnt/shani/charmm/workspace/covid-19/mm/pdb/ligands_with_H'

for pdbfile in ${pdb_input_ligand}*pdb
#for  pdbfile in "${pdb_input_ligand}7bqy_ligand.pdb" ###for specific file
do
PDB=$(echo "${pdbfile##*/}")     
IDPDB=$(echo "$PDB" | cut -f 1 -d '.')
babel "${pdb_input_ligand}${IDPDB}.pdb" -O "$pdb_output_ligand/${IDPDB}.pdb" -h
#babel "${pdb_output_ligand}/${IDPDB}.pdb" -osmi >> "$smiles_dir/smiles.smi" 

done

