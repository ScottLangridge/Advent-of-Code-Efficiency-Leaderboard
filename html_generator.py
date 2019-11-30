from consts import LEADERBOARD_TEMPLATE, INDEX_PATH
from players_interface import PlayersInterface


class HTMLGenerator:
    def __init__(self, players_interface):
        self.players = players_interface

        with open(LEADERBOARD_TEMPLATE, 'r') as f:
            self.leaderboard_template = f.read()

    def update_leaderboard(self):
        lines = []
        for day in range(1, 26):
            for level in [1, 2]:
                lines.append('<h2>Day %s - Part %s</h2>' % (day, level))
                lines.extend(self.gen_rankings(day, level))
                lines.append('')

        positions_string = '\n'.join(lines)
        leaderboard_html = self.leaderboard_template % positions_string

        with open(INDEX_PATH, 'w') as f:
            f.write(leaderboard_html)

    def gen_rankings(self, day, level):
        # Collect and sort times
        raw_times = []
        for player in self.players.values():
            player_name = player.name
            solve_time = player.get_time(str(day), str(level))
            if solve_time is not None:
                raw_times.append((solve_time, player_name))
        raw_times.sort()

        # Collate into printable lines rankings
        lines = []
        count = 0
        for i in raw_times:
            count += 1
            lines.append('<p>  ' + str(count) + '. ' + i[1] + ' - ' + str(i[0]) + '</p>')

        return lines
