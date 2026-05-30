class Solution:
    def passwordStrength(self, password: str) -> int:
        seen = set()
        strength = 0
        for p in password:
            if p not in seen:
                seen.add(p)
                if ord('a') <= ord(p) <= ord('z'):
                    strength += 1
                elif ord('A') <= ord(p) <= ord('Z'):
                    strength += 2
                elif ord('0') <= ord(p) <= ord('9'):
                    strength += 3
                elif p == '!' or p == '@' or p == '#' or p == '$':
                    strength += 5

        return strength
