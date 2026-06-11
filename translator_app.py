import os
import sys
from deep_translator import GoogleTranslator
import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Словарь поддерживаемых языков (на русском для UI : код для API)
LANG_RU_NAMES = {
    'Автоопределение': 'auto',
    'Английский': 'en',
    'Русский': 'ru',
    'Украинский': 'uk',
    'Немецкий': 'de',
    'Французский': 'fr',
    'Испанский': 'es',
    'Итальянский': 'it',
    'Китайский': 'zh-CN',
    'Японский': 'ja',
    'Корейский': 'ko',
    'Арабский': 'ar',
    'Турецкий': 'tr'
}

lang_ru_names = sorted([name for name in LANG_RU_NAMES if name != 'Автоопределение'])
lang_ru_names.insert(0, 'Автоопределение')
lang_name_to_code = {name: code for name, code in LANG_RU_NAMES.items()}
code_to_lang_name = {code: name for name, code in LANG_RU_NAMES.items()}

def translate_text():
    text_to_translate = input_text.get("1.0", "end-1c").strip()
    src_lang_name = src_lang_var.get()
    dest_lang_name = dest_lang_var.get()
    
    src_lang_code = lang_name_to_code.get(src_lang_name, 'auto')
    dest_lang_code = lang_name_to_code.get(dest_lang_name, 'ru')
    
    detected_lang_label.configure(text="Исходный текст:")

    if not text_to_translate:
        display_result("Пожалуйста, введите текст для перевода.")
        return

    try:
        # deep-translator автоматически обрабатывает 'auto'
        translator = GoogleTranslator(source=src_lang_code, target=dest_lang_code)
        translated_str = translator.translate(text_to_translate)
        
        if src_lang_code == 'auto':
            # Дополнительный быстрый запрос для детекции, если нужно вывести имя языка в UI
            try:
                from deep_translator import single_detection
                # Заглушка, чтобы не спамить сеть, если библиотека не импортировалась
                detected_code = GoogleTranslator().single_detection(text_to_translate, api_key='not_used')
                detected_name = code_to_lang_name.get(detected_code, detected_code.upper())
                detected_lang_label.configure(text=f"Исходный текст: (Определено: {detected_name})")
            except Exception:
                detected_lang_label.configure(text="Исходный текст: (Язык определен)")
        
        display_result(translated_str)
        
    except Exception as e:
        print(f"Ошибка перевода: {e}")
        display_result("Ошибка перевода. Проверьте интернет-соединение или попробуйте позже.")

def display_result(text):
    translated_text.configure(state=ctk.NORMAL)
    translated_text.delete("1.0", ctk.END)
    translated_text.insert("1.0", text)
    translated_text.configure(state=ctk.DISABLED)

def swap_languages():
    src = src_lang_var.get()
    dest = dest_lang_var.get()
    
    if dest == 'Автоопределение':
        display_result("Нельзя установить 'Автоопределение' в качестве целевого языка.")
        return
        
    src_lang_var.set(dest)
    dest_lang_var.set(src)
    detected_lang_label.configure(text="Исходный текст:")
    
    if input_text.get("1.0", "end-1c").strip():
        translate_text()

# Создание GUI
root = ctk.CTk()
root.title("Modern Translator")
root.geometry("700x480")
root.minsize(600, 400)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(3, weight=1)

header = ctk.CTkLabel(root, text="Переводчик текста", font=ctk.CTkFont(family="Arial", size=22, weight="bold"))
header.grid(row=0, column=0, columnspan=2, pady=(15, 10))

lang_frame = ctk.CTkFrame(root)
lang_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky="ew")
lang_frame.grid_columnconfigure(0, weight=1) 
lang_frame.grid_columnconfigure(1, weight=0) 
lang_frame.grid_columnconfigure(2, weight=1) 

src_lang_var = ctk.StringVar(lang_frame, value="Автоопределение")
src_lang_menu = ctk.CTkComboBox(lang_frame, values=lang_ru_names, variable=src_lang_var, width=180)
src_lang_menu.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

swap_button = ctk.CTkButton(lang_frame, text="⇄", command=swap_languages, width=40, height=30, font=ctk.CTkFont(size=16, weight="bold"))
swap_button.grid(row=0, column=1, padx=5, pady=10)

dest_lang_var = ctk.StringVar(lang_frame, value="Русский")
dest_lang_menu = ctk.CTkComboBox(lang_frame, values=[name for name in lang_ru_names if name != 'Автоопределение'], variable=dest_lang_var, width=180)
dest_lang_menu.grid(row=0, column=2, padx=10, pady=10, sticky="ew")

detected_lang_label = ctk.CTkLabel(root, text="Исходный текст:", font=ctk.CTkFont(size=13, weight="bold"))
detected_lang_label.grid(row=2, column=0, padx=20, pady=(10, 0), sticky="w")
input_text = ctk.CTkTextbox(root, height=150, wrap="word", font=ctk.CTkFont(size=14))
input_text.grid(row=3, column=0, padx=20, pady=(5, 10), sticky="nsew")

translated_label = ctk.CTkLabel(root, text="Переведенный текст:", font=ctk.CTkFont(size=13, weight="bold"))
translated_label.grid(row=2, column=1, padx=20, pady=(10, 0), sticky="w")
translated_text = ctk.CTkTextbox(root, height=150, wrap="word", state=ctk.DISABLED, font=ctk.CTkFont(size=14)) 
translated_text.grid(row=3, column=1, padx=20, pady=(5, 10), sticky="nsew")

translate_button = ctk.CTkButton(root, text="Перевести", command=translate_text, font=ctk.CTkFont(size=15, weight="bold"), height=42)
translate_button.grid(row=4, column=0, columnspan=2, padx=20, pady=(10, 20), sticky="ew")

if __name__ == "__main__":
    root.mainloop()