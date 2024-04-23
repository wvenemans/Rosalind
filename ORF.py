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
    

    DNAString = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"

    


    RNAString = DNAString.replace("T", "U")
    complement = RNAString.replace("A", "u").replace("U", "a").replace("C", "g").replace("G", "c").upper()[::-1]

    print(RNAString)
    print(complement)


    protein = ""

    for i in range(0, len(RNAString)):

        if RNAString[i:i+3] == "AUG":
            protein = "M"

            for i in range(i+3, len(RNAString), 3):

                if RNAString[i:i+3] in rna_codex[''] or i+3 > len(RNAString):
                    print(protein)
                    break

                for key, value in rna_codex.items():
                    if RNAString[i:i+3] in value:
                        protein += key
                        break

    for i in range(0, len(complement)):
        if RNAString[i:i+3] == "AUG":
            protein = "M"

            for i in range(i+3, len(RNAString), 3):

                if RNAString[i:i+3] in rna_codex[''] or i+3 > len(RNAString):
                    print(protein)
                    break

                for key, value in rna_codex.items():
                    if RNAString[i:i+3] in value:
                        protein += key
                        break




if __name__ == "__main__":
    main()