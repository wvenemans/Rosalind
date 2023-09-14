import numpy as np

def main():


    with open("6- Point Mutations/data.txt", "r") as f:
        DNAstring = f.readlines()

        DNAstring = [x.strip() for x in DNAstring]
        hammingDistance = 0

        for x in range(len(DNAstring[0])):
            if DNAstring[0][x] != DNAstring[1][x]:
                hammingDistance += 1


        print(hammingDistance)





if __name__ == "__main__":
    main()