from abc import ABC


class ProviderFactory:
    @staticmethod
    def create_provider(communication_type, provider, id):
        if communication_type == 'EMAIL':
            ob = EmailProviderCreator()
            return ob.create_provider(provider, id)
        elif communication_type == 'SMS':
            ob = SMSProviderCreator()
            return ob.create_provider(provider, id)
        elif communication_type == 'SOUNDBOX':
            ob = SMSProviderCreator()
            return ob.create_provider(provider, id)
        else:
            print("Invalid provider type")
            return None


class IProviderCreator(ABC):
    def create_provider(self, provider, id):
        pass


class EmailProviderCreator(IProviderCreator):
    def create_provider(self, provider, id):
        username = input("Enter email provider username: ")
        password = input("Enter email provider password: ")
        email_url = input("Enter email provider URL: ")
        return {
            "id": id,
            "name": provider,
            "username": username,
            "password": password,
            "EMAIL": email_url
        }


class SMSProviderCreator(IProviderCreator):
    def create_provider(self, provider, id):
        username = input("Enter SMS provider username: ")
        password = input("Enter SMS provider password: ")
        sms_url = input("Enter SMS URL: ")
        return {
            "id": id,
            "name": provider,
            "username": username,
            "password": password,
            "SMS": sms_url
        }


class SoundboxProviderCreator(IProviderCreator):
    def create_provider(self, provider: str, id: str):
        username = input("Enter Soundbox provider username: ")
        password = input("Enter Soundbox provider password: ")
        soundbox_url = input("Enter soundbox URL: ")
        return {
            "id": id,
            "name": provider,
            "username": username,
            "password": password,
            "SOUNDBOX": soundbox_url
        }
