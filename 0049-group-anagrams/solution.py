class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Time Complexity: O(m*n) -> m is the number of given strings, and n is the average length of each string
        # Space Complexity: ?
        
        # hashmap mapping charCount to list of anagrams
        anagMap = defaultdict(list)
        """
        defaultdict(list) is used because the line:
            anagMap[tuple(count)].append(s)
        on a regular dict the first time the key is accessed, since the key doesnt exist it, and there is nothing to append to :)
        defaultdict(list) auto-creates an empty list for any missing key, so we can append directly before creating the key, so it basically does this but prettier:
            if key not in d:
                d[key] = []
            d[key].append(value)
        """

        for s in strs:
            # array to represent a string by the count of each of its letters
            count = [0] * 26 

            # add the number of each letter in its corresponding index (a is 0, b is 1, etc)
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            # since lists cant be keys in python, we use tuple, add the string to the map value
            anagMap[tuple(count)].append(s)

        return list(anagMap.values())
        """
            anagMap = {
                (1,0,1,0,1,0,...): ["eat", "tea"],
                (0,1,1,0,0,0,...): ["bat"]
            }

            anagMap.values() → (a special view object, not a list)
                → dict_values([["eat","tea"], ["bat"]])

            list(anagMap.values()) → (an actual list)
                → [["eat","tea"],["bat"]]
        """
