from html_generator import HTMLGenerator
from players_interface import PlayersInterface
from solution_timer import SolutionTimer


def main():
    players = PlayersInterface().players
    timer = SolutionTimer(players)
    html_gen = HTMLGenerator(players)

    while True:
        for player in players.values():
            timer.time_solutions(player.pid)
            html_gen.update_leaderboard()


if __name__ == '__main__':
    main()
