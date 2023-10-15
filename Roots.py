from tkinter import *
import customtkinter as ctk
import time


class Roots:
    root = ctk.CTk(fg_color="#101519")
    initialFrame = ctk.CTkFrame(root, fg_color="#101519")
    WindowsFrame = ctk.CTkFrame(root, fg_color="#101519")
    writeButtonFrame = ctk.CTkFrame(root, fg_color="#101519")
    root.geometry("1800x900")
    initialFrame.grid(row=0, column=0, padx=4, pady=0)
    WindowsFrame.grid(row=0, column=1, padx=20, pady=0)
    writeButtonFrame.grid(row=1, column=1, padx=20, pady=0)

    def close_root():
        Roots.root.destroy()

    def loading_window():
        loading = ctk.CTk(fg_color="#101519")
        loading.geometry("300x100")
        loading.title("Creating Mod")

        label = ctk.CTkLabel(loading, text="Creating Mod...", font=("Arial", 12))
        label.pack(pady=10)

        progressbar = ctk.CTkProgressBar(loading, mode="determinate")
        progressbar.pack(pady=10)
        progressbar.start()  # Start the progress bar animation

        def simulate_task():
            # Simulate some time-consuming task
            for _ in range(20):
                loading.update_idletasks()
                time.sleep(0.1)
                loading.update()

            progressbar.stop()
            loading.destroy()
            Roots.close_root()  # Close the main application

        loading.after(100, simulate_task)
