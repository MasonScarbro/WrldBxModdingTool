from tkinter import *
import customtkinter as ctk
import re

import numpy as np
import array as arr
import string
from GUI import Formatting
from Constants import Config
from Roots import Roots
from Entries import Entries
from customtkinter import filedialog
import os
from pathlib import Path
import shutil
from Options import Options

# Set the working directory to the directory containing Main.py
os.chdir(os.path.dirname(__file__))



# ---------------------- BUTTON COMMANDS ---------------------- #
projectile_paths = []
trait_string = ''
effect_string = ''
projectile_string = ''
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
                    "\n\t\t" + "AssetManager.traits.add(" + traitId +");"
                    "\n\t\t" + "PlayerConfig.unlockTrait(" + traitId +".id);"
                    "\n\t\t" + "addTraitToLocalizedLibrary(" + traitId +".id, " + '"' + Entries.description.get() + '");'
                    "\n")
        traitsArr.append(traitId)
        Formatting.add_trait_to_list(traitId, traits_window)
        Options.populate_options(traitsArr) #ATTACK FEATURE | WIP
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
                    "\n\t\t" + effectId + ".description = " + '"' + Entries.description.get() + '";'
                    "\n\t\t" + effectId + ".name = " + '"status_title_' + effectId + '";'
                    "\n\t\t" + "AssetManager.status.add(" + effectId +");"
                    "\n\t\t" + "localizeStatus(" + effectId + ".id, " + '"' +effectId + '", ' + effectId + ".description" + ');'
                    "\n")
        effectsArr.append(effectId)
        Formatting.add_effect_to_list(effectId, effects_window)
        print(effectsArr)

# WRITING TO FILE BUTTON | TESTING #
def write():
    program_files_path = Path(os.environ['PROGRAMFILES(X86)']) if os.name == 'nt' else Path('/usr/local') #Cross OS compatability
    modFolder_base_path = program_files_path / "Steam" / "steamapps" / "common" / "worldbox" / "Mods" # the base path of the folder (if it exists if not we do the same thing but we create the file)
    assembly_file_path = program_files_path / "Steam" / "steamapps" / "common" / "worldbox" / "worldbox_Data" / "Managed" / "Assembly-CSharp.dll"

    count = 1
    if projectile_paths:
     for projectile_path in projectile_paths:
          projectile_path = Path(projectile_path)
          for fileName in projectile_path.glob("*.png"):
               path = fileName
               pathBefore = re.search(r'^(.*\\)([^\\]+)$', str(path)) # Regex for everything before the png
               pathBefore = pathBefore.group(1) 
               #print(pathBefore) -- TESTING

               path.rename(pathBefore + str(count) + ".png") #now the path rename will rename every single image to a count
               count += 1

    if modFolder_base_path.exists():
    
         print("Check")
         base_path = modFolder_base_path / Entries.modName.get() #- Instead of  my mod it will just be the name of the mod
         effects_path = base_path / "GameResources" / "effects" / "projectiles"
         code_path = base_path / "Code"
         assembly_path = base_path / "Assemblies"
         base_path.mkdir(parents=True, exist_ok=True)
         effects_path.mkdir(parents=True, exist_ok=True)
         code_path.mkdir(parents=True, exist_ok=True)
         assembly_path.mkdir(parents=True, exist_ok=True)
         #print(code_path.exists()) --TESTING
         
         if projectile_paths:
          for projectile_path in projectile_paths:
                    lastDir = re.search(r'\/([^/]+)$', projectile_path)
                    lastDir = lastDir.group(1)
                    projectile_path = Path(projectile_path)
                    projectile_path.rename(effects_path / lastDir)

         Config.TRAIT_CODE_BEGINNING = Config.TRAIT_CODE_BEGINNING.replace("MyMod", Entries.modName.get())
         Config.EFFECTS_CODE_BEGINNING = Config.EFFECTS_CODE_BEGINNING.replace("MyMod", Entries.modName.get())
         Config.PROJECTILE_CODE_BEGINNING = Config.PROJECTILE_CODE_BEGINNING.replace("MyMod", Entries.modName.get())
         Config.MAIN_CODE = Config.MAIN_CODE.replace("MyMod", Entries.modName.get())

         write_to_json(base_path)
         shutil.copy2(assembly_file_path, assembly_path)
         with open(code_path / "Main.cs", 'a') as f:
            f.write(Config.MAIN_CODE)
         with open(code_path / "NewTraits.cs", 'a') as f:
            f.write(Config.TRAIT_CODE_BEGINNING + trait_string + Config.TRAIT_CODE_ENDING)
         with open(code_path / "NewEffects.cs", 'a') as f:
             f.write(Config.EFFECTS_CODE_BEGINNING + effect_string + Config.EFFECTS_CODE_ENDING)
         with open(code_path / "NewProjectiles.cs", 'a') as f:
             f.write(Config.PROJECTILE_CODE_BEGINNING + projectile_string + Config.PROJECTILE_CODE_ENDING)
         print(projectile_paths)
         Roots.loading_window()
    else:
        print(modFolder_base_path.exists() + modFolder_base_path)
         
    

