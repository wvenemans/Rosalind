def main():

    with open('9 - Motif\data.txt') as f:
        data = f.readlines()

    data = [x.strip() for x in data]

    dnastring = data[0]
    motif = data[1]

    motifLocations = []

    for i in range(len(dnastring)):
        if dnastring[i:i+len(motif)] == motif:
            motifLocations.append(i+1)

    motifLocations = str(motifLocations).strip('[]').replace(',', '')

    print(motifLocations)



if __name__ == "__main__":   
    main()