class Solution:
    '''
    This problem is related to evaluating expressions.
    Where in an open parenteheses, this indicates the expression is evaluated
    recursively.
    "(1+(4+5+2)-3)+(6+8)"

    We only support addition and subtraction operations so let's start there.
    '''

    def compute(self, operator, a, b):
        a, b = int(a), int(b)

        match operator:
            case "+":
                return a + b
            case "-":
                return a - b
            case _:
                raise RuntimeError("Unrecognized operator")

    '''
     1. addition
     2. subtraction
     3. minus sign as a unary operator.
    '''
    def calculate(self, s: str) -> int:
        a, b, operator = "", "", ""
        # store results in a

        i, n = 0, len(s)

        # Inner function which clears a and b.
        def processValue(val):
            nonlocal a 
            nonlocal b
            nonlocal operator

            if a == "":
                if operator == "-":
                    a = "-"+val
                else:
                    a = val
            else:
                b = val
                a = self.compute(operator, a, b)
                # clear since computation completed
                b, operator = "", ""


            return

        while i < n:
            if s[i] == "(":
                val, new_i = self.calculate(s[i+1:])
                processValue(val)
                # start processing the expression where the inner one ends.
                i += new_i + 1
                continue
                # this is essentially equivalent to processing a number 
            if s[i] == ")":
                # we'll only encounter this in a deeper level of recursion
                return (a, i+1)
            if str.isdigit(s[i]):
                processValue(s[i])
            if s[i] == "+" or s[i] == "-":
                operator = s[i]
            i += 1

        return a


s = Solution() 

# print(s.calculate("2 + 2"))
# print(s.calculate("2 - 2"))
# print(s.calculate("-1 + 5"))
# print(s.calculate("2 - (1+5)"))
print(s.calculate("2 - ((1+5)-6)"))




