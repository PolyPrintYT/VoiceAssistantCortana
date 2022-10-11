import random
from general.module_base import ModuleBase
import modules


class Awake(ModuleBase):
    def __init__(self, part_of_json_file, speaker):
        super().__init__(part_of_json_file, speaker)

    def perform_check(self, microphone_recognized_text, handled_by):
        result = self.retrieve_json_part_single(microphone_recognized_text)
        if result is not None:
            if isinstance(handled_by, modules.inDevelopment.discord_connection.DiscordClient):
                print("trying to send the message")
                handled_by.send_message(random.choice(result["response"]))
            else:
                self.speaker.speak(random.choice(result["response"]))
