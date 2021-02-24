#!/usr/bin/perl
#
# Written by DTM 11/13/2003
# Prepares a fixed pdb file for reading by CHARMM
# Usage: pdbfix.pl filename
#
 
####################################################
      
$pdbfile = shift(@ARGV);
#$outpdbfile = $pdbfile . "_fix";
$outpdbfile = "/home/qnt/shani/charmm/workspace/covid-19/mm/pdb/proteins_charmmfixed/" . $pdbfile;

open (INDAT, "<$pdbfile") || die "Cannot open file $pdbfile to read.\n";
open (OUTDAT, ">$outpdbfile") || die "Cannot open file $datfile to write.\n";
while ($line = <INDAT>) {
 
     $line =~ s/CD1 ILE/CD  ILE/;
     $line =~ s/O   SER A  38/OT1 SER A  38/;
     $line =~ s/OXT SER/OT2 SER/;
     $line =~ s/HIS A  41/HSD A  41/;
     $line =~ s/HIS A  64/HSP A  64/;
     $line =~ s/HIS A  80/HSD A  80/;
     $line =~ s/HIS A 163/HSP A 163/;
     $line =~ s/HIS A 164/HSE A 164/;
     $line =~ s/HIS A 172/HSP A 172/;
     $line =~ s/HIS A 246/HSP A 246/;
     printf(OUTDAT "%s",$line);
}

close(INDAT);
close(OUTDAT);

printf("The file %s was written\n",$outpdbfile);
