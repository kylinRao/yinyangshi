import datetime,os,sys,time



tasksList = [

    {"fixdeTime":datetime.time(5,0,0,0),"fileName":"all.py"},

    {"fixdeTime":datetime.time(9,0,0,0),"fileName":"juexing.py"},
    {"fixdeTime":datetime.time(11,0,0,0),"fileName":"yuhun.py"},


    {"fixdeTime":datetime.time(15,0,0,0),"fileName":"tansuo.py"},
    {"fixdeTime":datetime.time(17,0,0,0),"fileName":"jieJieTuPo.py"},


]

def run(now,*args):
    for subDic in args[0]:
        #print type(subDic),subDic
        if now.hour == subDic["fixdeTime"].hour and now.minute == subDic["fixdeTime"].minute:
            print "cmd : python  {fileName}".format(fileName=subDic["fileName"])
            os.system("python  {fileName}".format(fileName=subDic["fileName"]))
    return True


if __name__ == '__main__':

    print "this py script executed when windows starts,scheduled yinyangshi tasks are written down in this script!"
    print "we have the following tasks to be done:"
    for item in tasksList:
        print item
    while 1:
        now = datetime.datetime.now()

        run(now,tasksList)
        time.sleep(50)





