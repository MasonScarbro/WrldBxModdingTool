from tkinter import *
import customtkinter as ctk
import re
import os
import numpy as np
import array as arr
import string


# ROOT DECLARATION #
root = ctk.CTk(fg_color="#101519")

root.geometry("1290x720")



# ---------------------- CONSTANTS ---------------------- #

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

EFFECTS_CODE_BEGINNING = TRAIT_CODE_BEGINNING.replace("Traits", "Effects")

TRAIT_CODE_ENDING = ("\n\n"
                     "\t\t}"
                     "\n"
                     "\n \t\t//OTHER FUNCTIONS GO HERE i.e custom death effects etc. \n"
                     "\n"
                     "\t\tpublic static void addTraitToLocalizedLibrary(string id, string description)"
                     "\n\t\t{"
                     "\n"
                     '\n\t\t\tstring language = Reflection.GetField(LocalizedTextManager.instance.GetType(), LocalizedTextManager.instance, "language") as string;'
                     '\n\t\t\tDictionary<string, string> localizedText = Reflection.GetField(LocalizedTextManager.instance.GetType(), LocalizedTextManager.instance, "localizedText") as Dictionary<string, string>;'
                     '\n\t\t\tlocalizedText.Add("trait_" + id, id);'
                     '\n\t\t\tlocalizedText.Add("trait_" + id + "_info", description);'
                     '\n\t\t}'
                     "\n"
                     "\t}"
                     "\n"
                     "}") 



EFFECTS_CODE_ENDING = (TRAIT_CODE_ENDING
                       .replace('localizedText.Add("trait_" + id, id);', 'localizedText.Add(name, id);' )
                       .replace('localizedText.Add("trait_" + id + "_info", description);', 'localizedText.Add(description, description);')
                       .replace('addTraitToLocalizedLibrary(string id, string description)', 'localizeStatus(string id, string name, string description)')) 

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

# ---------------------------------------------------------- #



# ---------------------- BUTTON COMMANDS ---------------------- #
trait_string = ''
effect_string = ''
effectsArr = []
traitsArr = []
def traitCreate():
    """
    TESTING:
    with open('NewTraits.cs', 'w') as f:
        f.write(MAIN_CODE); 
    """
    global traitsArr
    global trait_string
    traitId = "".join(inputTraitId.get().split())
    if traitId in traitsArr:
         trait_string += "\n\t\t// You tried to create a trait with the same name of " + inputTraitId.get() + " That's not possible in coding!"
         print(traitsArr)
    else:
        trait_string += ("\n\t\tActorTrait " + traitId + " = new ActorTrait();"
                    "\n\t\t" + traitId + ".id" + " = " + '"' + inputTraitId.get() + '";'
                    "\n\t\t" + traitId + ".path_icon" + " = " + '"ui/icons/achievements/achievements_thedemon";'
                    "\n\t\t" + traitId + ".base_stats[S.damage] += " + damage.get() + "f;"
                    "\n\t\t" + traitId + ".base_stats[S.health] += " + health.get() + "f;"
                    "\n\t\t" + traitId + ".base_stats[S.attack_speed] += " + attackSpeed.get() + "f;"
                    "\n\t\t" + traitId + ".base_stats[S.critical_chance] += " + criticalChance.get() + "f;"
                    "\n\t\t" + traitId + ".base_stats[S.speed] += " + speed.get() + "f;"
                    "\n\t\t" + traitId + ".base_stats[S.dodge] += " + dodge.get() + "f;"
                    "\n\t\t" + traitId + ".base_stats[S.accuracy] += " + accuracy.get() + "f;"
                    "\n\t\t" + traitId + ".base_stats[S.range] += " + rangeT.get() + "f;"
                    "\n\t\t" + traitId + ".base_stats[S.scale] += " + scale.get() + "f;"
                    "\n\t\t" + traitId + ".action_attack_target = new AttackAction(ActionLibrary.add" + options.get() + "OnTarget);"
                    "\n\t\t" + "AssetManager.traits.add(" + traitId +");"
                    "\n\t\t" + "PlayerConfig.unlockTrait(" + traitId +".id);"
                    "\n\t\t" + "addTraitToLocalizedLibrary(" + traitId +".id, " + '"' + description.get() + '");'
                    "\n")
        traitsArr.append(traitId)
        print(traitsArr)

