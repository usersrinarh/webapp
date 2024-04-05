import sys
from tkinter import *
import subprocess

def run_subprocess(script_path):
    try:
        subprocess.run([sys.executable, script_path])
    except Exception as e:
        print(f"An error occurred: {e}")

def heartattackpredictor():
    run_subprocess("C:\\Users\\Srinath\\OneDrive\\Others\\Desktop\\bit\\heartdisease.py")

def diabeticpredictor():
    run_subprocess("C:\\Users\\Srinath\\OneDrive\\Others\\Desktop\\bit\\pyFile.py")

def main():
    root = Tk()
    root.title("Health Diagnostic AI Predictor")
    root.geometry("676x380")

    bg = PhotoImage(file="C:\\Users\\Srinath\\OneDrive\\Others\\Desktop\\bit\\dp4.png")
    canvas = Canvas(root, width=676, height=380)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg, anchor="nw")

    heartattack_button = Button(root, text="Heart Attack Predictor", command=heartattackpredictor)
    heartattack_button.pack(pady=10)

    diabetic_button = Button(root, text="Diabetic Predictor", command=diabeticpredictor)
    diabetic_button.pack(pady=20)

    root.mainloop()
