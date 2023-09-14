import os
import numpy as np



def main():
    #print("test")

    
    DNAstring = np.genfromtxt("2/rosalind_rna.txt", dtype=str)
    DNAstring = str(DNAstring)
    DNAstring = DNAstring.replace("T", "U")
    print(DNAstring)


if __name__ == "__main__":
    main()