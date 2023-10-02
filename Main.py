from tkinter import *
import customtkinter as ctk
import re
import os
"""
NOTES:
     if os.path.exists('NewTraits.cs'):
        #additional lines:
        with open('NewTraits.cs', 'a') as f:
                
    else:
        #starting code logic
        with open('NewTraits.cs', 'a') as f:
            f.write("using System; \n" 
                + "using System.Threading; \n" 
                + "using NCMS; \n" 
                + "using UnityEngine; \n"
                + "using ReflectionUtility; \n"
                + "using System.Text; \n"
                + "using System.Collections.Generic; \n"
                + "using System.Linq; \n"
                + "using System.Text; \n"
                + "using ai; \n")

I will probably have to add the initial and new to a string
      that gets written to a file at teh end of create a mod that 
      way we can make the file names based on the modname at the end
      or we could do it this way and make a counter fo each time they 
      click finish in order to make the file names the name concatenated with the 
      counter but the first idea is better
"""

root = ctk.CTk(fg_color="#101519")
root.geometry("1080x720")
#frames add frames to have more things


#CONSTANTS:

TRAIT_CODE_BEGINNING = ("using System; \n" 
                        "using System.Threading; \n"
                        "using NCMS; \n" 
                        "using UnityEngine; \n"
                        "using ReflectionUtility; \n"
                        "using System.Text; \n"
                        "using System.Collections.Generic; \n"
                        "using System.Linq; \n"
                        "using System.Text; \n"
                        "using ai; \n"
                        "\n"
                        "namespace MyMod \n{"
                        "\n"
                        "\t class Traits \n\t{"
                        "\n"
                        "\t\t public static void init() \n\t\t{")

TRAIT_CODE_ENDING = "\n\n" + "\t\t}" + "\n" +"\n \t\t//OTHER FUNCTIONS GO HERE i.e custom death effects etc. \n" + "\n" + "\t}" + "\n" + "}" 

MAIN_CODE = ("using System; \n"
             "using NCMS; \n"
             "using UnityEngine; \n"
             "ReflectionUtility; \n"
             "\n\n"
             "namespace MyMod \n"
             "{ \n"
             "\t[ModEntry] \n"
             "\tclass Main : MonoBehavior \n"
             "\t{"
             "\t\tvoid Awake() \n"
             "\t\t{ \n"
             "\t\t\tTraits.init();\n"
             "\t\t\tEffects.init();\n"
             "\t\t} \n"
             "\t}\n"
             "}"
             )
#BUTTON LOGIC FUNCTIONS:
string = ''
def traitCreate():
    """
    TESTING:
    with open('NewTraits.cs', 'w') as f:
        f.write(MAIN_CODE); 
    """
    global string
    
    string += ("\n\t\tActorTrait " + inputTraitId.get() + "new ActorTrait();"
                "\n\t\t" + inputTraitId.get() + ".id" + " = " + '"' + inputTraitId.get() + '";'
                "\n\t\t" + inputTraitId.get() + ".path_icon" + " = " + '"ui/icons/achievements/achievements_thedemon";'
                "\n\t\t" + inputTraitId.get() + ".base_stats[S.damage] += " + damage.get() + "f;"
                "\n\t\t" + inputTraitId.get() + ".base_stats[S.health] += " + health.get() + "f;"
                "\n\t\t" + inputTraitId.get() + ".base_stats[S.attack_speed] += " + attackSpeed.get() + "f;"
                "\n\t\t" + inputTraitId.get() + ".base_stats[S.critical_chance] += " + criticalChance.get() + "f;"
                "\n\t\t" + inputTraitId.get() + ".base_stats[S.speed] += " + speed.get() + "f;"
                "\n\t\t" + inputTraitId.get() + ".base_stats[S.dodge] += " + dodge.get() + "f;"
                "\n\t\t" + inputTraitId.get() + ".base_stats[S.accuracy] += " + accuracy.get() + "f;"
                "\n\t\t" + inputTraitId.get() + ".base_stats[S.range] += " + rangeT.get() + "f;"
                "\n\t\t" + inputTraitId.get() + ".base_stats[S.scale] += " + scale.get() + "f;"
                "\n\t\t" + inputTraitId.get() + ".action_attack_target = new AttackAction(ActionLibrary.add" + options.get() + "OnTarget);"
                "\n")
    
def write():
    with open('NewTraits.cs', 'a') as f:
            f.write(string)

