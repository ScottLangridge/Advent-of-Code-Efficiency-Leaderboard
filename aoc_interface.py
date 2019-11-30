import json

import requests

from consts import PUZZLES_JSON, ANSWER_PAGE_URL, SESSION_COOKIE, SUCCESS_MSG, FAIL_MSG


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

    def verify_solution(self, year, day, level, answer):
        if self.puzzles[str(day)]['answer'] is None:
            url = ANSWER_PAGE_URL % (str(year), str(day))
            form_data = {"level": level, "answer": answer}
            headers = {'cookie': 'session=%s' % SESSION_COOKIE}

            response = requests.post(url, form_data, headers=headers).text

            if response.find(SUCCESS_MSG) != -1:
                self.puzzles[str(day)]['answer'] = answer
                self.save_json()
                return True
            elif response.find(FAIL_MSG):
                return False
            else:
                raise Exception("Verification of solution failed; Neither success msg nor fail msg were returned.")

        elif self.puzzles[str(day)]['answer'] == answer:
            return True
        return False
