from commander import Command

class VkBot:
    def __init__(self,session_api,event,p,time):
        self.p=p
        self.time=time
        self.event=event
        self.session_api=session_api
        self._USER_ID=event.peer_id
        self._USERNAME=self._get_user_name_from_vk_id(session_api,event.peer_id)

        self.Com=Command()


        self._COMMANDS=["ПРИВЕТ","ПОГОДА","ВРЕМЯ","ОВ","РС","РН","ПОМОЩЬ"]



    def _get_user_name_from_vk_id(self,session_api,user_id):
        user_name=session_api.users.get(user_id=user_id)[0]['first_name']
        return user_name



    def new_message(self, message):
        if message.upper()==self._COMMANDS[0]:
            return f"Привет-привет, {self._USERNAME}!"
        elif message.upper()==self._COMMANDS[1]:
            return self.Com.get_weather(self.p,self.time)
        elif message.upper()==self._COMMANDS[2]:
            return  self.Com.get_time()
        elif message.upper()==self._COMMANDS[3]:
            return self.Com.get_time_shower()
        elif message.upper()==self._COMMANDS[4]:
            return self.Com.get_schedule_today(self._USER_ID)
        elif message.upper()==self._COMMANDS[5]:
            return self.Com.get_schedule_week(self._USER_ID)
        elif message.upper()==self._COMMANDS[6]:
            return self.Com.get_help()
        elif message.upper=="ВОЙТИ":
            return 'Вы вошли'
        else:
            return "Не понимаю о чем вы..."


