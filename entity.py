class Entity:

    def __init__(self, name, armor=1, health=100, damage=10):
        self.name = name
        self._armor = armor
        self.health = health
        self.damage = damage
        self._armor_increase = 1
        self.was_attack = False

    def _calculate_damage(self, enemy_armor):
        return self.damage / enemy_armor

    def _attack(self, enemy):
        enemy.health -= self._calculate_damage(enemy.get_armor())

    def _defend(self):
        self._armor += self._armor_increase

    def get_armor(self):
        return self._armor

    def turn(self, enemy):
        if self.was_attack:
            self._defend()
            self.was_attack = False
        else:
            self._attack(enemy)

    def reset(self):
        self.health = 100
        self._armor = 1