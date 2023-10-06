import customtkinter as ctk

class Formatting:
    def new_label(string, frame):
        return ctk.CTkLabel(frame, text=string, font=ctk.CTkFont(family="", size=15, weight="bold"), text_color="#fcf9ff")
        
    def create_labels_traits(frame): 
        idLabel = Formatting.new_label("Trait Name: ", frame)
        healthLabel = Formatting.new_label("Health: ", frame)
        damageLabel = Formatting.new_label("Damage: ", frame)
        attackSpeedLabel = Formatting.new_label("Attack Speed: ", frame)
        critChanceLabel = Formatting.new_label("Crit Chance: ", frame)
        rangeLabel = Formatting.new_label("Range: ", frame)
        accLabel = Formatting.new_label("Accuracy: ", frame)
        speedLabel = Formatting.new_label("Speed: ", frame)
        dodgeLabel = Formatting.new_label("Dodge Chance: ", frame)
        intelligenceLabel = Formatting.new_label("Intelligence: ", frame)
        warfareLabel = Formatting.new_label("Warfare: ", frame)
        stewardshipLabel = Formatting.new_label("Stewardship: ", frame)
        scaleLabel = Formatting.new_label("Scale: ", frame)
        descLabel = Formatting.new_label("Description: ", frame)
        effectsLabel = Formatting.new_label("Attack Effects: ", frame)

        return [
        idLabel, healthLabel, damageLabel, attackSpeedLabel, critChanceLabel, 
        rangeLabel, accLabel, speedLabel, dodgeLabel, intelligenceLabel, 
        warfareLabel, stewardshipLabel,
        scaleLabel, descLabel, effectsLabel
        ]

    def create_labels_effects(frame): 
        idLabel = Formatting.new_label("Effect Name: ", frame)
        healthLabel = Formatting.new_label("Health: ", frame)
        damageLabel = Formatting.new_label("Damage: ", frame)
        attackSpeedLabel = Formatting.new_label("Attack Speed: ", frame)
        critChanceLabel = Formatting.new_label("Crit Chance: ", frame)
        rangeLabel = Formatting.new_label("Range: ", frame)
        accLabel = Formatting.new_label("Accuracy: ", frame)
        speedLabel = Formatting.new_label("Speed: ", frame)
        dodgeLabel = Formatting.new_label("Dodge Chance: ", frame)
        intelligenceLabel = Formatting.new_label("Intelligence: ", frame)
        duration = Formatting.new_label("Duration: ", frame)
        knockbackLabel = Formatting.new_label("KnockBack", frame)
        knockbackRLabel = Formatting.new_label("KnockBack Reduction", frame)
        descLabel = Formatting.new_label("Description: ", frame)

        return [
        idLabel, healthLabel, damageLabel, attackSpeedLabel, critChanceLabel, 
        rangeLabel, accLabel, speedLabel, dodgeLabel, intelligenceLabel, duration, 
        knockbackLabel, knockbackRLabel, descLabel,
        ]

    # TRAIT AND EFFECT LABEL FUCTIONS #
    def add_trait_to_list(id, frame):
        traitAdded = ctk.CTkLabel(frame, text=id, font=ctk.CTkFont(family="", size=12, weight="normal"), text_color="#fcf9ff")
        traitAdded.pack()

    def add_effect_to_list(id, frame):
        traitAdded = ctk.CTkLabel(frame, text=id, font=ctk.CTkFont(family="", size=12, weight="normal"), text_color="#fcf9ff")
        traitAdded.pack()

    def window_formatting(frame): 
        traits_window_label = ctk.CTkLabel(frame, text="Traits Added: ", font=ctk.CTkFont(family="", size=15, weight="bold"), text_color="#fcf9ff")
        effects_window_label = ctk.CTkLabel(frame, text="Effects Added: ", font=ctk.CTkFont(family="", size=15, weight="bold"), text_color="#fcf9ff")
        effects_window_label.grid(row=0, column=0, padx=10, pady=4)
        traits_window_label.grid(row=0, column=1, padx=10, pady=4)
        effects_window =ctk.CTkScrollableFrame(frame, fg_color="#203547", width=150, height=200)
        effects_window.grid(row=1, column=0, padx=10, pady=4)
        traits_window =ctk.CTkScrollableFrame(frame, fg_color="#203547", width=150, height=200)
        traits_window.grid(row=1, column=1, padx=10, pady=4)
        return effects_window, traits_window


    