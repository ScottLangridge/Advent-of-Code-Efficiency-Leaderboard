from html_generator import HTMLGenerator
from players_interface import PlayersInterface
from solution_timer import SolutionTimer


def main():
    print('getting players')
    players_interface = PlayersInterface()
    print('setting up timer')
    timer = SolutionTimer(players_interface)
    print('setting up htmlgen')
    html_gen = HTMLGenerator(players_interface)

    #while True:
    for player in players_interface.players.values():
        print('Timing Player:', player.name)
        timer.time_solutions(player.pid)
        print('Generating Html')
        html_gen.update_leaderboard()


if __name__ == '__main__':
    main()