# BUTTON FOR ATTACK CREATION #
def create_attack_for_trait():
    
    print("clicked")
    print(Options.attack_options.get())
    global trait_string
    
                    
    #I Know, Im Editing a constant which is evil or whatever but I did Not whant to create a new variable and or take this var out of constants its to pretty there
    if Options.attack_actions.get() == "Assorted Magic":
        trait_string = trait_string.replace("//" + Options.attack_options.get() + "AttackFunction", Options.attack_options.get() + ".action_attack_target = new AttackAction(" + Options.attack_options.get() + "Attack);")
        Config.TRAIT_CODE_ENDING = Config.TRAIT_CODE_ENDING.replace("//HERE GOES FUNCTIONS",
                                                                    "public static bool " + Options.attack_options.get() + "Attack"
                                                                    + Config.ATTACK_ACTION_BEGGINING + Config.ASSORTED_MAGIC_CODE +  Config.ATTACK_ACTION_ENDING) 
        traitsArr.remove(Options.attack_options.get())
        Options.populate_options(traitsArr)
        
    elif Options.attack_actions.get() in ["BurningEffect", "SlowEffect", "FrozenEffect", "PoisonedEffect"]:
        trait_string = trait_string.replace("//" + Options.attack_options.get() + "AttackFunction", Options.attack_options.get() + ".action_attack_target = new AttackAction(ActionLibrary.add" + Options.attack_actions.get() + "OnTarget);")
        traitsArr.remove(Options.attack_options.get())
        Options.populate_options(traitsArr)

    else:
        trait_string = trait_string.replace("//" + Options.attack_options.get() + "AttackFunction", Options.attack_options.get() + ".action_attack_target = new AttackAction(" + Options.attack_options.get() + "Attack);")
        Config.TRAIT_CODE_ENDING = Config.TRAIT_CODE_ENDING.replace("//HERE GOES FUNCTIONS",
                                                                    "public static bool " + Options.attack_options.get() + "Attack" + Config.ATTACK_ACTION_BEGGINING 
                                                                    + Config.PROJECTILE_ACTION_BEGGINING + '\n\t\t\t\t\tEffectsLibrary.spawnProjectile(' + '"' + Options.attack_actions.get() + '"' + ', newPoint, newPoint2, 0.0f);' +  Config.PROJECTILE_ACTION_ENDING + Config.ATTACK_ACTION_ENDING)
        traitsArr.remove(Options.attack_options.get())
        Options.populate_options(traitsArr)

