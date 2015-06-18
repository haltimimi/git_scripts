digitLetters = {"2": 'abc', "3": 'def', "4": 'ghi', "5": 'jkl', "6": 'mno', "7": 'prs', "8": 'tuv', "9": 'wxy'}

def getLetters(number): 
    result = []
    for digit in number:
        if digit in digitLetters:
            result.append(digitLetters[digit])
        else:
            result.append(digit)
    return result

def getCombinations(letterList):
    if len(letterList) == 1:
        return list(letterList[0])
    else:
        result = []
        for letter in letterList[0]:
            result = result + (map(lambda x: letter + x, getCombinations(letterList[1:]))) 
        return result

def run(number):
    print getCombinations(getLetters(number))

