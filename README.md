# DecoyPYrat
DecoyPYrat - Fast Hybrid Decoy Sequence Database Creation for Proteomic Mass Spectrometery Analyses

Accurate statistical evaluation of sequence database peptide identifications from tandem mass spectra is essential in mass spectrometry based proteomics experiments. These statistics are dependent on accurately modelling random identifications. The target-decoy approach has risen to become the de facto approach to calculating false discovery rates in proteomic datasets. The main principle of this approach is to search a set of decoy protein sequences that emulate the size and composition of the target protein sequences searched whilst not matching real proteins in the sample. To do this, it is commonplace to reverse or shuffle the proteins and peptides in the target database. However, these approaches have their drawbacks and limitations. A key confounding issue is the peptide redundancy between target and decoy databases leading to inaccurate FDR estimation. This inaccuracy is further amplified at the protein level and when searching large sequence databases such as those used for proteogenomics. Here, we provide a unifying hybrid tool, DecoyPYrat, to quickly and efficiently generate decoy sequences with minimal overlap between target and decoy peptides.  Applying a reversed decoy approach can produce up to 5% peptide redundancy and many more additional peptides will have the exact same precursor mass as a target peptide. This hybrid method addresses both these issues by first switching proteolytic cleavage sites with preceding amino acid, reversing the database and then shuffling any redundant sequences. This flexible tool reduces the peptide overlap between target and decoy peptides to about 1% of peptides, making a more robust decoy model suitable for large search spaces. 

Download and Installation:

You will need to have Python 3.x installed to run this tool. Python can be download here - https://www.python.org/.

Usage:

DecoyPYrat creates decoy protein sequences for assessing FDR in proteomic mass spectrometry experiments. Each protein is reversed and the cleavage sites switched with preceding amino acid. Peptides are checked for existence in target sequences and if found the tool will attempt to shuffle them iterativly until they are unique.


James.Wright@sanger.ac.uk 2016

DecoyPYrat is a Python 3.x program, basic usage to generate a hybrid decoy database using default tryptic cleavage rules:

python decoyPYrat.py example.fasta

 

Full usage:

python decoyPYrat.py [-h] [--cleavage_sites CSITES]
                      [--anti_cleavage_sites NOC] [--cleavage_position {c,n}]
                      [--min_peptide_length MINLEN] [--max_iterations MAXIT]
                      [--do_not_shuffle] [--do_not_switch]
                      [--decoy_prefix DPREFIX] [--output_fasta DOUT]
                      [--temp_file TOUT] [--no_isobaric] [--memory_save]
                      *.fasta|*.fa

positional arguments:
  *.fasta|*.fa          FASTA file of target proteins sequences for which to create decoys

optional arguments:
  -h                            Show help message and exit
  -c CSITES              A list of amino acids at which to cleave during digestion. Default = KR
  -a NOC                   A list of amino acids at which not to cleave if following cleavage site ie. Proline. Default = none
  -p {c,n}                   Set cleavage to be c or n terminal of specified cleavage sites. Default = c
  -l MINLEN             Set minimum length of peptides to compare between target and decoy. Default = 5
  -n MAXIT               Set maximum number of times to shuffle a peptide to make it non-target before failing. Default=100
  -x                            Turn OFF shuffling of decoy peptides that are in the target database. Default=false
 -s                             Turn OFF switching of cleavage site with preceding amino acid. Default=false
  -d DPREFIX           Set accesion prefix for decoy proteins in output. Default=XXX
  -o DOUT                Set file to write decoy proteins to. Default=decoy.fa
  -t TOUT                 Set temporary file to write decoys prior to shuffling. Default=tmp.fa
  -i                            Do not make decoy peptides isobaric. Default=false
 -m                          Slower but uses less memory (does not store decoy peptide list). Default=false

Copyright (c) 2016 James Christopher Wright - Wellcome Trust Sanger Institute

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
 

Contact
james.wright@sanger.ac.uk

Please Cite:
J Proteomics Bioinform. 2016 Jun 27;9(6):176-180.
DecoyPyrat: Fast Non-redundant Hybrid Decoy Sequence Generation for Large Scale Proteomics.
Wright JC1, Choudhary JS1.
Author information

Abstract
Accurate statistical evaluation of sequence database peptide identifications from tandem mass spectra is essential in mass spectrometry based proteomics experiments. These statistics are dependent on accurately modelling random identifications. The target-decoy approach has risen to become the de facto approach to calculating FDR in proteomic datasets. The main principle of this approach is to search a set of decoy protein sequences that emulate the size and composition of the target protein sequences searched whilst not matching real proteins in the sample. To do this, it is commonplace to reverse or shuffle the proteins and peptides in the target database. However, these approaches have their drawbacks and limitations. A key confounding issue is the peptide redundancy between target and decoy databases leading to inaccurate FDR estimation. This inaccuracy is further amplified at the protein level and when searching large sequence databases such as those used for proteogenomics. Here, we present a unifying hybrid method to quickly and efficiently generate decoy sequences with minimal overlap between target and decoy peptides. We show that applying a reversed decoy approach can produce up to 5% peptide redundancy and many more additional peptides will have the exact same precursor mass as a target peptide. Our hybrid method addresses both these issues by first switching proteolytic cleavage sites with preceding amino acid, reversing the database and then shuffling any redundant sequences. This flexible hybrid method reduces the peptide overlap between target and decoy peptides to about 1% of peptides, making a more robust decoy model suitable for large search spaces. We also demonstrate the anti-conservative effect of redundant peptides on the calculation of q-values in mouse brain tissue data.

KEYWORDS:
Database searching; FDR; Python; Sequence database; Shotgun proteomics; Target-decoy
PMID: 27418748 PMCID: PMC4941923 DOI: 10.4172/jpb.1000404
