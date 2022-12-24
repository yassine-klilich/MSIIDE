
#### Exercice 1
# n = input()
# if (n >= 10):
#   print("V")
# elif (n >= 7 and n < 10):
#   print("R")
# elif (n < 7):
#   print("NV")



#### Exercice 2
# a, b = 100, 22
# if b > a:
#   print("b est plus grand que a")
# elif b < a:
#   print("a est plus grand que b")
# else:
#   print("b equals a")



#### Exercice 3
# i = 0
# while i < 6:
#   print(i, end = ", ")
#   if i == 3:
#     break
#   i += 1

# i = 0
# while i < 6:
#   print("la valeur de " + str(i), end = "\n")
#   if i == 3:
#     break
#   i += 1



#### Exercice 4
# for i in range(5):
#   print("debut iteration", i, end="\n")
#   print("bonjour")
#   if i == 2:
#     continue
#   print("Fin iteration", i)
# print("apres la boucle")



#### Exercice 5
# for i in range(20, 36):
#   print(i, end=" ")
#   for i in range(10, 30, 5):
#     print(i, " ")



#### Exercice 6
# def table(base):
#   nb = 6
#   while nb < 10:
#     print(nb*base)
#     nb += 1

# table(6)



#### Exercice 6
# def table(base):
#   nb = 1
#   while nb <= 10:
#     print(nb*base)
#     nb += 1

# a = 1
# while a <= 10:
#   print("-----------------")
#   table(a)
#   a += 1



#### Exercice 7
# def printPrime():
#   global prime
#   prime = 2000
#   print("Prime (local): ", prime)

# printPrime()
# print("Prime: ", prime)



# #### Exercice 8
# a = 10
# b = 221
# ab_max = 0
# if a < b:
#   ab_max = b
# else:
#   ab_max = a
# print(ab_max)


#### Exercice 9
# a = 10
# b = 221
# ab_min = 0
# if a > b:
#   ab_min = b
# else:
#   ab_min = a
# print(ab_min)


#### exercice
# import math
# def cube(n):
#   return n * 2

# def volume(r):
#   return 4 * math.pi * cube(r) / 3

# a = input("Entrer un nombre: ")
# print(volume(a))


#### exercice
# nombre = [5, 10, 20, 30, 40]
# print(nombre[2])
# print(nombre[1:3])
# print(nombre[2:3])
# print(nombre[2:])
# print(nombre[:2])
# print(nombre[-1])
# print(nombre[-2])


#### example
# animaux = ['girafe', 'tigre', 'singe', 'souris']
# print(animaux[0:2])
# print(animaux[0:3])
# print(animaux[0:])
# print(animaux[:])
# print(animaux[1:])
# print(animaux[1:-1])


#### example
# notes = ["saida", 16, "ahmad", 12, "Khalid", 17, "Farah", 8]
# print(notes[0:2])
# print(notes[2:4])
# print(notes[4:6])


#### example
# stuff = [500, 'Hello', 3.14, ["batata", 345, "issable"]]
# stuff[-1][2] = "holaaa"
# stuff[-1].append("holaaa 2")
# print(stuff)


# #### exemple
# nombre = [45, 22, 62, 33, 423, 4]
# print(nombre)
# nombre.sort()
# print(nombre)
# nombre.append(333)
# print(nombre)
# nombre.sort()
# print(nombre)
# nombre.reverse()
# print(nombre)
# print(nombre.index(22))
# nombre.remove(45)
# print(nombre)
# del nombre[2]
# print(nombre)


#### exemple
# print(list(range(10)))
# print(list(range(10, -10, -3)))




#### Tkinter
# from tkinter import *
# window = Tk()
# window.title("Title")
# label = Label(window, text = "Bonjour…!", fg="green").pack()
# window.geometry("300x300")
# top_frame = Frame(window, bg="green").pack()
# bottom_frame = Frame(window, bg="red").pack()
# label2 = Label(top_frame, text="label 1").pack()
# label1 = Label(bottom_frame, text="label 2").pack(side="right")
# btn = Button(window, text="Quit", command = window.destroy).pack()
# window.mainloop()



#### 
# import random
# print(random.randrange(8))
# print(random.randrange(8))
# print(random.randrange(8))
# print(random.randrange(8))


####
# from tkinter import *
# import random

# def drawLine():
#   global x1, y1, x2, y2, color
#   can1.create_line(x1, y1, x2, y2, width=2, fill=color)
#   x1, y1, x2, y2 = 10, y1 - 10, 290, y2 - 10

# def changeColor():
#   global color
#   palette=["purple", "green", "blue", "yellow", "orange", "maroon", "black", "cyan", "dark green", "grey"]
#   c = random.randrange(8)
#   color = palette[c]

# x1, y1, x2, y2 = 10, 150, 290, 150
# color = "dark green"

# fen1 = Tk()
# can1 = Canvas(fen1, bg="dark grey", height=300, width=300)
# can1.pack(side=LEFT)
# btn1 = Button(fen1, text="Quitter", command=fen1.quit)
# btn1.pack(side=BOTTOM)
# btn2 = Button(fen1, text="Tracer une ligne", command=drawLine)
# btn2.pack()
# btn3 = Button(fen1, text="Autre coulor", command=changeColor)
# btn3.pack()
# fen1.mainloop()



#### 
class Personne:
  def __init__(self):
    self.nom = "Klilich"
    self.prenom = "Yassine"
    self.age = 26
    self.address = "Branes 1"
    
per1 = Personne()
print(per1.nom)
