import os
import platform
import random
from general.module_base import ModuleBase


class Program(ModuleBase):
    def __init__(self, part_of_json_file, speaker):
        super().__init__(part_of_json_file[platform.system()], speaker)

    def perform_check(self, microphone_recognized_text):
        result = self.retrieve_json_part_multiple(microphone_recognized_text)
        if result is not None:
            if result["type"] == "open_executable":
                self.speaker.speak(random.choice(result["response"]))
                os.system("\"" + result["folder"] + result["file_name"] + ".exe \"")
            if result["type"] == "website":
                self.speaker.speak(random.choice(result["response"]))
                os.system("start " + result["url"])
            if result["type"] == "kill_executable":
                self.speaker.speak("closing " + result["file_name"])
                os.system("taskkill /im " + result["file_name"] + ".exe /F")
