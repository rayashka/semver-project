# utils.py - Вспомогательные функции
import json

def load_config():
    """Загружает конфигурацию из файла"""
    try:
        with open('config.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"default_name": "World", "language": "en"}

def get_greeting():
    config = load_config()
    return f"Hello {config.get('default_name', 'World')}!"

def get_version():
    return "1.2.0"

def greet_user(name):
    """Приветствие по имени"""
    if not name or name.strip() == "":
        config = load_config()
        name = config.get("default_name", "Guest")
    return f"Hello, {name}!"

def greet_multiple(names):
    """Новая функция - приветствие нескольких людей"""
    if not names:
        return greet_user(None)
    return [greet_user(name) for name in names]