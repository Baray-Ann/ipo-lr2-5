print("Дано число n. С начала суток прошло n минут. Определите, сколько часов и минут будут показывать электронные часы в этот момент. ")
n=int(input("Введите кол-во минут с момента начала суток:"))
print("Кол-во минут: ", n)
h=n // 60 % 24
m=n % 60
print("Время: ",h,":", m)
