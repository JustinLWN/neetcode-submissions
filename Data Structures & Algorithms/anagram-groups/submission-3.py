class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Dict = {}
        for word in strs:
            s_word = "".join(sorted(word))
            if s_word not in Dict:
                Dict[s_word] = []
            Dict[s_word].append(word)

        result = []
        for k,v in Dict.items():
            result.append(v)
        return result