import telegram
import requests

bot_token = '6448952050:AAFg5DDTF6y36dlDfVVPGi23pMOdWqrHS3Q'
bot = telegram.Bot(token=bot_token)


def request_to_telegram(user_req, office):
    chat_id = 559091554
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    text = f'Срочная заявка: {user_req}, помещение {office}'
    params = {'chat_id': chat_id, 'text': text}
    response = requests.get(url, params=params)
    print(f'Сообщение отправлено: {response.json()}')
