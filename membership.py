gpy= input("введите тип членство (золото, серебро, обычный):")
sum = float(input("введите сумму покупки:"))
discount=0

if gpy=="1":
    if sum > 100:
        discount = .2
    else:
        discount=0.10
elif gpy=="2":
    if sum > 100:
        discount = .15
    else:
        discount=0.05
elif gpy=="3":
    if sum >100:
        discount=0.05
    else:
        discount=0
print(discount * sum )