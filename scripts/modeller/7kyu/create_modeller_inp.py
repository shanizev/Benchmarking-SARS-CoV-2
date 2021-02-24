#python
import glob
import re
import os
import subprocess
#subprocess.call(["ls", "-l"]) 



#lst_pdb = glob.glob('*.pdb')

#for x in lst_pdb 
#   if x == ''


#print(os.system('sh createinput.sh $pdb $refpdb'))


## first file in current dir (with full path)
file = os.path.join(os.getcwd(), os.listdir(os.getcwd())[0])
dir = os.path.dirname(file) ## directory of file
#print(str(dir))
dir2 = dir.split('/')[-1]
#print(dir2)

lst_pdb = glob.glob('*.pdb')
#for i in range(len(lst_pdb)):
lst_pdb2 = list([ lst_pdb[i].split('.',1)[0] for i in range(len(lst_pdb))])
#print(lst_pdb2)
pdb = list([i for i in lst_pdb2 if i == dir2])[0]
refpdb =list([i for i in lst_pdb2 if i != dir2])[0]

print(pdb)
print(refpdb)

subprocess.call(['createinput.sh',  pdb, refpdb])
print('hi')


