import sys
import os

# Ajuste de caminho para encontrar o lab03
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lab03.models import Warrior, Mage
from collection import PlayerCollection
import strategies as st

def main():
    # Создание коллекции
    squad = PlayerCollection("Alpha Team")
    squad.add(Warrior("Conan", level=10, health=50))
    squad.add(Mage("Gandalf", level=20, health=30))
    squad.add(Warrior("Aragorn", level=15, health=40))
    squad.add(Mage("Jaina", level=18, health=10))
    squad.add(Warrior("Gimli", level=8, health=90))

    print("="*50)
    print(" ЛАБОРАТОРНАЯ РАБОТА №5 — ДЕМОНСТРАЦИЯ ")
    print("="*50)

    # СЦЕНАРИЙ 1: Полная цепочка
    print("\n=== СЦЕНАРИЙ 1: Цепочка операций (Method Chaining) ===")
    (squad
        .filter_by(st.is_alive)
        .sort_by(st.by_level)
        .apply(lambda p: print(f"  Обработка: {p.nickname} (Ур. {p.level})")))

    # СЦЕНАРИЙ 2: Заменяемость стратегий
    print("\n=== СЦЕНАРИЙ 2: Заменяемость стратегий ===")
    buff_strategy = st.ExperienceBuff(500)
    heal_strategy = st.HealthRestore(25)
    
    print("1. Применяем Buff опыта (+500 XP):")
    squad.apply(buff_strategy)
    for p in squad: 
        xp = getattr(p, 'experience', getattr(p, '_experience', 0))
        print(f"  {p.nickname} | XP: {xp}")
    
    print("\n2. Применяем Восстановление здоровья (+25 HP):")
    squad.apply(heal_strategy)
    for p in squad: 
        hp = getattr(p, 'health', 0)
        print(f"  {p.nickname} | HP: {hp}")

    # СЦЕНАРИЙ 3: Сложный фильтр через Lambda
    print("\n=== СЦЕНАРИЙ 3: Сложный фильтр через Lambda ===")
    elite_warriors = squad.filter_by(lambda p: st.is_warrior(p) and getattr(p, 'health', 0) > 50)
    
    count = 0
    for p in elite_warriors:
        print(f"  [ELITE] {p.nickname} (HP: {getattr(p, 'health', 0)})")
        count += 1
    print(f"\nНайдено элитных воинов: {count}")

    print("\n" + "="*50)
    print(" ТЕСТИРОВАНИЕ ЗАВЕРШЕНО УСПЕШНО ")
    print("="*50)

# ESTA LINHA É O QUE FAZ O PROGRAMA RODAR!
if __name__ == "__main__":
    main()
