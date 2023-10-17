from tkinter import *
import customtkinter as ctk
from Roots import Roots


class Options:
    OPTIONS = [
        "BurningEffect",
        "SlowEffect",
        "FrozenEffect",
        "PoisonedEffect",
    ]

    # Potentially append the action to the end of the list and use the same method as populate array to dynamically add the item to the list
    actions = ["Assorted Magic"]

    T_OR_F = ["true", "false"]

    options = ctk.StringVar(value="BurningEffect")
    attack_options = ctk.StringVar(value="")
    attack_actions = ctk.StringVar(value="")

    look_to_target = ctk.StringVar(value="false")
    looped = ctk.StringVar(value="true")
    looped_dropdown = ctk.CTkOptionMenu(
        Roots.initialFrame,
        values=T_OR_F,
        variable=looped,
        fg_color="#203547",
        button_color="#203547",
    )
    look_to_target_dropdown = ctk.CTkOptionMenu(
        Roots.initialFrame,
        values=T_OR_F,
        variable=look_to_target,
        fg_color="#203547",
        button_color="#203547",
    )

    dropdown = ctk.CTkOptionMenu(
        Roots.initialFrame,
        values=OPTIONS,
        variable=options,
        fg_color="#203547",
        button_color="#203547",
    )

    attack_action_dropdown = ctk.CTkOptionMenu(
        Roots.initialFrame,
        values=actions,
        variable=attack_actions,
        fg_color="#203547",
        button_color="#203547",
    )
    attack_action_dropdown.grid(row=1, column=8, padx=2, pady=4)

    def populate_options_actions(sprite):
        Options.actions.append(sprite)
        attack_action_dropdown = ctk.CTkOptionMenu(
            Roots.initialFrame,
            values=Options.actions,
            variable=Options.attack_actions,
            fg_color="#203547",
            button_color="#203547",
        )
        attack_action_dropdown.grid(row=1, column=8, padx=2, pady=4)

    # ATTACK ACTION FEATURE | WIP
    def populate_options(dynamic_options):
        dropdown2 = ctk.CTkOptionMenu(
            Roots.initialFrame,
            values=dynamic_options,
            variable=Options.attack_options,
            fg_color="#203547",
            button_color="#203547",
        )
        dropdown2.grid(row=0, column=8, padx=2, pady=4)
