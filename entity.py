class Entity:

    def __init__(self, name, health=100, damage=10):
        self.name = name
        self.health = health
        self.damage = damage
        self._body_parts = ('head', 'body', 'left_hand', 'right_hand', 'left_foot', 'right_foot')
        self.defend_part = ''
        self.attack_part = ''

    def defend(self, part):
        self.defend_part = part

    def attack(self, enemy, part):
        self.attack_part = part
        if enemy.defend_part == self.attack_part:
            return 'Blocked!'
        enemy.health -= self.damage
        return f'{enemy.name} has {enemy.health}hp!' \
               f'{self.name} has {self.health}hp!'

    def _get_body_parts_for_render(self):
        result = ''
        for index, part in enumerate(self._body_parts, start=1):
            result += f'{index}. {part}\n'
        return result

    def _get_part_by_number(self, number):
        try:
            return self._body_parts[number-1]
        except IndexError:
            return False

    def turn(self, enemy):
        while True:
            print('Which part you want to defend?')
            print(self._get_body_parts_for_render())
            choice = int(input('Your choice as number: '))
            part = self._get_part_by_number(choice)
            if not part:
                print('Incorrect choice!\nTry again!')
                continue
            self.defend(part)
            print('Which part you want to attack?')
            print(self._get_body_parts_for_render())
            choice = int(input('Your choice as number: '))
            part = self._get_part_by_number(choice)
            if not part:
                print('Incorrect choice!\nTry again!')
                continue
            print(self.attack(enemy, part))
            break


    def reset(self):
        self.health = 100
        self._armor = 1