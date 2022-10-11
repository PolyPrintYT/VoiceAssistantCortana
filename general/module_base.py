import random


class ModuleBase:
    def __init__(self, json_file, speaker):
        self.json_file = json_file
        self.speaker = speaker

    def retrieve_json_part_single(self, microphone_recognized_text):
        for wake_word in self.json_file["wake_words"]:
            wake_word_part_indexes = []
            if len(set(str(microphone_recognized_text).split()).intersection(set(str(wake_word).split()))) == len(str(wake_word).split()):
                for wake_word_part in str(wake_word).split():
                    wake_word_part_indexes.append(str(microphone_recognized_text).index(wake_word_part))
                if wake_word_part_indexes == sorted(wake_word_part_indexes):
                    return self.json_file

    def retrieve_json_part_multiple(self, microphone_recognized_text):
        for json_file_part in self.json_file:
            for wake_word in json_file_part["wake_words"]:
                wake_word_part_indexes = []
                if len(set(str(microphone_recognized_text).split()).intersection(set(str(wake_word).split()))) == len(str(wake_word).split()):
                    for wake_word_part in str(wake_word).split():
                        wake_word_part_indexes.append(str(microphone_recognized_text).index(wake_word_part))
                    if wake_word_part_indexes == sorted(wake_word_part_indexes):
                        return json_file_part
