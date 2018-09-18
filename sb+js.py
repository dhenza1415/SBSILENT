# "utf-8"
#thanks to allfams

from LineAPI.linepy import *
from LineAPI.akad.ttypes import Message
from LineAPI.akad.ttypes import ContentType as Type
from LineAPI.akad.ttypes import ChatRoomAnnouncementContents
from LineAPI.akad.ttypes import ChatRoomAnnouncement
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, multiprocessing, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib3, urllib.parse, ffmpy, html5lib, wikipedia, atexit, timeit, pafy, youtube_dl, traceback
from gtts import gTTS
from googletrans import Translator

cl = LINE("ExRl4m4WGW1xbj12hT5b.SCwNhYE4y4LUNus/QfFtwW.rA4h9CTREToJsfdbeEAbirT88JGabSjAnatJAAkZNZc=")
cl.log("Auth Token : " + str(cl.authToken))
cl.log("Timeline Token : " + str(cl.tl.channelAccessToken))

ka = LINE("ExPx0AUHSaIP2fEcWHq4.XuQrezi1qIyJlRlvV0wxra.bTo9fBsgruAKuVdFvIp+TuYTat0xZ/oRioYHz+hqmzA=")
ka.log("Auth Token : " + str(ka.authToken))
ka.log("Timeline Token : " + str(ka.tl.channelAccessToken))

oepoll = OEPoll(cl)
call = cl
creator = ["ub1c5a71f27b863896e9d44bea857d35b"]
owner = ["ub1c5a71f27b863896e9d44bea857d35b"]
admin = ["ub1c5a71f27b863896e9d44bea857d35b"]
staff = ["ub1c5a71f27b863896e9d44bea857d35b"]
mid = cl.getProfile().mid
Amid = ka.getProfile().mid
Bots = [Amid,mid]
Saints = admin + owner + staff
Team = creator + owner + admin + staff + Bots
Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)

protectcancel = []
welcome = []

responsename = cl.getProfile().displayName

settings = {
    "Picture":False,
    "group":{},
    "groupPicture":False,
    "changePicture":False,
    "autoJoinTicket":False,
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.200.32.99 Safari/537.36"
    ]
}

wait = {
    "limit": 2,
    "RAlimit": 2,
    "owner":{},
    "admin":{},
    "addadmin":False,
    "delladmin":False,
    "staff":{},
    "addstaff":False,
    "dellstaff":False,
    "bots":{},
    "addbots":False,
    "dellbots":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":True,
    "contact":False,
    'autoJoin':True,
    'autoAdd':True,
    'autoCancel':{"on":True, "members":1},
    'autoLeave':False,
    'autoLeave1':False,
    "detectMention":False,
    "Mentionkick":False,
    "welcomeOn":False,
    "sticker":False,
    "selfbot":True,
    "mention":"Jones Kerjaannya Tkg Ngintip",
    "Respontag":"EH KANG COLI TAG MULU",
    "welcome":"Wellcome to my Fams",
    "comment":"Auto like By S̶̭̗̞̙̿͑̽̆̃̒į̷̙̝̦̤̜̗́̉ͅl̸̛͓͋͋͆̍ę̶͇̮̦̣̖̙̘̪̉n̸͍̦͉̖̟͚̗̣̍̓̽̅̚ť̴̙͋ ̷̨̳̠͎̮̘͇̀̅̀͒̈́͊̕͝T̸̡̯̗̩̺͉̑́͛̌̒ͅé̶̡̱̯̮̯̊̏́̀̃͜a̴̭͓̫͚̐́̂̍̂̊̋̚m̸̨̨̹͎͍̳̥͆̓͗̿͐͗͑̿̓͠ ̴̠͐̂B̷̛̳͎̫̻̫̯̣͓̲͋̀͋̋͊̈͗͑o̵̲̾̈́͒͗t̴̢͍̫̰̠̞͖͍̬̑̊̽͒́̈́͗ͅ",
    "message":"Thanks for add me..\n\nOpen Order Selfbot Protect dan bot Protect S̶̭̗̞̙̿͑̽̆̃̒į̷̙̝̦̤̜̗́̉ͅl̸̛͓͋͋͆̍ę̶͇̮̦̣̖̙̘̪̉n̸͍̦͉̖̟͚̗̣̍̓̽̅̚ť̴̙͋ ̷̨̳̠͎̮̘͇̀̅̀͒̈́͊̕͝T̸̡̯̗̩̺͉̑́͛̌̒ͅé̶̡̱̯̮̯̊̏́̀̃͜a̴̭͓̫͚̐́̂̍̂̊̋̚m̸̨̨̹͎͍̳̥͆̓͗̿͐͗͑̿̓͠ ̴̠͐̂B̷̛̳͎̫̻̫̯̣͓̲͋̀͋̋͊̈͗͑o̵̲̾̈́͒͗t̴̢͍̫̰̠̞͖͍̬̑̊̽͒́̈́͗ͅ"
}

protect = {
    "pqr":[],
    "pinv":[],
    "proall":[],
    "antijs":[],
    "protect":[]
}

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

mulai = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def restart_program(): 
    python = sys.executable
    os.execl(python, python, * sys.argv)

