from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import pymysql

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registeration Window")
        self.root.geometry("1330x700+0+0")
        self.root.config(bg="white")
        