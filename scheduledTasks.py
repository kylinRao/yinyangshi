import datetime,os,sys,time

tasksList = [

    {"fixdeTime":datetime.time(5,0,0,0),"fileName":"all.py"},

]

def run(now,*args):
    for subDic in args[0]:
        print type(subDic),subDic
        if now.hour == subDic["fixdeTime"].hour and now.minute == subDic["fixdeTime"].minute:
            os.system("python  {fileName}".format(fileName=subDic["fileName"]))
    return True


if __name__ == '__main__':
    while 1:
        now = datetime.datetime.now()

        run(now,tasksList)
        time.sleep(50)





