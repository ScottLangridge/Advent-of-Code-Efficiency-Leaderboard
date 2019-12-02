import datetime
from html_generator import HTMLGenerator
from players_interface import PlayersInterface
from solution_timer import SolutionTimer


def main():
    players_interface = PlayersInterface()
    timer = SolutionTimer(players_interface)
    html_gen = HTMLGenerator(players_interface)

    while True:
        print(datetime.now())

        # Pull Repos
        print('  Pulling Repos')
        players_interface.pull_all_repos()

        # Time All Players
        print('  Timing Players')
        for player in players_interface.players.values():
            timer.time_solutions(player.pid)

        # Record Times
        print('  Updating Leaderboard\n')
        html_gen.update_leaderboard()


if __name__ == '__main__':
    main()
