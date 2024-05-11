from abc import ABC


class ISoundBoxRequest(ABC):
    def __init__(self, sender, receiver, subject, message):
        self.subject = subject
        self.sender = sender
        self.receiver = receiver
        self.message = message

    def process_request(self, username, password):
        pass


class SoundCloudRequest(ISoundBoxRequest):
    def process_request(self, username, password):
        print("SoundCloudRequest processed")
