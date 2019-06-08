import sys
import random

if __name__ == "__main__":
    targetFileName = "mutate_dna.txt"
    destFileName = "short_read.txt"
    shortLength = 50
    shortCount = 200

    argvLength = len(sys.argv)
    if argvLength >= 2:
        targetFileName = sys.argv[1]
    if argvLength >= 3:
        destFileName = sys.argv[2]
    if argvLength >= 4:
        shortLength = int(sys.argv[3])
    if argvLength >= 5:
        shortCount = int(sys.argv[4])
    
    targetFile = open(targetFileName, 'r')
    destFile = open(destFileName, 'w')

    targetString = targetFile.readline()
    targetLength = len(targetString)

    for i in range(0, shortCount):
        index = random.randint(0, targetLength - shortLength - 1)
        shortRead = targetString[index: index+shortLength]
        destFile.write(shortRead + '\n')

    targetFile.close()
    destFile.close()

    print("target length : " + str(targetLength))
    print("short read length : " + str(shortLength))
    print("short reads count : " + str(shortCount))
    print("short reads rate : " + str(shortCount * shortLength / targetLength))
    print("short read success!")