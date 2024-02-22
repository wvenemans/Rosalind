from urllib.request import urlopen

def FASTAparser(proteinID):

    #get the fasta file from uniprot
    url = 'https://www.uniprot.org/uniprot/'+proteinID+'.fasta'
    fasta = urlopen(url).read().decode('utf-8')

    #remove the first line
    fasta = fasta.split('\n', 1)[1]
    #remove the newlines
    fasta = fasta.replace('\n', '')

    return fasta