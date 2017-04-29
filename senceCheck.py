#coding=utf-8
from conf.globalFacts import *
from siftxy import *
# import logging.config
# logging.config.fileConfig(r"L:\appAutoScripts\conf\logging.conf")
# loggerInner = logging.getLogger("logger_root")




#返回当前的场景值
def get_sence(bigPic,sences=senceList):

    for sence in sences:
        loggerInner.debug("now sence is "+sence["sence"])

        x,y = get_x_y(bigPic,sence["path"],accurate=0.1)
        if x != "nox":
            #print "found",sence["sence"]
            loggerInner.info("------found a matched position {x},{y} ,sencePic is {sencePic},flagPic is {flagPic},now exit  get_sence() ".format(x=x,y=y,sencePic=bigPic,flagPic=sence["path"]))
            return sence["sence"]
    loggerInner.info("------no sence is found in preset sences ,return otherSence for default!!!")
    return "otherSence"

if __name__ == '__main__':
    #get_sence("prePic/testPic/screenshot.png")


    # get_sence("prePic/testPic/test.png")
    # get_sence("prePic/testPic/SenceTanSuoFuBenFighting.png")
    sence = get_sence(defaultSSPath)
    print sence
    # get_sence("prePic/testPic/SenceVictory.png")
    # get_sence("prePic/testPic/SenceVictoryDaMo.png")
    # get_sence("prePic/testPic/SenceVictoryDaMoOpened.png")
    # get_sence("prePic/testPic/boss.png")





