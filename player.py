class Player:
    def __init__(self, pid, player_def):
        self.pid = pid
        self.name = player_def['name']
        self.remote = player_def['remoteRepo']
        self.local = player_def['localRepo']
        self.times = player_def['times']

    def get_time(self, day, level):
        return self.times[str(day)][str(level)]

    def set_time(self, val, day, level):
        self.times[str(day)][str(level)] = val
