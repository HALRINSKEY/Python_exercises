def check_parentheses(a_string):
    little_stack = []
    midlle_stack = []

    for c in a_string:
        if c == "(":
            little_stack.append(c)
        if c == ")":
            if len(little_stack) == 0:
                return False
            else:
                little_stack.pop()

        if c == "{":
            midlle_stack.append(c)
        if c == "}":
            if len(midlle_stack) == 0:
                return False
            else:
                midlle_stack.pop()

    return not (little_stack and midlle_stack)

print(check_parentheses("(}{)"))

class MaxStack():
    def __init__(self) -> None:
        self.main = []
        self.max = []

    def push(self, n):
        if len(self.main) == 0:
            self.max.append(n)
        elif n >= self.max[-1]:
            self.max.append(n)
        else:
            self.max.append(self.max[-1])

        self.main.append(n)


    def pop(self):
        self.max.pop()
        return self.main.pop()
    
    def get_max(self):
        return self.max[-1]





