class Player:
    def __init__(self, pid, player_def):
        self.pid = pid
        self.name = player_def['name']
        self.remote = player_def['remoteRepo']
        self.local = player_def['localRepo']
