#!/bin/bash

###create input files for running charmm 

string=`basename $1`
PDB=$(echo "${string##*/}")  ##remove the / in order to get just the pdb
IDPDB=$(echo "$PDB" | cut -f 1 -d '.') # remove the .pdb    
        
cat > /home/qnt/shani/charmm/workspace/covid-19/mm/wrk/cov2.s1.$PDB.inp << EOF
* Created by DTM 18/09/2007
* Modified by DTM 23/07/2009
* Edit by shani 
*

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
! Initialization

BOMBLEVEL -1           ! Allow presence of missing residues
WRNLEV    10

set PDBFILE $IDPDB
set sol     covid-19
set calc    mm


stream /home/qnt/shani/charmm/workspace/scripts/param.str
stream /home/qnt/shani/charmm/workspace/covid-19/mm/stream/@PDBFILE_cryst.dat
set refpdb 5r84   ! This serves as reference structure
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
! Read topology and parameter files

!read topology
open read card unit 10 name @TopPro
read rtf card unit 10
close unit 10

!read parameters
open read card unit 10 name @ParPro
read param card unit 10
close unit 10



!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
! Read in reference PDB file
open unit 1 form read name @pdbDIR/proteins_charmmfixed/@refpdb.pdb
read sequ pdb unit 1
generate PEP0 setup first nter last cter
rewind unit 1
read coor pdb unit 1
close unit 1

set offset ?nres

! Read in structure from pdb file
open read card unit 1 name @pdbDIR/proteins_charmmfixed/@pdbfile.pdb
read sequ pdb unit 1
generate PEP1 setup first nter last cter
rewind unit 1
read coor pdb unit 1 offset @offset
close unit 1



print coor

! build in missing hydrogens if using a crystal structure (NMR has hydrogens)
ic purge
ic param
ic fill preserve
ic build
hbuild 
ic fill
ic para
ic build


! Create second protomer
generate PEP2 dupl PEP1
coor dupl sele segi PEP1 end sele segi PEP2 end

coor stat sele all end

! Perform rotation followed by translation of second protomer
! Variable are read in at top of file
coor rota matrix sele segi PEP2 end
 @xrot     0.000000  0.000000
 0.000000  @yrot     0.000000
 0.000000  0.000000  @zrot

coor tran xdir @xmov ydir @ymov zdir @zmov sele segi PEP2 end

coor stat sele all end

! Perform superpositioning of everything relative to PEP0 (in comp)
define cmnres sele resid 1:300 end
coor copy comp
coor dupl comp sele segid PEP0 .and. cmnres end sele segid PEP1 .and. cmnres end
coor orient rms selec segid PEP1 .and. cmnres end
coor copy sele segid PEP0 end

open write unit 25 form name @pdbDIR/proteins_final/@pdbfile_1.pdb
write coor pdb unit 25 sele segi PEP1 end
close unit 25

open write unit 25 form name @pdbDIR/proteins_final/@pdbfile_2.pdb
write coor pdb unit 25 sele segi PEP2 end
close unit 25

stop

		

            
EOF
        


