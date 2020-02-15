from vk_bot import VkBot
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll,VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
from _thread import start_new_thread
import registration as Reg
import key
import bs4
import requests
from fake_useragent import UserAgent

class Key():
    def __init__(self,event,payload):
        self.message=event.obj.text
        self.id=event.obj.peer_id
        self.payload=payload
        self.chek=0
        com_line = []
        com_line.append(payload)
        self.com_line=com_line

    def start(self):
        lencom_line=len(self.com_line)
        message=self.message
        payload=self.com_line[lencom_line-1]
        print(self.com_line)
        if payload==1:
            write_msg(event.obj.peer_id, get_random_id(), "Ваш факультет?", self.fak())
            Reg.id_reg(self.id)
        elif payload==2:
            write_msg(event.obj.peer_id, get_random_id(), "Ваш курс?", self.kurs())
            Reg.fak_reg(self.id,message)
        elif payload==3:
            write_msg(event.obj.peer_id, get_random_id(), "Ваша группа?", self.group(payload))
            Reg.kurs_reg(self.id,message)
        elif payload==4:
            write_msg(event.obj.peer_id, get_random_id(), "Ваша группа?", self.group(payload))
            Reg.kurs_reg(self.id,message)
        elif payload==5:
            write_msg(event.obj.peer_id, get_random_id(), "Ваша группа?", self.group(payload))
            Reg.kurs_reg(self.id,message)
        elif payload==6:
            write_msg(event.obj.peer_id, get_random_id(), "Ваша группа?", self.group(payload))
            Reg.kurs_reg(self.id,message)
        elif 616<=payload<=639:
            write_msg(event.obj.peer_id, get_random_id(), "Ваша группа делиться на подгруппы?", self.check_podgroup())
            Reg.group_reg(self.id,message)
        elif payload==101:
            text=Reg.get_info_id(self.id)
            write_msg(event.obj.peer_id, get_random_id(), text, self.begin())
        elif payload==100:
            write_msg(event.obj.peer_id, get_random_id(), "Ваша подгруппа?", self.podgroup())
        elif payload==1001 or payload==1002:
            Reg.reg_podgroup(self.id,message)
            text = Reg.get_info_id(self.id)
            write_msg(event.obj.peer_id, get_random_id(), text, self.begin())
        elif payload==10:
            check = True
            Reg.check(self.id, check)
            write_msg(event.obj.peer_id, get_random_id(), 'Здравствуйте', creat_keyboard())
        elif payload==2001:
            Reg.del_user(self.id)
            self.com_line[lencom_line - 1]=1
            self.start()
        else:
            return None


    def reg(self):
        key=VkKeyboard(one_time=False)
        key.add_button("Регистрация", color=VkKeyboardColor.POSITIVE,payload=1)
        return key.get_keyboard()

    def fak(self):
        key = VkKeyboard(one_time=False)
        key.add_button("ФМИТИ", color=VkKeyboardColor.POSITIVE,payload=2)
        return key.get_keyboard()

    def kurs(self):
        key = VkKeyboard(one_time=False)
        key.add_button("1", color=VkKeyboardColor.POSITIVE,payload=3)
        key.add_button("2", color=VkKeyboardColor.POSITIVE,payload=4)
        key.add_line()
        key.add_button("3", color=VkKeyboardColor.POSITIVE,payload=5)
        key.add_button("4", color=VkKeyboardColor.POSITIVE,payload=6)
        key.add_line()
        key.add_button("Начать с начало",color=VkKeyboardColor.POSITIVE,payload=2001)
        return key.get_keyboard()

    def group(self,kurs):
        key = VkKeyboard(one_time=False)
        if kurs==3:
            key.add_button("619", color=VkKeyboardColor.POSITIVE, payload=619)
            key.add_button("629", color=VkKeyboardColor.POSITIVE, payload=629)
            key.add_button("639", color=VkKeyboardColor.POSITIVE, payload=639)
            key.add_line()
            key.add_button("Начать с начало",color=VkKeyboardColor.POSITIVE,payload=2001)
        elif kurs==4:
            key.add_button("618", color=VkKeyboardColor.POSITIVE, payload=618)
            key.add_button("628", color=VkKeyboardColor.POSITIVE, payload=628)
            key.add_button("638", color=VkKeyboardColor.POSITIVE, payload=638)
            key.add_line()
            key.add_button("Начать с начало",color=VkKeyboardColor.POSITIVE,payload=2001)
        elif kurs==5:
            key.add_button("617", color=VkKeyboardColor.POSITIVE, payload=617)
            key.add_button("627", color=VkKeyboardColor.POSITIVE, payload=627)
            key.add_button("637", color=VkKeyboardColor.POSITIVE, payload=637)
            key.add_line()
            key.add_button("Начать с начало",color=VkKeyboardColor.POSITIVE,payload=2001)
        elif kurs==6:
            key.add_button("616", color=VkKeyboardColor.POSITIVE, payload=616)
            key.add_button("626", color=VkKeyboardColor.POSITIVE, payload=626)
            key.add_button("636", color=VkKeyboardColor.POSITIVE, payload=636)
            key.add_line()
            key.add_button("Начать с начало",color=VkKeyboardColor.POSITIVE,payload=2001)
        return key.get_keyboard()

    def check_podgroup(self):
        key=VkKeyboard(one_time=False)
        key.add_button('Да', color=VkKeyboardColor.POSITIVE, payload=100)
        key.add_button('Нет', color=VkKeyboardColor.POSITIVE, payload=101)
        key.add_line()
        key.add_button("Начать с начало",color=VkKeyboardColor.POSITIVE,payload=2001)
        return key.get_keyboard()

    def podgroup(self):
        key=VkKeyboard(one_time=False)
        key.add_button('1', color=VkKeyboardColor.POSITIVE, payload=1001)
        key.add_button('2', color=VkKeyboardColor.POSITIVE, payload=1002)
        key.add_line()
        key.add_button("Начать с начало",color=VkKeyboardColor.POSITIVE,payload=2001)
        return key.get_keyboard()

    def begin(self):
        key = VkKeyboard(one_time=False)
        key.add_button("Войти", color=VkKeyboardColor.POSITIVE,payload=10)
        key.add_line()
        key.add_button("Начать с начало", color=VkKeyboardColor.POSITIVE, payload=2001)
        return key.get_keyboard()


