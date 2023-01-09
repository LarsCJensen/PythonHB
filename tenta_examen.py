import random


# lista =[1, 2, 5, 5, 2, 3, 4, 4, 4] #numerisk lista
# new_list=[]
# remove_index=[]
# for i in range(len(lista)):
#     for j in range(i+1,len(lista)):
#         if lista[j]==lista[i]:
#             remove_index.append(j)
# for i in range(len(lista)):
#     if i in remove_index: 
#         continue
#     new_list.append(lista[i])
# print(new_list) 

def funk(N):
    for i in range(1, N):
        print('A'*i)
    for i in range(N, 0, -1):
        print('A'*i)
# funk(5)


lista_1 =[[1000, 2000, 3000],
          [4000, 5000, 6000],
          [7000, 8000, 9000]]

# print(lista_1[2][1])

minTal = 1.2e-27
# print(type(minTal))

# mittTal = 3+5
# if mittTal < 8:
#     print('1')
# if mittTal < 9:
#     print('2')
# elif mittTal >= 8:
#     print('3')


# while True:
x = random.randrange(3,22,5)
# print(x)

# summa = 0
# i = 1
# while i < 10:
#     summa = summa + i
# i = i + 1
# print("Summan är ", summa)

Lista = [2.3,'apelsin',2342346]
# print(Lista[1])
# print(Lista[2])
# print(Lista[3])

# år = int(input(f'Skriv ett årtal: '))
# if not (år % 4 ==0 and år % 100 !=0) or år % 400 == 0:
#     print(f'Inte skottår')
# else:
#     print(f'Skottår')

# money = 43
# age = 18
# afford = False
# if age >= 18:
#     if money >= 50:
#         afford = True
# else:
#     if money >= 25:
#         afford = True
# if afford:
#     print("Du har råd")
# else:
#     print("Du har inte råd")


# x = int(input("Skriv in ett heltal \n"))
# y = 0
# c = 0
# b = 10
# temp = x
# while(temp > 0):
#     y = ((temp % 2)*(b**c)) + y
#     temp = int(temp/2)
#     c += 1
# print(f'{x}  {y}')

# frukter = ["banan", "apelsin", "äpple", "päron"]
# for i in range(len(frukter)):
#     print("frukt nr %d: %s" % (i+1, frukter[i]))

# myString = 'Test123ABC'
# print(myString[4:7])

# f = open('nyFil.txt', 'x')

mittTal = 4.523432
print(f'{mittTal:.2f}')