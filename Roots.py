from tkinter import *
import customtkinter as ctk


class Roots:
    root = ctk.CTk(fg_color="#101519")
    initialFrame = ctk.CTkFrame(root, fg_color="#101519")
    WindowsFrame = ctk.CTkFrame(root, fg_color="#101519")
    root.geometry("1800x900")
    initialFrame.grid(row=0, column=0, padx=4, pady=0)
    WindowsFrame.grid(row=0, column=1, padx=20, pady=0)
