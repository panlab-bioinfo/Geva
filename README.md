# GEVA Criteria for Completeness and Accuracy of Assemblies Assessment
## Assessment
GEVA is a software package for the completeness and accuracy assessment for genome assemblies.  

GEVA concludes 5 criteria for the assessment of synthetic datasets, three criteria are used to measure completeness, namely completeness rate (CR), single-copy completeness rate (SCR), and duplicated completeness rate (DCR). To evaluate the assembly accuracy, we announces two criteria, the average proportion of the largest category (APLC), and the average distance difference (ADF).   

GEVA is a software package written in python. ASSca5 runs as a command-line program with a variety of user-options and is freely available for download below, compatible for Unix/Linux/Mac OS.  


## Prerequisite
> * Python 3.7 (tested with Python v3.7.12) or higher
> * pandas v1.1.4 or higher

## Installation
You can compile a static version using the following command:  
``` git clone https://github.com/rookieluohh/benchmark ```  
``` cd benchmark ``` 

## Usage
`geva.py` is a python script used a reference genome and a assembly to assess synthetic datasets, which contains 5 parameters:  

    python geva [-h] -i INPUT -r REFERENCE [-k KMER_LENGTH] [-s SAMPLE] -o OUT_PREFIX  

where `-i` sets a input file of fasta format in use; `-r` sets the reference genome of assembly with fasta format; `-k` specifies the k-mer length used to assess the assembly, and the default value is `21`; `-s` means the number of reference unique k-mer used in the the assessment, the default value is `"all"`, using all reference unique kmers to assess the assembly will be slow for some complex genomes, so randomly sampling some reference unique kmers for assessment will greatly speed up the script and memory consumption, and we recommend the k is `200,000`; `-o` specifies the prefix of output files. 

For example, a typical assessment command line looks like:  

    python geva.py -i haplotype.fasta -r haplotype_ref.fasta -o test  

If the process of this script is running out of memory or too slow, we recommend you to use `-s` parameter:

    python geva.py -i haplotype.fasta -r haplotype_ref.fasta -s 200000 -o test 


## Citation
If you geva in any published work, please cite the following manuscript:  
***[Yu W, Luo H, Yang J, Zhang S, Jiang H, Zhao X, et al. Comprehensive assessment of 11 de novo HiFi assemblers on complex eukaryotic genomes and metagenomes. Genome Research. 2024](https://pubmed.ncbi.nlm.nih.gov/38428994/);***

