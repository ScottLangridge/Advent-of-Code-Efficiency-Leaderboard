import os
import importlib.util
from time import time

from aoc_interface import AOCInterface
from consts import YEAR


# noinspection PyBroadException
class SolutionTimer:
    def __init__(self):
        self.aoc_interface = AOCInterface()

    def time_solutions(self, player):
        # Build list of locations
        files = {}
        for r, d, f in os.walk(player.local):
            for file in f:
                if '.py' in file:
                    files[file] = os.path.join(r, file)

        # Time each file
        base_filename = 'day%s-%s.py'
        for day in range(1, 26):
            for level in [1, 2]:
                try:
                    # Run solution
                    path = files[base_filename % (f'{day:02}', level)]
                    result, run_time = self.time_main(path)

                    # If solution is correct, record it
                    if self.aoc_interface.verify_solution(str(YEAR), str(day), level, result):
                        player.set_time(run_time, str(day), str(level))
                except:
                    pass

    @staticmethod
    def time_main(filepath):
        spec = importlib.util.spec_from_file_location("module.name", filepath)
        imported_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(imported_module)

        start_time = time()
        result = imported_module.main()
        end_time = time()

        return result, end_time - start_time
