import datetime
import random
from general.module_base import ModuleBase


class Closing(ModuleBase):
    def __init__(self, part_of_json_file, speaker):
        super().__init__(part_of_json_file, speaker)

    def perform_check(self, microphone_recognized_text):
        result = self.retrieve_json_part_single(microphone_recognized_text)
        if result is not None:
            current_hour = int(datetime.datetime.now().strftime("%H"))
            if 0 >= current_hour < 6:
                self.speaker.speak(random.choice(result["night"]))
            elif 6 >= current_hour < 12:
                self.speaker.speak(random.choice(result["morning"]))
            elif 12 >= current_hour < 18:
                self.speaker.speak(random.choice(result["afternoon"]))
            else:
                self.speaker.speak(random.choice(result["evening"]))
            return False
        return True
