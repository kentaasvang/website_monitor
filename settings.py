import os
from models import TwilioSettings

from dotenv import load_dotenv
load_dotenv()

twilio_settings = TwilioSettings(
    account_sid=os.getenv('TWILIO_ACCOUNT_SID'),
    auth_token=os.getenv('TWILIO_AUTH_TOKEN'),
    phone_number=os.getenv('TWILIO_PHONE_NUMBER')
)