def effectCreate():
    """
    TESTING:
    with open('NewTraits.cs', 'w') as f:
        f.write(MAIN_CODE); 
    """
    global effectsArr
    global effect_string
    effectId = "".join(inputEffectId.get().split())
    if effectId in effectsArr:
         effect_string += "\n\t\t// You tried to create an effect with the same name of " + inputEffectId.get() + " That's not possible in coding!"
         print(effectsArr)
    else:
        effect_string += ("\n\t\tStatusEffect " + effectId + " = new StatusEffect();"
                    "\n\t\t" + effectId + ".id" + " = " + '"' + inputEffectId.get() + '";'
                    "\n\t\t" + effectId + ".duration" + " = " + duration.get() + "f;"
                    "\n\t\t" + effectId + ".base_stats[S.damage] += " + damage_effect.get() + "f;"
                    "\n\t\t" + effectId + ".base_stats[S.health] += " + health_effect.get() + "f;"
                    "\n\t\t" + effectId + ".base_stats[S.attack_speed] += " + attackSpeed_effect.get() + "f;"
                    "\n\t\t" + effectId + ".base_stats[S.critical_chance] += " + criticalChance_effect.get() + "f;"
                    "\n\t\t" + effectId + ".base_stats[S.speed] += " + speed_effect.get() + "f;"
                    "\n\t\t" + effectId + ".base_stats[S.dodge] += " + dodge_effect.get() + "f;"
                    "\n\t\t" + effectId + ".base_stats[S.accuracy] += " + accuracy_effect.get() + "f;"
                    "\n\t\t" + effectId + ".base_stats[S.range] += " + rangeE.get() + "f;"
                    "\n\t\t" + effectId + ".base_stats[S.knockback_reduction] += " + knockbackR_effect.get() + "f;"
                    "\n\t\t" + effectId + ".base_stats[S.knockback] += " + knockback_effect.get() + "f;"
                    "\n\t\t" + effectId + ".path_icon" + " = " + '"ui/icons/achievements/achievements_thedemon";'
                    "\n\t\t" + effectId + ".name = " + '"status_title_' + effectId + '";'
                    "\n\t\t" + "AssetManager.status.add(" + effectId +");"
                    "\n\t\t" + "addTraitToLocalizedLibrary(" + effectId +".id, " + '"' + description.get() + '");'
                    "\n")
        effectsArr.append(effectId)
        print(effectsArr)
    
def write():
    with open('NewTraits.cs', 'a') as f:
            f.write(TRAIT_CODE_BEGINNING + trait_string + TRAIT_CODE_ENDING)
    with open('NewEffects.cs', 'a') as f:
            f.write(EFFECTS_CODE_BEGINNING + effect_string + EFFECTS_CODE_ENDING)


# ---------------------------------------------------------- #



# ----------------------BUTTONS ---------------------- #

traitCreate = ctk.CTkButton(root, text="Create Trait", width=100, fg_color="#fcf9ff", text_color="#101519", corner_radius=5, command=traitCreate)
effectCreate = ctk.CTkButton(root, text="Create Effect", width=100, fg_color="#fcf9ff", text_color="#101519", corner_radius=5, command=effectCreate)
write = ctk.CTkButton(root, text="Write", width=200, fg_color="#fcf9ff", text_color="#101519", corner_radius=5, command=write)

# ---------------------------------------------------------- #



# ---------------------- LABLES ---------------------- #
def new_label(string):
     return ctk.CTkLabel(root, text=string, font=ctk.CTkFont(family="", size=15, weight="bold"), text_color="#fcf9ff")
     
def create_labels_traits(): 
    idLabel = new_label("Trait Name: ")
    healthLabel = new_label("Health: ")
    damageLabel = new_label("Damage: ")
    attackSpeedLabel = new_label("Attack Speed: ")
    critChanceLabel = new_label("Crit Chance: ")
    rangeLabel = new_label("Range: ")
    accLabel = new_label("Accuracy: ")
    speedLabel = new_label("Speed: ")
    dodgeLabel = new_label("Dodge Chance: ")
    intelligenceLabel = new_label("Intelligence: ")
    scaleLabel = new_label("Scale: ")
    descLabel = new_label("Description: ")
    effectsLabel = new_label("Attack Effects: ")

    return [
    idLabel, healthLabel, damageLabel, attackSpeedLabel, critChanceLabel, 
    rangeLabel, accLabel, speedLabel, dodgeLabel, intelligenceLabel, 
    scaleLabel, descLabel, effectsLabel
    ]

def create_labels_effects(): 
    idLabel = new_label("Effect Name: ")
    healthLabel = new_label("Health: ")
    damageLabel = new_label("Damage: ")
    attackSpeedLabel = new_label("Attack Speed: ")
    critChanceLabel = new_label("Crit Chance: ")
    rangeLabel = new_label("Range: ")
    accLabel = new_label("Accuracy: ")
    speedLabel = new_label("Speed: ")
    dodgeLabel = new_label("Dodge Chance: ")
    intelligenceLabel = new_label("Intelligence: ")
    duration = new_label("Duration: ")
    knockbackLabel = new_label("KnockBack")
    knockbackRLabel = new_label("KnockBack Reduction")
    descLabel = new_label("Description: ")

    return [
    idLabel, healthLabel, damageLabel, attackSpeedLabel, critChanceLabel, 
    rangeLabel, accLabel, speedLabel, dodgeLabel, intelligenceLabel, duration, 
     knockbackLabel, knockbackRLabel, descLabel,
    ]

