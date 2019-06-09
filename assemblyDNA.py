import time

def bruteforce(shortread, originDNA, missmatch=3):
    originLength = len(originDNA)
    shortreadLength = len(shortread)

    for i in range(0, originLength - shortreadLength):
        _missmatch = 0
        isMathched = True
        for j in range(0, len(shortread)):
            if originDNA[i+j] == shortread[j]:
                continue
            elif originDNA[i+j] != shortread[j] and _missmatch < missmatch:
                _missmatch = _missmatch + 1
            else:
                isMathched = False
                break

        if isMathched:
            return i

    return None

def kmp(originDNA):
    def resultFunction(shortread, originDNA):
        return None

    return resultFunction

def readShortSequence(filename):
    file = open(filename, 'r')
    shortreads = file.read().splitlines()
    return shortreads

def readOriginDNA(filename):
    file = open(filename, 'r')
    originDNA = file.read()

    return originDNA

def assembly(shortreads, originDNA, getPosition=bruteforce):
    assembly = '-' * len(originDNA)

    for shortread in shortreads:
        length = len(shortread)
        index = getPosition(shortread, originDNA)
        if index:
            assembly = assembly[:index] + shortread + assembly[index + length:]

    return assembly

    
def writeDNA(assembly, filename):
    file = open(filename, 'w')
    file.write(assembly)

def compareDNA(originDNA, assemblyDNA):
    originLength = len(originDNA)
    assemblyLength = len(assemblyDNA)

    matchCount = 0

    for i in range(0, originLength):
        if originDNA[i] == assemblyDNA[i]:
            matchCount = matchCount + 1

    print("origin length : " + str(originLength))
    print("aseembly legnth : " + str(assemblyLength))
    print("matched count : " + str(matchCount))
    print("match rate : " + str(matchCount / originLength))

class Timer:
    time = None

    @staticmethod
    def start():
        if Timer.time:
            raise Exception("already run")

        Timer.time = time.time()
    
    @staticmethod
    def finish():
        if not Timer.time:
            raise Exception("not started")

        executeTime = time.time() - Timer.time
        Timer.time = None
        return executeTime

if __name__ == "__main__":
    shortreads = readShortSequence("short_read.txt")
    originDNA = readOriginDNA("origin_dna.txt")
    Timer.start()
    assemblyDNA = assembly(shortreads, originDNA)
    runtime = Timer.finish()
    writeDNA(assemblyDNA, "assembly_dna.txt")
    compareDNA(originDNA, assemblyDNA)
    print("execute time : " + str(runtime))