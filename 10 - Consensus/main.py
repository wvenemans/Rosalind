import numpy as np

def main():

    with open('10 - Consensus\data.txt') as f:
        data = f.readlines()


    DNA = dict()

    data = [x.strip() for x in data]
    length = 0

    for line in data:
        if line.startswith('>'):
            dna = line[1:]
            DNA[dna] = ''
        else:
            DNA[dna] += line
            length = len(DNA[dna])



    Adenine = np.zeros(length)
    Cytosine = np.zeros(length)
    Guanine = np.zeros(length)
    Thymine = np.zeros(length)

    for key, value in DNA.items():
        for i in range(len(value)-1):
            if value[i] == 'A':
                Adenine[i] += 1
            elif value[i] == 'C':
                Cytosine[i] += 1
            elif value[i] == 'G':
                Guanine[i] += 1
            elif value[i] == 'T':
                Thymine[i] += 1

    consensus = ''

    for i in range(len(Adenine)):
        biggest = max(Adenine[i], Cytosine[i], Guanine[i], Thymine[i])
        if biggest == Adenine[i]:
            consensus += 'A'
        elif biggest == Cytosine[i]:
            consensus += 'C'
        elif biggest == Guanine[i]:
            consensus += 'G'
        elif biggest == Thymine[i]:
            consensus += 'T'

    print(consensus)

    with open('10 - Consensus\output.txt', 'w') as f:
        f.write(consensus)

        print('A: ', end='')
        f.write('\nA: ')
        for i in Adenine:
            print(int(i), end=' ')
            f.write(str(int(i)) + ' ')

    print('\nC: ', end='')
    f.write('\nC: ')
    for i in Cytosine:
        f.write(str(int(i)) + ' ')
        print(int(i), end=' ')

    print('\nG: ', end='')
    f.write('\nG: ')
    for i in Guanine:
        print(int(i), end=' ')
        f.write(str(int(i)) + ' ')

    print('\nT: ', end='')
    f.write('\nT: ')
    for i in Thymine:
        print(int(i), end=' ')
        f.write(str(int(i)) + ' ')
        


if __name__ == '__main__':
    main()