# advanced.py - Расширенные функции
from utils import greet_user

def formal_greeting(name):
    """Формальное приветствие"""
    return f"Good day, {name}. It is a pleasure to meet you."

def casual_greeting(name):
    """Неформальное приветствие"""
    return f"Hey {name}! What's up?"

def get_all_greetings(name):
    """Все типы приветствий"""
    return {
        "standard": greet_user(name),
        "formal": formal_greeting(name),
        "casual": casual_greeting(name)
    }