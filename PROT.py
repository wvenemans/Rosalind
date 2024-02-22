import numpy as np
def main():

    

    rna_codex = {
            'A': ['GCU', 'GCC', 'GCA', 'GCG'],
            'C': ['UGU', 'UGC'],
            'D': ['GAU', 'GAC'],
            'E': ['GAA', 'GAG'],
            'F': ['UUU', 'UUC'],
            'G': ['GGU', 'GGC', 'GGA', 'GGG'],
            'H': ['CAU', 'CAC'],
            'I': ['AUU', 'AUC', 'AUA'],
            'K': ['AAA', 'AAG'],
            'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
            'M': ['AUG'],
            'N': ['AAU', 'AAC'],
            'P': ['CCU', 'CCC', 'CCA', 'CCG'],
            'Q': ['CAA', 'CAG'],
            'R': ['AGA', 'AGG', 'CGU', 'CGC', 'CGA', 'CGG'],
            'S': ['AGU', 'AGC', 'UCU', 'UCC', 'UCA', 'UCG'],
            'T': ['ACU', 'ACC', 'ACA', 'ACG'],
            'V': ['GUU', 'GUC', 'GUA', 'GUG'],
            'W': ['UGG'],
            'Y': ['UAU', 'UAC'],
            '': ['UGA', 'UAA', 'UAG']
            }
    

    with open("8 - Protein translation/data.txt", "r") as f:
        data = f.readlines()

    data = data[0]
    protein = ""

    x = 0
    while x < len(data): 

        Codon = ""
        Codon += data[x]
        Codon += data[x+1]
        Codon += data[x+2]
        
        for key, value in rna_codex.items():
            if Codon in value:
                protein += key
                break

        x = x + 3
    

    print(protein)
    newFile = np.savetxt("8 - Protein translation/protein.txt", [protein], fmt="%s")



if __name__ == "__main__":
    main()