# utils.py - Вспомогательные функции

def get_greeting():
    return "Hello World!"

def get_version():
    return "1.1.1"

def greet_user(name):
    """Приветствие по имени"""
    if not name or name.strip() == "":
        name = "Guest"  # ИСПРАВЛЕНИЕ: обработка пустого имени
    return f"Hello, {name}!"