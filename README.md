# dna-sequencing [![Build Status](https://travis-ci.com/cheukky/dna-sequencing.svg?branch=master)](https://travis-ci.com/cheukky/dna-sequencing)
A small project that accepts a string and outputs various statistics for it

This program accepts a string of characters and calculates the following:

* The number of As (upper or lower case)
* The number of Cs (upper or lower case)
* The number of Gs (upper or lower case)
* The number of Ts (upper or lower case)
* The number of other characters.
* The percentage that each group represents in the input string.
* The greatest number of consecutive As (upper or lower case).
* The greatest number of consecutive Cs (upper or lower case).
* The greatest number of consecutive Gs (upper or lower case).
* The greatest number of consecutive Ts (upper or lower case).

The output is printed to console and the function also returns a dicionary of the results.
Can be run on the CLI like this
```python
python dna_sequencing.py [sequence to be interpreted]
```
