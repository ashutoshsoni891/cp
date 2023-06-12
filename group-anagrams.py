class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def calcASCII(s):
            sum = 0
            for c in s:
                sum += ord(c)
            return sum

        def getASCIIMap(arrStrings):
            asciiMap = {}
            for s in strs:

                asciiValue = calcASCII(s)
                key = str(asciiValue)

                if key not in asciiMap.keys():
                    asciiMap[key] = [s]
                else:
                    asciiMap[key].append(s)

            return asciiMap

        asciiMap = getASCIIMap(strs)
        resultArr = []
        for v in asciiMap.values():
            resultArr.append(v)
        return resultArr
