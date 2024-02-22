import numpy as np
def main():

    genotypeDistrubution = np.genfromtxt('13 - E(Offspring)\data.txt', delimiter=' ')
    expected_value = 0

    for i in range(len(genotypeDistrubution)):
        # AA-AA
        if i == 0:
            expected_value += genotypeDistrubution[i] * 2
        # AA-Aa
        elif i == 1:
            expected_value += genotypeDistrubution[i] * 2
        # AA-aa
        elif i == 2:
            expected_value += genotypeDistrubution[i] * 2
        # Aa-Aa
        elif i == 3:
            expected_value += genotypeDistrubution[i] * 1.5
        # Aa-aa
        elif i == 4:
            expected_value += genotypeDistrubution[i] * 1
        # aa-aa
        elif i == 5:
            expected_value += genotypeDistrubution[i] * 0

    print(expected_value)

    

    

if __name__ == '__main__':
    main()