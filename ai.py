import random
from entity import Entity


class AI(Entity):

    def __init__(self, name):
        super().__init__(name)
        self._stats_file_name = 'ai.stats'
        self._wins = 0
        self._loses = 0
        self._attack_parts = {
            'attack-head': 1.0,
            'attack-body': 1.0,
            'attack-left_hand': 1.0,
            'attack-right_hand': 1.0,
            'attack-left_foot': 1.0,
            'attack-right_foot': 1.0,
        }

        self._defend_parts = {
            'defend-head': 1.0,
            'defend-body': 1.0,
            'defend-left_hand': 1.0,
            'defend-right_hand': 1.0,
            'defend-left_foot': 1.0,
            'defend-right_foot': 1.0,
        }
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
                elif status in self._attack_parts.keys():
                    self._attack_parts[status] = float(value)
                elif status in self._defend_parts.keys():
                    self._defend_parts[status] = float(value)

    def _write_stats(self):
        with open('ai.stats', 'w') as f:
            data = f'wins {self._wins}\n' \
                   f'loses {self._loses}\n'
            for key, value in self._attack_parts.items():
                data += f'{key} {value}\n'
            for key, value in self._defend_parts.items():
                data += f'{key} {value}\n'
            f.write(data)

    def update_stats(self, enemy):
        part = enemy.attack_part
        key = f'defend-{part}'
        print(key)
        self._defend_parts[key] += 0.1

        if self.attack_part != enemy.defend_part:
            key = f'attack-{self.attack_part}'
            self._attack_parts[key] += 0.1

    def turn(self, enemy):
        attack_part = random.choices(self._body_parts, tuple(self._attack_parts.values()))
        block_part = random.choices(self._body_parts, tuple(self._defend_parts.values()))
        attack_part_choice = attack_part[0]
        block_part_choice = block_part[0]

        self.defend(block_part_choice)
        self.attack(enemy, attack_part_choice)
