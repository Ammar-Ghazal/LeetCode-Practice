class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        # Time complexity: O(N*L^2), N -> length of wordList, L -> length of each word
        # Space complexity: O(N*L), if we treat word length as constant, O(N) for both time and space
        if endWord not in wordList: return 0

        queue, wordList = deque([beginWord]), set(wordList)
        changes = 1
        alph = "abcdefghijklmnopqrstuvwxyz"

        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur == endWord:
                    return changes
            
                for i in range(len(cur)):
                    prefix, suffix = cur[:i], cur[i+1:]
                    for letter in alph:
                        word = prefix + letter + suffix # this takes O(L) time since we are copying to a new string
                        if word in wordList:
                            queue.append(word)
                            wordList.remove(word)
                    
            changes += 1
        
        return 0
