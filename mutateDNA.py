import sys # for read argv
import random

if __name__ == "__main__":
    originFileName = "origin_dna.txt"
    mutationRate = 0.05

    argvLength = len(sys.argv)
    if argvLength >= 2:
        originFileName = sys.argv[1]
    if argvLength >= 3:
        mutationRate = float(sys.argv[2])

    originFile = open(originFileName, "r")
    mutateFile = open("mutate_dna.txt", "w")

    originDNA = originFile.readline()
    mutateDNA = originDNA
    DNALength = len(originDNA)

    mutationLength = int(DNALength * mutationRate)

    for i in range(0, mutationLength):
        index = random.randint(0, DNALength)
        mutateOrigin = originDNA[index - 1]
        mutateTo = random.choice('ACGT'.replace(mutateOrigin, ''))
        mutateDNA = "".join((mutateDNA[:index-1], mutateTo, mutateDNA[index:]))

    mutateFile.write(mutateDNA)

    originFile.close()
    mutateFile.close()

    print("DNA length : " + str(len(originDNA)))
    print("target mutation rate : " + str(mutationRate))
    print("target mutation count : " + str(mutationLength))
    print("mutate success!")