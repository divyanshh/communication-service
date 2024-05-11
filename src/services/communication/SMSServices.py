from abc import ABC


class ISMSRequest(ABC):
    def __init__(self, mobile_no, message):
        self.mobile_no = mobile_no
        self.message = message

    def process_request(self, username, password, phone_number):
        pass


class JIOSMSRequest(ISMSRequest):
    def process_request(self, username, password, phone_number):
        print("SMS Request processed")
