from abc import ABC


class IEmailRequest(ABC):
    def __init__(self, sender, receiver, subject, message):
        self.subject = subject
        self.sender = sender
        self.receiver = receiver
        self.message = message

    def process_request(self, username, password):
        pass


class GmailRequest(IEmailRequest):
    def process_request(self, username, password):
        print("Request processed")