# ---------------------------------------------------------- #



# ---------------------- ENTRY POINTS ---------------------- #

def new_entry():
    return ctk.CTkEntry(root, border_color="#1D3142", fg_color="#203547", text_color="#D0D0E1")

inputTraitId = new_entry()
inputTraitId.insert(0, "randoTrait")
health = new_entry()
health.insert(0, 0)
damage = new_entry()
damage.insert(0, 0)
attackSpeed = new_entry()
attackSpeed.insert(0, 0)
criticalChance = new_entry()
criticalChance.insert(0, 0.0)
rangeT = new_entry()
rangeT.insert(0, 0)
accuracy = new_entry()
accuracy.insert(0, 0)
speed = new_entry()
speed.insert(0, 0)
dodge = new_entry()
dodge.insert(0, 0.0)
intelligence = new_entry()
intelligence.insert(0, 0)
scale = new_entry()
scale.insert(0, 0.0)
description = new_entry()
description.insert(0, "This Is My First Trait!")


inputEffectId = new_entry()
inputEffectId.insert(0, "randoEffect")
health_effect = new_entry()
health_effect.insert(0, 0)
damage_effect = new_entry()
damage_effect.insert(0, 0)
attackSpeed_effect = new_entry()
attackSpeed_effect.insert(0, 0)
criticalChance_effect = new_entry()
criticalChance_effect.insert(0, 0.0)
rangeE = new_entry()
rangeE.insert(0, 0)
accuracy_effect = new_entry()
accuracy_effect.insert(0, 0)
speed_effect = new_entry()
speed_effect.insert(0, 0)
dodge_effect = new_entry()
dodge_effect.insert(0, 0.0)
intelligence_effect = new_entry()
intelligence_effect.insert(0, 0)
duration = new_entry()
duration.insert(0, 0)
knockback_effect = new_entry()
knockback_effect.insert(0, 0.0)
knockbackR_effect = new_entry()
knockbackR_effect.insert(0, 0.0)
description_effect = new_entry()
description_effect.insert(0, "This Is My First Effect!")

    

# ---------------------------------------------------------- #



# ---------------------- OPTIONS ---------------------- #

OPTIONS = [
     "BurningEffect",
     "SlowEffect",
     "FrozenEffect",
     "PoisonedEffect",

]

options = ctk.StringVar(value="BurningEffect")
dropdown = ctk.CTkOptionMenu(root, values=OPTIONS, variable=options, fg_color="#203547",button_color="#203547")

# ---------------------------------------------------------- #




# ---------------------- FORMATTING ---------------------- #
def setup_labels():
    trait_labels = create_labels_traits()
    effect_labels = create_labels_effects()

    for i, trait_labels in enumerate(trait_labels):
        trait_labels.grid(row=i, column=0, padx=4, pady=4)

    for i, effect_labels in enumerate(effect_labels):
        effect_labels.grid(row=i, column=3, padx=10, pady=4)
        

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
description.grid(row=11, column=1, padx=2, pady=4)
dropdown.grid(row=12, column=1, padx=2, pady=4)

inputEffectId.grid(row=0, column=4, padx=4, pady=4)
health_effect.grid(row=1, column=4, padx=4, pady=4)
damage_effect.grid(row=2, column=4, padx=4, pady=4)
attackSpeed_effect.grid(row=3, column=4, padx=4, pady=4)
criticalChance_effect.grid(row=4, column=4, padx=4, pady=4)
rangeE.grid(row=5, column=4, padx=4, pady=4)
accuracy_effect.grid(row=6, column=4, padx=4, pady=4)
speed_effect.grid(row=7, column=4, padx=4, pady=4)
dodge_effect.grid(row=8, column=4, padx=4, pady=4)
intelligence_effect.grid(row=9, column=4, padx=4, pady=4)
duration.grid(row=10, column=4, padx=4, pady=4)
knockback_effect.grid(row=11, column=4, padx=4, pady=4)
knockbackR_effect.grid(row=12, column=4, padx=4, pady=4)
description_effect.grid(row=13, column=4, padx=4, pady=4)



traitCreate.grid(row=13, column=1, padx=1, pady=10)
effectCreate.grid(row=14, column=4, padx=1, pady=10)
write.grid(row=14, column=1, padx=10, pady=20)

setup_labels()
# ---------------------------------------------------------- #


root.mainloop() #Main Loop