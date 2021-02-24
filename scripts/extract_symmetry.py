'''
This script will write the symmetry operation in order to create dimer structures in CHARMM. 
it taking the data from the original PDB files and write file_name+'_cryst.dat file 

'''
import glob

lst_pdb = glob.glob('*.pdb')
for i in range(len(lst_pdb)):
    f = open(lst_pdb[i], "r")
    txt = f.readlines()
    file_name = lst_pdb[i].split('.',1)[0]

    xrot = list([txt[i].split()[-4] for i in range(0, len(txt)) if 'REMARK 350   BIOMT1' in txt[i]])[-1]
    yrot = list([txt[i].split()[-3] for i in range(0, len(txt)) if 'REMARK 350   BIOMT2' in txt[i]])[-1]
    zrot = list([txt[i].split()[-2] for i in range(0, len(txt)) if 'REMARK 350   BIOMT3' in txt[i]])[-1]

    xmov = list([txt[i].split()[-1] for i in range(0, len(txt)) if 'REMARK 350   BIOMT1' in txt[i]])[-1]
    ymov = list([txt[i].split()[-1] for i in range(0, len(txt)) if 'REMARK 350   BIOMT2' in txt[i]])[-1]
    zmov = list([txt[i].split()[-1] for i in range(0, len(txt)) if 'REMARK 350   BIOMT3' in txt[i]])[-1]

    print(file_name,xrot,yrot,zrot,xmov,ymov,zmov)

    with open(file_name+'_cryst.dat', 'w') as the_file:
        the_file.write('* Read in crystal transformation data\n'+'*\n\n'
                       'set pdbfile '+ file_name +'\n'
                       'set xrot ' +xrot + '\n'
                       'set yrot ' +yrot + '\n'
                       'set zrot ' + zrot + '\n'
                       'set xmov ' + xmov + '\n'
                       'set ymov ' + ymov + '\n'
                       'set zmov ' +zmov + '\n'

                   )
