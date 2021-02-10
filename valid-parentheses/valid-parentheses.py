class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map_ = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        for char in s:
            if char in map_ and stack and stack[-1] == map_[char]:
                stack.pop()
            else:
                stack.append(char)
        
        return False if stack else True
                