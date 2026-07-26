import tkinter as tk
from tkinter import messagebox

class MorseCode:
    def __init__(self, root,):
        self.root = root
        self.root.configure(bg="#000000")
        self.root_label = tk.Label(self.root, text="Enter the text",font=("Times New Roman", 15, "bold"), bg="#FFFFFF", fg="#4768C4")
        self.root_label.pack(pady=10)
        self.root_entry = tk.Entry(self.root, font=("Times New Roman", 15, "bold"), bg="#FFFFFF", fg="#4768C4")
        self.root_entry.pack(pady=30)
        self.root_btn = tk.Button(self.root, text="Translate", font=("Arial", 12, "bold"), bg="#FFFFFF", fg="#830730", command= self.Translate)
        self.root_btn.pack(pady=10)
        self.root_btn2 = tk.Button(self.root, text="Reset",font=("Arial", 12, "bold"),bg="#FFFFFF",fg="#479FC4",command= self.Reset)
        self.root_btn2.pack(pady=10)
        self.output_label = tk.Label(self.root, text="", font=("Times New Roman", 12), bg="#000000", fg="#FFFFFF")
        self.output_label.pack(pady=10)
        
    MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..__..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'}

    
    def Translate(self):
        text = self.root_entry.get()
        if not text:
            messagebox.showwarning("Warning", "Please enter text to translate.")
            return ""
        morse_list = []
        for char in text.upper():
            if char == ' ':
                morse_list.append('/')
            elif char in self.MORSE_CODE_DICT:
                morse_list.append(self.MORSE_CODE_DICT[char])
            else:
                morse_list.append('?')
        result = ' '.join(morse_list)
        try:
            self.output_label.config(text=result)
            messagebox.showinfo("Morse Code", result)
        except Exception:
            pass
        return result
    def Reset(self):
        try:
            self.root_entry.delete(0, tk.END)
        except Exception:
            pass
        try:
            self.output_label.config(text="")
        except Exception:
            self.output_label = tk.Label(self.root, text="", font=("Times New Roman", 12), bg="#000000", fg="#FFFFFF")
            self.output_label.pack(pady=10)
        try:
            self.root_entry.focus_set()
        except Exception:
            pass

if __name__ == '__main__':
    window = tk.Tk()
    window.geometry("400x500")
    window.resizable(False, False)
    window.title("Text to Morse Code")
    app = MorseCode(window)
    window.mainloop()