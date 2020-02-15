from datetime import datetime, timedelta
import bs4
import requests
import registration
import r619
import r629
import r639
import r618
import r628
import r638
import r617
import r627
import r637
import r616
import r626_1
import r626_2
import r636
from fake_useragent import UserAgent

class Command():
    def __init__(self):
        self.time=datetime.now()
    def get_time(self):
        time = self.time
        time=datetime.strftime(time,'%H:%M')
        return time

    def get_time_shower(self):
        pocket = 'Перемена'
        time1 = self.time
        if time1 >= datetime(time1.year, time1.month, time1.day, hour=8, minute=0) and time1 <= datetime(time1.year,
                                                                                                         time1.month,
                                                                                                         time1.day,
                                                                                                         hour=8,
                                                                                                         minute=45):
            pocket = datetime(time1.year, time1.month, time1.day, hour=8, minute=45) - timedelta(hours=time1.hour,
                                                                                                 minutes=time1.minute)
        elif time1 >= datetime(time1.year, time1.month, time1.day, hour=8, minute=50) and time1 <= datetime(time1.year,
                                                                                                            time1.month,
                                                                                                            time1.day,
                                                                                                            hour=9,
                                                                                                            minute=35):
            pocket = datetime(time1.year, time1.month, time1.day, hour=9, minute=35) - timedelta(hours=time1.hour,
                                                                                                 minutes=time1.minute)
        elif time1 >= datetime(time1.year, time1.month, time1.day, hour=9, minute=45) and time1 <= datetime(time1.year,
                                                                                                            time1.month,
                                                                                                            time1.day,
                                                                                                            hour=10,
                                                                                                            minute=30):
            pocket = datetime(time1.year, time1.month, time1.day, hour=10, minute=30) - timedelta(hours=time1.hour,
                                                                                                  minutes=time1.minute)
        elif time1 >= datetime(time1.year, time1.month, time1.day, hour=10, minute=35) and time1 <= datetime(time1.year,
                                                                                                             time1.month,
                                                                                                             time1.day,
                                                                                                             hour=11,
                                                                                                             minute=20):
            pocket = datetime(time1.year, time1.month, time1.day, hour=11, minute=20) - timedelta(hours=time1.hour,
                                                                                                  minutes=time1.minute)
        elif time1 >= datetime(time1.year, time1.month, time1.day, hour=11, minute=40) and time1 <= datetime(time1.year,
                                                                                                             time1.month,
                                                                                                             time1.day,
                                                                                                             hour=12,
                                                                                                             minute=25):
            pocket = datetime(time1.year, time1.month, time1.day, hour=12, minute=25) - timedelta(hours=time1.hour,
                                                                                                  minutes=time1.minute)
        elif time1 >= datetime(time1.year, time1.month, time1.day, hour=12, minute=30) and time1 <= datetime(time1.year,
                                                                                                             time1.month,
                                                                                                             time1.day,
                                                                                                             hour=13,
                                                                                                             minute=15):
            pocket = datetime(time1.year, time1.month, time1.day, hour=13, minute=15) - timedelta(hours=time1.hour,
                                                                                                  minutes=time1.minute)
        elif time1 >= datetime(time1.year, time1.month, time1.day, hour=13, minute=25) and time1 <= datetime(time1.year,
                                                                                                             time1.month,
                                                                                                             time1.day,
                                                                                                             hour=14,
                                                                                                             minute=40):
            pocket = datetime(time1.year, time1.month, time1.day, hour=14, minute=10) - timedelta(hours=time1.hour,
                                                                                                  minutes=time1.minute)
        elif time1 >= datetime(time1.year, time1.month, time1.day, hour=14, minute=15) and time1 <= datetime(time1.year,
                                                                                                             time1.month,
                                                                                                             time1.day,
                                                                                                             hour=15,
                                                                                                             minute=00):
            pocket = datetime(time1.year, time1.month, time1.day, hour=15, minute=0) - timedelta(hours=time1.hour,
                                                                                                 minutes=time1.minute)
        elif time1 >= datetime(time1.year, time1.month, time1.day, hour=15, minute=20) and time1 <= datetime(time1.year,
                                                                                                             time1.month,
                                                                                                             time1.day,
                                                                                                             hour=16,
                                                                                                             minute=5):
            pocket = datetime(time1.year, time1.month, time1.day, hour=16, minute=5) - timedelta(hours=time1.hour,
                                                                                                 minutes=time1.minute)
        elif time1 >= datetime(time1.year, time1.month, time1.day, hour=16, minute=10) and time1 <= datetime(time1.year,
                                                                                                             time1.month,
                                                                                                             time1.day,
                                                                                                             hour=16,
                                                                                                             minute=55):
            pocket = datetime(time1.year, time1.month, time1.day, hour=16, minute=55) - timedelta(hours=time1.hour,
                                                                                                  minutes=time1.minute)
        else:
            if time1 < datetime(time1.year, time1.month, time1.day, hour=8, minute=0):
                pocket = 'Пары не начались'
            elif time1 > datetime(time1.year, time1.month, time1.day, hour=16, minute=55):
                pocket = 'Пары закончились'
        if type(pocket) is str:
            return pocket
        else:
            if type(pocket) is datetime:
                return "До конца пары осталось " + str(pocket.minute) + "-минут"

    def get_schedule_week(self,id):
        file=registration.get_group(id)
        kod = file + '.monday()'
        otv = eval(kod)
        kod = file + '.tuesday()'
        otv += "\n\n"+eval(kod)
        kod = file + '.wednesday()'
        otv += "\n\n"+eval(kod)
        kod = file + '.thursday()'
        otv += "\n\n"+eval(kod)
        kod = file + '.friday()'
        otv += "\n\n"+eval(kod)
        return otv

    def get_schedule_today(self,id):
        file=registration.get_group(id)
        week_day=datetime.now()
        week_day=week_day.strftime('%A').lower()
        kod=file+'.'+week_day+'()'
        otv=eval(kod)
        return otv

    def get_weather(self,p,time):
        weather1 = p[8].text+"°"
        weather2 = p[9].text+"°"
        weather3 = p[10].text+"°"
        weather4 = p[11].text+"°"
        weather5 = p[12].text+"°"
        weather6 = p[13].text+"°"

        time1 = time[2].text[0]+":00"
        time2 = time[3].text[:2]+":00"
        time3 = time[4].text[:2]+":00"
        time4 = time[5].text[:2]+":00"
        time5 = time[6].text[:2]+":00"
        time6 = time[7].text[:2]+":00"

        result = ''
        result = result + (
                    'Утром  :' + time1 + " \"" + weather1 + "\"" + ' - ' + time2 + " \"" + weather2 + "\"") + '\n'
        result = result + (
                    'Днём   :' + time3 + " \"" + weather3 + "\"" + ' - ' + time4 + " \"" + weather4 + "\"") + '\n'
        result = result + (
                    'Вечером:' + time5 + " \"" + weather5 + "\"" + ' - ' + time6 + " \"" + weather6 + "\"")

        return result

    def get_help(self):
        text="Команды:\n" \
             "Помощь-вывод команд\n" \
             "Время-вывод времени\n" \
             "ОВ-оставшееся время до звонка или конца пары\n" \
             "РС-расписание пар на сегодня\n" \
             "РН-расписание пар на неделю\n"
        return text