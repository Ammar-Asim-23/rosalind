sample = '''TCATCATTGTATACCATAGCTCACTTTGTTGCGTCACAGCCCCTGAACATCAGGCCTAACCTGAGTCTCTGACCTTTTTACTGTCGAGCTTCATTGGTCGAGGATCCTGGACTACCCGCGACGGAAGTCAGCTGTCGCAGTACTAAACATGACTACGTTGCGAACCTCGTCACAGAGCCATGAGGATTAGCATACCGATGAGGTGCCAGTTGGAAGTGGTAAATCGTCGGAACCTGCATACACGTCGTAGGACGAGCCCGAACAGAAAAGCCAGGAGCTCCAGCTATCCTGCACGCCGTGTACAAAGAGTTACAACAACCTTTACGAGGATAGGACCAGAACTCCGACAGTAAGGGGCCGAACGTGCACCTAGTTCTGGGCTCGCGACAGAGGGATGATGCGCTGCGATTTGTGCTCAAGCCCACAGTATATGGTGATTTATAGTTCGTCTCCCTCAAGAACCGAGTCCGATTCCGTTAAATACCCGACTAATCCAGTAGGGCCATGTTCATGGTAGGTGCTGTAATGGTCGTGAGACAATAAACATATGCTCACTGATCGTAAGTCCTCCCATACAAACGGCGCCGTGAATGTGCGTCCCCCTTGTTACGAGAATGGATTATGTCCACGCCATTCTAGTTCTGTACGATGGGGGTTCGCCATACTCGGATCAAACAAAGTACGGTAGCCAGATTTTCGGTGGGTACCTGGGGCGCTGTGCACAAAGCGTAAGCGAGAGATTGGAGAATTCCCGGGCCTCATATATGCAGGCCTCCAGACTCTGACCGTGGATTTCATAATGGGAAAGATAAGGTTCGCCAGTAGATCGTCTCTTTCAGGCTCTAGAGTAAGTTT'''

dic = {
    'A':'T',
    'T':'A',
    'G':'C',
    'C':'G',
}
result=''
for i in sample:
    result += dic[i]

result = result[::-1]
print(result)