from aoc_interface import AOCInterface
from players_interface import PlayersInterface
from solution_timer import SolutionTimer


def main():
    timer = SolutionTimer()
    players = PlayersInterface().players
    puzzles = AOCInterface().puzzles

    for player in players.values():
        timer.time_solutions(player)


if __name__ == '__main__':
    main()
