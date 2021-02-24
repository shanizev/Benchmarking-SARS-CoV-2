from modeller import *
from modeller.automodel import *    # Load the automodel class


log.verbose()
env = environ()

# directories for input atom files
env.io.atom_files_directory = ['.', '../atom_files']

pdb_to_model ='7kyu'

class MyModel(automodel): #here you define which residues to model, all the rest will be exactly as the crystal structure 
    def select_atoms(self):
        return selection(self.residue_range('47', '48'))#,
                         #self.residue_range('38', '42'),
			#			 self.residue_range('90', '94'),
			#			 self.residue_range('311', '312'),
			#			 self.residue_range('315', '321'))

a = MyModel(env, alnfile = 'alignment1.ali',
            knowns = '7kyu',#,'ies_pepe','ies_pepa','ies_pepc','ies_pepf'), #option to do model based on several templates  
			 sequence = '7ju7')
##i think that the known should be the pdb that we want to model and the sequence is the full sequence

a.starting_model= 1
a.ending_model  = 1 #number of models 

a.make()

#Filename(molpdf, mode=r)
a.write(file=pdb_to_model+'_model.pdb')


