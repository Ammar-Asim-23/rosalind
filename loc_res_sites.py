'''
Locating Restriction Sites

Problem

Figure 2. Palindromic recognition site
A DNA string is a reverse palindrome if it is equal to its reverse complement. 
For instance, GCATGC is a reverse palindrome because its reverse complement is GCATGC.

Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string having length between 4 and 12. 
You may return these pairs in any order
'''

def parse_fasta(data):
    """Parse FASTA format data into a dictionary with labels as keys and DNA strings as values."""
    fasta_dict = {}
    for entry in data:
        if entry.strip():
            lines = entry.strip().split('\n')
            label = lines[0]
            dna_sequence = ''.join(lines[1:])
            fasta_dict[label] = dna_sequence
    return fasta_dict

def reverse_complement(sequence):
    """Return the reverse complement of a DNA sequence."""
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in reversed(sequence))

def find_reverse_palindromes(dna, min_len=4, max_len=12):
    """Find all reverse palindromes in the DNA string within the given length range."""
    results = []
    for start in range(len(dna)):
        for length in range(min_len, max_len + 1):
            end = start + length
            if end > len(dna):
                break
            substring = dna[start:end]
            if substring == reverse_complement(substring):
                results.append((start + 1, length))
    return results

# Input data
with open('input.txt', 'r') as file:
    fasta_data = file.read().strip().split('>')


fasta_dict = parse_fasta(fasta_data)
dna_sequence = next(iter(fasta_dict.values()))

palindromes = find_reverse_palindromes(dna_sequence)

with open('output.txt', 'w') as file:
    for position, length in palindromes:
        file.write(f"{position} {length}\n")

print("Output written to output.txt")