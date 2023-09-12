import os
from dotenv import load_dotenv
load_dotenv()
from heyoo import WhatsApp

credentials = {
    'access_token': os.environ['ACCESS_TOKEN'],
    'phone_number_id': os.environ['PHONE_NUMBER_ID']
}

messenger = WhatsApp(credentials['access_token'], phone_number_id=credentials['phone_number_id'])

result = messenger.send_message('Your message ', 'Mobile eg: 541135846028')

print(result)
