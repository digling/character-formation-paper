# Source code and data accompanying the paper "Studying Old Chinese phonology by exploring character formation patterns"

## Requirements

If you want to run all scripts such as we did, and want to convert the data as well to PDF, you need to install pandoc (version 1.16.0.2 was the one we used).

Otherwise, all dependencies in terms of Python3 code, assuming that you have the program pip installed along with Python3, can be installed by typing:

```shell
$ pip install -r pip-requirements.txt
```

## Running the scripts

We supply a makefile to make it convenient to run all code.

To re-compile the data we used, type:
```
$ make dataset
```

To carry out the analysis for A/B distinction (`sandeng`), type:

```
$ make sandeng
```

Similarly, you can run the analysis on `kl` (that is, on velar-liquid clusters in the OC script), or on `uvulars` (which tests to which degree the ancient script reflects uvulars). 

To run all analyses, just type:

```
$ make all
```

If you want to convert your results to PDF, run

```
$ make all-p
```

In all cases, the files with the results of the analyses will be written to the folder `output/`, in form of HTML and PDF.