def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "Mention User「{}」\n\n  [ Mention ]\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "Sider User「{}」\nHaii ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "Member Masuk「{}」\nHaii  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\nNama grup : "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = cl.getAllContactIds()
        gid = cl.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"\nJam : "+datetime.strftime(timeNow,'%H:%M:%S')+" Wib\nGroup : "+str(len(gid))+"\nTeman : "+str(len(teman))+"\nxpired : In "+hari+"\nVersion : Sempak Bot\nTanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\nRuntime : \n • "+bot
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention1(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd

def help():
    num = 1
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "┌──S̶̭̗̞̙̿͑̽̆̃̒į̷̙̝̦̤̜̗́̉ͅl̸̛͓͋͋͆̍ę̶͇̮̦̣̖̙̘̪̉n̸͍̦͉̖̟͚̗̣̍̓̽̅̚ť̴̙͋ ̷̨̳̠͎̮̘͇̀̅̀͒̈́͊̕͝T̸̡̯̗̩̺͉̑́͛̌̒ͅé̶̡̱̯̮̯̊̏́̀̃͜a̴̭͓̫͚̐́̂̍̂̊̋̚m̸̨̨̹͎͍̳̥͆̓͗̿͐͗͑̿̓͠ ̴̠͐̂B̷̛̳͎̫̻̫̯̣͓̲͋̀͋̋͊̈͗͑o̵̲̾̈́͒͗t̴̢͍̫̰̠̞͖͍̬̑̊̽͒́̈́͗ͅ───\n"
    helpMessage += "│ Sb Admin and staff \n"
    helpMessage += "├───────────────\n"
    helpMessage += "│%i. " % num + key + "Me\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "get mid @\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "Whois @\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "Mybot\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "Settings\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "About\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "Abort\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "Rtime\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "Creator\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "Sp\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "@Bye\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "Leave「Namagrup」\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "Ginfo\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "Open\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "Close\n"
    num = (num+1)
    helpMessage += "│%i ." % num + key + "Url grup\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "Glist\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "Stafflist\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "Botlist\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "Infogrup「angka」\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "Infomem「angka」\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "Rchat\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "Sider on/off\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "Upfoto\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "Upgrup\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "Bcast:「Text」\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "Set sname\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "Sname\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "Reset sname\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "Musik Judul lagu\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "Ytmp3: Judul lagu\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "Ytmp4: Judul Video\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "Ssider: text\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "Spesan: text\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "Swelcome: text\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "Srepson: text\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "Ceksider/off\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "Cekpesan/off\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "Cekrespon\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "Cekwelcome\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "Sticker「on/off\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "Respon「on/off」\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "Welcome「on/off」\n"
    num = (num+1)
    helpMessage += "├───────────────\n"
    helpMessage += "│ TEAM BOT PROTECT \n"
    helpMessage += "├───────────────\n"
    helpMessage += "│              S̶̭̗̞̙̿͑̽̆̃̒į̷̙̝̦̤̜̗́̉ͅl̸̛͓͋͋͆̍ę̶͇̮̦̣̖̙̘̪̉n̸͍̦͉̖̟͚̗̣̍̓̽̅̚ť̴̙͋ ̷̨̳̠͎̮̘͇̀̅̀͒̈́͊̕͝T̸̡̯̗̩̺͉̑́͛̌̒ͅé̶̡̱̯̮̯̊̏́̀̃͜a̴̭͓̫͚̐́̂̍̂̊̋̚m̸̨̨̹͎͍̳̥͆̓͗̿͐͗͑̿̓͠ ̴̠͐̂B̷̛̳͎̫̻̫̯̣͓̲͋̀͋̋͊̈͗͑o̵̲̾̈́͒͗t̴̢͍̫̰̠̞͖͍̬̑̊̽͒́̈́͗ͅ \n"
    helpMessage += "└───────────────"
    return helpMessage

def helpbot():
    num = 1
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage2 = "┌───────────────\n"
    helpMessage2 += "│ Sb Owner and admin  \n"
    helpMessage2 += "├───────────────\n"
    helpMessage2 += "│%i. " % num + key + "Adminexpl:on\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "Admin:on @\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "Admin:on\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "Adminexpl:on @\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "Owner:on\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "Staff:on\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "Staff:on @\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "Staffexpl:on\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "Staffexpl:on @\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "Bot:on\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "Bot:on @\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "Botexpl:on\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "Botexpl:on @\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "Ban:on @\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "Ban:on\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "Unban:on @\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "Unban:on\n"
    num = (num+1)
    helpMessage2 += "│%i ." % num + key + "Talkban:on @\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "Talkban:on\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "Untalkban:on @\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "Untalkban:on\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "Talkbanlist\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "Kick:on @\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "Banlist\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "Clearban\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "Allpro on/off\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "Denyurl on/off\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "Protect on/off\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "Proall on/off\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "Denyinvite on/off\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "Procancel on/off\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "Js on/off\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "Kicker\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "Autojoin on/off\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "Jointicket on/off\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "Autoadd on/off\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "leave on/off\n"
    num = (num+1)
    helpMessage2 += "├───────────────\n"
    helpMessage2 += "│ TEAM BOT PROTECT \n"
    helpMessage2 += "├───────────────\n"
    helpMessage2 += "│          S̶̭̗̞̙̿͑̽̆̃̒į̷̙̝̦̤̜̗́̉ͅl̸̛͓͋͋͆̍ę̶͇̮̦̣̖̙̘̪̉n̸͍̦͉̖̟͚̗̣̍̓̽̅̚ť̴̙͋ ̷̨̳̠͎̮̘͇̀̅̀͒̈́͊̕͝T̸̡̯̗̩̺͉̑́͛̌̒ͅé̶̡̱̯̮̯̊̏́̀̃͜a̴̭͓̫͚̐́̂̍̂̊̋̚m̸̨̨̹͎͍̳̥͆̓͗̿͐͗͑̿̓͠ ̴̠͐̂B̷̛̳͎̫̻̫̯̣͓̲͋̀͋̋͊̈͗͑o̵̲̾̈́͒͗t̴̢͍̫̰̠̞͖͍̬̑̊̽͒́̈́͗ͅ \n"
    helpMessage2 += "└───────────────"
    return helpMessage2

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        
        if op.type == 11:
            if op.param1 in protect["pqr"]:
                if op.param2 in Bots:
                    X = cl.getGroup(op.param1)
                    if X.preventedJoinByTicket == False:
                        X.preventedJoinByTicket = True
                        cl.updateGroup(X)
                else:
                    X = cl.getGroup(op.param1)
                    if X.preventedJoinByTicket == False:
                        X.preventedJoinByTicket = True
                        cl.updateGroup(X)
                        if op.param2 in Bots:
                            pass
                        elif op.param2 in owner:
                            pass
                        elif op.param2 in admin:
                            pass
                        elif op.param2 in staff:
                            pass
                        elif op.param2 in Bots:
                            pass
                        else:
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            wait["blacklist"][op.param2] = True
#====================================================================== PROTECTUPDATEGROUP
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in admin and op.param2 not in owner and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"See you next time... 🙏\n Group " +str(ginfo.name))
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Hai.." + str(ginfo.name))

        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)

                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=[str for str in InviterX if str == tag]
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
#____________________________________________________________________
            if op.param1 in protect['pinv']:
                if op.param2 in Bots:
                    pass
                elif op.param2 in Bots:
                    pass
                elif op.param2 in owner:
                    pass
                elif op.param2 in admin:
                    pass
                elif op.param2 in staff:
                    pass
                else:
                    inv1 = op.param3.replace('\x1e',',')
                    inv2 = inv1.split(',')
                    for _mid in inv2:
                        cl.cancelGroupInvitation(op.param1,[_mid])
                    if op.param2 in Bots:
                        pass
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        wait["blacklist"][op.param2] = True
#____________________________________________________________________
        if op.type == 13:
            if op.param2 in wait["blacklist"]:
                if op.param2 in Bots:
                    pass
                elif staff in wait["blacklist"]:
                    pass
                elif admin in wait["blacklist"]:
                    pass
                elif owner in wait["blacklist"]:
                    pass
                elif Bots in wait["blacklist"]:
                    pass
                else:
                    pass
                    cl.cancelGroupInvitation(op.param1,[op.param2])
                    try:
                        cl.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        pass
#____________________________________________________________________
        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                welcomeMembers(op.param1, [op.param2])
                cl.sendImageWithURL(op.param1, image)

        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                if op.param2 in Bots:
                    pass
                elif staff in wait["blacklist"]:
                    pass
                elif admin in wait["blacklist"]:
                    pass
                elif owner in wait["blacklist"]:
                    pass
                elif Bots in wait["blacklist"]:
                    pass
                else:
                    pass
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
#____________________________________________________________________
        if op.type == 19:
            if op.param2 in wait["blacklist"]:
                if op.param2 in Bots:
                    pass
                elif staff in wait["blacklist"]:
                    pass
                elif admin in wait["blacklist"]:
                    pass
                elif owner in wait["blacklist"]:
                    pass
                elif Bots in wait["blacklist"]:
                    pass
                else:
                    pass
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
#____________________________________________________________________
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        cl.sendMessage(op.param1, wait["message"])

        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param3 in Bots:
                    if op.param2 not in Bots and op.param2 not in Team:
                        wait["blacklist"][op.param2] = True
                        try:
                            if op.param3 not in wait["blacklist"]:
                                cl.findAndAddContactsByMid(op.param1,[Amid])
                                cl.kickoutFromGroup(op.param1,[op.param2])
                                cl.inviteIntoGroup(op.param1,[Amid])
                        except:
                            pass

        if op.type == 32:
            if op.param3 in Amid:
                if op.param2 not in Bots or op.param2 not in owner or op.param2 not in admin or op.param2 not in staff:
                     wait["blacklist"][op.param2] = True
                     try:
                         cl.inviteIntoGroup(op.param1,[op.param3])
                         cl.kickoutFromGroup(op.param1,[op.param2])
                         cl.sendMessage(op.param1, "itu ProtectJs Bosskuh Jgn di Cancel")
                     except:
                         pass
