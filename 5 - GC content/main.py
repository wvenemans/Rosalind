import numpy as np
import os

def main():


    with open("5 - GC content/test.txt") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    

    biggest = 0
    biggestName = ""

    for x in range(len(content)):

        if content[x][0] == ">":

            name = content[x]

            DNAstring = ""

            for y in range(x+1, len(content)):

                if content[y][0] == ">":

                    break

                else:

                    DNAstring += content[y]

            DNAstring = np.array(list(DNAstring))

            count = 0

            for z in range(len(DNAstring)):

                if DNAstring[z] == "G" or DNAstring[z] == "C":

                    count += 1

            if count/len(DNAstring) > biggest:

                biggest = count/len(DNAstring)
                
                biggestName = name


    print(biggestName)
    print(biggest*100)
        






if __name__ == "__main__":
    main()