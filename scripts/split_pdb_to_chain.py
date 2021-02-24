
#this script split the pdb to chains

import glob
import os

lst_pdb = glob.glob('*.pdb')

#file_list_pdb = [os.path.splitext(x)[0] for x in lst_pdb]

def write_to_file(res_name,atom_list):
    with open('../ligands/'+ file_name[:-4] +'_'+res_name.replace(' ','')+ '_ligand.pdb', 'w') as w:
        for item in atom_list:
            w.write("%s" % item)


for file_name in lst_pdb:

    f = open(file_name, "r")
    txt = f.readlines()

    a_chain = []
    b_chain = []
    c_chain = []
    d_chain = []
    e_chain = []
    ligands = []
    ligand_final =[]
    res_name = []

    for i in range(0, len(txt)):
        if 'ATOM' in txt[i]:
            #print(txt[i][21])
            if txt[i][21] == 'A':
                a_chain.append(txt[i])
            elif txt[i][21] == 'B':
                b_chain.append(txt[i])
            elif txt[i][21] == 'C':
                c_chain.append(txt[i])
            elif txt[i][21] == 'D':
                d_chain.append(txt[i])
            elif txt[i][21] == 'E ':
                e_chain.append(txt[i])

        if 'TER' in txt[i] and 'HETATM' in txt[i+1] and txt[i][0:3] == 'TER':

            ligands.append(txt[i+1:len(txt)])
            flattened_ligands = [val for sublist in ligands for val in sublist]

            #print(len(flattened_ligands))
    #print(len(flattened_ligands))
    i = 0
    #print(i < len(flattened_ligands))
    #print(type(i))
    while i < len(flattened_ligands):

        #print(i)
        x = flattened_ligands[i]
        #print(type(x))
        if 'HOH' in x or 'DMS' in x or 'REMARK' in x or 'PEG' in x or 'MES' in x or 'DOD' in x or 'GOL' in x \
                or 'ANISOU' in x or '1PE' in x or 'EDO' in x or 'CONECT' in x:
            #print(x)
            flattened_ligands.remove(x)
        elif 'HETATM' in x:

            if x.split()[3] == 'CL' or x.split()[3] == 'NA':

                flattened_ligands.remove(x)

            else:
                i +=1
        else:
            i += 1

    ligands_dict = {}

    for i in flattened_ligands:
        # print(type(i.split()[4]))
        if 'HETATM' in i or 'ATOM' in i:
            key = i.split()[3]+' '+i.split()[4]
            if key not in ligands_dict.keys():
                ligands_dict[key] = [i]
            else:
                ligands_dict[key].append(i)
    print(ligands_dict)
    if len(ligands_dict) == 1:
        print(file_name,'one ligand')
        pass
    elif len(ligands_dict) >1:
        for i in ligands_dict.keys():
            write_to_file(i, ligands_dict[i])

    # for x in range(len(flattened_ligands)):
    #     if 'HETATM' in flattened_ligands[x]:
    #         #print(flattened_ligands[x])
    #         res_name.append(flattened_ligands[x].split()[4])
    # unique_res = set(res_name)
    # if len(unique_res) > 1:
    #     list_of_list = [None] * len(unique_res)
    #
    #     for i in range(len(flattened_ligands)):
    #         if flattened_ligands[i] == unique_res[0]
    #             list_of_list[0].append

            #
            # if item in flattened_ligands[x]:
            #
            #     write_to_file(item,flattened_ligands[x])



    if len(a_chain) > 0:
        with open('../proteins/'+file_name[:-4]+'.pdb', 'w') as w:
            for item in a_chain:
                w.write("%s" % item)

    if len(b_chain) > 0:
        with open('../proteins/'+file_name[:-4]+'_b.pdb', 'w') as w:
            for item in b_chain:
                w.write("%s" % item)

    if len(c_chain) > 0:
        with open('../proteins/'+file_name[:-4]+'_c.pdb', 'w') as w:
            for item in c_chain:
                w.write("%s" % item)

    if len(d_chain) > 0:
        with open('../proteins/'+file_name[:-4]+'_d.pdb', 'w') as w:
            for item in d_chain:
                w.write("%s" % item)

    if len(e_chain) > 0:
        with open('../proteins/'+file_name[:-4]+'_e.pdb', 'w') as w:
            for item in e_chain:
                w.write("%s" % item)

    if len(flattened_ligands) > 0:
        with open('../ligands/'+file_name[:-4]+'_ligand.pdb', 'w') as w:
            for item in flattened_ligands:
                w.write("%s" % item)
