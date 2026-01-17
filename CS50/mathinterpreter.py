exp = input("show the expression: ").split()
exp1 = float(exp[0])
exps = exp[1]
exp2 = float(exp[2])

if exps == "+":
    print(exp1+exp2)
elif exps == "-":
    print(exp1 - exp2)
elif exps == "/":
    print(exp1 / exp2)
elif exps == "*":
    print(exp1 * exp2)
else:
    ...



