from entity import Entity
from ai import AI

player = Entity('Игрок', damage=25)
ai = AI('ИИ')

games_count = 100

for _ in range(games_count):
    while player.health > 0 and ai.health > 0:
        player.turn(ai)
        ai.turn(player)

    if player.health > 0:
        ai.update_stats(is_winner=False)
    elif player.health <= 0:
        ai.update_stats(is_winner=True)
    else:
        print('Ничья')

    player.reset()
    ai.reset()
