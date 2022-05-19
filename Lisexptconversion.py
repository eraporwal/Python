y="22+18/4-3"
x=len(y)

for i in y:
    expression=""
    operand=""
    if i==numeral(y):
        operand=operand + i
    else:
        expression=expression+operand
        expression=expression+i
        operand=""
        
        



def numeral(y):
    for i in range(x):
        if i==0 & i==9:
            return true
        else:
            return false
        
print(expression)
