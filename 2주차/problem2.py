from typing import List
expression = "100-200*300-500+20"

def calculate(num1, num2, sign):
    if sign == "+":
        return str(int(num1) + int(num2))
    if sign == "-":
        return str(int(num1) - int(num2))
    if sign == "*":
        return str(int(num1) * int(num2))

def reduction(exp1,signs):
    exp=exp1.copy()
    temp=""
    for sig in signs:
        temparray = []

        while len(exp) !=0:
            temp=exp.pop(0)
            print(temparray, temp, exp)
            if temp == sig:
                temparray.append(calculate(temparray.pop(), exp.pop(0), sig))
            else:
                temparray.append(temp)
        exp = temparray

    return abs(int(exp[0]))

def solution(expression):
    splitexp = expression
    splitexp = splitexp.replace('+', ' + ')
    splitexp = splitexp.replace('-', ' - ')
    splitexp = splitexp.replace('*', ' * ')
    splitexp = splitexp.split(' ')
    priorities = [("+", "-", "*"), ("+", "*", "-"), ("-", "+", "*"), ("-", "*", "+"), ("*", "+", "-"), ("*", "-", "+")]
    result=[]
    for i in priorities:
        result.append(reduction(splitexp, i))
    return max(result)

print(solution(expression))