def write_msg(peer_id, random_id, message, keyboard):
    session_api.messages.send(peer_id=peer_id, random_id=random_id, message=message, keyboard=keyboard)


def creat_keyboard():
    keyboard=VkKeyboard(one_time=False)
    keyboard.add_button("Привет",color=VkKeyboardColor.POSITIVE)
    keyboard.add_button("Помощь", color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button("Время", color=VkKeyboardColor.POSITIVE)
    keyboard.add_button("ОВ", color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button("РС", color=VkKeyboardColor.POSITIVE)
    keyboard.add_button("РН", color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button("Погода", color=VkKeyboardColor.POSITIVE)
    return keyboard.get_keyboard()

http = "https://www.gismeteo.ru/weather-gorno-altaysk-5180/"
soup = requests.get(http, headers={'User-Agent': UserAgent().chrome})
b = bs4.BeautifulSoup(soup.text, "html.parser")
p = b.findAll('span', class_="unit_temperature_c")
time = b.find_all('div', class_="w_time")

token=key.key()
vk_session=vk_api.VkApi(token=token)


session_api=vk_session.get_api()
longpoll=VkBotLongPoll(vk_session,group_id=188534813,wait=25)

def handler(event):
    if Reg.search_user(event):
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.from_user:
                bot = VkBot(session_api, event.obj,p,time)
                if event.obj.text.upper() == "SANTA-CLOSE":
                    exit()
                write_msg(event.obj.peer_id, get_random_id(), bot.new_message(event.obj.text), creat_keyboard())
    else:
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.from_user:
                print(event)
                if event.obj.payload != None:
                    payload = int(event.obj.payload)
                else:
                    payload = None

                print(type(payload))
                keyboard = Key(event, payload)

                if payload == None:
                    write_msg(event.obj.peer_id, get_random_id(), "Здрайствуйте вы не прошили регистрацию.",
                              keyboard.reg())
                else:
                    keyboard.start()


while True:
    for event in longpoll.listen():
        start_new_thread(handler, (event,))
