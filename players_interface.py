import json
from git import Repo

from consts import PLAYERS_JSON, REPO_FOLDER
from player import Player


class PlayersInterface:
    def __init__(self):
        self.players = {}
        self.load_players()
        self.pull_all_repos()

    # Generates self.players from the json file
    def load_players(self):
        with open(PLAYERS_JSON, 'r') as f:
            raw_json = f.read()
        players_info_dict = json.loads(raw_json)

        for pid in players_info_dict.keys():
            self.players[pid] = Player(pid, players_info_dict[pid])

    # Saves self.players to the json file
    def save_players(self):
        player_dict = {}
        for i in self.players.values():
            player_dict[i.pid] = {'name': i.name, 'remoteRepo': i.remote, 'localRepo': i.local, 'times': i.times}

        raw_json = json.dumps(player_dict, sort_keys=True, indent=2)
        with open(PLAYERS_JSON, 'w') as f:
            f.write(raw_json)

    # Pulls/Clones the repos of all of the players
    def pull_all_repos(self):
        for pid in self.players:
            self.pull_player_repo(pid)

    # Pulls/Clones the repo of a given player
    def pull_player_repo(self, pid):
        player = self.players[pid]
        local_repo_path = REPO_FOLDER + '/' + pid

        if player.local is None:
            player.repo = Repo.clone_from(player.remote, local_repo_path)
            player.local = local_repo_path
            self.save_players()
        else:
            player.repo = Repo(local_repo_path)
            player.repo.remote('origin').pull()
