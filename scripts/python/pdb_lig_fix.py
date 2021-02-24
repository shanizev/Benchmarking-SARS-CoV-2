#!/usr/bin/env python
# Usage: pdb_lig_fix.py file
# The scripts adds numbers to hydrogens
# Should work for up to 999 hydrogens
# Written by DTM 24/4/2020
# Last updated 24/4/2020

import sys
import os
import tempfile

tmp=tempfile.mkstemp()

space_str = ' '
space_num = 3
space_after = space_str*space_num
string1 = space_str + 'H' + space_after
with open(sys.argv[1]) as fd1:
    with open(tmp[1],'w') as fd2:
        i = 1
        for line in fd1:
            if (line.find(string1) != -1):
                string0 = str(i)
                if (i < 100):
                    string2 = space_str + 'H' + string0 + space_str*(space_num - len(string0))
                else:
                    string2 = 'H' + string0 + space_str*(space_num + 1 - len(string0))
                line = line.replace(string1, string2)
                i += 1
            fd2.write(line)
    os.rename(tmp[1],sys.argv[2])
