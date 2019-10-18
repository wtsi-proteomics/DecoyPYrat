# DecoyPYrat
DecoyPYrat - Fast Hybrid Decoy Sequence Database Creation for Proteomic Mass Spectrometery Analyses

Accurate statistical evaluation of sequence database peptide identifications from tandem mass spectra is essential in mass spectrometry based proteomics experiments. These statistics are dependent on accurately modelling random identifications.

The target-decoy approach has risen to become the de-facto approach to calculating false discovery rates (FDR) in proteomic datasets. The main principle of this approach is to search a set of decoy protein sequences that emulate the size and composition of the target protein sequences searched whilst not matching real proteins in the sample.

DecoyPYrat creates decoy protein sequences by following these steps: each protein is reversed and the cleavage sites switched with preceding amino acid. Peptides are checked for existence in target sequences and if found the tool will attempt to shuffle them iterativly until they are unique.

## Download and Installation

### Bioconda

DecoyPYrat is available in the bioconda bioinformatics software repository. To access it, first install [Miniconda](https://docs.conda.io/en/latest/miniconda.html), and then run the command:

```shell
conda install -c bioconda decoypyrat
```

After this, you can invoke the software like this:

```shell
decoypyrat
```

### Direct script usage

You can clone this repository and invoke the software like this:

```shell
python decoypyrat/decoyPYrat.py
```

### Getting help

You can see the full usage instructions by specifying the "-h" argument:

If installing with Bioconda:
```shell
decoypyrat -h
```

If using the script directly:
```shell
python decoypyrat/decoyPYrat.py -h
```

## Citation:
[DecoyPyrat: Fast Non-redundant Hybrid Decoy Sequence Generation for Large Scale Proteomics.
J Proteomics Bioinform. 2016 Jun 27;9(6):176-180.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4941923/)
