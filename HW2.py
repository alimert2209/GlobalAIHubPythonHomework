infos = []
name=str(input("Adınız: "))
surname=str(input("Soyadınız: "))
age=int(input("Yaşınız: "))
birth=int(input("Doğum yılınız: "))
infos.append(name)
infos.append(surname)
infos.append(age)
infos.append(birth)

for i in range(4):
    print(infos[i])
print(infos)
if age<18:
    print("You can't go out because it's too dangerous!")
else:
    print("You can go out to the street.")