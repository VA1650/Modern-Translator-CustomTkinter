# 🌍 Modern-Translator-CustomTkinter

A lightweight desktop translator with automatic language detection. The UI is built using `customtkinter`, providing a modern look and native support for system themes. Translation logic is powered by the stable `deep-translator` engine (Google Translate API).

## ✨ Key Features

* Asynchronous Auto-Detection: Automatically detects the source language and notifies the user via the UI.
* Language Swap: Quick swap functionality (⇄) for source and target languages with validation logic (prevents setting "Auto-detect" as the target language).
* Modern UX: Dynamic state management for text containers (disabled/normal) to prevent accidental result modification.
* Fluid Layout: Uses the `Grid` geometry manager to ensure interface elements scale proportionally with the main window size.

## ⚙️ Requirements & Installation

### 1. Clone the repository
bash
git clone https://github.com/your-username/Modern-Translator-CustomTkinter.git
cd Modern-Translator-CustomTkinter

### 2. Install dependencies
bash
pip install customtkinter deep-translator

### 3. Launch the application
bash
python main.py

## 🛠 Tech Stack

* GUI: `customtkinter` (modern wrapper for classic tkinter with hardware-accelerated frame rendering).
* Engine: `deep-translator` (GoogleTranslator module) — chosen as a reliable successor to legacy libraries like `googletrans`.
