import datetime
import os
import importlib.util
from time import time

from aoc_interface import AOCInterface
from consts import YEAR


# noinspection PyBroadException
class SolutionTimer:
    def __init__(self, players_interface):
        self.aoc_interface = AOCInterface()
        self.players_interface = players_interface
        self.solution_filenames = []
        td = datetime.timedelta(hours=-5, minutes=-5)
        self.tz = datetime.timezone(td)

    def time_solutions(self, pid):
        # Build map of solution filenames to paths of players corresponding solutions
        player = self.players_interface.players[pid]
        player_solution_files = self.list_files(player)

        if pid != 'LangridgeS':
            return

        # Time each file
        day_of_month = datetime.datetime.now(self.tz).day
        for day in range(1, day_of_month + 1):
            for level in [1, 2]:
                try:
                    # Run solution
                    file_key = self.gen_filename(day, level)
                    path = player_solution_files[file_key]
                    puzzle_input = self.aoc_interface.get_input(YEAR, day)
                    result, run_time = self.time_main(path, puzzle_input)

                    # If solution is correct, record it
                    if self.aoc_interface.verify_solution(str(YEAR), str(day), level, result):
                        player.set_time(run_time, str(day), str(level))
                        self.players_interface.save_players()
                except Exception as e:
                    pass

    @staticmethod
    def gen_filename(day, level):
        base_filename = 'day%s-%s.py'
        return base_filename % (f'{day:02}', level)

    @staticmethod
    def list_files(player):
        files = {}
        for r, d, f in os.walk(player.local):
            for file in f:
                if '.py' in file:
                    files[file] = os.path.join(r, file)
        return files

    @staticmethod
    def time_main(filepath, puzzle_input):
        spec = importlib.util.spec_from_file_location("module.name", filepath)
        imported_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(imported_module)

        start_time = time()
        result = str(imported_module.main(puzzle_input))
        end_time = time()

        return result, end_time - start_time
