from Scripts.FASTAparser import FASTAparser

# N{P}[ST]{P}


def main():
    with open("data.txt") as f:
        content = f.readlines()
    content = [x.strip() for x in content]


    for x in range(len(content)):

        fasta = FASTAparser(content[x])
    
        check = False

        for y in range(len(fasta)-3):

            if fasta[y] == "N" and fasta[y+1] != "P" and fasta[y+2] in ["S", "T"] and fasta[y+3] != "P":

                if check == False:
                    print(content[x])
                    check = True

                print(y+1, end=" ")





if __name__ == "__main__":
    main()