import os
import numpy as np



def main():
    #print("test")

    
    DNAstring = np.genfromtxt("1/rosalind_dna.txt", dtype=str)
    DNAstring = str(DNAstring)
    A = DNAstring.count("A")
    C = DNAstring.count("C")
    G = DNAstring.count("G")
    T = DNAstring.count("T")

    print(A, C, G, T)





if __name__ == "__main__":
    main()