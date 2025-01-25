from pynput import keyboard, mouse
import pyperclip
import tkinter as tk
from tkinter import ttk
import requests
import platform
import subprocess
import os


# Fetch selected text
def get_selected_text():
    system = platform.system()
    if system == "Linux":
        try:
            result = subprocess.run(["xclip", "-o", "-selection", "primary"], capture_output=True, text=True)
            return result.stdout.strip()
        except FileNotFoundError:
            return "xclip not found. Install it using 'sudo apt install xclip'."
    elif system == "Darwin":  # macOS
        try:
            script = 'tell application "System Events" to keystroke "c" using command down'
            subprocess.run(["osascript", "-e", script])
            import pyperclip
            return pyperclip.paste()
        except Exception as e:
            return f"Error fetching selected text: {e}"
    elif system == "Windows":
        try:
            import pyautogui
            pyautogui.hotkey("ctrl", "c")
            import pyperclip
            return pyperclip.paste()
        except Exception as e:
            return f"Error fetching selected text: {e}"
    else:
        return "Unsupported platform."


# Translate text using Google Translate API
def translate_text(text, target_lang="si"):
    base_url = "http://translate.googleapis.com/translate_a/single"
    params = {
        "client": "gtx",
        "sl": "auto",  # Source language (auto-detect)
        "tl": target_lang,  # Target language
        "dt": "t",  # Return translation text
        "q": text  # Text to translate
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()

        # Parse the response JSON
        data = response.json()

        # Combine all translated segments
        translation = "\n".join([item[0] for item in data[0]])
        return translation
    except Exception as e:
        return f"Error: {e}"


# Save user preferences (font size, font family, window size, and language)
def save_config(font_size, font_family, window_width, window_height, language):
    with open("config.txt", "w") as config_file:
        config_file.write(f"{font_size}\n")
        config_file.write(f"{font_family}\n")
        config_file.write(f"{window_width}\n")
        config_file.write(f"{window_height}\n")
        config_file.write(f"{language}\n")


# Load user preferences (font size, font family, window size, and language)
def load_config():
    if os.path.exists("config.txt"):
        with open("config.txt", "r") as config_file:
            font_size = int(config_file.readline().strip())
            font_family = config_file.readline().strip()
            window_width = int(config_file.readline().strip())
            window_height = int(config_file.readline().strip())
            language = config_file.readline().strip()
            return font_size, font_family, window_width, window_height, language
    else:
        return 14, "Arial", 600, 400, "si"  # Default values


# Popup with translation
def translate_and_show():
    # Load previous settings
    font_size, font_family, window_width, window_height, language = load_config()

    # Get selected text
    selected_text = get_selected_text()
    if not selected_text.strip():
        return

    # Translate text
    translated_text = translate_text(selected_text, target_lang=language)

    # Create a pop-up window
    root = tk.Tk()
    root.title("Translation Popup")
    root.geometry(f"{window_width}x{window_height}")  # Set window size from config
    root.resizable(True, True)  # Allow resizing

    # Dynamically change font size and family
    def update_font(event=None):
        font_size = int(font_size_combo.get())
        font_family = font_family_combo.get()
        text_widget.config(font=(font_family, font_size))
        # save_config(font_size, font_family, root.winfo_width(), root.winfo_height(), language)  # Save settings

    # Update language and refresh translation
    def update_language(event=None):
        nonlocal language
        language = language_combo.get()
        translated_text = translate_text(selected_text, target_lang=language)
        text_widget.delete("1.0", tk.END)
        text_widget.insert("1.0", translated_text)
        save_config(font_size, font_family, root.winfo_width(), root.winfo_height(), language)  # Save settings

    # Close popup on mouse hover or Esc key
    def close_popup(event=None):
        root.destroy()

    # Get cursor position
    def get_cursor_position():
        mouse_controller = mouse.Controller()
        position = mouse_controller.position
        return position

    x, y = get_cursor_position()
    root.geometry(f"+{int(x)+10}+{int(y)+10}")

    # Frame for font size, font family, and language combo boxes
    control_frame = tk.Frame(root)
    control_frame.pack(anchor="n", pady=5, padx=10)

    # Font size combo box
    font_size_combo = ttk.Combobox(control_frame, values=[10, 12, 14, 16, 18, 20, 24, 28, 32], width=5)
    font_size_combo.set(font_size)
    font_size_combo.pack(side="left", padx=5)
    font_size_combo.bind("<<ComboboxSelected>>", update_font)

    # Font family combo box (list of common fonts)
    font_family_combo = ttk.Combobox(control_frame, values=["Arial", "Noto Sans Sinhala", "Iskoola Pota", "Times New Roman", "Courier New", "Helvetica"], width=15)
    font_family_combo.set(font_family)
    font_family_combo.pack(side="left", padx=5)
    font_family_combo.bind("<<ComboboxSelected>>", update_font)

    # Language selection combo box
    language_combo = ttk.Combobox(control_frame, values=["af", "am", "ar", "as", "az", "be", "bg", "bn", "bs", "ca", "cs", "cy", "da", "de", "dz", "el", "en", "eo", "es", "et", "eu", "fa", "fi", "fo", "fr", "ga", "gl", "gu", "he", "hi", "hr", "ht", "hu", "hy", "id", "is", "it", "ja", "jv", "ka", "kk", "km", "kn", "ko", "lo", "lt", "lv", "mk", "ml", "mr", "ms", "my", "nb", "ne", "nl", "nn", "pl", "ps", "pt", "qu", "ro", "ru", "rw", "se", "si", "sk", "sl", "sq", "sr", "su", "sv", "sw", "ta", "te", "th", "tl", "tr", "uk", "ur", "vi", "vo", "wa", "xh", "yi", "zh-CN", "zh-TW", "zu"], width=10)
    language_combo.set(language)
    language_combo.pack(side="left", padx=5)
    language_combo.bind("<<ComboboxSelected>>", update_language)

    # Create a Text widget for displaying the translated text
    text_widget = tk.Text(root, font=(font_family, font_size), wrap="word", bg="yellow", fg="black", undo=True, selectbackground="lightblue")
    text_widget.insert("1.0", translated_text)
    text_widget.config(state="normal")  # Make the text widget editable
    text_widget.pack(fill="both", expand=True, padx=10, pady=10)

    # Add a scrollbar to the Text widget
    scrollbar = tk.Scrollbar(root, command=text_widget.yview)
    text_widget.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    # Bind close events
    root.bind("<Escape>", close_popup)  # Close on Esc key
    root.bind("<FocusOut>", close_popup)   # Close on mouse leave

    root.mainloop()


# Listener for key combination
def on_activate():
    translate_and_show()

def main():
    # Register hotkey
    hotkey = keyboard.GlobalHotKeys({"<ctrl>+.": on_activate})

    # Run the hotkey listener
    hotkey.start()
    hotkey.join()

if __name__ == '__main__':
    main()
