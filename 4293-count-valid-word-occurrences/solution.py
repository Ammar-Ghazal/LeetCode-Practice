class Solution:
    def countWordOccurrences(self, chunks: list[str], queries: list[str]) -> list[int]:
        from collections import Counter
        
        s = "".join(chunks)
        words = []
        i = 0
        n = len(s)
        
        while i < n:
            # skip non-word characters (separators)
            if not s[i].isalpha():
                i += 1
                continue
            
            # build a word starting at i
            start = i
            while i < n:
                if s[i].isalpha():
                    i += 1
                # hyphen counts as joiner only if surrounded by lowercase letters
                elif s[i] == '-' and i + 1 < n and s[i+1].isalpha():
                    i += 1
                else:
                    break
            
            words.append(s[start:i])
        
        counts = Counter(words)
        return [counts[q] for q in queries]
