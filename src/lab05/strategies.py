# strategies.py

class ExperienceBuff:
    """Callable-объект для начисления опыта."""
    def __init__(self, bonus_xp: int):
        self.bonus_xp = bonus_xp

    def __call__(self, player):
        # Usamos hasattr para evitar erros se o atributo variar
        if hasattr(player, 'experience'):
            player.experience += self.bonus_xp
        elif hasattr(player, '_experience'):
            player._experience += self.bonus_xp
        return player

class HealthRestore:
    """Callable-объект для восстановления здоровья."""
    def __init__(self, amount: int):
        self.amount = amount

    def __call__(self, player):
        # Garantimos que acessamos a propriedade correta
        current_health = getattr(player, 'health', 0)
        player.health = min(100, current_health + self.amount)
        return player

# --- Mantemos as outras funções como estavam ---

def is_warrior(player) -> bool:
    from models import Warrior
    return isinstance(player, Warrior)

def is_alive(player) -> bool:
    # Tenta chamar o método is_alive() ou checar o atributo health
    if hasattr(player, 'is_alive'):
        return player.is_alive()
    return getattr(player, 'health', 0) > 0

def by_level(player):
    return getattr(player, 'level', 0)
