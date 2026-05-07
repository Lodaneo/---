# collection.py
import sys
import os

# Ajuste de caminho para encontrar o lab03
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class PlayerCollection:
    def __init__(self, name="Squad", items=None):
        self.name = name
        self._items = items if items is not None else []

    def add(self, item):
        self._items.append(item)
        return self

    # --- Nota 5: Цепочка операций (Method Chaining) ---

    def filter_by(self, predicate):
        """Фильтрация: возвращает НОВУЮ коллекцию для цепочки"""
        filtered_items = list(filter(predicate, self._items))
        return PlayerCollection(f"Filtered {self.name}", filtered_items)

    def sort_by(self, key_func, reverse=True):
        """Сортировка: меняет порядок и возвращает self"""
        self._items.sort(key=key_func, reverse=reverse)
        return self

    def apply(self, func):
        """Применяет функцию ко всем элементам (Nota 5)"""
        # func pode ser uma função normal, lambda ou callable object
        self._items = [func(item) for item in self._items]
        return self

    def __iter__(self):
        return iter(self._items)

    def __str__(self):
        return f"--- {self.name} ({len(self._items)} чел.) ---"
