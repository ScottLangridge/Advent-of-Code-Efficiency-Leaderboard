import json

import requests

from consts import PUZZLES_JSON, ANSWER_PAGE_URL, INPUT_PAGE_URL, SESSION_COOKIE, SUCCESS_MSG, FAIL_MSG


class AOCInterface:
    def __init__(self):
        self.puzzles = {}
        self.load_json()

    def load_json(self, filepath=PUZZLES_JSON):
        with open(filepath, 'r') as f:
            raw_json = f.read()
        self.puzzles = json.loads(raw_json)

    def save_json(self, filepath=PUZZLES_JSON):
        raw_json = json.dumps(self.puzzles, sort_keys=True, indent=2)
        with open(filepath, 'w') as f:
            f.write(raw_json)

    def get_input(self, year, day):
        if self.puzzles[str(day)]['input'] is None:
            url = INPUT_PAGE_URL % (str(year), str(day))
            headers = {'cookie': 'session=%s' % SESSION_COOKIE}
            print('MAKING REQUEST TO AOC')
            response = requests.post(url, headers=headers).text
            response = response.strip('\n')
            self.puzzles[str(day)]['input'] = response
            self.save_json()
        return self.puzzles[str(day)]['input']

    def verify_solution(self, year, day, level, answer):
        if self.puzzles[str(day)]['answer'][str(level)] is not None:
            # If there is already an answer in memory use that one
            if self.puzzles[str(day)]['answer'][str(level)] == answer:
                return True
            else:
                return False
        else:
            # Get response from AOC
            url = ANSWER_PAGE_URL % (str(year), str(day))
            form_data = {"level": level, "answer": answer}
            headers = {'cookie': 'session=%s' % SESSION_COOKIE}
            print('MAKING REQUEST TO AOC')
            response = requests.post(url, form_data, headers=headers).text

            # Determine whether or not answer is correct
            if response.find(SUCCESS_MSG) != -1:
                self.puzzles[str(day)]['answer'][str(level)] = answer
                self.save_json()
                return True
            elif response.find(FAIL_MSG):
                return False
            else:
                raise Exception("Verification of solution failed; Neither success msg nor fail msg were returned.")
