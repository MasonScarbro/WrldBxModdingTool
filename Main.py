from tkinter import *
import customtkinter as ctk
import re

root = ctk.CTk(fg_color="#101519")
root.geometry("1080x720")
#frames add frames to have more things

'''
def myClick():
    noSpace = ''.join(input1.get().split())
    myctk.CTkLabel = ctk.CTkLabel(root, text=noSpace)
    myLabel.pack()

myButton = Button(root, text="Pooo", command=myClick)
myButton.pack()
'''
#Buttons:
finish = ctk.CTkButton(root, text="Finish", width=80, fg_color="#fcf9ff", text_color="#101519", corner_radius=5)

#Labels:
idLabel = ctk.CTkLabel(root, text="Trait name: ", font=ctk.CTkFont(size=15, weight="bold"), text_color="#fcf9ff")
healthLabel = ctk.CTkLabel(root, text="Health: ", font=ctk.CTkFont(size=15, weight="bold"), text_color="#fcf9ff")
damageLabel = ctk.CTkLabel(root, text="Damage: ", font=ctk.CTkFont(size=15, weight="bold"), text_color="#fcf9ff")
attackSpeedLabel = ctk.CTkLabel(root, text="Attack Speed: ", font=ctk.CTkFont(size=15, weight="bold"), text_color="#fcf9ff")
critChanceLabel = ctk.CTkLabel(root, text="Crit Chance: ", font=ctk.CTkFont(size=15, weight="bold"), text_color="#fcf9ff")
rangeLabel = ctk.CTkLabel(root, text="Range: ", font=ctk.CTkFont(size=15, weight="bold"), text_color="#fcf9ff")
accLabel = ctk.CTkLabel(root, text="Accuracy: ", font=ctk.CTkFont(size=15, weight="bold"), text_color="#fcf9ff")
dodgeLabel = ctk.CTkLabel(root, text="Dodge Chance: ", font=ctk.CTkFont(size=15, weight="bold"), text_color="#fcf9ff")
intelligenceLabel = ctk.CTkLabel(root, text="Intelligence: ", font=ctk.CTkFont(size=15, weight="bold"), text_color="#fcf9ff")
descLabel = ctk.CTkLabel(root, text="Description: ", font=ctk.CTkFont(size=15, weight="bold"), text_color="#fcf9ff")

#Entry points:
inputTraitId = Entry(root)
inputTraitId.insert(0, "")
health = Entry(root)
health.insert(0, "")
damage = Entry(root)
damage.insert(0, "")
attackSpeed = Entry(root)
attackSpeed.insert(0, "")
criticalChance = Entry(root)
criticalChance.insert(0, "Percent as Decimal!")
rangeT = Entry(root)
rangeT.insert(0, "")
accuracy = Entry(root)
accuracy.insert(0, "")
dodge = Entry(root)
dodge.insert(0, "Percent as Decimal!")
intelligence = Entry(root)
intelligence.insert(0, "")
description = Entry(root)
description.insert(0, "")

#Formating:
idLabel.grid(row=0, column=0, padx=2, pady=6)
healthLabel.grid(row=1, column=0, padx=2, pady=6)
damageLabel.grid(row=2, column=0, padx=2, pady=6)
attackSpeedLabel.grid(row=3, column=0, padx=2, pady=6)
critChanceLabel.grid(row=4, column=0, padx=2, pady=6)
rangeLabel.grid(row=5, column=0, padx=2, pady=6)
accLabel.grid(row=6, column=0, padx=2, pady=6)
dodgeLabel.grid(row=7, column=0, padx=2, pady=6)
intelligenceLabel.grid(row=8, column=0, padx=2, pady=6)
descLabel.grid(row=9, column=0, padx=2, pady=6)


inputTraitId.grid(row=0, column=1, padx=2, pady=6)
health.grid(row=1, column=1, padx=2, pady=6)
damage.grid(row=2, column=1, padx=2, pady=6)
attackSpeed.grid(row=3, column=1, padx=2, pady=6)
criticalChance.grid(row=4, column=1, padx=2, pady=6)
rangeT.grid(row=5, column=1, padx=2, pady=6)
accuracy.grid(row=6, column=1, padx=2, pady=6)
dodge.grid(row=7, column=1, padx=2, pady=6)
intelligence.grid(row=8, column=1, padx=2, pady=6)
description.grid(row=9, column=1, padx=2, pady=6)

finish.grid(row=10, column=1, padx=1, pady=10)

root.mainloop()