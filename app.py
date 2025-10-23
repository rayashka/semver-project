# app.py - Главное приложение
from utils import get_greeting, get_version, greet_multiple

def main():
    print(get_greeting())
    print(f"Version: {get_version()}")
    
    # Демонстрация новой функциональности
    names = ["Alice", "Bob", "Charlie"]
    greetings = greet_multiple(names)
    for greeting in greetings:
        print(greeting)
    
if __name__ == "__main__":
    main()