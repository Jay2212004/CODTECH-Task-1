'''This program creates a password strength tester with a Tkinter interface. 
Users type in their username and password. 
The program then checks how strong the password is. 
It looks at things like how long it is how complex it is, and if it's unique. 
The program shows how strong the password is with different colors. 
We can also click a button to see or hide the password. 
The program checks a few things about the password. 
It sees how long it is. It makes sure it's not too much like the username. 
It checks for big and small letters, numbers, and special symbols. 
The program has boxes where you type your username and password. 
It has buttons to test the password and to show or hide it. 
The program calls passwords "Very Strong," "Strong," "Medium," or "Weak." 
Each level has its own color.
'''
import string
import tkinter as tk
from tkinter import ttk

def assess_password_strength(username, password):
    if len(password) < 8:
        return "Too Short", 0, 'red'
    if any(username[i:i+3].lower() in password.lower() for i in range(len(username) - 2)):
        return "Password is similar to username", 0, 'red'
    if not any(char.islower() for char in password):
        return "Needs a lowercase letter", 0, 'red'
    if len(password) <= 15 and not any(char.isupper() for char in password):
        return "Needs an uppercase letter", 0, 'red'

    length_score = len(password)
    complexity_score = 0
    uniqueness_score = len(set(password))
    
    if any(char.islower() for char in password):
        complexity_score += 1
    if any(char.isupper() for char in password):
        complexity_score += 1
    if any(char.isdigit() for char in password):
        complexity_score += 1
    if any(char in string.punctuation for char in password):
        complexity_score += 1

    total_score = length_score + complexity_score * 2 + uniqueness_score
    
    if total_score >= 30:
        return "Very Strong", total_score, 'green'
    elif total_score >= 20:
        return "Strong", total_score, 'green'
    elif total_score >= 10:
        return "Medium", total_score, 'yellow'
    else:
        return "Weak", total_score, 'red'

def toggle_password():
    if password_entry.cget('show') == '':
        password_entry.config(show='*')
        eye_button.config(text='Show')
    else:
        password_entry.config(show='')
        eye_button.config(text='Hide')

def check_password():
    username = username_entry.get()
    password = password_entry.get()
    strength, score, color = assess_password_strength(username, password)
    result_label.config(text=f"Password Strength: {strength} (Score: {score})", foreground=color)

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("450x350")
root.configure(bg='#f0f0f0')

style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12), background="#f0f0f0")
style.configure("TButton", font=("Helvetica", 12), padding=6)
style.configure("TEntry", font=("Helvetica", 12), padding=6)

ttk.Label(root, text="Enter your username:").pack(pady=5)
username_entry = ttk.Entry(root, width=30)
username_entry.pack(pady=5)

ttk.Label(root, text="Enter your password:").pack(pady=10)
password_entry = ttk.Entry(root, show='*', width=30)
password_entry.pack(pady=10)

eye_button = ttk.Button(root, text='Show Password', command=toggle_password)
eye_button.pack(pady=5)

check_button = ttk.Button(root, text="Check Strength", command=check_password)
check_button.pack(pady=10)

result_label = ttk.Label(root, text="Password Strength: ")
result_label.pack(pady=10)

root.mainloop()
