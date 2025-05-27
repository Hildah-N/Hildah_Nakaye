class Calculator:
    def add(self, *args):
        if len(args) == 2:
            return args[0] + args[1]
        elif len(args) == 3:
            return args[0] + args[1] + args[2]
        else:
            return sum(args)

calc = Calculator()
print(calc.add(2, 3))        # 5
print(calc.add(2, 3, 4))     # 9
print(calc.add(1, 2, 3, 4))  # 10