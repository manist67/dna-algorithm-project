import sys # sys for input arguments
import random # random for generate the random string

if __name__ == "__main__":
    dnaLength = 10000
    if len(sys.argv) == 2:
        dnaLength = int(sys.argv[1])

    fileWrite = open("origin_dna.txt", "w")

    newDNA = ''.join(random.choice('ACGT') for _ in range(0, dnaLength))

    fileWrite.write(newDNA)

    fileWrite.close()

    print("generate success!")