import json
import random

from common import get_logger
from .prompts import FLUX_SIMPLE_PROMPT
from .FlagHandler import FlagsHandler, res_spliter

logger = get_logger("ComfyBOT")


class FluxTxtToImageHandler:
    _neg_token = '!neg!'

    def __init__(self):
        self.workflow_as_text = FLUX_SIMPLE_PROMPT
        self._flags_handler = FlagsHandler(r'--(\w+)\s+([^\s]+)')
        self._flags_handler.set_flags("seed", [["46", "inputs", "seed"]])
        self._flags_handler.set_flags("positive-prompt", [["40", "inputs", "prompt"]])
        self._flags_handler.set_flags("negative-prompt", [["41", "inputs", "prompt"]])

    def handle(self, message):
        prompt = json.loads(self.workflow_as_text)
        flags = self._flags_handler.extract_flags(message)
        positive_prompt = self._flags_handler.clean_from_flags(message)
        parts = positive_prompt.split(self._neg_token, maxsplit=1)

        self._flags_handler.manipulate_prompt("positive-prompt", parts[0], prompt)

        if len(parts) > 1:
            self._flags_handler.manipulate_prompt("negative-prompt", parts[1], prompt)

        self._flags_handler.manipulate_prompt("seed", str(random.randint(1, 2 ** 64)), prompt)

        for flagTuple in flags:
            self._flags_handler.manipulate_prompt(flagTuple[0], flagTuple[1], prompt)
            pass

        return prompt


    def describe(self, prompt):
        return ""


    def info(self):
        prompt = json.loads(self.workflow_as_text)
        return f'''
# Handler: {self.key()}

## Special tokens:
`{self._neg_token}` - will split the message into positive/negative prompts.
'''


    def key(self):
        return "FluxTxt2Img"


    def default_flags(self):
        return ""

