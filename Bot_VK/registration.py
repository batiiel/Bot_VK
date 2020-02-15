import pickle


    #def __init__(self,event):
        #self.peer_id=event.obj.peer_id
def check(id,check):
    data = read_file()
    check = {'check': check}
    data[id].update(check)
    write_file(data)

def read_file():
    f=open('data.pkl','rb')
    try:
        data=pickle.load(f)
    except EOFError:
        data={}
    f.close()
    return data

def write_file(data):
    f=open('data.pkl','wb')
    pickle.dump(data,f)
    f.close()

def search_user(event):
    data=read_file()
    id=event.obj.peer_id
    if event.obj.peer_id in data.keys():
        if data[id].get('check')==True:
            return True
    else:
        return False

def id_reg(id):
    data=read_file()
    data[id]={}
    check={'check':False}
    data[id].update(check)
    write_file(data)

def fak_reg(id,fak):
    data=read_file()
    fak={'fak':fak}
    data[id].update(fak)
    write_file(data)

def kurs_reg(id,kurs):
    data=read_file()
    kurs={'kurs':kurs}
    data[id].update(kurs)
    write_file(data)

def group_reg(id,group):
    data = read_file()
    group = {'group': group}
    data[id].update(group)
    write_file(data)

def reg_podgroup(id, podgroup):
    data = read_file()
    podgroup = {'podgroup': podgroup}
    data[id].update(podgroup)
    write_file(data)

def get_info_id(id):
    data=read_file()
    text="Вы зарегистировались." \
         "\nПроверьте свои данные." \
         "\nВаш факультет: "+str(data[id].get('fak'))+ \
         "\nВаш курс: " +str(data[id].get('kurs'))+\
         "\nВаша группа: " +str(data[id].get('group'))
    if data[id].get('podgroup') != None:
        text+="\nВаша подгруппа" +str(data[id].get('podgroup'))
    return text

def get_group(id):
    data = read_file()
    file='r'+str(data[id].get('group'))
    if data[id].get('podgroup')!=None:
        file+='_'+str(data[id].get('podgroup'))
    return file

def del_user(id):
    data=read_file()
    data_copy=dict(data)
    del data_copy[id]
    write_file(data_copy)