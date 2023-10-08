from tkinter import *
import customtkinter as ctk
import re
import os
import numpy as np
import array as arr
import string
from GUI import Formatting
from Constants import Config


# ROOT DECLARATION #
root = ctk.CTk(fg_color="#101519")
initialFrame = ctk.CTkFrame(root, fg_color="#101519")
WindowsFrame = ctk.CTkFrame(root, fg_color="#101519")
root.geometry("1290x720")
initialFrame.grid(row=0, column=0, padx=4, pady=0)
WindowsFrame.grid(row=0, column=1, padx=20, pady=0)






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
                    "\n\t\t//" + traitId + "AttackFunction"
                    "\n\t\t" + traitId + ".action_attack_target = new AttackAction(ActionLibrary.add" + options.get() + "OnTarget);"
                    "\n\t\t" + "AssetManager.traits.add(" + traitId +");"
                    "\n\t\t" + "PlayerConfig.unlockTrait(" + traitId +".id);"
                    "\n\t\t" + "addTraitToLocalizedLibrary(" + traitId +".id, " + '"' + description.get() + '");'
                    "\n")
        traitsArr.append(traitId)
        Formatting.add_trait_to_list(traitId, traits_window)
        populate_options(traitsArr) #ATTACK FEATURE | WIP
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
        Formatting.add_effect_to_list(effectId, effects_window)
        print(effectsArr)

# WRITING TO FILE BUTTON | TESTING #
def write():
    with open('NewTraits.cs', 'a') as f:
            f.write(Config.TRAIT_CODE_BEGINNING + trait_string + Config.TRAIT_CODE_ENDING)
    with open('NewEffects.cs', 'a') as f:
            f.write(Config.EFFECTS_CODE_BEGINNING + effect_string + Config.EFFECTS_CODE_ENDING)

# BUTTON FOR ATTACK CREATION #
def create_attack_for_trait():
    
    print("clicked")
    print(attack_options.get())
    global trait_string
    
                    
    #I Know, Im Editing a constant which is evil or whatever but I did Not whant to create a new variable and or take this var out of constants its to pretty there
    if attack_actions.get() == "Assorted Magic":
        trait_string = trait_string.replace("//" + attack_options.get() + "AttackFunction", attack_options.get() + ".action_attack_target = new AttackAction(" + attack_options.get() + "Attack);")
        Config.TRAIT_CODE_ENDING = Config.TRAIT_CODE_ENDING.replace("//HERE GOES FUNCTIONS",
                                                                    "public static bool " + attack_options.get() + "Attack"
                                                                    + Config.ATTACK_ACTION_BEGGINING + Config.ASSORTED_MAGIC_CODE +  Config.ATTACK_ACTION_ENDING) 
    elif attack_actions.get() == "":
         Config.TRAIT_CODE_ENDING = Config.TRAIT_CODE_ENDING

# ---------------------------------------------------------- #



# ----------------------BUTTONS ---------------------- #
def new_button(string, cmd): 
     return ctk.CTkButton(initialFrame, text=string, width=100, fg_color="#fcf9ff", text_color="#101519", corner_radius=5, command=cmd)
     
traitCreate = new_button("Create Trait", traitCreate)
effectCreate = new_button("Create Effect", effectCreate)
write = new_button("Write", write)
attackCreate = new_button("Create Atttack", create_attack_for_trait)
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

ACTIONS = [
     "Assorted Magic"
]

options = ctk.StringVar(value="BurningEffect")
attack_options = ctk.StringVar(value="")
attack_actions = ctk.StringVar(value="")
dropdown = ctk.CTkOptionMenu(initialFrame, values=OPTIONS, variable=options, fg_color="#203547",button_color="#203547")
attack_action_dropdown = ctk.CTkOptionMenu(initialFrame, values=ACTIONS, variable=attack_actions, fg_color="#203547",button_color="#203547")
attack_action_dropdown.grid(row=1, column=6, padx=2, pady=4)
# ATTACK ACTION FEATURE | WIP
def populate_options(dynamic_options):    
    dropdown2 = ctk.CTkOptionMenu(initialFrame, values=dynamic_options, variable=attack_options, fg_color="#203547",button_color="#203547")
    dropdown2.grid(row=0, column=6, padx=2, pady=4)
# ---------------------------------------------------------- #

# ---------------------- FORMATTING ---------------------- #
def setup_labels():
    trait_labels = Formatting.create_labels_traits(initialFrame)
    effect_labels = Formatting.create_labels_effects(initialFrame)
    action_labels = Formatting.create_labels_actions(initialFrame)
    for i, trait_labels in enumerate(trait_labels):
        trait_labels.grid(row=i, column=0, padx=4, pady=4)

    for i, effect_labels in enumerate(effect_labels):
        effect_labels.grid(row=i, column=3, padx=10, pady=4)

    for i, action_labels in enumerate(action_labels):
         action_labels.grid(row=i, column=5, padx=10, pady=4)

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
effects_window, traits_window = Formatting.window_formatting(WindowsFrame) # These Vars are called in Button Logic!


write.grid(row=16, column=1, padx=10, pady=20) #Write button only used for testing right now

attackCreate.grid(row=2, column=6, padx=2, pady=4) #ATTACK CREATION FEATURE | WIP

format_entries() #called function
setup_labels() #called function
# ---------------------------------------------------------- #


root.mainloop() #Main Loop