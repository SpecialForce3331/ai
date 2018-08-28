from entity import Entity
from ai import AI

player = Entity('Игрок', damage=10)
ai = AI('ИИ')

games_count = 1

for _ in range(games_count):
    while player.health > 0 and ai.health > 0:
        player.turn(ai)
        ai.turn(player)
        ai.update_stats(player)

    if player.health > 0:
        print('Победа за игроком')
    elif player.health <= 0:
        print('Победа за ИИ')
    else:
        print('Ничья')

    player.reset()
    ai.reset()
