import tkinter as tk
import difflib

def load_dictionary(file_path):
    words = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                word = line.strip().lower()
                if word:
                    words.append(word)
    except FileNotFoundError:
        print("Dictionary file not found!")
    return words

def autocorrect_word(word, dictionary_words):
    matches = difflib.get_close_matches(word.lower(), dictionary_words, n=1, cutoff=0.7)
    return matches[0] if matches else word

def autocorrect_text(text, dictionary_words):
    words = text.split()
    corrected_words = []
    for word in words:
        corrected_words.append(autocorrect_word(word, dictionary_words))
    return " ".join(corrected_words)

def on_key_release(event):
    text = input_box.get("1.0", tk.END).strip()
    corrected = autocorrect_text(text, dictionary_words)

    output_box.config(state=tk.NORMAL)
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, corrected)
    output_box.config(state=tk.DISABLED)

dictionary_words = load_dictionary("dictionary.txt")

if not dictionary_words:
    print("Dictionary is empty or not loaded.")
    exit()

window = tk.Tk()
window.title("Live Autocorrect Tool")
window.geometry("600x400")

tk.Label(window, text="Type here (Auto-Correct While Typing):").pack(pady=5)

input_box = tk.Text(window, height=5, font=("Arial", 11))
input_box.pack(padx=10, pady=5, fill=tk.BOTH)
input_box.bind("<KeyRelease>", on_key_release)

tk.Label(window, text="Corrected Output:").pack(pady=5)

output_box = tk.Text(window, height=5, font=("Arial", 11), state=tk.DISABLED)
output_box.pack(padx=10, pady=5, fill=tk.BOTH)

window.mainloop()

