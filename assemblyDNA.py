import time
def bitap(pattern, text, mismatch=3):
    m = len(pattern)
    S_table = {
        'A': 0,
        'C': 0,
        'G': 0,
        'T': 0
    }

    for i, c in enumerate(pattern):
        S_table[c] |= 1 << i
    # 테이블 생성 for masking

    R0 = 0
    R1 = 0
    R2 = 0
    mask = 1 << (m - 1) 

    j = 0
    while j < len(text):
        c = text[j]
        j+=1

        S = S_table[c] # 해당 문자에 대한 pattern 마스킹 숫자 가져옴
        shR0 = (R0 << 1) | 1 # 이전 text에 대한 정보들 + 현재 정보를 갖기위한 마스킹
        R0 = shR0 & S 
        R1 = ((R1 << 1) | 1) & S | shR0 
        R2 = ((R2 << 2) | 3) & S | shR0

        if R0 & mask: # exact match
            return j - m
        elif R1 & mask: # match with one substitution
            return j - m
        elif R2 & mask: # match with two substitutions
            return j - m

def bruteforce(shortread, originDNA, mismatch=3):
    originLength = len(originDNA)
    shortreadLength = len(shortread)

    for i in range(0, originLength - shortreadLength):
        _mismatch = 0
        isMathched = True
        for j in range(0, len(shortread)):
            if originDNA[i+j] == shortread[j]:
                continue
            elif originDNA[i+j] != shortread[j] and _mismatch < mismatch:
                _mismatch = _mismatch + 1
            else:
                isMathched = False
                break

        if isMathched:
            return i

    return None

def bm():
    def acgt(char):
        if char == "A":
            return 0
        elif char == "C":
            return 1
        elif char == "G":
            return 2
        else:
            return 3

    def badCharHeuristic(string, size): 
        badChar = [-1]*4 
    
        for i in range(size): 
            badChar[acgt(string[i])] = i; 
    
        return badChar 
    
    def search(shortRead, originDNA, mismatch=3): 
        m = len(shortRead) 
        n = len(originDNA) 

        badChar = badCharHeuristic(shortRead, m)  

        s = 0
        while(s <= n-m): 
            j = m-1

            while j>=0 and shortRead[j] == originDNA[s+j]:
                j -= 1

            if j<0: 
                return s
            else: 
                s += max(1, j-badChar[acgt(originDNA[s+j])]) 

    return search


def kmp():
    def partial(pattern):
        ret = [0]

        for i in range(1, len(pattern)):
            j = ret[i-1]
            while j > 0 and pattern[j] != pattern[i]:
                j = ret[j-1]
            ret.append(j + 1 if pattern[j] == pattern[i] else j)
        return ret
    
    def resultFunction(shortread, originDNA, mismatch=3):
        part, result, j = partial(shortread), [], 0

        for i in range(len(originDNA)):
            while j > 0 and originDNA[i] != shortread[j]:
                j = part[j - 1]
            if originDNA[i] == shortread[j]: j += 1
            if j == len(shortread): 
                result = i - (j - 1) 
                break

        return result

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
    print("assembly legnth : " + str(assemblyLength))
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
    assemblyDNA = assembly(shortreads, originDNA, kmp())
    runtime = Timer.finish()
    writeDNA(assemblyDNA, "assembly_dna.txt")
    compareDNA(originDNA, assemblyDNA)
    print("execute time : " + str(runtime))