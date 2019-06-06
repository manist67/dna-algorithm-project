import sys

if __name__ == "__main__":
    originFileName = "origin_dna.txt"
    mutateFileName = "mutate_dna.txt"

    argvLength = len(sys.argv)
    if argvLength >= 2:
        originFileName = sys.argv[1]
    if argvLength >= 3:
        mutateFileName = sys.argv[2]

    originFile = open(originFileName)
    mutateFile = open(mutateFileName)
    
    originDNA = originFile.readline()
    mutateDNA = mutateFile.readline()
    
    originDNALength = len(originDNA)
    mutateDNALength = len(mutateDNA)

    if originDNALength != mutateDNALength:
        print("origin DNA length : " + str(originDNALength))
        print("mutate DNA length : " + str(mutateDNALength))
        print("DNA length is not matched!")
        print("mutate fail!")
        exit(0)
    
    mutationCount = 0
    for i in range(0, originDNALength):
        if originDNA[i] != mutateDNA[i]:
            mutationCount+=1

    mutationRate = mutationCount / originDNALength

    originFile.close()
    mutateFile.close()

    print("origin dna length : " + str(originDNALength))
    print("mutate dna length : " + str(mutateDNALength))
    print("mutation count : " + str(mutationCount))
    print("mutation rate : " + str(mutationRate))