#BUTTONS:
traitCreate = ctk.CTkButton(root, text="Create Trait", width=100, fg_color="#fcf9ff", text_color="#101519", corner_radius=5, command=traitCreate)
write = ctk.CTkButton(root, text="Write", width=200, fg_color="#fcf9ff", text_color="#101519", corner_radius=5, command=write)
#LABELS:
idLabel = ctk.CTkLabel(root, text="Trait name: ", font=ctk.CTkFont(size=15, weight="bold"), text_color="#fcf9ff")
healthLabel = ctk.CTkLabel(root, text="Health: ", font=ctk.CTkFont(size=15, weight="bold"), text_color="#fcf9ff")
damageLabel = ctk.CTkLabel(root, text="Damage: ", font=ctk.CTkFont(size=15, weight="bold"), text_color="#fcf9ff")
attackSpeedLabel = ctk.CTkLabel(root, text="Attack Speed: ", font=ctk.CTkFont(size=15, weight="bold"), text_color="#fcf9ff")
critChanceLabel = ctk.CTkLabel(root, text="Crit Chance: ", font=ctk.CTkFont(size=15, weight="bold"), text_color="#fcf9ff")
rangeLabel = ctk.CTkLabel(root, text="Range: ", font=ctk.CTkFont(size=15, weight="bold"), text_color="#fcf9ff")
accLabel = ctk.CTkLabel(root, text="Accuracy: ", font=ctk.CTkFont(size=15, weight="bold"), text_color="#fcf9ff")
speedLabel = ctk.CTkLabel(root, text="Speed: ", font=ctk.CTkFont(size=15, weight="bold"), text_color="#fcf9ff")
dodgeLabel = ctk.CTkLabel(root, text="Dodge Chance: ", font=ctk.CTkFont(size=15, weight="bold"), text_color="#fcf9ff")
intelligenceLabel = ctk.CTkLabel(root, text="Intelligence: ", font=ctk.CTkFont(size=15, weight="bold"), text_color="#fcf9ff")
scaleLabel = ctk.CTkLabel(root, text="Scale: ", font=ctk.CTkFont(size=15, weight="bold"), text_color="#fcf9ff")
descLabel = ctk.CTkLabel(root, text="Description: ", font=ctk.CTkFont(size=15, weight="bold"), text_color="#fcf9ff")
effectsLabel = ctk.CTkLabel(root, text="Attack Effects: ", font=ctk.CTkFont(size=15, weight="bold"), text_color="#fcf9ff")
#ENTRY POINTS:
inputTraitId = ctk.CTkEntry(root, border_color="#1D3142", fg_color="#203547", text_color="#D0D0E1")
inputTraitId.insert(0, "randoTrait")
health = ctk.CTkEntry(root, border_color="#1D3142", fg_color="#203547", text_color="#D0D0E1")
health.insert(0, 0)
damage = ctk.CTkEntry(root, border_color="#1D3142", fg_color="#203547", text_color="#D0D0E1")
damage.insert(0, 0)
attackSpeed = ctk.CTkEntry(root, border_color="#1D3142", fg_color="#203547", text_color="#D0D0E1")
attackSpeed.insert(0, 0)
criticalChance = ctk.CTkEntry(root, border_color="#1D3142", fg_color="#203547", text_color="#D0D0E1")
criticalChance.insert(0, 0.0)
rangeT = ctk.CTkEntry(root, border_color="#1D3142", fg_color="#203547", text_color="#D0D0E1")
rangeT.insert(0, 0)
accuracy = ctk.CTkEntry(root, border_color="#1D3142", fg_color="#203547", text_color="#D0D0E1")
accuracy.insert(0, 0)
speed = ctk.CTkEntry(root, border_color="#1D3142", fg_color="#203547", text_color="#D0D0E1")
speed.insert(0, 0)
dodge = ctk.CTkEntry(root, border_color="#1D3142", fg_color="#203547", text_color="#D0D0E1")
dodge.insert(0, 0.0)
intelligence = ctk.CTkEntry(root, border_color="#1D3142", fg_color="#203547", text_color="#D0D0E1")
intelligence.insert(0, 0)
scale = ctk.CTkEntry(root, border_color="#1D3142", fg_color="#203547", text_color="#D0D0E1")
scale.insert(0, 0)
description = ctk.CTkEntry(root, border_color="#1D3142", fg_color="#203547", text_color="#D0D0E1")
description.insert(0, "This Is My First Mod!")

OPTIONS = [
     "BurningEffect",
     "SlowEffect",
     "FrozenEffect",
     "PoisonedEffect",

]

options = StringVar()
options.set("BurningEffect")
dropdown = OptionMenu(root, options, *OPTIONS)

#FORMATTING:
idLabel.grid(row=0, column=0, padx=2, pady=4)
healthLabel.grid(row=1, column=0, padx=2, pady=4)
damageLabel.grid(row=2, column=0, padx=2, pady=4)
attackSpeedLabel.grid(row=3, column=0, padx=2, pady=4)
critChanceLabel.grid(row=4, column=0, padx=2, pady=4)
rangeLabel.grid(row=5, column=0, padx=2, pady=4)
accLabel.grid(row=6, column=0, padx=2, pady=4)
speedLabel.grid(row=7, column=0, padx=2, pady=4)
dodgeLabel.grid(row=8, column=0, padx=2, pady=4)
intelligenceLabel.grid(row=9, column=0, padx=2, pady=4)
scaleLabel.grid(row=10, column=0, padx=2, pady=4)
effectsLabel.grid(row=11, column=0, padx=2, pady=4)
descLabel.grid(row=12, column=0, padx=2, pady=4)


inputTraitId.grid(row=0, column=1, padx=2, pady=4)
health.grid(row=1, column=1, padx=2, pady=4)
damage.grid(row=2, column=1, padx=2, pady=4)
attackSpeed.grid(row=3, column=1, padx=2, pady=4)
criticalChance.grid(row=4, column=1, padx=2, pady=4)
rangeT.grid(row=5, column=1, padx=2, pady=4)
accuracy.grid(row=6, column=1, padx=2, pady=4)
speed.grid(row=7, column=1, padx=2, pady=4)
dodge.grid(row=8, column=1, padx=2, pady=4)
intelligence.grid(row=9, column=1, padx=2, pady=4)
scale.grid(row=10, column=1, padx=2, pady=4)
dropdown.grid(row=11, column=1, padx=2, pady=4)
description.grid(row=12, column=1, padx=2, pady=4)


traitCreate.grid(row=13, column=1, padx=1, pady=10)
write.grid(row=14, column=1, padx=1, pady=10)



        

root.mainloop()