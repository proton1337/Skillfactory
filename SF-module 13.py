S=0 #сумма к оплате
quantity=int(input("Введите количество билетов, которые вы хотите приобрести "))
if quantity<=0:
    print("Вы ввели некорректное количество билетов")
for i in range(quantity):
    age=int(input("Введите возраст посетителя "))
    if age<0:
        print("Введите настоящий возраст")
    elif age<18:
        S+=0
    elif 18<=age<25:
        S+=990
    else:
        S+=1390
if quantity>3:
    S*=0.90
print("Сумма к оплате =",S)
