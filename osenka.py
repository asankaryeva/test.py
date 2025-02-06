persent=float(input("ваша оценка"))
homework=str(input("все домашки были выполнины"))

if persent >=90:
    homework = input("homework yes or no")
    if homework == "yes":
        print("ОТЛИЧНО A+")
    else:
        print("ХОРОШАЯ РАБОТА, НО СДАЙ ВСЕ ЗАДАНИЯ. ОЦЕНКА А")
elif persent >=80:
    homework = input("вы ходили на занятие")
    if homework == "yes":
        print("ХОРОШО В+")
    else:
        print("посещай занатие. C")
else:
    print("старайся лучше!")
