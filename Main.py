from tkinter import *
import customtkinter as ctk
import re
import os
import numpy as np
import array as arr
import string
from GUI import Formatting
from Constants import Config
from Roots import Roots
from Entries import Entries
from customtkinter import filedialog


#filename = ctk.filedialog.askopenfilename(title="Select Sprite", filetypes=(("What goes here?"),()))





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
    traitId = "".join(Entries.inputTraitId.get().split())
    if traitId in traitsArr:
         trait_string += "\n\t\t// You tried to create a trait with the same name of " + Entries.inputTraitId.get() + " That's not possible in coding!"
         print(traitsArr)
    else:
        trait_string += ("\n\t\tActorTrait " + traitId + " = new ActorTrait();"
                    "\n\t\t" + traitId + ".id" + " = " + '"' + Entries.inputTraitId.get() + '";'
                    "\n\t\t" + traitId + ".path_icon" + " = " + '"ui/icons/achievements/achievements_thedemon";'
                    "\n\t\t" + traitId + ".base_stats[S.damage] += " + Entries.damage.get() + "f;"
                    "\n\t\t" + traitId + ".base_stats[S.health] += " + Entries.health.get() + "f;"
                    "\n\t\t" + traitId + ".base_stats[S.attack_speed] += " + Entries.attackSpeed.get() + "f;"
                    "\n\t\t" + traitId + ".base_stats[S.critical_chance] += " + Entries.criticalChance.get() + "f;"
                    "\n\t\t" + traitId + ".base_stats[S.speed] += " + Entries.speed.get() + "f;"
                    "\n\t\t" + traitId + ".base_stats[S.dodge] += " + Entries.dodge.get() + "f;"
                    "\n\t\t" + traitId + ".base_stats[S.accuracy] += " + Entries.accuracy.get() + "f;"
                    "\n\t\t" + traitId + ".base_stats[S.range] += " + Entries.rangeT.get() + "f;"
                    "\n\t\t" + traitId + ".base_stats[S.scale] += " + Entries.scale.get() + "f;"
                    "\n\t\t" + traitId + ".base_stats[S.intelligence] += " + Entries.intelligence.get() + "f;"
                    "\n\t\t" + traitId + ".base_stats[S.warfare] += " + Entries.warfare.get() + "f;"
                    "\n\t\t" + traitId + ".base_stats[S.stewardship] += " + Entries.stewardship.get() + "f;"
                    "\n\t\t//" + traitId + "AttackFunction"
                    "\n\t\t" + traitId + ".action_attack_target = new AttackAction(ActionLibrary.add" + options.get() + "OnTarget);"
                    "\n\t\t" + "AssetManager.traits.add(" + traitId +");"
                    "\n\t\t" + "PlayerConfig.unlockTrait(" + traitId +".id);"
                    "\n\t\t" + "addTraitToLocalizedLibrary(" + traitId +".id, " + '"' + Entries.description.get() + '");'
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
    effectId = "".join(Entries.inputEffectId.get().split())
    if effectId in effectsArr:
         effect_string += "\n\t\t// You tried to create an effect with the same name of " + Entries.inputEffectId.get() + " That's not possible in coding!"
         print(effectsArr)
    else:
        effect_string += ("\n\t\tStatusEffect " + effectId + " = new StatusEffect();"
                    "\n\t\t" + effectId + ".id" + " = " + '"' + Entries.inputEffectId.get() + '";'
                    "\n\t\t" + effectId + ".duration" + " = " + Entries.duration.get() + "f;"
                    "\n\t\t" + effectId + ".base_stats[S.damage] += " + Entries.damage_effect.get() + "f;"
                    "\n\t\t" + effectId + ".base_stats[S.health] += " + Entries.health_effect.get() + "f;"
                    "\n\t\t" + effectId + ".base_stats[S.attack_speed] += " + Entries.attackSpeed_effect.get() + "f;"
                    "\n\t\t" + effectId + ".base_stats[S.critical_chance] += " + Entries.criticalChance_effect.get() + "f;"
                    "\n\t\t" + effectId + ".base_stats[S.speed] += " + Entries.speed_effect.get() + "f;"
                    "\n\t\t" + effectId + ".base_stats[S.dodge] += " + Entries.dodge_effect.get() + "f;"
                    "\n\t\t" + effectId + ".base_stats[S.accuracy] += " + Entries.accuracy_effect.get() + "f;"
                    "\n\t\t" + effectId + ".base_stats[S.range] += " + Entries.rangeE.get() + "f;"
                    "\n\t\t" + effectId + ".base_stats[S.knockback_reduction] += " + Entries.knockbackR_effect.get() + "f;"
                    "\n\t\t" + effectId + ".base_stats[S.knockback] += " + Entries.knockback_effect.get() + "f;"
                    "\n\t\t" + effectId + ".path_icon" + " = " + '"ui/icons/achievements/achievements_thedemon";'
                    "\n\t\t" + effectId + ".name = " + '"status_title_' + effectId + '";'
                    "\n\t\t" + "AssetManager.status.add(" + effectId +");"
                    "\n\t\t" + "addTraitToLocalizedLibrary(" + effectId +".id, " + '"' + Entries.description.get() + '");'
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
     return ctk.CTkButton(Roots.initialFrame, text=string, width=100, fg_color="#fcf9ff", text_color="#101519", corner_radius=5, command=cmd)
     
traitCreate = new_button("Create Trait", traitCreate)
effectCreate = new_button("Create Effect", effectCreate)
write = new_button("Write", write)
attackCreate = new_button("Create Atttack", create_attack_for_trait)
# ---------------------------------------------------------- #



# ---------------------- OPTIONS ---------------------- #

OPTIONS = [
     "BurningEffect",
     "SlowEffect",
     "FrozenEffect",
     "PoisonedEffect",

]

#Potentially append the action to the end of the list and use the same method as populate array to dynamically add the item to the list
actions = [
     "Assorted Magic"
]

options = ctk.StringVar(value="BurningEffect")
attack_options = ctk.StringVar(value="")
attack_actions = ctk.StringVar(value="")

dropdown = ctk.CTkOptionMenu(Roots.initialFrame, values=OPTIONS, variable=options, fg_color="#203547",button_color="#203547")

attack_action_dropdown = ctk.CTkOptionMenu(Roots.initialFrame, values=actions, variable=attack_actions, fg_color="#203547",button_color="#203547")
attack_action_dropdown.grid(row=1, column=8, padx=2, pady=4)


# ATTACK ACTION FEATURE | WIP
def populate_options(dynamic_options):    
    dropdown2 = ctk.CTkOptionMenu(Roots.initialFrame, values=dynamic_options, variable=attack_options, fg_color="#203547",button_color="#203547")
    dropdown2.grid(row=0, column=8, padx=2, pady=4)



     
# ---------------------------------------------------------- #

# ---------------------- FORMATTING ---------------------- #
def setup_labels():
    trait_labels = Formatting.create_labels_traits(Roots.initialFrame)
    effect_labels = Formatting.create_labels_effects(Roots.initialFrame)
    action_labels = Formatting.create_labels_actions(Roots.initialFrame)
    projectile_labels = Formatting.create_labels_projectiles(Roots.initialFrame)
    for i, trait_labels in enumerate(trait_labels):
        trait_labels.grid(row=i, column=0, padx=4, pady=4)

    for i, effect_labels in enumerate(effect_labels):
        effect_labels.grid(row=i, column=3, padx=10, pady=4)

    for i, action_labels in enumerate(action_labels):
         action_labels.grid(row=i, column=7, padx=10, pady=4)
    
    for i, projectile_labels in enumerate(projectile_labels):
         projectile_labels.grid(row=i, column=5, padx=10, pady=4)

    

def format_entries():
     traits_entries = Entries.entryTraitArr
     effect_entries = Entries.entryEffectAr
     projecile_entries = Entries.entryProjectilesArr

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

     for i, projecile_entries in enumerate(projecile_entries):
          projecile_entries.grid(row=i, column=6, padx=2, pady=4)

            

#    WINDOW FORMATTING    #
effects_window, traits_window = Formatting.window_formatting(Roots.WindowsFrame) # These Vars are called in Button Logic!


write.grid(row=16, column=1, padx=10, pady=20) #Write button only used for testing right now

attackCreate.grid(row=2, column=5, padx=2, pady=4) #ATTACK CREATION FEATURE | WIP

format_entries() #called function
setup_labels() #called function
# ---------------------------------------------------------- #


Roots.root.mainloop() #Main Loop