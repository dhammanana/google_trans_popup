# Google Translate Popup

Google Translate Popup is a Python-based tool that allows you to quickly translate selected text using the Google Translate API. The translation is displayed in a pop-up window with customizable settings such as font size, font family, and target language.

## Features

- Translate selected text with a hotkey (`Ctrl + .`).
- Automatically detects the selected text and translates it.
- Supports customization of font size, font family, and target language.
- Configurable to remember user preferences (saved in `config.txt`).
- Works on Linux, macOS, and Windows.

---

## Installation

To install the package, you can use `pip` to install it directly from the GitHub repository:

bash

CopyEdit

`pip install git+https://github.com/dhammanana/google_trans_popup.git`

---

## Usage

After installation, you can run the tool by using the following command:

bash

CopyEdit

`googletrans`

### Steps:

1. Select some text in any application.
2. Press `Ctrl + .` to trigger the translation popup.
3. A popup will appear showing the translation of the selected text.

---

#### 1. Install `PyInstaller`

First, ensure you have `PyInstaller` installed. You can install it with:

bash

CopyEdit

`pip install pyinstaller`

---

#### 2. Build the Executable

Navigate to the root directory of your project (where `google_trans.py` is located). Run the following command:

bash

CopyEdit

`pyinstaller --onefile --name googletrans google_trans_popup/google_trans.py`

- `--onefile`: Packages everything into a single executable.
- `--name googletrans`: Sets the name of the output executable as `googletrans`.
- `google_trans_popup/google_trans.py`: The path to your main Python script.

---

#### 3. Locate the Executable

Once the build process is complete, the executable will be located in the `dist/` directory of your project. For example:

CopyEdit

`dist/ └── googletrans.exe`

---

#### 4. Run the Executable

You can now run the executable directly in the Windows command prompt or by double-clicking it:

bash

CopyEdit

`googletrans.exe`

---

### Notes for Windows Users

1. **Hotkey Compatibility**: Ensure your system supports global hotkeys (used by the script for `Ctrl + .`).
2. **Include Required Files**: If your script depends on additional files (e.g., `config.txt`), you may need to package them with the executable. You can include them by using the `--add-data` option with `pyinstaller`.

Example:

bash

CopyEdit

`pyinstaller --onefile --name googletrans --add-data "google_trans_popup/config.txt;google_trans_popup" google_trans_popup/google_trans.py`

3. **Test the Executable**: Run the `.exe` file on a clean system (or virtual machine) to ensure all dependencies are bundled correctly.


---

## Requirements

The package automatically installs the required dependencies. However, here’s a list of the primary libraries used:

- `pynput`
- `pyperclip`
- `requests`
- `tkinter` (comes pre-installed with Python)

### Additional Notes:

- On **Linux**, you may need to install `xclip` if it’s not already installed:
    
    bash
    
    CopyEdit
    
    `sudo apt install xclip`
    

---

## Contributing

If you'd like to contribute to the project:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
