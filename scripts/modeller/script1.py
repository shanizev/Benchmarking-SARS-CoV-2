from modeller import *
import glob
# Get the sequence of the 1qg8 PDB file, and write to an alignment file

#pdb_files='/home/qnt/shani/modeller/pdb_files/'
#seq_files='/home/qnt/shani/modeller/sequence/'

lst_pdb = glob.glob('*.pdb')
for i in range(len(lst_pdb)):
	code = lst_pdb[i].split('.',1)[0]
	#code = 'ies_pepb'
	#print(file_name)
	e = environ()
	m = model(e, file=code)
	aln = alignment(e)
	aln.append_model(m, align_codes=code)
	aln.write(file=code+'.seq')
