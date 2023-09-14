import os
import numpy as np



def main():
    #print("test")

    
    DNAstring = np.genfromtxt("3/rosalind_revc.txt", dtype=str)
    DNAstring = str(DNAstring)
    DNAstring = DNAstring[::-1]
    DNAstring = np.array(list(DNAstring))

    for x in range(len(DNAstring)):
        if DNAstring[x] == "A":
            DNAstring[x] = "T"
        elif DNAstring[x] == "T":
            DNAstring[x] = "A"
        elif DNAstring[x] == "G":
            DNAstring[x] = "C"
        elif DNAstring[x] == "C":
            DNAstring[x] = "G"

    DNAstring = "".join(DNAstring)



    print(DNAstring)


if __name__ == "__main__":
    main()