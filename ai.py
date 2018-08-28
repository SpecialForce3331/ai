import random
from entity import Entity


class AI(Entity):

    def __init__(self, name):
        super().__init__(name)
        self._stats_file_name = 'ai.stats'
        self._wins = 0
        self._loses = 0
        self._attack_rate = 1.0
        self._defend_rate = 1.0
        self._read_stats()

    def __del__(self):
        self._write_stats()

    def _read_stats(self):
        with open(self._stats_file_name) as f:
            for line in f:
                status, value = line.split()
                if status == 'wins':
                    self._wins = int(value)
                elif status == 'loses':
                    self._loses = int(value)
                elif status == 'attack_rate':
                    self._attack_rate = float(value)
                elif status == 'defend_rate':
                    self._defend_rate = float(value)

    def _write_stats(self):
        with open('ai.stats', 'w') as f:
            f.write(f'wins {self._wins}\n'
                    f'loses {self._loses}\n'
                    f'attack_rate {self._attack_rate}\n'
                    f'defend_rate {self._defend_rate}')

    # Собственно псевдо разум нашего псевдо ИИ.
    def update_stats(self, is_winner):
        if is_winner:
            self._wins += 1
            if (self._wins - self._loses) < 5:  # Если мы выиграли 5 раз подряд, то ничего не делаем
                if self._attack_rate < self._defend_rate:  # Если наши победы благодаря тому, что у нас высокий критерий защиты, то давайте его увеличим
                    self._defend_rate += 0.1
                else:  # Если же все это благодаря атаке, то нарастим ее.
                    self._attack_rate += 0.1
        else:
            self._loses += 1
            if (self._wins - self._loses) < 5:
                if self._defend_rate < self._attack_rate:
                    self._defend_rate += 0.1
                else:
                    self._attack_rate += 0.1

    def turn(self, enemy):
        result = random.choices(['attack', 'defend'], [self._attack_rate, self._defend_rate])
        result = result[0]
        if result == 'attack':
            self._attack(enemy)
        else:
            self._defend()


# ДЗ
# str rjust, ljust