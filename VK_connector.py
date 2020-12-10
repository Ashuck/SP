import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

from vk_config import token, Kbr, kbr_schet
from answers import from_inline


vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk=vk_session)

cmn_commands = {
    "Проверки счетной палаты": {
        "text": "По теме 'Проверки счетной палаты' доступны следующие консультации:",
        "kbr": kbr_schet.get_keyboard()
    },
    "Вопрос 2": {
        "text": "По данной теме доступны следующие консультации",
        "kbr": '[]'
    },
    "Вопрос 3": {
        "text": "По данной теме доступны следующие консультации",
        "kbr": '[]'
    },
}

cmn_commands.update(from_inline)

try:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text and event.from_user:
            if event.text.lower() == "получить справку":
                vk.messages.send(
                    user_id= event.user_id,
                    random_id= event.random_id,
                    message= "С помощью этой клавиатуры вы сможете получить ответы на некоторые вопросы",
                    keyboard= Kbr
                    )
            
            # Обрабатываем "#ошибка"
            elif cmn_commands.get(event.text):
                answer = cmn_commands.get(event.text)
                vk.messages.send(
                    user_id= event.user_id,
                    random_id= event.random_id,
                    message= answer['text'],
                    keyboard= answer['kbr']
                    )
    
except KeyboardInterrupt:
    print("\nStop")
    exit()
