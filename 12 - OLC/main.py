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

    overlap = 1

    for dna1 in DNA:
        for dna2 in DNA:
                if dna1 != dna2:
                    while DNA[dna1][-overlap:] == DNA[dna2][:overlap]:
                        overlap += 1
    
                    print(dna1, dna2, DNA[dna1][-overlap:], DNA[dna2][:overlap])
    



    

    

if __name__ == '__main__':
    main()