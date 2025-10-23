# app.py - Главное приложение
from utils import get_greeting, get_version, greet_multiple
from advanced import get_all_greetings

def main():
    print(get_greeting())
    print(f"Version: {get_version()}")
    
    # Демонстрация новой функциональности
    names = ["Alice", "Bob", "Charlie"]
    greetings = greet_multiple(names)
    for greeting in greetings:
        print(greeting)
    
    # Показываем все типы приветствий
    print("\nAll greeting types for Alice:")
    all_greetings = get_all_greetings("Alice")
    for style, greeting in all_greetings.items():
        print(f"{style}: {greeting}")
    
if __name__ == "__main__":
    main()