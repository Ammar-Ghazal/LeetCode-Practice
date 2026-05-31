class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        """
        defaultdict(list) is used because of this line:
            anagMap[tuple(count)].append(s)
        on a regular dict the first time the key is accessed, it still doesnt exist, and will throw an error when you try to append to nothing
        defaultdict(list) auto-creates an empty list for any missing key, so we can "append" before creating the key, so it basically does this but prettier:
            if key not in d:
                d[key] = []
            d[key].append(value)
        """
        
        for s in strs:
            output[tuple(sorted(s))].append(s)

        return list(output.values())

        """
            output = {
                (1,0,1,0,1,0,...): ["eat", "tea"],
                (0,1,1,0,0,0,...): ["bat"]
            }

            output.values() → (a special view object, not a list)
                → dict_values([["eat","tea"], ["bat"]])

            list(output.values()) → (an actual list)
                → [["eat","tea"],["bat"]]
        """
