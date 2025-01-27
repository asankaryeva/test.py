print("1. +")
print("2. _")
print("3. *")
print("4. /")
print("5. %")
print("6. sqrt")
print("7.pow")
print("8. pow3")


oper=input("operator:")

num1=int(input("number 1:"))
num2=int(input("number 2:"))

if oper=='1':
    print(num1+num2)
elif oper=='2':
    print(num1-num2)   
elif oper=='3':
    print(num1*num2)
elif oper=='4':
    print(num1/num2)
elif oper=='5':
    sum=(num1*num2)/100
    print(sum)
elif oper =='6':
    sqrt=num1**(0.5)
    print(sqrt)
elif open=='7':
    result=(num1**num2)
    print(result)
elif oper=='8':
    result=(num1**3)
    print(result)    