# create projectile and choose sprite might end up being the same button
def choose_sprite():
     
     filepath = ctk.filedialog.askdirectory(title="Select Sprite")

     lastDir = re.search(r'\/([^/]+)$', filepath)
     lastDir = lastDir.group(1)
     print("Directory: " +  lastDir) # Use last dir as the texture name since it will be stored in the projectiles 
     #Path(filepath).rename('\Program Files (x86)\Steam\steamapps\common\worldbox\\' +  lastDir) -- WHEN WE WRITE TO FILE LOOP THORUGH THE DIRS AND DO THIS BUT FOR PROJECTILES
     global projectile_string
     projectile_string += ("\n"
                           "\t\t\tAssetManager.projectiles.add(new ProjectileAsset" 
                           "\n\t\t\t{"
                           "\n\t\t\t\tid = " + '"' + Entries.inputProjectileId.get() + '",'
                           "\n\t\t\t\tspeed = " + Entries.speed_projectile.get() + "f,"
                           "\n\t\t\t\ttexture = " + '"' + lastDir + '",'
                           "\n\t\t\t\ttexture_shadow = " + '"' + "shadow_ball" + '",'
                           "\n\t\t\t\tendEffect = string.Empty,"
                           "\n\t\t\t\tterraformRange = " + Entries.terraform_range.get() + ","
                           "\n\t\t\t\tdraw_light_area = true,"
                           "\n\t\t\t\tdraw_light_size = 0.1f,"
                           "\n\t\t\t\tlooped = " + Options.looped.get() + ","
                           "\n\t\t\t\tlook_at_target = " + Options.look_to_target.get() + ","   
                           "\n\t\t\t\tsound_launch =" + '"event:/SFX/WEAPONS/WeaponFireballStart"' + ","
                           "\n\t\t\t\tstartScale = " + Entries.start_scale.get() + "f,"
                           "\n\t\t\t\ttargetScale = " + Entries.target_scale.get() + "f,"
                           "\n\t\t\t});"
                           "\n")

     # - NOTES - #
     # we will later loop through this and change all the paths to be stoed inside projectiles
     # before that we will loop through each path and change all files to be 0 to n where n is number of sprites
     # as for what the texture will be named it will just be the current file path stripped done to the filename prior to it being appended
     projectile_paths.append(filepath) #loop thorugh and change the file path like we did up there at the end when we write 
     Options.populate_options_actions(Entries.inputProjectileId.get())
     Formatting.add_trait_to_list(Entries.inputProjectileId.get(), projectile_window)
     

def write_to_json(base_path):
    
    json = ('{\n'
  '\n"name":' + '"' + Entries.modName.get() + '",'
  '\n"author": "Mason Scarbro",'
  '\n"version": "0.0.1",'
  '\n"description": "My First Mod!",'
  '\n"targetGameBuild": 558,'
  '\n"iconPath": "icon.png"'
'\n}')
    with open(base_path / "mod.json", 'a') as f:
            f.write(json)
    
     

# ---------------------------------------------------------- #



# ----------------------BUTTONS ---------------------- #
def new_button(string, cmd): 
     return ctk.CTkButton(Roots.initialFrame, text=string, width=100, fg_color="#fcf9ff", text_color="#101519", corner_radius=5, command=cmd)
     
traitCreate = new_button("Create Trait", traitCreate)
effectCreate = new_button("Create Effect", effectCreate)
write = ctk.CTkButton(Roots.writeButtonFrame, text="Create Mod", width=100, fg_color="#fcf9ff", text_color="#101519", corner_radius=5, command=write)
attackCreate = new_button("Create Atttack", create_attack_for_trait)
sprite = new_button("Choose Sprite", choose_sprite)
# ---------------------------------------------------------- #



# ---------------------- OPTIONS ---------------------- #





     
# ---------------------------------------------------------- #

# ---------------------- FORMATTING ---------------------- #


    

def format_entries():
     traits_entries = Entries.entryTraitArr
     effect_entries = Entries.entryEffectAr
     projecile_entries = Entries.entryProjectilesArr

     for i, traits_entries in enumerate(traits_entries):
          traits_entries.grid(row=i, column=1, padx=2, pady=4)
          length=i+1
    
     
     traitCreate.grid(row=length, column=1, padx=2, pady=4)
     length=0 #reset length fopr next for loop

     for i, effect_entries in enumerate(effect_entries):
          effect_entries.grid(row=i, column=4, padx=2, pady=4)
          length=i+1
     effectCreate.grid(row=length, column=4, padx=2, pady=4)
     length=0

     for i, projecile_entries in enumerate(projecile_entries):
          projecile_entries.grid(row=i, column=6, padx=2, pady=4)
          length=i+1
     sprite.grid(row=length, column=6, padx=2, pady=4)
            

#    WINDOW FORMATTING    #
effects_window, traits_window, projectile_window = Formatting.window_formatting(Roots.WindowsFrame) # These Vars are called in Button Logic!


write.grid(row=2, column=1, padx=10, pady=20) #Write button only used for testing right now

attackCreate.grid(row=3, column=8, padx=2, pady=4) #ATTACK CREATION FEATURE | WIP

format_entries() #called function
Formatting.setup_labels() #called function
# ---------------------------------------------------------- #


Roots.root.mainloop() #Main Loop