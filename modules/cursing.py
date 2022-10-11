import random
from general.module_base import ModuleBase

class Cursing(ModuleBase):
    def __init__(self, part_of_json_file, speaker):
        super().__init__(part_of_json_file, speaker)

    def perform_check(self, microphone_recognized_text):
        result = self.retrieve_json_part_single(microphone_recognized_text)
        if result is not None:
            self.speaker.speak(random.choice(result["response"]))
