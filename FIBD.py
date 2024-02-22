def main():

    month = 95
    death = 20

    rabbits = []
    for x in range(month):
        if x < 2:
            rabbits.append(1)

        elif (x < death) or (death == 0):
            rabbits.append(rabbits[x-1] + rabbits[x-2])

        elif x == death:
            rabbits.append(rabbits[x-1] + rabbits[x-2] - 1)
        else:
            rabbits.append(rabbits[x-1] + rabbits[x-2] - rabbits[x-(death+1)])
    
    print(rabbits[-1])



if __name__ == '__main__':
    main()