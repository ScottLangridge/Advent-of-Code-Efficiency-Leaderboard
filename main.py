from players_interface import PlayersInterface
from solution_timer import SolutionTimer


def main():
    timer = SolutionTimer()
    players = PlayersInterface().players

    while True:
        for player in players.values():
            timer.time_solutions(player)


if __name__ == '__main__':
    main()
