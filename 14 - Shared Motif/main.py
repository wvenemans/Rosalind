def main():
    
    with open('14 - Shared Motif\data.txt') as f:
        data = f.readlines()

    DNA = dict()

    data = [x.strip() for x in data]

    for line in data:

        if line.startswith('>'):

            dna = line[1:]
            DNA[dna] = ''

        else:

            DNA[dna] += line

    DNA = list(DNA.values())

    longestMotif = ''

    for i in range(len(DNA[0])):

        for j in range(i + 1, len(DNA[0]) + 1):

            motif = DNA[0][i:j]

            if all(motif in dna for dna in DNA):

                if len(motif) > len(longestMotif):
                    
                    longestMotif = motif

    print(longestMotif)

    


if __name__ == '__main__':
    main()