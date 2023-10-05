from tkinter import *
import customtkinter as ctk
import re
import os
import numpy as np
import array as arr
import string


# ROOT DECLARATION #
root = ctk.CTk(fg_color="#101519")
initialFrame = ctk.CTkFrame(root, fg_color="#101519")
WindowsFrame = ctk.CTkFrame(root, fg_color="#101519")
root.geometry("1290x720")
initialFrame.grid(row=0, column=0, padx=4, pady=0)
WindowsFrame.grid(row=0, column=1, padx=20, pady=0)



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
                    "\n\t\t" + traitId + ".base_stats[S.intelligence] += " + intelligence.get() + "f;"
                    "\n\t\t" + traitId + ".base_stats[S.warfare] += " + warfare.get() + "f;"
                    "\n\t\t" + traitId + ".base_stats[S.stewardship] += " + stewardship.get() + "f;"
                    "\n\t\t" + traitId + ".action_attack_target = new AttackAction(ActionLibrary.add" + options.get() + "OnTarget);"
                    "\n\t\t" + "AssetManager.traits.add(" + traitId +");"
                    "\n\t\t" + "PlayerConfig.unlockTrait(" + traitId +".id);"
                    "\n\t\t" + "addTraitToLocalizedLibrary(" + traitId +".id, " + '"' + description.get() + '");'
                    "\n")
        traitsArr.append(traitId)
        add_trait_to_list(traitId)
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
        add_effect_to_list(effectId)
        print(effectsArr)
    
def write():
    with open('NewTraits.cs', 'a') as f:
            f.write(TRAIT_CODE_BEGINNING + trait_string + TRAIT_CODE_ENDING)
    with open('NewEffects.cs', 'a') as f:
            f.write(EFFECTS_CODE_BEGINNING + effect_string + EFFECTS_CODE_ENDING)


# ---------------------------------------------------------- #



# ----------------------BUTTONS ---------------------- #

traitCreate = ctk.CTkButton(initialFrame, text="Create Trait", width=100, fg_color="#fcf9ff", text_color="#101519", corner_radius=5, command=traitCreate)
effectCreate = ctk.CTkButton(initialFrame, text="Create Effect", width=100, fg_color="#fcf9ff", text_color="#101519", corner_radius=5, command=effectCreate)
write = ctk.CTkButton(initialFrame, text="Write", width=200, fg_color="#fcf9ff", text_color="#101519", corner_radius=5, command=write)

# ---------------------------------------------------------- #



# ---------------------- LABLES ---------------------- #
def new_label(string):
     return ctk.CTkLabel(initialFrame, text=string, font=ctk.CTkFont(family="", size=15, weight="bold"), text_color="#fcf9ff")
     
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
    warfareLabel = new_label("Warfare: ")
    stewardshipLabel = new_label("Stewardship: ")
    scaleLabel = new_label("Scale: ")
    descLabel = new_label("Description: ")
    effectsLabel = new_label("Attack Effects: ")

    return [
    idLabel, healthLabel, damageLabel, attackSpeedLabel, critChanceLabel, 
    rangeLabel, accLabel, speedLabel, dodgeLabel, intelligenceLabel, 
    warfareLabel, stewardshipLabel,
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

# TRAIT AND EFFECT LABEL FUCTIONS #
def add_trait_to_list(id):
    traitAdded = ctk.CTkLabel(traits_window, text=id, font=ctk.CTkFont(family="", size=12, weight="normal"), text_color="#fcf9ff")
    traitAdded.pack()

def add_effect_to_list(id):
    traitAdded = ctk.CTkLabel(effects_window, text=id, font=ctk.CTkFont(family="", size=12, weight="normal"), text_color="#fcf9ff")
    traitAdded.pack()

# ---------------------------------------------------------- #



# ---------------------- ENTRY POINTS ---------------------- #

def new_entry():
    return ctk.CTkEntry(initialFrame, border_color="#1D3142", fg_color="#203547", text_color="#D0D0E1")

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
warfare = new_entry()
warfare.insert(0, 0)
stewardship = new_entry()
stewardship.insert(0, 0)
scale = new_entry()
scale.insert(0, 0.0)
description = new_entry()
description.insert(0, "This Is My First Trait!")

entryTraitArr = [inputTraitId, health, damage, attackSpeed, criticalChance,
                  rangeT, accuracy, speed, dodge, intelligence, warfare, stewardship, 
                   scale, description, ]

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

entryEffectAr = [inputEffectId, health_effect, damage_effect, 
                 attackSpeed_effect, criticalChance_effect,
                 rangeE, accuracy_effect, speed_effect, dodge_effect,
                 intelligence_effect, duration, knockback_effect, 
                 knockbackR_effect, description_effect
                 ]



# ---------------------------------------------------------- #



# ---------------------- OPTIONS ---------------------- #

OPTIONS = [
     "BurningEffect",
     "SlowEffect",
     "FrozenEffect",
     "PoisonedEffect",

]

options = ctk.StringVar(value="BurningEffect")
dropdown = ctk.CTkOptionMenu(initialFrame, values=OPTIONS, variable=options, fg_color="#203547",button_color="#203547")

# ---------------------------------------------------------- #




# ---------------------- FORMATTING ---------------------- #
def setup_labels():
    trait_labels = create_labels_traits()
    effect_labels = create_labels_effects()

    for i, trait_labels in enumerate(trait_labels):
        trait_labels.grid(row=i, column=0, padx=4, pady=4)

    for i, effect_labels in enumerate(effect_labels):
        effect_labels.grid(row=i, column=3, padx=10, pady=4)

def format_entries():
     traits_entries = entryTraitArr
     effect_entries = entryEffectAr

     for i, traits_entries in enumerate(traits_entries):
          traits_entries.grid(row=i, column=1, padx=2, pady=4)
          length=i+1
    
     dropdown.grid(row=length, column=1, padx=2, pady=4)
     traitCreate.grid(row=length+1, column=1, padx=2, pady=4)
     length=0 #reset length fopr next for loop

     for i, effect_entries in enumerate(effect_entries):
          effect_entries.grid(row=i, column=4, padx=2, pady=4)
          length=i+1
     effectCreate.grid(row=length, column=4, padx=2, pady=4)
            

#    WINDOW FORMATTING    #
traits_window_label = ctk.CTkLabel(WindowsFrame, text="Traits Added: ", font=ctk.CTkFont(family="", size=15, weight="bold"), text_color="#fcf9ff")
effects_window_label = ctk.CTkLabel(WindowsFrame, text="Effects Added: ", font=ctk.CTkFont(family="", size=15, weight="bold"), text_color="#fcf9ff")
effects_window_label.grid(row=0, column=0, padx=10, pady=4)
traits_window_label.grid(row=0, column=1, padx=10, pady=4)
effects_window =ctk.CTkScrollableFrame(WindowsFrame, fg_color="#203547", width=150, height=200)
effects_window.grid(row=1, column=0, padx=10, pady=4)
traits_window =ctk.CTkScrollableFrame(WindowsFrame, fg_color="#203547", width=150, height=200)
traits_window.grid(row=1, column=1, padx=10, pady=4)


write.grid(row=16, column=1, padx=10, pady=20) #Write button only used for testing right now

format_entries() #called function
setup_labels() #called function
# ---------------------------------------------------------- #


root.mainloop() #Main Loop