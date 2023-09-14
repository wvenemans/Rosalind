import numpy as np

def main():
    print("test")


    info = np.genfromtxt("4- Rabbits/rosalind_fib.txt", dtype=int)
    months = info[0]
    litter = info[1]

    rabbits = [1, 1]
    for x in range(2, months):
        rabbits.append(rabbits[x-1] + rabbits[x-2]*litter)

    print(rabbits)
    

if __name__ == "__main__":
    main()