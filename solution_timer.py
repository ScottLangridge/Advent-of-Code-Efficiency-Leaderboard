import os
import importlib.util
from time import time

from aoc_interface import AOCInterface
from players_interface import PlayersInterface
from consts import YEAR


# noinspection PyBroadException
class SolutionTimer:
    def __init__(self, players_interface):
        self.aoc_interface = AOCInterface()
        self.players_interface = players_interface
        self.solution_filenames = []

    def time_solutions(self, pid):
        # Build map of solution filenames to paths of players corresponding solutions
        player = self.players_interface[pid]
        player_solution_files = self.list_files(player)

        # Time each file
        for day in range(1, 26):
            for level in [1, 2]:
                try:
                    # Run solution
                    path = player_solution_files[self.gen_filename(day, level)]
                    result, run_time = self.time_main(path)

                    # If solution is correct, record it
                    if self.aoc_interface.verify_solution(str(YEAR), str(day), level, result):
                        player.set_time(run_time, str(day), str(level))
                        self.players_interface.save_players()
                except:
                    pass

    @staticmethod
    def gen_filename(day, level):
        base_filename = 'day%s-%s.py'
        return base_filename % (day, level)

    @staticmethod
    def list_files(player):
        files = {}
        for r, d, f in os.walk(player.local):
            for file in f:
                if '.py' in file:
                    files[file] = os.path.join(r, file)
        return files

    @staticmethod
    def time_main(filepath):
        spec = importlib.util.spec_from_file_location("module.name", filepath)
        imported_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(imported_module)

        start_time = time()
        result = imported_module.main()
        end_time = time()

        return result, end_time - start_time
