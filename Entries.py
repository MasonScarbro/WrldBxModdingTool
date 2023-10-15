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


class Entries:
    def new_entry():
        return ctk.CTkEntry(
            Roots.initialFrame,
            border_color="#1D3142",
            fg_color="#203547",
            text_color="#D0D0E1",
        )

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

    entryTraitArr = [
        inputTraitId,
        health,
        damage,
        attackSpeed,
        criticalChance,
        rangeT,
        accuracy,
        speed,
        dodge,
        intelligence,
        warfare,
        stewardship,
        scale,
        description,
    ]

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

    entryEffectAr = [
        inputEffectId,
        health_effect,
        damage_effect,
        attackSpeed_effect,
        criticalChance_effect,
        rangeE,
        accuracy_effect,
        speed_effect,
        dodge_effect,
        intelligence_effect,
        duration,
        knockback_effect,
        knockbackR_effect,
        description_effect,
    ]

    inputProjectileId = new_entry()
    inputProjectileId.insert(0, "ProjectileRando")
    speed_projectile = new_entry()
    speed_projectile.insert(0, 0)
    terraform_range = new_entry()
    terraform_range.insert(0, 0)
    start_scale = new_entry()
    start_scale.insert(0, 0.0)
    target_scale = new_entry()
    target_scale.insert(0, 0.0)

    entryProjectilesArr = [
        inputProjectileId,
        speed_projectile,
        terraform_range,
        start_scale,
        target_scale,
    ]

    modName = ctk.CTkEntry(
            Roots.writeButtonFrame,
            border_color="#1D3142",
            fg_color="#203547",
            text_color="#D0D0E1",
        )
    modName.insert(0, "NameOfTheMod")
    modName.grid(row=1, column=1, padx=10, pady=20)