#____________________________________________________________________
        if op.type == 19:
            if op.param1 in protect["proall"]:
                if op.param2 in Bots:
                    pass
                elif op.param2 in Bots:
                    pass
                elif op.param2 in owner:
                    pass
                elif op.param2 in admin:
                    pass
                elif op.param2 in staff:
                    pass
                else:
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    if op.param3 in wait["blacklist"]:
                        pass
                    else:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                        wait["blacklist"][op.param2] = True

            if op.param1 in protect["protect"]:
                if op.param2 in Bots:
                    pass
                elif op.param2 in owner:
                    pass
                elif op.param2 in admin:
                    pass
                elif op.param2 in staff:
                    pass
                elif op.param2 in Bots:
                    pass
                else:
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True

            if op.param1 in protect["antijs"]:
                if op.param3 in mid:
                    if op.param2 in Bots:
                        pass
                    elif op.param2 in Bots:
                        pass
                    elif op.param2 in owner:
                        pass
                    elif op.param2 in admin:
                        pass
                    elif op.param2 in staff:
                        pass
                    else:
                        ka.acceptGroupInvitation(op.param1)
                        G = ka.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ka.updateGroup(G)
                        Ticket = ka.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = True
                        wait["blacklist"][op.param2] = True

            try:
                if op.param3 in owner:
                    if op.param2 in Bots:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in owner:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in admin:
                        pass
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                if op.param3 in admin:
                    if op.param2 in Bots:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in owner:
                        pass
                    elif op.param2 in admin:
                        pass
                    elif op.param2 in Bots:
                        pass
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                if op.param3 in staff:
                    if op.param2 in Bots:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in staff:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in owner:
                        pass
                    elif op.param2 in admin:
                        pass
                    elif op.param2 in staff:
                        pass
                    elif op.param2 in Bots:
                        pass
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                if op.param3 in mid:
                    if op.param2 in Bots:
                    	pass
                    elif op.param2 in owner:
                        pass
                    elif op.param2 in admin:
                        pass
                    elif op.param2 in staff:
                        pass
                    elif op.param2 in Bots:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                        ka.kickoutFromGroup(op.param1,[op.param2])
                        ka.inviteIntoGroup(op.param1,[op.param3])
                        cl.acceptGroupInvitation(op.param1)
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                if op.param3 in Amid:
                    if op.param2 in Bots:
                        pass
                    elif op.param2 in owner:
                        pass
                    elif op.param2 in admin:
                        pass
                    elif op.param2 in staff:
                        pass
                    elif op.param2 in Bots:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.inviteIntoGroup(op.param1,[op.param3])
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
            except:
                pass

        if op.type == 55:
            try:
                if op.param1 in Setmain["RAreadPoint"]:
                   if op.param2 in Setmain["RAreadMember"][op.param1]:
                       pass
                   else:
                       Setmain["RAreadMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                if op.param2 in Bots:
                    pass
                elif staff in wait["blacklist"]:
                    pass
                elif admin in wait["blacklist"]:
                    pass
                elif owner in wait["blacklist"]:
                    pass
                elif Bots in wait["blacklist"]:
                    pass
                else:
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass

            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = cl.getContact(op.param2)
                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        cl.sendImageWithURL(op.param1, image)
                        cl.sendMessage(op.param1, None, contentMetadata={"STKID":"5510","STKPKGID":"608","STKVER":"16"}, contentType=7)

        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          cl.kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              cl.kickoutFromGroup(msg.to, [msg._from])
                          except:
                              pass
               if 'MENTION' in msg.contentMetadata.keys() != None:
                if msg._from not in Bots:
                 if wait["detectMention"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           saints = cl.getContact(msg._from)
                           sendMention1(msg.to, saints.mid, "", wait["Respontag"])
                           cl.sendMessage(msg.to, None, contentMetadata={"STKID":"52002769","STKPKGID":"11537","STKVER":"1"}, contentType=7)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                if msg._from not in Bots:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           cl.mentiontag(msg.to,[msg._from])
                           cl.sendMessage(msg.to, "No tag me....")
                           cl.kickoutFromGroup(msg.to, [msg._from])
                           break
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"Cek ID Sticker\n\nSTKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"Nama : " + msg.contentMetadata["displayName"] + "\nMID : " + msg.contentMetadata["mid"] + "\nStatus Msg : " + contact.statusMessage + "\nPicture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)

        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"Nama : " + msg.contentMetadata["displayName"] + "\nMID : " + msg.contentMetadata["mid"] + "\nStatus Msg : " + contact.statusMessage + "\nPicture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
#ADD Bots
               if msg.contentType == 13:
                 if msg._from in owner:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        cl.sendMessage(msg.to,"Already in bot")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        cl.sendMessage(msg.to,"Succes add bot")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Succes delete bot")
                    else:
                        wait["dellbots"] = True
                        cl.sendMessage(msg.to,"Nothing in bot")
#ADD STAFF
                 if msg._from in owner or msg._from in admin:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        cl.sendMessage(msg.to,"Already in stafflist")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        cl.sendMessage(msg.to,"Succes add to staff")
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Succes expel to staff")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        cl.sendMessage(msg.to,"Nothing in staff")
#ADD ADMIN
                 if msg._from in owner:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        cl.sendMessage(msg.to,"Already in Admin")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        cl.sendMessage(msg.to,"Succes Add to Admin")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Succes to expel admin")
                    else:
                        wait["delladmin"] = True
                        cl.sendMessage(msg.to,"Contact itu bukan admin")
#ADD BLACKLIST
                 if msg._from in owner:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendMessage(msg.to,"Already in blacklist")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        cl.sendMessage(msg.to,"Succes add to blacklist")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"Succes delete blacklist")
                    else:
                        wait["dblacklist"] = True
                        cl.sendMessage(msg.to,"Nothing in blacklist")
#TALKBAN
                 if msg._from in owner:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        cl.sendMessage(msg.to,"Already in Talkban")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        cl.sendMessage(msg.to,"Succes add to Talkban")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"Succes delete Talkban")
                    else:
                        wait["Talkdblacklist"] = True
                        cl.sendMessage(msg.to,"Nothing in Talkban")
