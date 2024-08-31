from twilio.rest import Client
from models import TwilioSettings


class TwilioClient:

    def __init__(self, settings: TwilioSettings):
        self._settings = settings

    def send_sms(self, to, body):
        account_sid = self._settings.TWILIO_ACCOUNT_SID
        auth_token = self._settings.TWILIO_AUTH_TOKEN
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_=self._settings.TWILIO_PHONE_NUMBER,
            body=body,
            to=to
        )

        return message.sid

