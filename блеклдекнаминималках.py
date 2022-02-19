import random

koloda = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4
random.shuffle(koloda)
count = 0 
n = 0

count += koloda[n]
print("Ваша карта: ", koloda[n])
print("Ваши очки: ", count)
while count < 22:
    a = int(input("Выберите действие: 1) Взять карту; 2) Не взять карту"))
    if a == 1:
        n = n + 1
        count += koloda[n] 
        print("Ваша карта: ", koloda[n])
        print("Ваши очки: ", count)
    elif a == 2:
        break
    if count == 21:
        break 
if count == 21:
    print("Вы выиграли") 
elif count > 21:
    print("Вы проиграли")
elif count < 21:
    print("Вы ушли")  