#UPDATE FOTO
               if msg.contentType == 1:
                 if msg._from in owner:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = cl.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            cl.sendMessage(msg.to, "Succes add picture")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False

               if msg.toType == 2:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   if settings["groupPicture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     cl.updateGroupPicture(msg.to, path)
                     cl.sendMessage(msg.to, "Succes change pict group")

               if msg.contentType == 1:
                   if msg._from in owner:
                       if mid in Setmain["RAfoto"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][mid]
                            cl.updateProfilePicture(path)
                            cl.sendMessage(msg.to,"Succes change pict")

               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        cl.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "help":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               helpMessage = help()
                               cl.sendMessage(msg.to, str(helpMessage))
                                                                                       
                        if cmd == "chatbot on":
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                wait["selfbot"] = True
                                cl.sendMessage(msg.to, "Chatbot has been enable")
                                
                        elif cmd == "chatbot off":
                            if msg._from in owner or msg._from in admin:
                                wait["selfbot"] = False
                                cl.sendMessage(msg.to, "Chatbot has been disable")
                                            
                        elif cmd == "help2":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               helpMessage2 = helpbot()
                               cl.sendMessage(msg.to, str(helpMessage2))

                        elif cmd == "settings":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "     Settings Bots     \n\n"
                                if wait["sticker"] == True: md+="⚫Sticker\n"
                                else: md+="⚪ Sticker\n"
                                if wait["contact"] == True: md+="⚫Contact\n"
                                else: md+="⚪ Contact\n"
                                if wait["detectMention"] == True: md+="⚫ Respon\n"
                                else: md+="⚪ Respon\n"
                                if wait["autoJoin"] == True: md+="⚫ Autojoin\n"
                                else: md+="⚪ Autojoin\n"
                                if settings["autoJoinTicket"] == True: md+="⚫ Jointicket\n"
                                else: md+="⚪ Jointicket\n"
                                if wait["autoAdd"] == True: md+="⚫ Autoadd\n"
                                else: md+="⚪ Autoadd\n"
                                if msg.to in welcome: md+="⚫ Welcome\n"
                                else: md+="⚪ Welcome\n"
                                if wait["autoLeave"] == True: md+="⚫ Autoleave\n"
                                else: md+="⚪ Autoleave\n"
                                if msg.to in protect["pqr"]: md+="⚫ Denyurl\n"
                                else: md+="⚪ Denyurl\n"
                                if msg.to in protect["proall"]: md+="⚫ Proall\n"
                                else: md+="⚪ Proall\n"
                                if msg.to in protect["protect"]: md+="⚫ Protect\n"
                                else: md+="⚪ Protect\n"
                                if msg.to in protect["pinv"]: md+="⚫ Denyinvite\n"
                                else: md+="⚪ Denyinvite\n"
                                if msg.to in protect["antijs"]: md+="⚫ Js\n"
                                else: md+="⚪ Js\n"
                                if msg.to in protectcancel: md+="⚫ Procancel\n"
                                else: md+="⚪ Procancel\n"
                                cl.sendMessage(msg.to, md+"\nDate : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nTime  "+ datetime.strftime(timeNow,'%H:%M:%S')+" ")
                                cl.sendMessage(msg.to, None, contentMetadata={"STKID":"33913762","STKPKGID":"10910","STKVER":"2"}, contentType=7)

                        elif cmd == "creator" or text.lower() == 'creator':
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                cl.sendText(msg.to,"Creator Kami")
                                ma = ""
                                for i in creator:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "about" or cmd == "informasi":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               sendMention(msg.to, sender, "●Bots Protect\n\n")
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)

                        elif cmd == "me" or text.lower() == 'me':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': msg._from}
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': msg._from}, contentType=13)
                               path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                               image = 'http://dl.profile.line.naver.jp'+path
                               cl.sendImageWithURL(msg.to, image)
                               cl.sendMessage(msg.to, None, contentMetadata={"STKID":"33913762","STKPKGID":"10910","STKVER":"2"}, contentType=7)
                               cl.sendMessage(msg.to, None, contentMetadata={"STKID":"15126","STKPKGID":"956","STKVER":"12"}, contentType=7)

                        elif text.lower() == "mymid":
                               cl.sendMessage(msg.to, msg._from)

                        elif ("Get id " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("Whois " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMid : " +key1+"\nStatus Msg"+str(mi.statusMessage))
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(cl.getContact(key1)):
                                   cl.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   cl.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif cmd == "mybot":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)
                               msg.contentMetadata = {'mid': Amid}
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': Amid}, contentType=13)

                        elif cmd == "reject":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                              ginvited = cl.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      cl.rejectGroupInvitation(gid)
                                  cl.sendMessage(to, "Succes reject {} ".format(str(len(ginvited))))
                              else:
                                  cl.sendMessage(to, "Nothing")

                        elif text.lower() == "rchat":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               try:
                                   cl.removeAllMessages(op.param2)
                                   ka.removeAllMessages(op.param2)
                                   cl.sendMessage(msg.to,"Done")
                                   ka.sendMessage(msg.to,"Done")
                               except:
                                   pass

                        elif cmd.startswith("bcast: "):
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = cl.getGroupIdsJoined()
                               for group in saya:
                                   cl.sendMessage(group,"●Broadcast \n\n" + str(pesan))

                        elif text.lower() == "sname":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               cl.sendMessage(msg.to, "● Sname \n\n" + str(Setmain["keyCommand"]) + " ")
                               
                        elif cmd.startswith("setsname "):
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendMessage(msg.to, "Succes change Sname")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   cl.sendMessage(msg.to, "● Sname change \n\nSname succes change to {}".format(str(key).lower()))

                        elif text.lower() == "reset sname":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               Setmain["keyCommand"] = ""
                               cl.sendMessage(msg.to, "Succes Reset Sname ")

                        elif cmd == "reboot":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               cl.sendMessage(msg.to, "please wait")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                               cl.sendMessage(msg.to, "Done...")
                            
                        elif cmd == "rtime":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "Active " +waktu(eltime)
                               cl.sendMessage(msg.to,bot)
                            
                        elif cmd == "ginfo":
                          if msg._from in owner or msg._from in admin or msg._from in staff:
                            try:
                                G = cl.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                cl.sendMessage(msg.to, "Group Info\n\nNama Group : {}".format(G.name)+ "\nID Group : {}".format(G.id)+ "\nPembuat : {}".format(G.creator.displayName)+ "\nWaktu Dibuat : {}".format(str(timeCreated))+ "\nJumlah Member : {}".format(str(len(G.members)))+ "\nJumlah Pending : {}".format(gPending)+ "\nGroup Qr : {}".format(gQr)+ "\nGroup Ticket : {}".format(gTicket))
                                cl.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                cl.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                cl.sendMessage(msg.to, str(e))

                        elif cmd.startswith("infogrup "):
                          if msg._from in owner or msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "Team Sempak Grup Info\n"
                                ret_ += "\nNama Group : {}".format(G.name)
                                ret_ += "\nID Group : {}".format(G.id)
                                ret_ += "\nPembuat : {}".format(gCreator)
                                ret_ += "\nWaktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\nJumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\nJumlah Pending : {}".format(gPending)
                                ret_ += "\nGroup Qr : {}".format(gQr)
                                ret_ += "\nGroup Ticket : {}".format(gTicket)
                                ret_ += ""
                                cl.sendMessage(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("infomem "):
                          if msg._from in owner or msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " ""+ str(no) + ". " + mem.displayName
                                cl.sendMessage(to,"Group Name : " + str(G.name) + " \n\nMember List \n" + ret_ + "\n\nTotal %i Members" % len(G.members))
                            except: 
                                pass

                        elif cmd.startswith("leave "):
                          if msg._from in owner or msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            for i in group:
                                ginfo = cl.getGroup(i)
                                if ginfo == group:
                                    cl.leaveGroup(i)
                                    cl.sendMessage(msg.to,"Leave in groups " +str(ginfo.name))

                        elif cmd == "flist":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               ma = ""
                               a = 0
                               gid = cl.getAllContactIds()
                               for i in gid:
                                   G = cl.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "" + str(a) + ". " +G.displayName+ "\n"
                               cl.sendMessage(msg.to,"●FRIEND LIST\n\n"+ma+"\nTotal"+str(len(gid))+"Friends")

                        elif cmd == "glist":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               ma = ""
                               a = 0
                               gid = cl.getGroupIdsJoined()
                               for i in gid:
                                   G = cl.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "" + str(a) + ". " +G.name+ "\n"
                               cl.sendMessage(msg.to,"●GROUP LIST\n\n"+ma+"\nTotal"+str(len(gid))+" Groups")

                        elif cmd == "curl":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "Url Closed")

                        elif cmd == "ourl":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                if msg.toType == 2:
                                   x = cl.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      cl.updateGroup(x)
                                   gurl = cl.reissueGroupTicket(msg.to)
                                   cl.sendMessage(msg.to, "Nama : "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)

#===========BOT UPDATE============#
                        elif cmd == "upgrup":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                cl.sendMessage(msg.to,"Send Picture")

                        elif cmd == "upbot":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                settings["changePicture"] = True
                                cl.sendMessage(msg.to,"Send Picture")
                                
                        elif cmd == "upfoto":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                Setmain["RAfoto"][mid] = True
                                cl.sendMessage(msg.to,"Send picture")

#===========BOT UPDATE============#
                        elif cmd == "mention" or text.lower() == '😆':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               group = cl.getGroup(msg.to)
                               nama = [contact.mid for contact in group.members]
                               nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                               if jml <= 20:
                                   mentionMembers(msg.to, nama)
                               if jml > 20 and jml < 20:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, len(nama)-1):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                               if jml > 20 and jml < 40:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, len(nama)-1):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                               if jml > 40 and jml < 60:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, len(nama)-1):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                               if jml > 60 and jml < 80:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, len(nama)-1):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                               if jml > 80 and jml < 100:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 100):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)

                        elif cmd == "botlist":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"●Botlist●\n\n\n"+ma+"\n%s Bots" %(str(len(Bots))))

                        elif cmd == "kicker":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    ginfo = cl.getGroup(msg.to)
                                    cl.inviteIntoGroup(msg.to, [Amid])
                                    cl.sendMessage(msg.to,"Done 😚😚 "+str(ginfo.name)+" siap backup")
                                except:
                                    pass

                        elif cmd == "stafflist":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"●Adminlist●\n\n●Owner\n"+ma+"\n●Admin\n"+mb+"\n●Staff:\n"+mc+"\n%s Adminlist" %(str(len(owner)+len(admin)+len(staff))))

                        elif cmd == "protectlist":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                mf= ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                f = 0
                                gid = protect["pqr"]
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getGroup(group).name + "\n"
                                gid = protect["protect"]
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getGroup(group).name + "\n"
                                gid = protect["proall"]
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +cl.getGroup(group).name + "\n"
                                gid = protect["pinv"]
                                for group in gid:
                               	    f = f + 1
                                    end = '\n'
                                    mf += str(f) + ". " +cl.getGroup(group).name + "\n"
                                cl.sendMessage(msg.to,"Settings Protection\n\n\nDenyurl :\n"+ma+"\nProall:\n"+mb+"\nProtect:\n"+md+"\nProtect Cancel:\n"+mc+"\nDenyinvite:\n"+mf+"\nProtectlist %s Grup protect" %(str(len(protect["pqr"])+len(protect["protect"])+len(protect["proall"])+len(protectcancel)+len(protect["pinv"]))))

                        elif cmd == "rname":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                cl.sendMessage(msg.to,responsename)

                        elif cmd == "@bye":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ka.sendMessage(msg.to, "See you guys "+str(G.name))
                                ka.leaveGroup(msg.to)
                                
                        elif cmd == ".bye":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                G = cl.getGroup(msg.to)
                                cl.sendMessage(msg.to, "See you next again "+str(G.name))
                                cl.leaveGroup(msg.to)

                        elif cmd.startswith("leave "):
                            if msg._from in admin or msg._from in owner:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    h = cl.getGroup(i).name
                                    if h == ng:
                                        cl.sendMessage(i, " Silahkan invite Ownernya ")
                                        cl.leaveGroup(i)
                                        cl.sendMessage(to,"Succes leave group " +h)

                        elif cmd == "timerespon":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = cl.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = cl.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                cl.sendMessage(msg.to, "●Time Respon●\n\n ●Get Profile\n   %.10f\n ●Get Contact\n   %.10f\n ●Get Group\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               start = time.time()
                               cl.sendMessage(msg.to, "Taken..")
                               elapsed_time = time.time() - start
                               cl.sendMessage(msg.to, "Time:\n{}".format(str(elapsed_time)))

                        elif cmd == "lurk:on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['RAreadPoint'][msg.to] = msg_id
                                 Setmain['RAreadMember'][msg.to] = {}
                                 cl.sendMessage(msg.to, "Lurking berhasil diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurk:off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['RAreadPoint'][msg.to]
                                 del Setmain['RAreadMember'][msg.to]
                                 cl.sendMessage(msg.to, "Lurking berhasil dinoaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurkers":
                          if msg._from in admin:
                            if msg.to in Setmain['RAreadPoint']:
                                if Setmain['RAreadMember'][msg.to] != {}:
                                    aa = []
                                    for x in Setmain['RAreadMember'][msg.to]:
                                        aa.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ Result {} member ]    \n\n  [ Lurkers ]\n1. ".format(str(len(aa)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in aa:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(aa):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(cl.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        cl.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['RAreadPoint'][msg.to]
                                        del Setmain['RAreadMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['RAreadPoint'][msg.to] = msg.id
                                    Setmain['RAreadMember'][msg.to] = {}
                                else:
                                    cl.sendMessage(msg.to, "User kosong...")
                            else:
                                cl.sendMessage(msg.to, "Ketik lurking on dulu")

                        elif cmd == "sider on":
                          if wait["selfbot"] == True:
                           if msg._from in owner or msg._from in admin or msg._from in staff:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cl.sendMessage(msg.to, "Cek sider diaktifkan\n\nDate "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nTime  "+ datetime.strftime(timeNow,'%H:%M:%S')+" ")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "sider off":
                          if wait["selfbot"] == True:
                           if msg._from in owner or msg._from in admin or msg._from in staff:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  cl.sendMessage(msg.to, "Cek sider dinonaktifkan\n\nDate "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nTime  "+ datetime.strftime(timeNow,'%H:%M:%S')+" ")
                              else:
                                  cl.sendMessage(msg.to, "Sudak tidak aktif")

#===========Hiburan============#
                        elif cmd.startswith("sholat: "):
                          if msg._from in admin:
                             sep = text.split(" ")
                             location = text.replace(sep[0] + " ","")
                             with requests.session() as web:
                                  web.headers["user-agent"] = random.choice(settings["userAgent"])
                                  r = web.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(urllib.parse.quote(location)))
                                  data = r.text
                                  data = json.loads(data)
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  if data[1] != "Subuh : " and data[2] != "Dzuhur : " and data[3] != "Ashar : " and data[4] != "Maghrib : " and data[5] != "Isha : ":
                                         ret_ = "「Jadwal Sholat」"
                                         ret_ += "\nLokasi : " + data[0]
                                         ret_ += "\n" + data[1]
                                         ret_ += "\n" + data[2]
                                         ret_ += "\n" + data[3]
                                         ret_ += "\n" + data[4]
                                         ret_ += "\n" + data[5]
                                         ret_ += "\n\nTanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                         ret_ += "\nJam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                  cl.sendMessage(msg.to, str(ret_))

                        elif cmd.startswith("cuaca: "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            location = text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                if "result" not in data:
                                    ret_ = "「Status Cuaca」"
                                    ret_ += "\nLokasi : " + data[0].replace("Temperatur di kota ","")
                                    ret_ += "\nSuhu : " + data[1].replace("Suhu : ","") + " C"
                                    ret_ += "\nKelembaban : " + data[2].replace("Kelembaban : ","") + " %"
                                    ret_ += "\nTekanan udara : " + data[3].replace("Tekanan udara : ","") + " HPa"
                                    ret_ += "\nKecepatan angin : " + data[4].replace("Kecepatan angin : ","") + " m/s"
                                    ret_ += "\n\nTanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                    ret_ += "\nJam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                cl.sendMessage(msg.to, str(ret_))

                        elif cmd.startswith("lokasi: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            location = msg.text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                if data[0] != "" and data[1] != "" and data[2] != "":
                                    link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                    ret_ = "「Info Lokasi」"
                                    ret_ += "\nLocation : " + data[0]
                                    ret_ += "\nGoogle Maps : " + link
                                else:
                                    ret_ = "[Details Location] Error : Location not found"
                                cl.sendMessage(msg.to,str(ret_))

                        elif cmd.startswith("lirik: "):
                           if msg._from in admin:
                               sep = msg.text.split(" ")
                               search = msg.text.replace(sep[0] + " ","")
                               params = {'songname': search}
                               with requests.session() as web:
                                   web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                   r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?{}".format(urllib.parse.urlencode(params)))
                                   try:
                                      data = json.loads(r.text)
                                      for song in data:
                                          songs = song[5]
                                          lyric = songs.replace('ti:','Title - ')
                                          lyric = lyric.replace('ar:','Artist - ')
                                          lyric = lyric.replace('al:','Album - ')
                                          removeString = "[1234567890.:]"
                                          for char in removeString:
                                              lyric = lyric.replace(char,'')
                                          ret_ = "╔══[ Lyric ]"
                                          ret_ += "\n╠ Nama lagu : {}".format(str(song[0]))
                                          ret_ += "\n╠ Durasi : {}".format(str(song[1]))
                                          ret_ += "\n╠ Link : {}".format(str(song[3]))
                                          ret_ += "\n╚══[ Finish ]\n\nLirik nya :\n{}".format(str(lyric))
                                          cl.sendText(msg.to, str(ret_))
                                   except:
                                       cl.sendMessage(to, "Lirik tidak ditemukan")
                            
                        elif cmd.startswith("musik "):
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               sep = msg.text.split(" ")
                               query = msg.text.replace(sep[0] + " ","")
                               cond = query.split("-")
                               search = str(cond[0])
                               with requests.session() as web:
                                   web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                   result = web.get("http://api.ntcorp.us/joox/search?q={}".format(str(search)))
                                   data = result.text
                                   data = json.loads(data)
                                   if len(cond) == 1:
                                      num = 0
                                      ret_ = "●Pencarian Musik \n"
                                      for music in data["result"]:
                                          num += 1
                                          ret_ += "\n {}. {}".format(str(num), str(music["single"]))
                                      ret_ += "\n\n {} Pencarian".format(str(len(data["result"])))
                                      cl.sendMessage(to, str(ret_))
                                      sendMention(msg.to, msg._from,"","\nJika ingin menggunakan,\nSilahkan gunakan:\n\nMusik penyanyi-angka")
                                   if len(cond) == 2:
                                        num = int(cond[1])
                                        if num <= len(data["result"]):
                                               music = data["result"][num - 1]
                                               with requests.session() as web:
                                                    web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                                    result = web.get("http://api.ntcorp.us/joox/song_info?sid={}".format(str(music["sid"])))
                                                    data = result.text
                                                    data = json.loads(data)
                                                    if data["result"] != []:
                                                         ret_ = "「 Pencarian Musik 」"
                                                         ret_ += "\n• Judul : {}".format(str(data["result"]["song"]))
                                                         ret_ += "\n• Album : {}".format(str(data["result"]["album"]))
                                                         ret_ += "\n• Ukuran : {}".format(str(data["result"]["size"]))
                                                         ret_ += " \n• Link Musik : {}".format(str(data["result"]["mp3"]))
                                                         ret_ += "\n「 Tunggu Musiknya Keluar 」"
                                                         cl.sendImageWithURL(to, str(data["result"]["img"]))
                                                         cl.sendMessage(to, str(ret_))
                                                         cl.sendAudioWithURL(to, str(data["result"]["mp3"][0]))

                        elif cmd.startswith("gimage: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            search = msg.text.replace(sep[0] + " ","")
                            url = "https://api.xeonwz.ga/api/image/google?q={}".format(urllib.parse.quote(search))
                            with requests.session() as web:
                                web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                r = web.get(url)
                                data = r.text
                                data = json.loads(data)
                                if data["data"] != []:
                                    start = timeit.timeit()
                                    items = data["data"]
                                    path = random.choice(items)
                                    a = items.index(path)
                                    b = len(items)
                                    cl.sendMessage(msg.to,"「Google Image」\nType : Search Image\nTime taken : %seconds" % (start))
                                    cl.sendImageWithURL(msg.to, str(path))

                        elif cmd.startswith("ytmp4: "):
                          if msg._from in owner or msg._from in admin or msg._from in staff:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\nAuthor : ' + str(vid.author)
                                    durasi = '\nDuration : ' + str(vid.duration)
                                    suka = '\nLikes : ' + str(vid.likes)
                                    rating = '\nRating : ' + str(vid.rating)
                                    deskripsi = '\nDeskripsi : ' + str(vid.description)
                                cl.sendVideoWithURL(msg.to, me)
                                cl.sendMessage(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                cl.sendMessage(msg.to,str(e))

                        elif cmd.startswith("ytmp3: "):
                          if msg._from in owner or msg._from in admin or msg._from in staff:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                bestaudio = vid.getbestaudio()
                                bestaudio.bitrate
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    shi = bestaudio.url
                                    me = best.url
                                    vin = s.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\nAuthor : ' + str(vid.author)
                                    durasi = '\nDuration : ' + str(vid.duration)
                                    suka = '\nLikes : ' + str(vid.likes)
                                    rating = '\nRating : ' + str(vid.rating)
                                    deskripsi = '\nDeskripsi : ' + str(vid.description)
                                cl.sendImageWithURL(msg.to, me)
                                cl.sendAudioWithURL(msg.to, shi)
                                cl.sendMessage(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                cl.sendMessage(msg.to,str(e))

                        elif cmd.startswith("mp3 "):
                          if msg._from in owner or msg._from in admin or msg._from in staff:
                                sep = msg.text.split(" ")
                                search = msg.text.replace(sep[0] + " ","")
                                with requests.session() as web:
                                      web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                      url = web.get("http://rahandiapi.herokuapp.com/youtubeapi/search?key=betakey&q={}".format(urllib.parse.quote(search)))
                                      data = url.text
                                      data = json.loads(data)
                                      if data["result"] != []:
                                          audio = random.choice(data["result"]["audiolist"])
                                          aud = audio["url"]
                                          start = timeit.timeit()
                                          ret = "「 Informasi Mp3 」\n"
                                          ret += "• Judul : {}".format(str(data["result"]["title"]))
                                          ret += "\n• Author : {}".format(str(data["result"]["author"]))
                                          ret += "\n• Durasi : {}".format(str(data["result"]["duration"]))
                                          ret += "\n• Like nya : {}".format(str(data["result"]["likes"]))
                                          ret += "\n• Rating : {}".format(str(data["result"]["rating"]))
                                          ret += "\n• TimeTaken : {}".format(str(start))
                                          ret += "\n• Deskripsi : {}\n「 Waiting Encoding 」".format(str(data["result"]["description"]))
                                          cl.sendMessage(msg.to, str(ret))
                                          cl.sendAudioWithURL(msg.to, str(aud))

                        elif cmd.startswith("profileig: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                instagram = msg.text.replace(sep[0] + " ","")
                                response = requests.get("https://www.instagram.com/"+instagram+"?__a=1")
                                data = response.json()
                                namaIG = str(data['user']['full_name'])
                                bioIG = str(data['user']['biography'])
                                mediaIG = str(data['user']['media']['count'])
                                verifIG = str(data['user']['is_verified'])
                                usernameIG = str(data['user']['username'])
                                followerIG = str(data['user']['followed_by']['count'])
                                profileIG = data['user']['profile_pic_url_hd']
                                privateIG = str(data['user']['is_private'])
                                followIG = str(data['user']['follows']['count'])
                                link = "Link : " + "https://www.instagram.com/" + instagram
                                text = "Name : "+namaIG+"\nUsername : "+usernameIG+"\nBiography : "+bioIG+"\nFollower : "+followerIG+"\nFollowing : "+followIG+"\nPost : "+mediaIG+"\nVerified : "+verifIG+"\nPrivate : "+privateIG+"" "\n" + link
                                cl.sendImageWithURL(msg.to, profileIG)
                                cl.sendMessage(msg.to, str(text))
                            except Exception as e:
                                    cl.sendMessage(msg.to, str(e))

                        elif cmd.startswith("cekdate: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            tanggal = msg.text.replace(sep[0] + " ","")
                            r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                            data=r.text
                            data=json.loads(data)
                            lahir = data["data"]["lahir"]
                            usia = data["data"]["usia"]
                            ultah = data["data"]["ultah"]
                            zodiak = data["data"]["zodiak"]
                            cl.sendMessage(msg.to,"Informasi™\n\n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak)

                        elif cmd.startswith("clone "):
                           if msg._from in admin:
                             if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                for mention in mentionees:
                                    contact = mention["M"]
                                    break
                                try:
                                    cl.cloneContactProfile(contact)
                                    ryan = cl.getContact(contact)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan =  "「 Clone Profile 」\nTarget nya "
                                    ret_ = "Berhasil clone profile target"
                                    ry = str(ryan.displayName)
                                    pesan = ''
                                    pesan2 = pesan+"@x \n"
                                    xlen = str(len(zxc)+len(xpesan))
                                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    text = xpesan + zxc + ret_ + ""
                                    cl.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                except:
                                    cl.sendMessage(msg.to, "Gagal clone profile")
                            
                        elif text.lower() == 'restore':
                           if msg._from in admin:
                              try:
                                  lineProfile.displayName = str(myProfile["displayName"])
                                  lineProfile.statusMessage = str(myProfile["statusMessage"])
                                  lineProfile.pictureStatus = str(myProfile["pictureStatus"])
                                  cl.updateProfileAttribute(8, lineProfile.pictureStatus)
                                  cl.updateProfile(lineProfile)
                                  sendMention(msg.to, sender, "「 Restore Profile 」\nNama ", " \nBerhasil restore profile")
                              except:
                                  cl.sendMessage(msg.to, "Gagal restore profile")

                        elif cmd.startswith("jumlah: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["RAlimit"] = num
                                cl.sendMessage(msg.to,"Spamtag change to " +strnum)

                        elif cmd.startswith("spamcall: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                cl.sendMessage(msg.to,"Total Spamcall Diubah Menjadi " +strnum)

                        elif cmd.startswith("spamtag "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(wait["RAlimit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                cl.sendMessage(msg)
                                            except Exception as e:
                                                cl.sendMessage(msg.to,str(e))
                                    else:
                                        cl.sendMessage(msg.to,"Jumlah melebihi 1000")
                                        
                        elif cmd.startswith("spamtag "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(key1)
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                cl.sendMessage(msg)
                                            except Exception as e:
                                                cl.sendMessage(msg.to,str(e))

                        elif cmd == "spamcall":
                          if wait["selfbot"] == True:
                           if msg._from in owner:
                             if msg.toType == 2:
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                cl.sendMessage(msg.to, "Berhasil mengundang {} undangan Call Grup".format(str(wait["limit"])))
                                call.acquireGroupCallRoute(to)
                                call.inviteIntoGroupCall(to, contactIds=members)
                                        
                        elif cmd == "spamcall":
                          if wait["selfbot"] == True:
                           if msg._from in owner:
                             if msg.toType == 2:
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                cl.sendMessage(msg.to, "Berhasil mengundang {} undangan Call Grup".format(str(wait["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                        call.acquireGroupCallRoute(to)
                                        call.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        cl.sendMessage(msg.to,str(e))
                                else:
                                    cl.sendMessage(msg.to,"Jumlah melebihi batas")

                        elif 'Gift: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)

                        elif 'Spam: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, str(Setmain["RAmessage1"]))

                        elif 'ID line: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              msgs = msg.text.replace('ID line: ','')
                              conn = cl.findContactsByUserid(msgs)
                              if True:
                                  cl.sendMessage(msg.to, "http://line.me/ti/p/~" + msgs)
                                  cl.sendMessage(msg.to, None, contentMetadata={'mid': conn.mid}, contentType=13)

#===========Protection============#
                        elif 'Welcome ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Welcome Msg sudah aktif"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Welcome Msg diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Welcome Msg dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Welcome Msg sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Denyurl ' in msg.text:
                           if msg._from in owner or msg._from in admin:
                              spl = msg.text.replace('Denyurl ','')
                              if spl == 'on':
                                  if msg.to in protect["pqr"]:
                                       msgs = "Denyurl has been active"
                                  else:
                                       protect["pqr"].append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Denyurl active\n\nIn group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "Activated\n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protect["pqr"]:
                                         protect["pqr"].remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Denyurl deactive\n\nIn Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Denyurl has been deactive"
                                    cl.sendMessage(msg.to, "Nonactive\n\n" + msgs)

                        elif 'Protect ' in msg.text:
                           if msg._from in owner or msg._from in admin:
                              spl = msg.text.replace('Protect ','')
                              if spl == 'on':
                                  if msg.to in protect["protect"]:
                                       msgs = "Protect has been active"
                                  else:
                                       protect["protect"].append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect Active\n\nIn group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "Activated\n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protect["protect"]:
                                         protect["protect"].remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect deactive\n\nIn group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect has been disable"
                                    cl.sendMessage(msg.to, "Nonactive\n\n" + msgs)

                        elif 'Proall ' in msg.text:
                           if msg._from in owner or msg._from in admin:
                              spl = msg.text.replace('Proall ','')
                              if spl == 'on':
                                  if msg.to in protect["proall"]:
                                       msgs = "Proall has been active"
                                  else:
                                       protect["proall"].append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect all active\n\nIn group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "Activated \n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protect["proall"]:
                                         protect["proall"].remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect all deactive\n\nIn group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect all has been disable"
                                    cl.sendMessage(msg.to, "Nonactive\n\n" + msgs)

                        elif 'Procancel ' in msg.text:
                           if msg._from in owner or msg._from in admin:
                              spl = msg.text.replace('Procancel ','')
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = "Protect cancel has been active "
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect cancel active\n\nIn group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "Activated\n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect cancel deactive\n\nIn group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect cancel has been disable"
                                    cl.sendMessage(msg.to, "Nonactive\n\n" + msgs)

                        elif 'Denyinvite ' in msg.text:
                           if msg._from in owner or msg._from in admin:
                              spl = msg.text.replace('Denyinvite ','')
                              if spl == 'on':
                                  if msg.to in protect["pinv"]:
                                       msgs = "Denyinvite has been active"
                                  else:
                                       protect["pinv"].append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Denyurl active\n\nIn group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "Activated \n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protect["pinv"]:
                                         protect["pinv"].remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Denyinvite deactive\nIn group : " +str(ginfo.name)
                                    else:
                                         msgs = "Denyinvite has been disable"
                                    cl.sendMessage(msg.to, "Nonactive\n\n" + msgs)

                        elif 'Js ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Js ','')
                              if spl == 'on':
                                  if msg.to in protect["antijs"]:
                                       msgs = "Protectjs has been active"
                                  else:
                                       protect["antijs"].append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protectjs activated\n\nin group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "active\n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protect["antijs"]:
                                         protect["antijs"].remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protectjs has been deactive\nin group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protectjs has been deactive"
                                    cl.sendMessage(msg.to, "nonactive\n" + msgs)

                        elif 'Allpro ' in msg.text:
                           if msg._from in owner or msg._from in admin:
                              spl = msg.text.replace('Allpro ','')
                              if spl == 'on':
                                  if msg.to in protect["pqr"]:
                                       msgs = ""
                                  else:
                                       protect["pqr"].append(msg.to)
                                  if msg.to in protect["protect"]:
                                      msgs = ""
                                  else:
                                      protect["protect"].append(msg.to)
                                  if msg.to in protect["pinv"]:
                                      msgs = ""
                                  else:
                                      protect["pinv"].append(msg.to)
                                  if msg.to in protect["proall"]:
                                      msgs = ""
                                  else:
                                      protect["proall"].append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Allpro has been active\n\nIn group : " +str(ginfo.name)
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Succes\nIn group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "Activated\n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protect["pqr"]:
                                         protect["pqr"].remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protect["protect"]:
                                         protect["protect"].remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protect["pinv"]:
                                         protect["pinv"].remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protect["proall"]:
                                         protect["proall"].remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Succes Nonactive Allpro\n\nIn group : " +str(ginfo.name)
                                    else:
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Allpro has been deactive\nDi Group : " +str(ginfo.name)
                                    cl.sendMessage(msg.to, "Nonactive\n" + msgs)

#===========KICKOUT============#
                        elif ("Kick:on " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           ka.kickoutFromGroup(msg.to, [target])
                                           print ("kicker1 kick user")
                                       except:
                                           cl.sendMessage(msg.to,"Nothing Assist")

#===========ADMIN ADD============#
                        elif ("Admin:on " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           admin.append(target)
                                           cl.sendMessage(msg.to,"Berhasil menambahkan admin")
                                       except:
                                           pass

                        elif ("Staff:on " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           staff.append(target)
                                           cl.sendMessage(msg.to,"Berhasil menambahkan staff")
                                       except:
                                           pass

                        elif ("Bot:on " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           Bots.append(target)
                                           cl.sendMessage(msg.to,"Succes Addbot")
                                       except:
                                           pass

                        elif ("Adminexpl:on " in msg.text):
                            if msg._from in owner or msg_from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           admin.remove(target)
                                           cl.sendMessage(msg.to,"Succes expel admin")
                                       except:
                                           pass

                        elif ("Staffexpl:on " in msg.text):
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           staff.remove(target)
                                           cl.sendMessage(msg.to,"Succes expel staff")
                                       except:
                                           pass

                        elif ("Botexpl:on " in msg.text):
                            if msg._from in owner:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           Bots.remove(target)
                                           cl.sendMessage(msg.to,"Succes expel Bots")
                                       except:
                                           pass

                        elif cmd == "admin:on" or text.lower() == 'admin:on':
                            if msg._from in owner:
                                wait["addadmin"] = True
                                cl.sendMessage(msg.to,"Send Contact")

                        elif cmd == "adminexpl:on" or text.lower() == 'adminexpl:on':
                            if msg._from in owner:
                                wait["delladmin"] = True
                                cl.sendMessage(msg.to,"Send contact")

                        elif cmd == "staff:on" or text.lower() == 'staff:on':
                            if msg._from in owner or msg._from in admin:
                                wait["addstaff"] = True
                                cl.sendMessage(msg.to,"Send contact")

                        elif cmd == "staffexpl:on" or text.lower() == 'staffexpl:on':
                            if msg._from in owner or msg._from in admin:
                                wait["dellstaff"] = True
                                cl.sendMessage(msg.to,"Send contact")

                        elif cmd == "bot:on" or text.lower() == 'bot:on':
                            if msg._from in owner or msg._from in admin:
                                wait["addbots"] = True
                                cl.sendMessage(msg.to,"Send contact")

                        elif cmd == "botexpl:on" or text.lower() == 'botexpl:on':
                            if msg._from in owner:
                                wait["dellbots"] = True
                                cl.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "abort" or text.lower() == 'refresh':
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                cl.sendMessage(msg.to,"All refresh")

                        elif cmd == "admin" or text.lower() == 'contact admin':
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                ma = ""
                                for i in admin:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "staff" or text.lower() == 'contact staff':
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                ma = ""
                                for i in staff:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "bot" or text.lower() == 'contact bot':
                            if msg._from in admin:
                                ma = ""
                                for i in Bots:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

#===========COMMAND ON OFF============#
                        elif cmd == "notag on" or text.lower() == 'notag on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["Mentionkick"] = True
                                cl.sendMessage(msg.to,"Notag diaktifkan")

                        elif cmd == "notag off" or text.lower() == 'notag off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["MentionKick"] = False
                                cl.sendMessage(msg.to,"Notag dinonaktifkan")

                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["contact"] = True
                                cl.sendMessage(msg.to,"Deteksi contact diaktifkan")

                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["contact"] = False
                                cl.sendMessage(msg.to,"Deteksi contact dinonaktifkan")

                        elif cmd == "respon on" or text.lower() == 'respon on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["detectMention"] = True
                                cl.sendMessage(msg.to,"Auto respon diaktifkan")

                        elif cmd == "respon off" or text.lower() == 'respon off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["detectMention"] = False
                                cl.sendMessage(msg.to,"Auto respon dinonaktifkan")

                        elif cmd == "autojoin on" or text.lower() == 'autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                wait["autoJoin"] = True
                                cl.sendMessage(msg.to,"Autojoin diaktifkan")

                        elif cmd == "autojoin off" or text.lower() == 'autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                wait["autoJoin"] = False
                                cl.sendMessage(msg.to,"Autojoin dinonaktifkan")

                        elif cmd == "autoleave on" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in admin or msg._from in owner:
                                wait["autoLeave"] = True
                                cl.sendMessage(msg.to,"Autoleave diaktifkan")

                        elif cmd == "autoleave off" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                wait["autoLeave"] = False
                                cl.sendMessage(msg.to,"Autoleave dinonaktifkan")

                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["autoAdd"] = True
                                cl.sendMessage(msg.to,"Auto add diaktifkan")

                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["autoAdd"] = False
                                cl.sendMessage(msg.to,"Auto add dinonaktifkan")

                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["sticker"] = True
                                cl.sendMessage(msg.to,"Deteksi sticker diaktifkan")

                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["sticker"] = False
                                cl.sendMessage(msg.to,"Deteksi sticker dinonaktifkan")

                        elif cmd == "jointicket on" or text.lower() == 'jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                settings["autoJoinTicket"] = True
                                cl.sendMessage(msg.to,"Join ticket diaktifkan")

                        elif cmd == "jointicket off" or text.lower() == 'jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                settings["autoJoinTicket"] = False
                                cl.sendMessage(msg.to,"Notag dinonaktifkan")

#===========COMMAND BLACKLIST============#
                        elif ("Talkban:on " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           wait["Talkblacklist"][target] = True
                                           cl.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Untalkban:on " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["Talkblacklist"][target]
                                           cl.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "talkban:on" or text.lower() == 'talkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["Talkwblacklist"] = True
                                cl.sendMessage(msg.to,"Send contact")

                        elif cmd == "untalkban:on" or text.lower() == 'untalkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["Talkdblacklist"] = True
                                cl.sendMessage(msg.to,"Send contact")

                        elif ("Ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           wait["blacklist"][target] = True
                                           cl.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Unban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           cl.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                wait["wblacklist"] = True
                                cl.sendMessage(msg.to,"Send contact")

                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                wait["dblacklist"] = True
                                cl.sendMessage(msg.to,"Send contact")

                        elif cmd == "banlist" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                              if wait["blacklist"] == {}:
                                cl.sendMessage(msg.to,"Nothing blacklist")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"Blacklist\n\n"+ma+"\n %s User" %(str(len(wait["blacklist"]))))

                        elif cmd == "talkbanlist" or text.lower() == 'talkbanlist':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                              if wait["Talkblacklist"] == {}:
                                cl.sendMessage(msg.to,"Tidak ada Talkban user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to," Talkban User\n\n"+ma+"\nTotal「%s」Talkban User" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "blc" or text.lower() == 'blc':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                              if wait["blacklist"] == {}:
                                    cl.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = cl.getContact(i)
                                        cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "clearban" or text.lower() == 'clearban':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = cl.getContacts(wait["blacklist"])
                              mc = "%i" % len(ragets)
                              cl.sendMessage(msg.to,"Succes clearall " +mc)
#===========COMMAND SET============#
                        elif 'Spesan: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Spesan: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Pesan Msg")
                              else:
                                  wait["message"] = spl
                                  cl.sendMessage(msg.to, "「Pesan Msg」\nPesan Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Swelcome: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Swelcome: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Welcome Msg")
                              else:
                                  wait["welcome"] = spl
                                  cl.sendMessage(msg.to, "「Welcome Msg」\nWelcome Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Srespon: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Srespon: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag"] = spl
                                  cl.sendMessage(msg.to, "「Respon Msg」\nRespon Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Sspam: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Sspam: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Spam")
                              else:
                                  Setmain["RAmessage1"] = spl
                                  cl.sendMessage(msg.to, "「Spam Msg」\nSpam Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Ssider: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Ssider: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Sider Msg")
                              else:
                                  wait["mention"] = spl
                                  cl.sendMessage(msg.to, "「Sider Msg」\nSider Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif text.lower() == "cpesan":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Pesan Msg」\nPesan Msg mu :\n\n「 " + str(wait["message"]) + " 」")

                        elif text.lower() == "cwelcome":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Welcome Msg」\nWelcome Msg mu :\n\n「 " + str(wait["welcome"]) + " 」")

                        elif text.lower() == "crespon":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Respon Msg」\nRespon Msg mu :\n\n「 " + str(wait["Respontag"]) + " 」")

                        elif text.lower() == "cspam":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Spam Msg」\nSpam Msg mu :\n\n「 " + str(Setmain["RAmessage1"]) + " 」")

                        elif text.lower() == "csider":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Sider Msg」\nSider Msg mu :\n\n「 " + str(wait["mention"]) + " 」")

#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                            if msg._from in admin or msg._from in owner:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = cl.findGroupByTicket(ticket_id)
                                     cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     cl.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group1 = ka.findGroupByTicket(ticket_id)

    except Exception as error:
        print (error)


while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                bot(op)
                # Don't remove this line, if you wan't get error soon!
                oepoll.setRevision(op.revision)
    except Exception as e:
        print(e)
