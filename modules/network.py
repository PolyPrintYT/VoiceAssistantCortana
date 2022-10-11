import random
from general.module_base import ModuleBase


class Network(ModuleBase):
    def __init__(self, part_of_json_file, speaker):
        super().__init__(part_of_json_file, speaker)

    def perform_check(self, microphone_recognized_text):
        result = self.retrieve_json_part_multiple(microphone_recognized_text)
        if result is not None:
            self.speedtest_client.get_best_server()
            self.speedtest_client.download()
            self.speedtest_client.upload()
            print(self.speedtest_client.results)
            if result["type"] == "upload":
                self.speaker.speak(random.choice(result["response"]) + f" {round(self.speedtest_client.results.upload / 1024 / 1024, 2)} mbps")
                pass
            if result["type"] == "download":
                self.speaker.speak(random.choice(result["response"]) + f" {round(self.speedtest_client.results.download / 1024 / 1024, 2)} mbps")
                pass
            if result["type"] == "ip_lan":
                self.speaker.speak(random.choice(result["response"]) + f" {self.speedtest_client.results.client['ip']}")
                pass
            if result["type"] == "ip_wan":
                self.speaker.speak(random.choice(result["response"]) + f" {self.speedtest_client.results.client['ip']}")
                pass
            if result["type"] == "overview":
                self.speaker.speak(random.choice(result["response"]))
                self.speaker.speak(random.choice(self.json_file[0]["response"]) + f" {round(self.speedtest_client.results.upload / 1024 / 1024, 2)} mbps")
                self.speaker.speak(random.choice(self.json_file[1]["response"]) + f" {round(self.speedtest_client.results.download / 1024 / 1024, 2)} mbps")
                self.speaker.speak(random.choice(self.json_file[2]["response"]) + f" {self.speedtest_client.results.client['ip']}")
                pass
