


def main():
    print("test")

    with open("7 - Mendel/data.txt", "r") as f:
        data = f.read().split(" ")

    k = int(data[0])
    m = int(data[1])
    n = int(data[2])
    total = k + m + n

    chance = 0

    chance += (k/total) * ((k-1)/(total-1))
    chance += (k/total) * (m/(total-1))
    chance += (k/total) * (n/(total-1))

    chance += (m/total) * (k/(total-1))
    chance += (m/total) * ((m-1)/(total-1)) * 0.75

    chance += (m/total) * (n/(total-1)) * 0.5

    chance += (n/total) * (k/(total-1))
    chance += (n/total) * (m/(total-1)) * 0.5

    

    print(chance)



"""	
AA x AA = 1 
AA x Aa = 1
AA x aa = 1
Aa x Aa = 1
Aa x aa = 0.5

"""	


if __name__ == "__main__":
    main()