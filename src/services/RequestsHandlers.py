import random


class EmailRequestHandler:
    def __init__(self, provider_service):
        self.provider_service = provider_service

    def process_request(self, request):
        communication_type = "EMAIL"
        provider_name = self.get_random_email_provider()
        comm_type, _, active_status = self.provider_service.get_provider(provider_name)

        if comm_type == communication_type and active_status:
            request.process_request(self.provider_service.providers_details[provider_name]["username"],
                                    self.provider_service.providers_details[provider_name]["password"])
            print("GMAIL request sent")
            return True
        else:
            print("EMAIL provider inactive")
        return False

    def get_random_email_provider(self):
        email_providers = [provider for provider, details in self.provider_service.providers_details.items() if
                           details.get("EMAIL")]
        if not email_providers:
            print("No active email providers available")
            return None
        return random.choice(email_providers)

