#coding=utf-8
import os
import logging.config
logging.config.fileConfig(r"L:\appAutoScripts\conf\logging.conf")
loggerInner = logging.getLogger("logger_root")
os.name

XMAX = 1280
YMAX = 720
TANSUOCOLOR = [61, 36, 19, 255]
RONG_CHA = 5
confPath = r"L:\appAutoScripts\conf"

defaultSSPath = "screenshot.png"
tanSuoPath = "prePic/tanSuoRuKou.png"
tanSuoPath_10 = "prePic/tanSuo_10.png"
tanSuoPath_10_tanSuo = "prePic/tanSuo_10_tanSuo.png"
tanSuoPath_10_tanSuo_kick = "prePic/tanSuo_10_tanSuo_kick.png"
jueXingPath = "prePic/jueXing.png"
jinRuYouXiPath = "prePic/jinRuYouXi.png"
tianLeiGuPath = "prePic/tianLeiGuo.png"
leiTiaoZhanPath = "prePic/leiTiaoZhan.png"
leiSiCengPath = "prePic/leiSiCeng.png"
zhunBeiPath = "prePic/zhunBei.png"
yeHuoLunPath = "prePic/yeHuoLun.png"

fuBenTanSuoKaiShiButton = "prePic/fuBenTanSuoTanSuoButton.png"
fuBenTanSuoDaXiaoBingWuHuangGuang = "prePic/tansuo_xiaobing_wuhuangguang.png"
tanSuoZhunBeiPath = "prePic/tanSuoZhunBeiPath.png"
fengZhuanFuPath = "prePic/fengZhuanFu.png"

yunHunPath = "prePic/yunHunRuKou.png"
baQiDaShenPath = "prePic/baQiDaShen.png"
noticeCloseButton = "prePic/noticeCloseButton.png"
bossJiangpinButton = "prePic/bossJiangpinButton.png"
shengjiConfirmButton = "prePic/shengjiConfirmButton.png"
noticeCloseButtonColor = "prePic/noticeCloseButtonColor.png"
baoXiang = "prePic/baoxiang.png"
food = "prePic/food.png"
buji = "prePic/buji.png"
attackButton = "prePic/attackButton.png"

####场景和场景标志图片定义
SenceFlagTanSuoFuBenFightingPic = "prePic/SenceFlagTanSuoFuBenFightingPic.png"
SenceFlagTanSuoFuBenXuanZePic = "prePic/SenceFlagTanSuoFuBenXuanZePic.png"
SenceFlagSenceVictory = "prePic/SenceFlagSenceVictoryPic.png"
SenceFlagVictoryDaMo = "prePic/SenceFlagVictoryDaMoPic.png"
SenceFlagVictoryDaMo2 = "prePic/SenceFlagVictoryDaMoPic2.png"
SenceTanSuoFuBenHomePagePic = "prePic/SenceTanSuoFuBenHomePagePic.png"
SenceBossFightPic = "prePic/bossFight.png"
SenceYaoQingPic = noticeCloseButtonColor


SenceTanSuoFuBenFighting = "SenceTanSuoFuBenFighting"
SenceTanSuoFuBenXuanZe = "SenceTanSuoFuBenXuanZe"
SenceVictory = "SenceVictory"
SenceVictoryDaMo = "SenceVictoryDaMo"
SenceTanSuoFuBenHomePage = "SenceTanSuoFuBenHomePage"
SenceBossFight = "bossFight"
SenceYaoQing = "yaoQing"
# 定义场景和场景标志图关联关系
senceList = [
    {"sence": SenceTanSuoFuBenXuanZe, "path": SenceFlagTanSuoFuBenXuanZePic},
    {"sence": SenceTanSuoFuBenFighting, "path": SenceFlagTanSuoFuBenFightingPic},

    {"sence": SenceVictory, "path": SenceFlagSenceVictory},
    {"sence": SenceVictoryDaMo, "path": SenceFlagVictoryDaMo},
    {"sence": SenceTanSuoFuBenHomePage, "path": SenceTanSuoFuBenHomePagePic},
    {"sence": SenceBossFight, "path": SenceBossFightPic},
    {"sence": SenceYaoQing, "path": SenceYaoQingPic},

]

# tanSuoZhunBeiPath.png
# 探索的关卡
tanSuoLevel10Path = "prePic/level/level10.png"
tanSuoLevel13Path = "prePic/level/level13.png"
