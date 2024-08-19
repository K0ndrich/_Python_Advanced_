# Орел и Решка
# Реализация стратегии Мортенгейла для вииграша в игру Орел и Решка


import random

# орел
HEADS = "heads"
# решка
TAILS = "tails"
# набор значений
COIN_VALUES = [HEADS, TAILS]


# функция определяет бросок монетки
def flip_coin():
    # возвращает рандомный елемент указаного списка
    random.choice(COIN_VALUES)


# сама стратегия Мартингейла
def play_martingale(*, starting_funds: int, min_bet: int, max_bet: int):

    # количество шагов до поражения игрока
    steps_to_loose = 0
    # текущие деньги игрока
    current_funds = starting_funds
    # текущая ставка игрока
    current_bet = min_bet

    while current_funds > 0:

        steps_to_loose += 1
        current_funds -= current_bet

        flipped_coin_value = flip_coin()

        # тут игрок выигрывает
        if flipped_coin_value == HEADS:

            win = current_bet * 2

            # отдаем пользователю выигрыш
            current_funds += win
            # текущая ставка становить минимальной
            current_bet = min_bet

        # тут игрок проигрывает
        else:
            # текущая ставка увеличиваеться в два раза
            current_bet *= 2

            # если текущая ставка больше максимальной, тогда текущая ставка становиться минимальной
            if current_bet > max_bet:
                current_bet = min_bet
            # если текущая ставка больше текущий средств пользователя, тогда текущая ставка становиться остатком средств пользователя
            if current_bet > current_funds:
                current_bet = current_funds

    # возвращаем количество шагом пользователя до поражения
    return steps_to_loose


# играем одним игроком
play_martingale(starting_funds=100, min_bet=2, max_bet=4)


# играет указанное количество игроков
def simulate_martingale_for_n_player(
    *, starting_funds: int, min_bet: int, max_bet: int, n_games: int
):
    # количество все шагов всех игроков до проигрыша
    total_steps_to_loose = 0

    for i in range(n_games):
        # количество шагов одного игрока до проигрыша
        step_to_loose = play_martingale(
            starting_funds=starting_funds, min_bet=min_bet, max_bet=max_bet
        )
        total_steps_to_loose += step_to_loose

    return total_steps_to_loose / n_games


# играем несолькими игроками
simulate_martingale_for_n_player(
    n_games=10, starting_funds=1000, min_bet=1, max_bet=100
)
