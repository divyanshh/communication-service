from src.services.ProviderFactory import ProviderFactory
from src.services.RequestsHandlers import EmailRequestHandler
from src.services.communication.EmailServices import IEmailRequest, GmailRequest
from src.services.communication.SMSServices import ISMSRequest
from src.services.communication.SoundBoxServices import ISoundBoxRequest


class ProviderService:
    def __init__(self):
        self.providers = {}
        self.providers_details = {}

    def add_provider(self, provider_details, communication_type):
        id = provider_details.get("id")

        if id in self.providers.get(communication_type, {}):
            print("Provider already exists")

        self.providers.setdefault(communication_type, {})[id] = True
        self.providers_details[id] = provider_details
        print("Provider set to active")
        return True

    def get_provider(self, id: str):
        for comm_type, providers in self.providers.items():
            if id in providers:
                active_status = providers[id]
                details = self.providers_details[id]
                print("Communication Type:", comm_type)
                print("Provider Details:")
                for key, value in details.items():
                    print(f"{key}: {value}")
                print("Active Status:", "Active" if active_status else "Inactive")
                return comm_type, details, active_status
        return None, None

    def update_state(self, provider_id: str, active: bool):
        comm_type, _, _ = self.get_provider(provider_id)
        if comm_type:
            self.providers[comm_type][provider_id] = active
            print("State updated successfully")
            return True
        else:
            print("Provider does not exist")
            return False

    def update_provider(self, provider_details):
        id = provider_details.get("id")
        if id in self.providers_details:
            self.providers_details[id].update(provider_details)
            return True
        else:
            print("Provider does not exist")
            return False

    def process_request(self, request):
        handler = None
        if isinstance(request, IEmailRequest):
            handler = EmailRequestHandler(self)
        elif isinstance(request, ISMSRequest):
            pass
            # handler = SMSRequestHandler(self) # TODO
        elif isinstance(request, ISoundBoxRequest):
            pass
            # handler = SoundBoxRequestHandler(self) # TODO

        if handler:
            return handler.process_request(request)
        else:
            print("Unsupported request type")
            return False


if __name__ == '__main__':
    provider_details = ProviderFactory.create_provider("EMAIL", "GMAIL", "1")
    ob = ProviderService()
    ob.add_provider(provider_details, "EMAIL")
    ob.get_provider("1")
    ob.update_state("1", False)
    provider_details["password"] = "updated_pass"
    ob.update_provider(provider_details)
    request = GmailRequest("Sender", "receiver", "subject", "message")
    ob.update_state("1", True)
    ob.process_request(request)

"""
# Sample output
Enter email provider username: user
Enter email provider password: pass
Enter email provider URL: https://gmail/send_email
Provider set to active
Communication Type: EMAIL
Provider Details:
id: 1
name: GMAIL
username: user
password: pass
EMAIL: https://gmail/send_email
Active Status: Active
Communication Type: EMAIL
Provider Details:
id: 1
name: GMAIL
username: user
password: pass
EMAIL: https://gmail/send_email
Active Status: Active
State updated successfully
Communication Type: EMAIL
Provider Details:
id: 1
name: GMAIL
username: user
password: updated_pass
EMAIL: https://gmail/send_email
Active Status: Inactive
State updated successfully
Communication Type: EMAIL
Provider Details:
id: 1
name: GMAIL
username: user
password: updated_pass
EMAIL: https://gmail/send_email
Active Status: Active
Request processed
GMAIL request sent
"""


