def main():


    with open('12 - OLC\data.txt') as f:
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

    for dna1 in DNA:
        for dna2 in DNA:

            if dna1 != dna2:

                if DNA[dna1][-3:] == DNA[dna2][:3]:

                    print(dna1, dna2)
    

if __name__ == '__main__':
    main()