class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        size = len(beginWord)
        

        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        wordPermutations = defaultdict(list)
        for word in wordList:
            for i in range(size):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                wordPermutations[word[:i] + "*" + word[i + 1 :]].append(word)

        # Queue for BFS
        queue = collections.deque([(beginWord, 1)])
        # Visited to make sure we don't repeat processing same word.
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.popleft()
            for i in range(size):
                # Intermediate words for current word
                intermediate_word = (
                    current_word[:i] + "*" + current_word[i + 1 :]
                )

                # Next states are all the words which share the same intermediate state.
                for word in wordPermutations[intermediate_word]:
                    # If at any point if we find what we are looking for
                    # i.e. the end word - we can return with the answer.
                    if word == endWord:
                        return level + 1
                    # Otherwise, add it to the BFS Queue. Also mark it visited
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                wordPermutations[intermediate_word] = []
        return 0
