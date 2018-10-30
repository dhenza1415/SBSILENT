# -*- coding: utf-8 -*-
from LineAPI.linepy import *
from LineAPI.akad.ttypes import Message
from LineAPI.akad.ttypes import ContentType as Type
from LineAPI.akad.ttypes import ChatRoomAnnouncementContents
from LineAPI.akad.ttypes import ChatRoomAnnouncement
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, multiprocessing, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib3, urllib.parse, html5lib, wikipedia, atexit, timeit, pafy, youtube_dl, traceback
from gtts import gTTS
from googletrans import Translator
#===============================================================================================
cl = LINE("EyunRbh5iBXFRF3M9Teb.SCwNhYE4y4LUNus/QfFtwW.AMBFtJT/Sh+IxtkarNzSB/jZn6/P15iCYUUUaOE8Kk0=")
cl.log("Auth Token : " + str(cl.authToken))
ki = LINE("EyF555kn6Rr8ODgQJI87.ryGTdQ0xa4vDVgdudJE/XW.QbwaTuZHx6ObHDvHwjNKBUu0pDsKe0s1DcHQSuZW/14=")
ki.log("Auth Token : " + str(ki.authToken))
kk = LINE("EyfyQNzcrxoPMHr0T5s9.k+n9YlUAYfbHu5wP4vHq/q.NOS2wc4xMKWLknBhQWnNaJf35BTzR1rGmgBxBqgd12A=")
kk.log("Auth Token : " + str(kk.authToken))
kc = LINE("EylzuydXkzQRy9rrSeKc.cL7O15BJz3PwUe+Wo2vK7a.GNRU8PZzRjx8XbOmXWsOr7yFcYkV0AR0x/gnfE4Qe9g=")
kc.log("Auth Token : " + str(kc.authToken))
kb = LINE("EyvSHA6sitTr7BgooQz7.kBfVdPNp3W59E4fW983bPW.4mkyVm4g+QfDX5O6dLFqhoczMeB6RHne1d3eVqiNprs=")
kb.log("Auth Token : " + str(kb.authToken))
sw = LINE("EyRVBTvpUYmzxxrkuyIe.362avKDVpNAqnxvrpmIUVG.uxbqgfzfztzEbnmPlqfiZ6KpN0dK4QfGRgA2l02KDKM=")
sw.log("Auth Token : " + str(sw.authToken))

print ("☆☆☆[ Creator Dhenz415 ]☆☆☆")

oepoll = OEPoll(cl)
call = cl

creator = ["ub1c5a71f27b863896e9d44bea857d35b","ufdc20b3a00b5e8f31e4f91017eb361b0","u4e31d7e10bff93329195d410e35ad641"]
owner = ["ub1c5a71f27b863896e9d44bea857d35b","ufdc20b3a00b5e8f31e4f91017eb361b0","u4e31d7e10bff93329195d410e35ad641"]
admin = ["ub1c5a71f27b863896e9d44bea857d35b","ufdc20b3a00b5e8f31e4f91017eb361b0","u4e31d7e10bff93329195d410e35ad641"]
staff = ["ub1c5a71f27b863896e9d44bea857d35b","ufdc20b3a00b5e8f31e4f91017eb361b0","u4e31d7e10bff93329195d410e35ad641"]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = kb.getProfile().mid
Zmid = sw.getProfile().mid
KAC = [ki,kk,kc,kb]
ABC = [ki,kk,kc,kb]
Bots = [mid,Amid,Bmid,Cmid,Dmid,Zmid]
Saints = admin + staff

protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
welcome = []
protectantijs = []
ghost = []
targets = []

welcome = []

responsename1 = ki.getProfile().displayName
responsename2 = kk.getProfile().displayName
responsename3 = kc.getProfile().displayName
responsename4 = kb.getProfile().displayName

settings = {
    "Picture":False,
    "group":{},
    "groupPicture":False,
    "changePicture":False,
    "autoJoinTicket":True,
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
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ]
}

wait = {
    "limit": 1,
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
    'autoLeave':False,
    'autoLeave1':False,
    "detectMention":True,
    "Mentionkick":False,
    "welcomeOn":False,
    "sticker":False,
    "selfbot":True,
    "Protectantijs":False,
    "Ghost":False,
    "mention":"Cuy ngintip mele gbung sini dihh",
    "Respontag":"Tag 1x besok bunting",
    "welcome":"Welcome semoga bahagia",
    "comment":"Auto like by 🛡Silent Bot🛡",
    "message":"Thanks for add me.\n☆ 🛡Silent Bot🛡\n Add Creator kami\nline.me/p/~dhenz415",
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

try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except:
    print("Couldn't read Log data")

with open('creator.json', 'r') as fp:
    creator = json.load(fp)
with open('owner.json', 'r') as fp:
    owner = json.load(fp)

Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)

mulai = time.time()
settingsOpen = codecs.open("temp.json","r","utf-8")
settings = json.load(settingsOpen)

mulai = time.time()
tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)
dangerMessage = ["cleanse","group cleansed.","mulai",".winebot",".kickall","mayhem","kick on","makasih :d","!kickall","nuke","บิน",".???","งงไปดิ","บินไปดิ","เซลกากจัง"]
#======================================================================================================#
def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

def restartBot():
    print ("RESTART SERVER")
    time.sleep(3)
    python = sys.executable
    os.execl(python, python, *sys.argv)

def logError(text):
    cl.log("[ ERROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
      error.write("\n[%s] %s" % (str(time), text))

def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))

def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

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

def sendAudioWithURL(self, to_, url):
        path = self.downloadFileWithURL(url)
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise Exception(e)

def sendAudioWithUrl(self, to_, url):
        path = '%s/pythonLine-%1.data' % (tempfile.gettempdir(), randint(0, 9))
        r = requests.get(url, stream=True, verify=False)
        if r.status_code == 200:
           with open(path, 'w') as f:
              shutil.copyfileobj(r.raw, f)
        else:
           raise Exception('Download audio failure.')
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise e

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Mention User「{}」\n\n  [ Mention ]\n1. ".format(str(len(mid)))
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
        textx = "🇦🇱Total Sider User「{}」\n🇦🇱Hai ".format(str(len(mid)))
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
            textx += mention+wait["mention"]+"\n\nGroup name: "+str(ginfo.name)
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
        contact = cl.getContact(op.param2).picturePath
        image = 'http://dl.profile.line.naver.jp'+contact
        cl.sendImageWithURL(op.param1, image)
        cl.sendMessage(to, None, contentMetadata={"STKID":"2754669","STKPKGID":"1066653","STKVER":"1"}, contentType=7)
    except Exception as error:
        cl.sendMessage(msg.to, None, contentMetadata={"STKID":"52002748","STKPKGID":"11537","STKVER":"1"}, contentType=7)
        
def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Member Masuk「{}」\nHaii  ".format(str(len(mid)))
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
        cl.sendMessage(msg.to, None, contentMetadata={"STKID":"52002748","STKPKGID":"11537","STKVER":"1"}, contentType=7)

def sendMention1(to, mid, firstmessage):
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
        text += mention+"🐤 Jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" Wib\n🐤 Group : "+str(len(gid))+"\n🐤 Teman : "+str(len(teman))+"\n🐤 Expired : In "+hari+"\n🐤 Version : SILENTBOTpy3\n🐤 Tanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n🐤 Runtime : \n • "+bot
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd

def help():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "╔═[🌻🛡Silent Bot🛡🌻]═╗\n│Using key「 " + key + " \n" + \
                  "╠✪➣ " + key + "Me\n" + \
                  "╠✪➣ " + key + "Mid「@」\n" + \
                  "╠✪➣ " + key + "Info「@」\n" + \
                  "╠✪➣ " + key + "Bacok「@」\n" + \
                  "╠✪➣ " + key + "Kickall「kick member」\n" + \
                  "╠✪➣ " + key + "Nuke「kickall member」\n" + \
                  "╠✪➣ " + key + "Go「cleanse」\n" + \
                  "╠✪➣ " + key + "Vc「@」\n" + \
                  "╠✪➣ " + key + "Mybot\n" + \
                  "╠✪➣ " + key + "Status\n" + \
                  "╠✪➣ " + key + "About\n" + \
                  "╠✪➣ " + key + "Respon\n" + \
                  "╠✪➣ " + key + "Restart\n" + \
                  "╠✪➣ " + key + "Runtime\n" + \
                  "╠✪➣ " + key + "Creator\n" + \
                  "╠✪➣ " + key + "Speed/Sp\n" + \
                  "╠✪➣ " + key + "Sptime\n" + \
                  "╠✪➣ " + key + "Tagall\n" + \
                  "╠✪➣ " + key + "Masuk\n" + \
                  "╠✪➣ " + key + "Pulang\n" + \
                  "╠✪➣ " + key + "byme\n" + \
                  "╠✪➣ " + key + "Leave「Namagrup」\n" + \
                  "╠✪➣ " + key + "Ginfo\n" + \
                  "╠✪➣ " + key + "Open\n" + \
                  "╠✪➣ " + key + "Close\n" + \
                  "╠✪➣ " + key + "Url grup\n" + \
                  "╠✪➣ " + key + "Gruplist\n" + \
                  "╠✪➣ " + key + "Infogrup「angka」\n" + \
                  "╠✪➣ " + key + "Infomem「angka」\n" + \
                  "╠✪➣ " + key + "Remove chat\n" + \
                  "╠✪➣ " + key + "Lurking「on/off」\n" + \
                  "╠✪➣ " + key + "Lurkers\n" + \
                  "╠✪➣ " + key + "Sider「on/off」\n" + \
                  "╠✪➣ " + key + "Updatefoto\n" + \
                  "╠✪➣ " + key + "Updategrup\n" + \
                  "╠✪➣ " + key + "Updatebot\n" + \
                  "╠✪➣ " + key + "Broadcast:「Text」\n" + \
                  "╠✪➣ " + key + "Setkey「New Key」\n" + \
                  "╠✪➣ " + key + "Mykey\n" + \
                  "╠✪➣ " + key + "Resetkey\n" + \
                  "╠✪➣ " + key + "Silentkiller「kickall」\n" + \
                  "\n  🛡─《Silent media》─🛡\n│Using key「 " + key + " \n" + \
                  "╠✪➣ " + key + "ID line:「Id Line nya」\n" + \
                  "╠✪➣ " + key + "Sholat:「Nama Kota」\n" + \
                  "╠✪➣ " + key + "/al quran「Query」\n" + \
                  "╠✪➣ " + key + "Cuaca:「Nama Kota」\n" + \
                  "╠✪➣ " + key + "Lokasi:「Nama Kota」\n" + \
                  "╠✪➣ " + key + "Music:「Judul Lagu」\n" + \
                  "╠✪➣ " + key + "Lirik:「Judul Lagu」\n" + \
                  "╠✪➣ " + key + "Ytmp3:「Judul Lagu」\n" + \
                  "╠✪➣ " + key + "Ytmp4:「Judul Video」\n" + \
                  "╠✪➣ " + key + "Profileig:「Nama IG」\n" + \
                  "╠✪➣ " + key + "!「Retrowave (teks)」\n" + \
                  "╠✪➣ " + key + "Cekdate:「tgl-bln-thn」\n" + \
                  "╠✪➣ " + key + "Jumlah:「angka」\n" + \
                  "╠✪➣ " + key + "Spamtag「@」\n" + \
                  "╠✪➣ " + key + "Spamcall:「jumlahnya」\n" + \
                  "╠✪➣ " + key + "Spamcall\n" + \
                  "\n  🛡─《Silent Protect》─🛡\n│Not Using key「 " + key + " \n" + \
                  "╠✪➣ " + key + "Notag「on/off」\n" + \
                  "╠✪➣ " + key + "Semuapro「on/off」\n" + \
                  "╠✪➣ " + key + "Protecturl「on/off」\n" + \
                  "╠✪➣ " + key + "Protectjoin「on/off」\n" + \
                  "╠✪➣ " + key + "Protectkick「on/off」\n" + \
                  "╠✪➣ " + key + "Protectinvite「on/off」\n" + \
                  "╠✪➣ " + key + "Protectcancel「on/off」\n" + \
                  "╠✪➣ " + key + "Js「on」\n" + \
                  "╠✪➣ " + key + "Js stay\n" + \
                  "╠✪➣ " + key + "Protectantijs「on/off」\n" + \
                  "╠✪➣ " + key + "Ghost bye\n" + \
                  "╠✪➣ " + key + "Ghost「on/off」\n" + \
                  "╠✪➣ " + key + "Kicker in\n" + \
                  "╠✪➣ " + key + "Kicker lv\n" + \
                  "╠✪➣ " + key + "Midbot\n" + \
                  "╠✪➣ " + key + "Sk\n" + \
                  "╠✪➣ " + key + "Sk on\n" + \
                  "\n  🛡─《Silent Settings》─🛡\n│Not Using key「 " + key + " \n" + \
                  "╠✪➣ " + key + "Sticker「on/off」\n" + \
                  "╠✪➣ " + key + "Respon「on/off」\n" + \
                  "╠✪➣ " + key + "Contact「on/off」\n" + \
                  "╠✪➣ " + key + "Autojoin「on/off」\n" + \
                  "╠✪➣ " + key + "Autoadd「on/off」\n" + \
                  "╠✪➣ " + key + "Welcome「on/off」\n" + \
                  "╠✪➣ " + key + "Autoleave「on/off」\n" + \
                  "\n  🛡─《SILENT Bot Admin》─🛡\n│Not Using key「 " + key + " 」\n" + \
                  "╠✪➣ " + key + "Admin:on\n" + \
                  "╠✪➣ " + key + "Admin:repeat\n" + \
                  "╠✪➣ " + key + "Staff:on\n" + \
                  "╠✪➣ " + key + "Staff:repeat\n" + \
                  "╠✪➣ " + key + "Bot:on\n" + \
                  "╠✪➣ " + key + "Bot:repeat\n" + \
                  "╠✪➣ " + key + "Adminadd「@」\n" + \
                  "╠✪➣ " + key + "Admindell「@」\n" + \
                  "╠✪➣ " + key + "Staffadd「@」\n" + \
                  "╠✪➣ " + key + "Staffdell「@」\n" + \
                  "╠✪➣ " + key + "Botadd「@」\n" + \
                  "╠✪➣ " + key + "Botdell「@」\n" + \
                  "╠✪➣ " + key + "Refresh\n" + \
                  "╠✪➣ " + key + "Listbot\n" + \
                  "╠✪➣ " + key + "Listadmin\n" + \
                  "╠✪➣ " + key + "Listprotect\n"+ \
                  "╚═[✪🌻🛡SilentBot🛡🌻✪]═╝"
    return helpMessage

def helpbot():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = "〔SilentBot\n│Not Using key「 " + key + " 」\n" + \
                  "🐞" + key + "Blc\n" + \
                  "🐞" + key + "Ban:on\n" + \
                  "🐞" + key + "Unban:on\n" + \
                  "🐞" + key + "Ban「@」\n" + \
                  "🐞" + key + "Unban「@」\n" + \
                  "🐞" + key + "Talkban「@」\n" + \
                  "🐞" + key + "Untalkban「@」\n" + \
                  "🐞" + key + "Talkban:on\n" + \
                  "🐞" + key + "Untalkban:on\n" + \
                  "🐞" + key + "Banlist\n" + \
                  "🐞" + key + "Talkban「on/off」\n" + \
                  "🐞" + key + "Talkbanlist\n" + \
                  "🐞" + key + "Clearban\n" + \
                  "🐞" + key + "Refresh\n" + \
                  "\n  🌻─〔SilentBot〕─🌻\n│Using key「 " + key + " 」\n" + \
                  "🐞" + key + "Cek sider\n" + \
                  "🐞" + key + "Cek spam\n" + \
                  "🐞" + key + "Cek pesan \n" + \
                  "🐞" + key + "Cek respon \n" + \
                  "🐞" + key + "Cek welcome\n" + \
                  "🐞" + key + "Set sider:「Text」\n" + \
                  "🐞" + key + "Set spam:「Text」\n" + \
                  "🐞" + key + "Set pesan:「Text」\n" + \
                  "🐞" + key + "Set respon:「Text」\n" + \
                  "🐞" + key + "Set welcome:「Text」\n" + \
                  "🐞" + key + "Myname:「Nama」\n" + \
                  "🐞" + key + "1in/2in/3in\n" + \
                  "🐞" + key + "1name:「Nama」\n" + \
                  "🐞" + key + "2name:「Nama」\n" + \
                  "🐞" + key + "3name:「Nama」\n" + \
                  "🐞" + key + "GhostCname:「Nama」\n" + \
                  "🐞" + key + "1Up「Image」\n" + \
                  "🐞" + key + "2Up「Image」\n" + \
                  "🐞" + key + "3Up「Image」\n" + \
                  "🐞" + key + "Ghostup「Image」\n" + \
                  "🐞" + key + "Gift:「Mid」「Result」\n" + \
                  "🐞" + key + "Spam:「Mid」「Result」\n" + \
                  "🌻🛡SilentBot🛡🌻"
                  
    return helpMessage1

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        
        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if cl.getGroup(op.param1).preventedJoinByTicket == True:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            cl.reissueGroupTicket(op.param1)
                            X = cl.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            cl.updateGroup(X)
                            cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                except:
                    try:
                        if ki.getGroup(op.param1).preventedJoinByTicket == True:
                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                ki.reissueGroupTicket(op.param1)
                                X = ki.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                ki.updateGroup(X)
                                cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                    except:
                        try:
                            if kk.getGroup(op.param1).preventedJoinByTicket == True:
                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                    kk.reissueGroupTicket(op.param1)
                                    X = kk.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    kk.updateGroup(X)
                                    cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                        except:
                            try:
                                if kc.getGroup(op.param1).preventedJoinByTicket == True:
                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                        kc.reissueGroupTicket(op.param1)
                                        X = kc.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        kc.updateGroup(X)
                                        cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                            except:
                                try:
                                    if cl.getGroup(op.param1).preventedJoinByTicket == True:
                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                            cl.reissueGroupTicket(op.param1)
                                            X = cl.getGroup(op.param1)
                                            X.preventedJoinByTicket = True
                                            cl.updateGroup(X)
                                            cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                except:
                                    try:
                                        if ki.getGroup(op.param1).preventedJoinByTicket == True:
                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                ki.reissueGroupTicket(op.param1)
                                                X = ki.getGroup(op.param1)
                                                X.preventedJoinByTicket = True
                                                ki.updateGroup(X)
                                                cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                    except:
                                        pass
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"I'm coming " + str(ginfo.name))

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Im' coming " +str(ginfo.name))
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"I'm coming " + str(ginfo.name))
            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        ki.sendMessage(op.param1,"Balik dullu\n Group " +str(ginfo.name))
                        ki.leaveGroup(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        ki.sendMessage(op.param1,"I'm coming " + str(ginfo.name))
            if Bmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
                        ki.sendMessage(op.param1,"Balik dul;u\n Group " +str(ginfo.name))
                        kk.leaveGroup(op.param1)
                    else:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
                        kk.sendMessage(op.param1,"I'm coming " + str(ginfo.name))
            if Cmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
                        kc.sendMessage(op.param1,"Pulang dullu\n Group " +str(ginfo.name))
                        kc.leaveGroup(op.param1)
                    else:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
                        kc.sendMessage(op.param1,"I'm coming" + str(ginfo.name))
            if Dmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kb.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
                        kb.sendMessage(op.param1,"Pulang dullu\n Group " +str(ginfo.name))
                        kb.leaveGroup(op.param1)
                    else:
                        kb.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
                        kb.sendMessage(op.param1,"I'm coming " + str(ginfo.name))

        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = cl.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            cl.cancelGroupInvitation(op.param1,[_mid])
                    except:
                        try:
                            group = ki.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                ki.cancelGroupInvitation(op.param1,[_mid])
                        except:
                            try:
                                group = kk.getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    kk.cancelGroupInvitation(op.param1,[_mid])
                            except:
                                try:
                                    group = kc.getGroup(op.param1)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                        kc.cancelGroupInvitation(op.param1,[_mid])
                                except:
                                    try:
                                        group = kc.getGroup(op.param1)
                                        gMembMids = [contact.mid for contact in group.invitee]
                                        for _mid in gMembMids:
                                            kc.cancelGroupInvitation(op.param1,[_mid])
                                    except:
                                        pass

        if op.type == 13:
            if op.param2 in wait["blacklist"]:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            ki.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                kk.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    kc.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                        kb.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        pass
                return

        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass
                return

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
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                        	kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass
                return

        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        cl.sendMessage(op.param1, wait["message"])

        if op.type == 19:
            if op.param2 in wait["blacklist"]:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass
                return

        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass
        if op.type == 19:
            try:
                if op.param1 in ghost:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        G = cl.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(op.param1)
                        sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                        sw.kickoutFromGroup(op.param1,[op.param2])
                        sw.leaveGroup(op.param1)
                        X = cl.getGroup(op.param1)
                        X.preventedJoinByTicket = True
                        cl.updateGroup(X)
            except:
                pass

        if op.type == 19:
            try:
                if op.param1 in protectantijs:
                  if op.param3 in mid:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        sw.acceptGroupInvitation(op.param1)
                        G = sw.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        sw.updateGroup(G)
                        Ticket = sw.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        sw.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = True
                        sw.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                        sw.leaveGroup(op.param1)
                        cl.inviteIntoGroup(op.param1,[Zmid])
                        cl.inviteIntoGroup(op.param1,[admin])
                    else:
                        pass
                if op.param3 in Zmid:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[Zmid])
                        cl.sendMessage(op.param1,"invite peotect sucses")
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[Zmid])
                        cl.sendMessage(op.param1,"invite protect sucses")
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if op.param3 in admin:
                        if op.param1 in protectantijs:
                            wait["blacklist"][op.param2] = True
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            cl.findAndAddContactsByMid(op.param3)
                            cl.inviteIntoGroup(op.param1,[op.param3])
                            cl.sendMessage(op.param1,"invite protect sucses")
                else:
                    pass
            except:
                pass

        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in wait["blacklist"]:
                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass
                            return

        if op.type == 32:
            if op.param3 in Zmid:
              if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                  wait["blacklist"][op.param2] = True
                  try:
                      if op.param3 not in wait["blacklist"]:
                          ki.inviteIntoGroup(op.param1,[Zmid])
                          ki.kickoutFromGroup(op.param1,[op.param2])
                          ki.sendMessage(op.param1, "Jir songong itu antijs di cancle kapok w cipok")
                  except:
                      try:
                          if op.param3 not in wait["blacklist"]:
                              kk.inviteIntoGroup(op.param1,[Zmid])
                              kk.kickoutFromGroup(op.param1,[op.param2])
                              kk.sendMessage(op.param1, "Jir songong itu antijs di cancle kapok w cipok")
                      except:
                          try:
                              if op.param3 not in wait["blacklist"]:
                                  kc.inviteIntoGroup(op.param1,[Zmid])
                                  kc.kickoutFromGroup(op.param1,[op.param2])
                                  kc.sendMessage(op.param1, "Jir songong itu antijs di cancle kapok w cipok")
                          except:
                              try:
                                  if op.param3 not in wait["blacklist"]:
                                      ki.inviteIntoGroup(op.param1,[Zmid])
                                      ki.kickoutFromGroup(op.param1,[op.param2])
                                      ki.sendMessage(op.param1, "Jir songong itu antijs di cancle kapok w cipok")
                              except:
                                  try:
                                      if op.param3 not in wait["blacklist"]:
                                          kk.inviteIntoGroup(op.param1,[Zmid])
                                          kk.kickoutFromGroup(op.param1,[op.param2])
                                          kk.sendMessage(op.param1, "Jir songong itu antijs di cancle kapok w cipok")
                                  except:
                                     pass
              return

        if op.type == 19:
            if mid in op.param3:
                print("Bots1 has been kicked")
                if op.param2 in Bots:
                    X = ki.getGroup(op.param1)
                    X.preventedJoinByTicket = False
                    ki.updateGroup(X)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                    X = cl.getGroup(op.param1)
                    X.preventedJoinByTicket = True
                    cl.updateGroup(X)
                    Ticket = cl.reissueGroupTicket(op.param1)
                else:
                    wait["blacklist"][op.param2] = True
                    print("Kicker has been blacklist")
                    try:
                        X = ki.getGroup(op.param1)
                        X.preventedJoinByTicket = False
                        ki.updateGroup(X)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X = cl.getGroup(op.param1)
                        X.preventedJoinByTicket = True
                        cl.updateGroup(X)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        print("Bots1 Joined openqr")
                    except:
                        try:
                            kc.inviteIntoGroup(op.param1,[op.param3])
                            cl.acceptGroupInvitation(op.param1)
                            kb.kickoutFromGroup(op.param1,[op.param2])
                            print("Bots1 Joined Invite 2")
                        except:
                            try:
                                G = kk.getGroup(op.param1)
                                G.preventedJoinByTicket = False
                                kk.updateGroup(G)
                                Ticket = kk.reissueGroupTicket(op.param1)
                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ki.kickoutFromGroup(op.param1,[op.param2])
                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                G = cl.getGroup(op.param1)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                                Ticket = ki.reissueGroupTicket(op.param1)
                                print("Bots1 Joined Open Qr 1")
                            except:
                                G = kb.getGroup(op.param1)
                                G.preventedJoinByTicket = False
                                kb.updateGroup(G)
                                Ticket = kb.reissueGroupTicket(op.param1)
                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                G = cl.getGroup(op.param1)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                Ticket = cl.reissueGroupTicket(op.param1)
                                print("Bots1 Joined Open Qr 2")

            if Amid in op.param3:
                print("Bots2 has been kicked")
                if op.param2 in Bots:
                    X = cl.getGroup(op.param1)
                    X.preventedJoinByTicket = False
                    cl.updateGroup(X)
                    Ticket = cl.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                    X = cl.getGroup(op.param1)
                    X.preventedJoinByTicket = True
                    cl.updateGroup(X)
                    Ticket = cl.reissueGroupTicket(op.param1)
                else:
                    wait["blacklist"][op.param2] = True
                    print("Kicker has been blacklist")
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        X = kc.getGroup(op.param1)
                        X.preventedJoinByTicket = False
                        kc.updateGroup(X)
                        Ticket = kc.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.kickoutFromGroup(op.param1,[op.param2])
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X = cl.getGroup(op.param1)
                        X.preventedJoinByTicket = True
                        cl.updateGroup(X)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        print("Bots2 Joined openqr")
                    except:
                        try:
                            kk.inviteIntoGroup(op.param1,[op.param3])
                            ki.acceptGroupInvitation(op.param1)
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            print("Bots2 Joined Invite 2")
                        except:
                            try:
                                kb.kickoutFromGroup(op.param1,[op.param2])
                                G = cl.getGroup(op.param1)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                Ticket = cl.reissueGroupTicket(op.param1)
                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                G = cl.getGroup(op.param1)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                                Ticket = cl.reissueGroupTicket(op.param1)
                                print("Bots2 Joined Open Qr 1")
                            except:
                                G = kk.getGroup(op.param1)
                                G.preventedJoinByTicket = False
                                kk.updateGroup(G)
                                Ticket = kk.reissueGroupTicket(op.param1)
                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                G = cl.getGroup(op.param1)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                Ticket = cl.reissueGroupTicket(op.param1)
                                print("Bots2 Joined Open Qr 2")

            if Bmid in op.param3:
                print("Bots3 has been kicked")
                if op.param2 in Bots:
                    X = cl.getGroup(op.param1)
                    X.preventedJoinByTicket = False
                    cl.updateGroup(X)
                    Ticket = cl.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                    X = cl.getGroup(op.param1)
                    X.preventedJoinByTicket = True
                    cl.updateGroup(X)
                    Ticket = cl.reissueGroupTicket(op.param1)
                else:
                    wait["blacklist"][op.param2] = True
                    print("Kicker has been blacklist")
                    try:
                        X = kb.getGroup(op.param1)
                        X.preventedJoinByTicket = False
                        ks.updateGroup(X)
                        Ticket = kb.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X = cl.getGroup(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        X.preventedJoinByTicket = True
                        cl.updateGroup(X)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        print("Bots3 Joined openqr")
                    except:
                        try:
                            cl.inviteIntoGroup(op.param1,[op.param3])
                            kk.acceptGroupInvitation(op.param1)
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            print("Bots3 Joined Invite 2")
                        except:
                            try:
                                kb.kickoutFromGroup(op.param1,[op.param2])
                                G = ki.getGroup(op.param1)
                                G.preventedJoinByTicket = False
                                ki.updateGroup(G)
                                Ticket = ki.reissueGroupTicket(op.param1)
                                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                G = ki.getGroup(op.param1)
                                G.preventedJoinByTicket = True
                                ki.updateGroup(G)
                                Ticket = ki.reissueGroupTicket(op.param1)
                                print("Bots3 Joined Open Qr 1")
                            except:
                                G = kb.getGroup(op.param1)
                                G.preventedJoinByTicket = False
                                kc.updateGroup(G)
                                Ticket = kb.reissueGroupTicket(op.param1)
                                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                G = cl.getGroup(op.param1)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                                kb.kickoutFromGroup(op.param1,[op.param2])
                                Ticket = cl.reissueGroupTicket(op.param1)
                                print("Bots3 Joined Open Qr 2")

            if Cmid in op.param3:
                print("Bots4 has been kicked")
                if op.param2 in Bots:
                    X = cl.getGroup(op.param1)
                    X.preventedJoinByTicket = False
                    cl.updateGroup(X)
                    Ticket = cl.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                    X = cl.getGroup(op.param1)
                    X.preventedJoinByTicket = True
                    cl.updateGroup(X)
                    Ticket = cl.reissueGroupTicket(op.param1)
                else:
                    wait["blacklist"][op.param2] = True
                    print("Kicker has been blacklist")
                    try:
                        X = kk.getGroup(op.param1)
                        X.preventedJoinByTicket = False
                        kk.updateGroup(X)
                        Ticket = kk.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X = kk.getGroup(op.param1)
                        X.preventedJoinByTicket = True
                        kk.updateGroup(X)
                        Ticket = kk.reissueGroupTicket(op.param1)
                        print("Bots4 Joined openqr")
                    except:
                        try:
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            kc.acceptGroupInvitation(op.param1)
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            print("Bots4 Joined Invite 2")
                        except:
                            try:
                                cl.kickoutFromGroup(op.param1,[op.param2])
                                G = ki.getGroup(op.param1)
                                G.preventedJoinByTicket = False
                                ki.updateGroup(G)
                                Ticket = ki.reissueGroupTicket(op.param1)
                                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                G = ki.getGroup(op.param1)
                                G.preventedJoinByTicket = True
                                ki.updateGroup(G)
                                Ticket = ki.reissueGroupTicket(op.param1)
                                print("Bots4 Joined Open Qr 1")
                            except:
                                G = kb.getGroup(op.param1)
                                G.preventedJoinByTicket = False
                                kb.updateGroup(G)
                                Ticket = kb.reissueGroupTicket(op.param1)
                                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                G = cl.getGroup(op.param1)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                                ki.kickoutFromGroup(op.param1,[op.param2])
                                Ticket = cl.reissueGroupTicket(op.param1)
                                print("Bots4 Joined Open Qr 2")

            if Dmid in op.param3:
                print("Bots4 has been kicked")
                if op.param2 in Bots:
                    X = cl.getGroup(op.param1)
                    X.preventedJoinByTicket = False
                    cl.updateGroup(X)
                    Ticket = cl.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                    X = cl.getGroup(op.param1)
                    X.preventedJoinByTicket = True
                    cl.updateGroup(X)
                    Ticket = cl.reissueGroupTicket(op.param1)
                else:
                    wait["blacklist"][op.param2] = True
                    print("Kicker has been blacklist")
                    try:
                        X = kc.getGroup(op.param1)
                        X.preventedJoinByTicket = False
                        kc.updateGroup(X)
                        Ticket = kc.reissueGroupTicket(op.param1)
                        kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X = kk.getGroup(op.param1)
                        X.preventedJoinByTicket = True
                        kk.updateGroup(X)
                        Ticket = kk.reissueGroupTicket(op.param1)
                        print("Bots4 Joined openqr")
                    except:
                        try:
                            kk.inviteIntoGroup(op.param1,[op.param3])
                            kb.acceptGroupInvitation(op.param1)
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            print("Bots4 Joined Invite 2")
                        except:
                            try:
                                ki.kickoutFromGroup(op.param1,[op.param2])
                                G = kk.getGroup(op.param1)
                                G.preventedJoinByTicket = False
                                kk.updateGroup(G)
                                Ticket = kk.reissueGroupTicket(op.param1)
                                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                G = kk.getGroup(op.param1)
                                G.preventedJoinByTicket = True
                                kk.updateGroup(G)
                                Ticket = kk.reissueGroupTicket(op.param1)
                                print("Bots4 Joined Open Qr 1")
                            except:
                                G = cl.getGroup(op.param1)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                Ticket = cl.reissueGroupTicket(op.param1)
                                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                G = cl.getGroup(op.param1)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                Ticket = cl.reissueGroupTicket(op.param1)
                                print("Bots4 Joined Open Qr 2")
                                
            if staff in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ki.findAndAddContactsByMid(op.param1,staff)
                        ki.inviteIntoGroup(op.param1,staff)
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            kk.findAndAddContactsByMid(op.param1,staff)
                            kk.inviteIntoGroup(op.param1,staff)
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.findAndAddContactsByMid(op.param1,staff)
                                kc.inviteIntoGroup(op.param1,staff)
                            except:
                                pass

                return
       
        if op.type == 55:
            try:
                if op.param1 in Setmain["readPoint"]:
                   if op.param2 in Setmain["readMember"][op.param1]:
                       pass
                   else:
                       Setmain["readMember"][op.param1][op.param2] = False
                else:
                   pass
            except:
                pass

        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass
                return

            if cctv['cyduk'][op.param1]==False:
                if op.param1 in cctv['point']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])

        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                   contact = cl.getContact(msg._from)
                   image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           cl.sendMessage(msg.to, wait["Respontag"])
                           cl.sendImageWithURL(msg.to,image)
                           rnd = ["Sekali tag besok bunting"]
                           p = random.choice(rnd)
                           lang = 'id'
                           tts = gTTS(text=p, lang=lang)
                           tts.save("hasil.mp3")
                           cl.sendAudio(msg.to,"hasil.mp3")
                           cl.sendMessage(msg.to, None, contentMetadata={"STKID":"51626511","STKPKGID":"11538","STKVER":"1"}, contentType=7)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           cl.mentiontag(msg.to,[msg._from])
                           cl.sendMessage(msg.to, "Crooottttt....")
                           cl.kickoutFromGroup(msg.to, [msg._from])
                           break
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"「Cek ID Sticker」\n🔴STKID : " + msg.contentMetadata["STKID"] + "\n🔴STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n🔴STKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to," Nama : " + msg.contentMetadata["displayName"] + "\n MID : " + msg.contentMetadata["mid"] + "\n Status Msg : " + contact.statusMessage + "\n Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
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
                        cl.sendMessage(msg.to,"✒ Nama : " + msg.contentMetadata["displayName"] + "\n✒ MID : " + msg.contentMetadata["mid"] + "\n✒ Status Msg : " + contact.statusMessage + "\n✒ Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
#ADD Bots
               if msg.contentType == 13:
                 if msg._from in admin:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        cl.sendMessage(msg.to,"Contact itu sudah jadi anggota bot")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke anggota bot")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Berhasil menghapus dari anggota bot")
                    else:
                        wait["dellbots"] = True
                        cl.sendMessage(msg.to,"Contact itu bukan anggota bot saints")
#ADD STAFF
                 if msg._from in admin:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        cl.sendMessage(msg.to,"Contact itu sudah jadi staff")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke staff")
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Berhasil menghapus dari staff")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        cl.sendMessage(msg.to,"Contact itu bukan staff")
#ADD ADMIN
                 if msg._from in admin:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        cl.sendMessage(msg.to,"Contact itu sudah jadi admin")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke admin")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Berhasil menghapus dari admin")
                    else:
                        wait["delladmin"] = True
                        cl.sendMessage(msg.to,"Contact itu bukan admin")
#ADD BLACKLIST
                 if msg._from in admin:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendMessage(msg.to,"Contact itu sudah ada di blacklist")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke blacklist user")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"Berhasil menghapus dari blacklist user")
                    else:
                        wait["dblacklist"] = True
                        cl.sendMessage(msg.to,"Contact itu tidak ada di blacklist")
#TALKBAN
                 if msg._from in admin:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        cl.sendMessage(msg.to,"Contact itu sudah ada di Talkban")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke Talkban user")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"Berhasil menghapus dari Talkban user")
                    else:
                        wait["Talkdblacklist"] = True
                        cl.sendMessage(msg.to,"Contact itu tidak ada di Talkban")
#UPDATE FOTO
               if msg.contentType == 1:
                 if msg._from in admin:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = cl.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            cl.sendMessage(msg.to, "Berhasil menambahkan gambar")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False

               if msg.toType == 2:
                 if msg._from in admin:
                   if settings["groupPicture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     cl.updateGroupPicture(msg.to, path)
                     cl.sendMessage(msg.to, "Berhasil mengubah foto group")

               if msg.contentType == 1:
                   if msg._from in admin:
                       if mid in Setmain["SKfoto"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del Setmain["SKfoto"][mid]
                            cl.updateProfilePicture(path)
                            cl.sendMessage(msg.to,"Foto berhasil dirubah")

               if msg.contentType == 1:
                 if msg._from in admin:
                        if Amid in Setmain["SKfoto"]:
                            path = ki.downloadObjectMsg(msg_id)
                            del Setmain["SKfoto"][Amid]
                            ki.updateProfilePicture(path)
                            ki.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Bmid in Setmain["SKfoto"]:
                            path = kk.downloadObjectMsg(msg_id)
                            del Setmain["SKfoto"][Bmid]
                            kk.updateProfilePicture(path)
                            kk.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Cmid in Setmain["SKfoto"]:
                            path = kc.downloadObjectMsg(msg_id)
                            del Setmain["SKfoto"][Cmid]
                            kc.updateProfilePicture(path)
                            kc.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Dmid in Setmain["SKfoto"]:
                            path = kc.downloadObjectMsg(msg_id)
                            del Setmain["SKfoto"][Cmid]
                            kb.updateProfilePicture(path)
                            kb.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Zmid in Setmain["SKfoto"]:
                            path = sw.downloadObjectMsg(msg_id)
                            del Setmain["SKfoto"][Zmid]
                            sw.updateProfilePicture(path)
                            sw.sendMessage(msg.to,"Foto berhasil dirubah")

               if msg.contentType == 1:
                 if msg._from in admin:
                   if settings["changePicture"] == True:
                     path1 = ki.downloadObjectMsg(msg_id)
                     path2 = kk.downloadObjectMsg(msg_id)
                     path3 = kc.downloadObjectMsg(msg_id)
                     path4 = kb.downloadObjectMsg(msg_id)
                     settings["changePicture"] = False
                     ki.updateProfilePicture(path1)
                     ki.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kk.updateProfilePicture(path2)
                     kk.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kc.updateProfilePicture(path3)
                     kc.sendMessage(msg.to, "Berhasil mengubah foto profike bot")
                     kb.updateProfilePicture(path4)
                     kb.sendMessage(msg.to, "Berhasil mengubah foto profike bot")

               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        cl.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "help":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage = help()
                               cl.sendMessage(msg.to, str(helpMessage))

                        if cmd == "self on":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                cl.sendMessage(msg.to, "Selfbot diaktifkan")

                        elif cmd == "self off":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                cl.sendMessage(msg.to, "Selfbot dinonaktifkan")

                        elif cmd == "help2":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage1 = helpbot()
                               cl.sendMessage(msg.to, str(helpMessage1))

                        elif cmd == "kicker status":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "╭⎓🇦🇱B◉T κι₢κεƦ🇦🇱⎓\n┋Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n┋Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]\n╰⎓⎓⎓⎓⎓⎓⎓⎓⎓⎓⎓⎓\n\n•❖{ S̶̭̗̞̙̿͑̽̆̃̒į̷̙̝̦̤̜̗́̉ͅl̸̛͓͋͋͆̍ę̶͇̮̦̣̖̙̘̪̉n̸͍̦͉̖̟͚̗̣̍̓̽̅̚ť̴̙͋ ̷̨̳̠͎̮̘͇̀̅̀͒̈́͊̕͝T̸̡̯̗̩̺͉̑́͛̌̒ͅé̶̡̱̯̮̯̊̏́̀̃͜a̴̭͓̫͚̐́̂̍̂̊̋̚m̸̨̨̹͎͍̳̥͆̓͗̿͐͗͑̿̓͠ ̴̠͐̂B̷̛̳͎̫̻̫̯̣͓̲͋̀͋̋͊̈͗͑o̵̲̾̈́͒͗t̴̢͍̫̰̠̞͖͍̬̑̊̽͒́̈́͗ͅ}❖•\n\n╭⎓⎓⎓⎓⎓⎓⎓⎓⎓⎓⎓⎓\n"
                                if wait["sticker"] == True: md+="┋ Sticker「on」\n"
                                else: md+="┋ Sticker「off」\n"
                                if wait["contact"] == True: md+="┋ Contact「on」\n"
                                else: md+="┋ Contact「off」\n"
                                if wait["talkban"] == True: md+="┋ Talkban「on」\n"
                                else: md+="┋Talkban「off」\n"
                                if wait["Mentionkick"] == True: md+="┋ Notag「on」\n"
                                else: md+="┋ Notag「off」\n"
                                if wait["detectMention"] == True: md+="┋ Respon「on」\n"
                                else: md+="┋ Respon「off」\n"
                                if wait["autoJoin"] == True: md+="┋ Autojoin「on」\n"
                                else: md+="┋ Autojoin「off」\n"
                                if wait["autoAdd"] == True: md+="┋ Autoadd「on」\n"
                                else: md+="┋ Autoadd「off」\n"
                                if msg.to in welcome: md+="┋ Welcome「on」\n"
                                else: md+="┋ Welcome「off」\n"
                                if wait["autoLeave"] == True: md+="┋ Autoleave「on」\n"
                                else: md+="┋ Autoleave「off」\n"
                                if msg.to in protectantijs: md+="┋ Protectantijs「on」\n"
                                else: md+="┋ Protectantijs「off」\n"
                                if msg.to in ghost: md+="┋ Ghost「on」\n"
                                else: md+="┋ Ghost「off」\n"
                                if msg.to in protectqr: md+="┋ Protecturl「on」\n"
                                else: md+="┋ Protecturl「off」\n"
                                if msg.to in protectjoin: md+="┋ Protectjoin「on」\n"
                                else: md+="┋ Protectjoin「off」\n"
                                if msg.to in protectkick: md+="┋ Protectkick「on」\n"
                                else: md+="┋ Protectkick「off」\n"
                                if msg.to in protectcancel: md+="┋ Protectcancel「on」\n╰⎓⎓⎓⎓⎓⎓⎓⎓⎓⎓⎓⎓⎓⎓⎓⎓"
                                else: md+="┋ Protectcancel「off」\n╰⎓⎓⎓⎓⎓⎓⎓⎓⎓⎓⎓⎓⎓"
                                cl.sendMessage(msg.to, md)

                        elif cmd == "creator" or text.lower() == 'creator':
                            if msg._from in admin:
                                cl.sendMessage(msg.to,"Creator Bots SILENTKILLER")
                                ma = ""
                                for i in creator:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "about" or cmd == "informasi":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendMention1(msg.to, sender, "「 Type Selfbot 」\n")
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)

                        elif cmd == "me" or text.lower() == 'me':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendMention(to, "「Auto Mention」\n😊@!", [sender])
                               cl.sendContact(to, sender)

                        elif text.lower() == "midku":
                               cl.sendMessage(msg.to, msg._from)
                        elif text.lower() == 'ass':
                               cl.sendMessage(msg.to, "Assalamu'alaikum Wr. Wb")
                               cl.sendMessage(msg.to, "السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                        elif text.lower() == 'wss':
                               cl.sendMessage(msg.to, "Wa'alaikumsallam.Wr,Wb")
                               cl.sendMessage(msg.to, "ُوَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ  ")
                        elif text.lower() == 'bot':
                               cl.sendMessage(msg.to, "Hadir mblo")
                        elif text.lower() == 'naga':       
                               cl.sendMessage(msg.to, None, contentMetadata={'STKID': '16510674','STKPKGID': '1433315','STKVER': '1'}, contentType = 7)
                               cl.sendMessage(msg.to, None, contentMetadata={'STKID': '16510675','STKPKGID': '1433315','STKVER': '1'}, contentType = 7)
                               cl.sendMessage(msg.to, None, contentMetadata={'STKID': '16510676','STKPKGID': '1433315','STKVER': '1'}, contentType = 7)
                               cl.sendMessage(msg.to, None, contentMetadata={'STKID': '16510677','STKPKGID': '1433315','STKVER': '1'}, contentType = 7)
                               cl.sendMessage(msg.to, None, contentMetadata={'STKID': '16510678','STKPKGID': '1433315','STKVER': '1'}, contentType = 7)
                               cl.sendMessage(msg.to, None, contentMetadata={'STKID': '16510679','STKPKGID': '1433315','STKVER': '1'}, contentType = 7)
                               cl.sendMessage(msg.to, None, contentMetadata={'STKID': '16510680','STKPKGID': '1433315','STKVER': '1'}, contentType = 7)
                               cl.sendMessage(msg.to, None, contentMetadata={'STKID': '16510681','STKPKGID': '1433315','STKVER': '1'}, contentType = 7)
                        elif ("Mid " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("Info " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "🇦🇱 Nama : "+str(mi.displayName)+"\n🇦🇱 Mid : " +key1+"\n🇦🇱 Status Msg"+str(mi.statusMessage))
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(cl.getContact(key1)):
                                   cl.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   cl.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))
                                   
                        elif cmd == "gas":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "ASSALAMUALAIKUM \nHALLOOO!!! SORRY ROOM KALIAN \n\nKEBANYAKAN ANU\nSILENT DATANG\nMAU SAPU ROOM GJ\nNO COMEND \nNO BAPER \nNO BACOT \nNO DESAH \nNO SPONSOR \nNO HATTERS\nROOM OKEP \nROOM JUDI\nROOM GAJELAS\SIAP KAMI BANTAII \n\n\n\n FUCK YOU...\nKENAPE LU PADA DIEM\nTANGKIS SU JANGAN CUMA NYIMAK\n\n\nDASAR ROOM PEA KAGAK JELAS\nSORRY BOS!!!\nGC LU MAU GUA SITA...!!!\n\n\n SALAM DARI KAMI S̴̬̦̈͛̈́̇̈́̈́͂͒I̴̡͈͓̖͉̟̲͚̮͚̾͌̂̅̈́̍̀͗̕͝L̴̯̝̣̉͜ͅḚ̵̻͆N̷̡̛͎̗̮̤̩̟̮̏̄́̔̄̀T̵̪̭͇̘̳̚ ̸̲̪̱͒́̂̀ͅK̶̨̟̥͊͑̍̆͌̎Ḯ̸̧̺͖͔̹̞̿͗̚Ļ̶̧̨̫̤͈̖͆͆̈̕̚L̵̖̤͈̜̳̉̽͋͛̈́E̸̡̖̠̦͛͜R̵͖̬̯̞̝̪̳̙̙̋͑̒͊̎̕̚͜\n\nHADIR DI ROOM ANDA\n\nRATA GAK RATA YANG PENTING KIBAR \nRATA KAMI SENANG\nGAKRATA TUNGGU KEDATANGAN KAMI LAGI\n\n\n  <<<SLAM CIAK S̴̬̦̈͛̈́̇̈́̈́͂͒I̴̡͈͓̖͉̟̲͚̮͚̾͌̂̅̈́̍̀͗̕͝L̴̯̝̣̉͜ͅḚ̵̻͆N̷̡̛͎̗̮̤̩̟̮̏̄́̔̄̀T̵̪̭͇̘̳̚ ̸̲̪̱͒́̂̀ͅK̶̨̟̥͊͑̍̆͌̎Ḯ̸̧̺͖͔̹̞̿͗̚Ļ̶̧̨̫̤͈̖͆͆̈̕̚L̵̖̤͈̜̳̉̽͋͛̈́E̸̡̖̠̦͛͜R̵͖̬̯̞̝̪̳̙̙̋͑̒͊̎̕̚͜>>> \n\n\n>>>>>>GO!!! <<<<<<\n\n\nCREATOR\n\n<<<<<<<<<<S̴̬̦̈͛̈́̇̈́̈́͂͒I̴̡͈͓̖͉̟̲͚̮͚̾͌̂̅̈́̍̀͗̕͝L̴̯̝̣̉͜ͅḚ̵̻͆N̷̡̛͎̗̮̤̩̟̮̏̄́̔̄̀T̵̪̭͇̘̳̚ ̸̲̪̱͒́̂̀ͅK̶̨̟̥͊͑̍̆͌̎Ḯ̸̧̺͖͔̹̞̿͗̚Ļ̶̧̨̫̤͈̖͆͆̈̕̚L̵̖̤͈̜̳̉̽͋͛̈́E̸̡̖̠̦͛͜R̵͖̬̯̞̝̪̳̙̙̋͑̒͊̎̕̚͜>>>>>>>>>>\n\nhttp://line.me/ti/p/~pxj5094s\nhttp://line.me/ti/p/~dhenz415")
                               cl.sendContact(to, mid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Cmid)
                               cl.sendContact(to, Dmid)
                               cl.sendContact(to, Zmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Cmid)
                               cl.sendContact(to, Dmid)
                               cl.sendContact(to, Zmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Cmid)
                               cl.sendContact(to, Dmid)
                               cl.sendContact(to, Zmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Cmid)
                               cl.sendContact(to, Dmid)
                               cl.sendContact(to, Zmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Cmid)
                               cl.sendContact(to, Dmid)
                               cl.sendContact(to, Zmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Cmid)
                               cl.sendContact(to, Dmid)
                               cl.sendContact(to, Zmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Cmid)
                               cl.sendContact(to, Dmid)
                               cl.sendContact(to, Zmid)
                               cl.sendMessage(to, None, contentMetadata={"STKID":"406","STKPKGID":"1","STKVER":"100"}, contentType=7)
                               cl.sendMessage(to, None, contentMetadata={"STKID":"406","STKPKGID":"1","STKVER":"100"}, contentType=7)
                               
                        elif text.lower() == "hapus chat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   cl.removeAllMessages(op.param2)
                               except:
                                   pass

                        elif text.lower() == "remove chat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   ki.removeAllMessages(op.param2)
                                   kk.removeAllMessages(op.param2)
                                   kc.removeAllMessages(op.param2)
                                   kb.removeAllMessages(op.param2)
                                   cl.sendMessage(msg.to,"Chat dibersihkan...")
                               except:
                                   pass

                        elif cmd.startswith("broadcast: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = cl.getGroupIdsJoined()
                               for group in saya:
                                   cl.sendMessage(group,"[ Promo ]\n" + str(pesan))

                        elif text.lower() == "mykey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Mykey」\nSetkey bot mu「 " + str(Setmain["keyCommand"]) + " 」")
                               
                        elif cmd.startswith("setkey "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendMessage(msg.to, "Gagal mengganti key")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   cl.sendMessage(msg.to, "「Setkey」\nSetkey diganti jadi「{}」".format(str(key).lower()))
                                   
                        elif cmd.startswith("/al quran "):
                            query = text.replace("/al quran ","")
                            text = query.split("-")
                            surah = int(text[0])
                            ayat1 = int(text[1])
                            ayat2 = int(text[2])
                            result = requests.get("https://farzain.xyz/api/alquran.php?id={}&from={}&to={}".format(surah, ayat1, ayat2))
                            data = result.text
                            data = json.loads(data)
                            if data["status"] == "success":
                                hasil = "「 Al-Qur'an 」\n"
                                hasil += "\n⚶Name : {}".format(str(data["nama_surat"]))
                                hasil += "\n⚶Meaning : {}".format(str(data["arti_surat"]))
                                hasil += "\n⚶Ayat :"
                                for ayat in data["ayat"]:
                                    hasil += "\n{}".format(str(ayat))
                                hasil += "\nMeaning Ayat :"
                                for arti in data["arti"]:
                                    hasil += "\n{}".format(str(arti))
                                cl.sendMessage(to, str(hasil))

                        elif text.lower() == "resetkey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["keyCommand"] = ""
                               cl.sendMessage(msg.to, "「Setkey」\nSetkey mu kembali ke awal")

                        elif cmd == "restart":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "Tunggu sebentar...")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                               cl.sendMessage(msg.to, "Silahkan gunakan seperti semula...")
                            
                        elif cmd == "runtime":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "Aktif " +waktu(eltime)
                               cl.sendMessage(msg.to,bot)
                            
                        elif cmd == "ginfo":
                          if msg._from in admin:
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
                                cl.sendMessage(msg.to, "🦂 SILENT Pro Grup Info\n\n🦂 Nama Group : {}".format(G.name)+ "\n🦂 ID Group : {}".format(G.id)+ "\n🦂 Pembuat : {}".format(G.creator.displayName)+ "\n🦂 Waktu Dibuat : {}".format(str(timeCreated))+ "\n🦂 Jumlah Member : {}".format(str(len(G.members)))+ "\n🦂 Jumlah Pending : {}".format(gPending)+ "\n🦂 Group Qr : {}".format(gQr)+ "\n🦂 Group Ticket : {}".format(gTicket))
                                cl.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                cl.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                cl.sendMessage(msg.to, str(e))

                        elif cmd.startswith("infogrup "):
                          if msg._from in admin:
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
                                ret_ += "⬅ ReyPro Grup Info\n"
                                ret_ += "\n⬅ Nama Group : {}".format(G.name)
                                ret_ += "\n⬅ ID Group : {}".format(G.id)
                                ret_ += "\n⬅ Pembuat : {}".format(gCreator)
                                ret_ += "\n⬅ Waktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\n⬅ Jumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\n⬅ Jumlah Pending : {}".format(gPending)
                                ret_ += "\n⬅ Group Qr : {}".format(gQr)
                                ret_ += "\n⬅ Group Ticket : {}".format(gTicket)
                                ret_ += ""
                                cl.sendMessage(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("infomem "):
                          if msg._from in admin:
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
                                    ret_ += "\n " "🦂 "+ str(no) + ". " + mem.displayName
                                cl.sendMessage(to,"🦂 Group Name : [ " + str(G.name) + " ]\n\n   [ List Member ]\n" + ret_ + "\n\n「Total %i Members」" % len(G.members))
                            except: 
                                pass

                        elif cmd.startswith("leave: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            for i in group:
                                ginfo = cl.getGroup(i)
                                if ginfo == group:
                                    ki.leaveGroup(i)
                                    kk.leaveGroup(i)
                                    kc.leaveGroup(i)
                                    km.leaveGroup(i)
                                    kb.leaveGroup(i)
                                    kd.leaveGroup(i)
                                    ke.leaveGroup(i)
                                    kf.leaveGroup(i)
                                    kg.leaveGroup(i)
                                    kh.leaveGroup(i)
                                    cl.sendMessage(msg.to,"Berhasil keluar di grup " +str(ginfo.name))

                        elif cmd == "fiendlist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getAllContactIds()
                               for i in gid:
                                   G = cl.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.displayName+ "\n"
                               cl.sendMessage(msg.to,"╔══[ FRIEND LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Friends ]")

                        elif cmd == "gruplist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getGroupIdsJoined()
                               for i in gid:
                                   G = cl.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               cl.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "gruplist1":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = ki.getGroupIdsJoined()
                               for i in gid:
                                   G = ki.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               ki.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "gruplist2":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kk.getGroupIdsJoined()
                               for i in gid:
                                   G = kk.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               kk.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "gruplist3":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kc.getGroupIdsJoined()
                               for i in gid:
                                   G = kc.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               kc.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "open":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "Url Opened")

                        elif cmd == "close":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "Url Closed")

                        elif cmd == "url grup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   x = cl.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      cl.updateGroup(x)
                                   gurl = cl.reissueGroupTicket(msg.to)
                                   cl.sendMessage(msg.to, "Nama : "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)

#==============BOT UPDATE============#
                        elif cmd == "updategrup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                cl.sendMessage(msg.to,"Send your images.....")

                        elif cmd == "updatebot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["changePicture"] = True
                                cl.sendMessage(msg.to,"Send your images.....")

                        elif cmd == "updatefoto":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["SKfoto"][mid] = True
                                cl.sendMessage(msg.to,"Send your images.....")

                        elif cmd == "1up":
                            if msg._from in admin:
                                Setmain["SKfoto"][Amid] = True
                                ki.sendMessage(msg.to,"Send your images.....")
                        elif cmd == "2up":
                            if msg._from in admin:
                                Setmain["SKfoto"][Bmid] = True
                                kk.sendMessage(msg.to,"Send your images.....")

                        elif cmd == "3up":
                            if msg._from in admin:
                                Setmain["SKfoto"][Cmid] = True
                                kc.sendMessage(msg.to,"Send your images.....")

                        elif cmd == "ghostup":
                            if msg._from in admin:
                                Setmain["SKfoto"][Zmid] = True
                                sw.sendMessage(msg.to,"Send your images.....")

                        elif cmd.startswith("myname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = cl.getProfile()
                                profile.displayName = string
                                cl.updateProfile(profile)
                                cl.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("1name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ki.getProfile()
                                profile.displayName = string
                                ki.updateProfile(profile)
                                ki.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("2name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kk.getProfile()
                                profile.displayName = string
                                kk.updateProfile(profile)
                                kk.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("3name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kc.getProfile()
                                profile.displayName = string
                                kc.updateProfile(profile)
                                kc.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("ghostcname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = sw.getProfile()
                                profile.displayName = string
                                sw.updateProfile(profile)
                                sw.sendMessage(msg.to,"Nama diganti jadi " + string + "")

#===========BOT UPDATE============#
                        elif cmd == "tagall" or text.lower() == 'mention':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               group = cl.getGroup(msg.to)
                               nama = [contact.mid for contact in group.members]
                               nm1, nm2, nm3, nm4,nm5,nm6,nm7, jml = [], [], [], [],[], [], [], len(nama)
                               if jml <= 20:
                                   mentionMembers(msg.to, nama)
                               if jml > 20 and jml < 40:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, len(nama)-1):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                               if jml > 40 and jml < 60:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, len(nama)-1):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                               if jml > 60 and jml < 80:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, len(nama)-1):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                               if jml > 80 and jml < 100:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, len(nama)-1):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                               if jml > 100 and jml < 120:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, len(nama)-1):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                               if jml > 120 and jml < 140:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, len(nama)-1):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                               if jml > 140 and jml < 160:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 139):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (140, len(nama)-1):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)

                        elif cmd == "listbot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"🇦🇱S̸͟͞i̸͟͞l̸͟͞e̸͟͞n̸͟͞t̸͟͞ p̸͟͞r̸͟͞o̸͟͞ bot\n\n"+ma+"\nTotal「%s」Bots" %(str(len(Bots))))

                        elif cmd == "listadmin":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
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
                                cl.sendMessage(msg.to,"🇦🇱S̸͟͞I̸͟͞L̸͟͞E̸͟͞N̸͟͞T̸͟͞ P̸͟͞R̸͟͞O̸͟͞ admin\n\nSuper admin:\n"+ma+"\nAdmin:\n"+mb+"\nStaff:\n"+mc+"\nTotal「%s」Daftar staff" %(str(len(owner)+len(admin)+len(staff))))

                        elif cmd == "listprotect":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                gid = protectqr
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectkick
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectjoin
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +cl.getGroup(group).name + "\n"
                                cl.sendMessage(msg.to,"🇦🇱 S̸͟͞I̸͟͞L̸͟͞E̸͟͞N̸͟͞T̸͟͞ Protection\n\n🇦🇱 PROTECT URL :\n"+ma+"\n🇦🇱 PROTECT KICK :\n"+mb+"\n🇦🇱 PROTECT JOIN :\n"+md+"\n🇦🇱 PROTECT CANCEL:\n"+mc+"\nTotal「%s」Grup yg dijaga" %(str(len(protectqr)+len(protectkick)+len(protectjoin)+len(protectcancel))))

                        elif cmd == "sk":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ki.sendMessage(msg.to,responsename1)
                                kk.sendMessage(msg.to,responsename2)
                                kc.sendMessage(msg.to,responsename3)
                                kb.sendMessage(msg.to,responsename4)

                        elif cmd == "kicker":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    anggota = [Amid,Bmid,Cmid,Dmid,Zmid]
                                    cl.inviteIntoGroup(msg.to, anggota)
                                    ki.acceptGroupInvitation(msg.to)
                                    kk.acceptGroupInvitation(msg.to)
                                    kc.acceptGroupInvitation(msg.to)
                                    kb.acceptGroupInvitation(msg.to)
                                    cl.sendMessage(msg.to,"Grup "+str(ginfo.name)+"Kicker sdah stay bos")
                                except:
                                    pass
                                    
                        elif cmd == "kicker stay":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    ginfo = cl.getGroup(msg.to)
                                    cl.inviteIntoGroup(msg.to, [Zmid])
                                    cl.sendMessage(msg.to,"Grup "+str(ginfo.name)+"Kicker siap stay")
                                except:
                                    pass
                                    
                          elif cmd == "kicker in":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = sw.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                sw.updateGroup(G)

                        elif cmd == "kicker lv":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                sw.leaveGroup(msg.to)

                        elif cmd == "masuk pak eko":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)

                        elif cmd == "pulang":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ki.sendMessage(msg.to, "Balik "+str(G.name))
                                ki.leaveGroup(msg.to)
                                kk.sendMessage(msg.to, "Balik "+str(G.name))
                                kk.leaveGroup(msg.to)
                                kc.sendMessage(msg.to, "Balik "+str(G.name))
                                kc.leaveGroup(msg.to)
                                kb.sendMessage(msg.to, "Balik "+str(G.name))
                                kb.leaveGroup(msg.to)
                                
                        elif cmd == "byme":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                cl.sendMessage(msg.to, "Makasih sudah invit ketemu lain waktu.. "+str(G.name))
                                cl.leaveGroup(msg.to)

                        elif cmd.startswith("leave "):
                            if msg._from in admin:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    h = cl.getGroup(i).name
                                    if h == ng:
                                        ki.sendMessage(i, "Silahkan admin invite atau masukan kembali")
                                        ki.leaveGroup(i)
                                        kk.leaveGroup(i)
                                        kc.leaveGroup(i)
                                        cl.sendMessage(to,"Berhasil keluar dari grup " +h)

                        elif cmd == "1in":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ki.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ki.updateGroup(G)

                        elif cmd == "2in":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kk.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kk.updateGroup(G)

                        elif cmd == "3in":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kc.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kc.updateGroup(G)

                        elif cmd == "ghost join":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = sw.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                sw.updateGroup(G)

                        elif cmd == "ghost bye":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                sw.leaveGroup(msg.to)

                        elif cmd == "sptime":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = cl.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = cl.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                cl.sendMessage(msg.to, "🦂 SILENT Speed respon\n\n - Get Profile\n   %.10f\n - Get Contact\n   %.10f\n - Get Group\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()
                               cl.sendMessage(msg.to, "Progres speed...")
                               elapsed_time = time.time() - start
                               cl.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               
                        elif cmd  == "mybot":
                          if msg._from in admin:
                              cl.sendContact(to, mid)
                              cl.sendContact(to, Amid)
                              cl.sendContact(to, Bmid)
                              cl.sendContact(to, Cmid)
                              cl.sendContact(to, Dmid)
                              cl.sendContact(to, Zmid)

                        elif cmd  == "midbot":
                          if msg._from in admin:
                              cl.sendMessage(msg.to,mid)
                              ki.sendMessage(msg.to,Amid)
                              kk.sendMessage(msg.to,Bmid)
                              kc.sendMessage(msg.to,Cmid)
                              kb.sendMessage(msg.to,Dmid)
                              cl.sendMessage(msg.to,Zmid)
                              
                        elif cmd == "sk":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ki.sendMessage(msg.to,responsename1)
                                kk.sendMessage(msg.to,responsename2)
                                kc.sendMessage(msg.to,responsename3)
                                kb.sendMessage(msg.to,responsename3)

                        
                        elif cmd == "sk on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    anggota = [Amid,Bmid,Cmid,Dmid,Zmid]
                                    cl.inviteIntoGroup(msg.to, anggota)
                                    ki.acceptGroupInvitation(msg.to)
                                    kk.acceptGroupInvitation(msg.to)
                                    kc.acceptGroupInvitation(msg.to)
                                    cl.sendMessage(msg.to,"Grup "+str(ginfo.name)+" pasukan stay bos")
                                except:
                                    pass

                        elif cmd == "lurking on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['SKreadPoint'][msg.to] = msg_id
                                 Setmain['SKreadMember'][msg.to] = {}
                                 cl.sendMessage(msg.to, "Lurking berhasil diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurking off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['SKreadPoint'][msg.to]
                                 del Setmain['SKreadMember'][msg.to]
                                 cl.sendMessage(msg.to, "Lurking berhasil dinoaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurkers":
                          if msg._from in admin:
                            if msg.to in Setmain['SKreadPoint']:
                                if Setmain['SKreadMember'][msg.to] != {}:
                                    aa = []
                                    for x in Setmain['SKreadMember'][msg.to]:
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
                                        cl.sendMessage(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['SKreadPoint'][msg.to]
                                        del Setmain['SKreadMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['SKreadPoint'][msg.to] = msg.id
                                    Setmain['SKreadMember'][msg.to] = {}
                                else:
                                    cl.sendMessage(msg.to, "User kosong...")
                            else:
                                cl.sendMessage(msg.to, "Ketik lurking on dulu")

                        elif cmd == "sider on":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cl.sendMessage(msg.to, "Cek sider diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
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
                           if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  cl.sendMessage(msg.to, "Cek sider dinonaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
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
                                         ret_ += "\n☉ Lokasi : " + data[0]
                                         ret_ += "\n☉ " + data[1]
                                         ret_ += "\n☉ " + data[2]
                                         ret_ += "\n☉ " + data[3]
                                         ret_ += "\n☉ " + data[4]
                                         ret_ += "\n☉ " + data[5]
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
                                    ret_ += "\n☉ Lokasi : " + data[0].replace("Temperatur di kota ","")
                                    ret_ += "\n☉ Suhu : " + data[1].replace("Suhu : ","") + " C"
                                    ret_ += "\n☉ Kelembaban : " + data[2].replace("Kelembaban : ","") + " %"
                                    ret_ += "\n☉ Tekanan udara : " + data[3].replace("Tekanan udara : ","") + " HPa"
                                    ret_ += "\n☉ Kecepatan angin : " + data[4].replace("Kecepatan angin : ","") + " m/s"
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
                                    ret_ += "\n☉ Location : " + data[0]
                                    ret_ += "\n☉ Google Maps : " + link
                                else:
                                    ret_ = "[Details Location] Error : Location not found"
                                cl.sendMessage(msg.to,str(ret_))

                        elif cmd.startswith("!"):
                           if msg._from in admin:
                               try:
                                   txt = text.replace('!','').split(' ')
                                   btype,ttype = random.choice([1,2,3,4,5]),random.choice([1,2,3,4])
                                   path = 'http://corrykalam.gq/retrowave.php?'
                                   if len(txt) == 1:
                                       params = {'text1': txt[0],'text2': '','text3': '','btype': str(btype),'ttype': str(ttype)}
                                   elif len(txt) == 2:
                                       params = {'text1': txt[0],'text2': txt[1],'text3': '','btype': str(btype),'ttype': str(ttype)}
                                   elif len(txt) == 3:
                                       params = {'text1': txt[0],'text2': txt[1],'text3': txt[2],'btype': str(btype),'ttype': str(ttype)}
                                   data = requests.get(path, params=params).json()
                                   cl.sendImageWithURL(receiver, data['image'])
                               except Exception as e:
                                   cl.sendMessage(receiver, str(e))

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
                                          cl.sendMessage(msg.to, str(ret_))
                                   except:
                                       cl.sendMessage(to, "Lirik tidak ditemukan")
                            
                        elif cmd.startswith("music: "):
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
                                          ret_ = "╔══[ Music ]"
                                          ret_ += "\n╠ Nama lagu : {}".format(str(song[0]))
                                          ret_ += "\n╠ Durasi : {}".format(str(song[1]))
                                          ret_ += "\n╠ Link : {}".format(str(song[3]))
                                          ret_ += "\n╚══[ Waiting Audio ]"
                                      cl.sendMessage(msg.to, str(ret_))
                                      cl.sendMessage(msg.to, "Mohon bersabar musicnya lagi di upload")
                                      cl.sendAudioWithURL(msg.to, song[3])
                                  except:
                                      cl.sendMessage(to, "Musik tidak ditemukan")

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
                          if msg._from in admin:
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
                                    author = '\n\n🦂 Author : ' + str(vid.author)
                                    durasi = '\n🦂 Duration : ' + str(vid.duration)
                                    suka = '\n🦂 Likes : ' + str(vid.likes)
                                    rating = '\n🦂 Rating : ' + str(vid.rating)
                                    deskripsi = '\n🦂 Deskripsi : ' + str(vid.description)
                                cl.sendVideoWithURL(msg.to, me)
                                cl.sendMessage(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                cl.sendMessage(msg.to,str(e))

                        elif cmd.startswith("ytmp3: "):
                          if msg._from in admin:
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
                                    author = '\n\n🦂 Author : ' + str(vid.author)
                                    durasi = '\n🦂 Duration : ' + str(vid.duration)
                                    suka = '\n🦂 Likes : ' + str(vid.likes)
                                    rating = '\n🦂 Rating : ' + str(vid.rating)
                                    deskripsi = '\n🦂 Deskripsi : ' + str(vid.description)
                                cl.sendImageWithURL(msg.to, me)
                                cl.sendAudioWithURL(msg.to, shi)
                                cl.sendMessage(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                cl.sendMessage(msg.to,str(e))

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
                                link = "🦂 Link : " + "https://www.instagram.com/" + instagram
                                text = "🦂 Name : "+namaIG+"\n?? Username : "+usernameIG+"\n🦂 Biography : "+bioIG+"\n🦂 Follower : "+followerIG+"\n🦂 Following : "+followIG+"\n🦂 Post : "+mediaIG+"\n🦂 Verified : "+verifIG+"\n🦂 Private : "+privateIG+"" "\n" + link
                                cl.sendImageWithURL(msg.to, profileIG)
                                cl.sendMessage(msg.to, str(text))
                            except Exception as e:
                                    cl.sendMessage(msg.to, str(e))
                        elif cmd == "cvp":
                                a = cl.downloadFileWithURL("https://youtu.be/wGC549XHh5o")
                                b = cl.downloadFileWithURL("https://youtu.be/wGC549XHh5o")
                                changeVideoAndPictureProfile(a, b)

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
                            cl.sendMessage(msg.to,"🌻 I N F O R M A S I 🌻\n\n"+"🦂 Date Of Birth : "+lahir+"\n🦂 Age : "+usia+"\n🦂 Ultah : "+ultah+"\n🦂 Zodiak : "+zodiak)

                        elif cmd.startswith("jumlah: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Setmain["SKlimit"] = num
                                cl.sendMessage(msg.to,"Total Spamtag Diubah Menjadi " +strnum)

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
                                    jmlh = int(Setmain["RAlimit"])
                                    if jmlh <= 100000:
                                        for x in range(jmlh):
                                            try:
                                                cl.sendMessage(msg)
                                            except Exception as e:
                                                cl.sendMessage(msg.to,str(e))
                                    else:
                                        cl.sendMessage(msg.to,"Jumlah melebihi 1000")
                                        
                        elif cmd == "spamcall":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                             if msg.toType == 2:
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                cl.sendMessage(msg.to, "Berhasil mengundang {} undangan Call Grup".format(str(wait["limit"])))
                                if jmlh <= 100000:
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
                              if jumlah <= 100000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      ki.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kk.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kc.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)

                        elif 'Spam: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 100000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, str(Setmain["SKmessage1"]))
                                      ki.sendMessage(midd, str(Setmain["SKmessage1"]))
                                      kk.sendMessage(midd, str(Setmain["SKmessage1"]))
                                      kc.sendMessage(midd, str(Setmain["SKmessage1"]))
                        elif cmd.startswith("spaminvid"):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    dan = text.split("|")
                                    userid = dan[1]
                                    namagrup = dan[2]
                                    jumlah = int(dan[3])
                                    grups = cl.groups
                                    tgb = cl.findContactsByUserid(userid)
                                    cl.findAndAddContactsByUserid(userid)
                                    if jumlah <= 1000:
                                        for var in range(0,jumlah):
                                            try:
                                                cl.createGroup(str(namagrup), [tgb.mid])
                                                for i in grups:
                                                	grup = cl.getGroup(i)
                                                	if grup.name == namagrup:
                                                	    cl.inviteIntoGroup(grup.id, [tgb.mid])
                                                	    cl.leaveGroup(grup.id)
                                                	    cl.sendText(to,"@! sukses spam grup!\n\nkorban: @!\njumlah: {}\nnama grup: {}".format(jumlah, str(namagrup)), [sender, tgb.mid])
                                            except Exception as e:
                                                cl.sendText(msg.to,str(e))
                                                
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

                        elif 'Protecturl ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protecturl ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = "Protect url sudah aktif"
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect url diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect url dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect url sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protectkick ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectkick ','')
                              if spl == 'on':
                                  if msg.to in protectkick:
                                       msgs = "Protect kick sudah aktif"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect kick diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect kick dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect kick sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protectinvite ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectinvite ','')
                              if spl == 'on':
                                  if msg.to in protectkick:
                                       msgs = "Protect invite sudah aktif"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect invite diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect invite dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect invite sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protectjoin ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectjoin ','')
                              if spl == 'on':
                                  if msg.to in protectjoin:
                                       msgs = "Protect join sudah aktif"
                                  else:
                                       protectjoin.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect join diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect join dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect join sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protectcancel ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectcancel ','')
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = "Protect cancel sudah aktif"
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect cancel diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect cancel dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect cancel sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                        elif 'Protectantijs ' in msg.text:
                          if msg._from in admin:
                             spl = msg.text.replace('Protectantijs ','')
                             if spl == 'on':
                                 if msg.to in protectantijs:
                                      msgs = "Protect antiJS sudah aktif"
                                 else:
                                        protectantijs.append(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "Protect antiJS diaktifkan\nDi Group : " +str(ginfo.name)
                                 cl.sendMessage(msg.to, "ãDiaktifkanã\n" + msgs)
                             elif spl == 'off':
                                   if msg.to in protectantijs:
                                        protectantijs.remove(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "Protect antiJS dinonaktifkan\nDi Group : " +str(ginfo.name)
                                   else:
                                        msgs = "Protect antiJS sudah tidak aktif"
                                   cl.sendMessage(msg.to, "ãDinonaktifkanã\n" + msgs)

                        elif 'Ghost ' in msg.text:
                          if msg._from in admin:
                             spl = msg.text.replace('Ghost ','')
                             if spl == 'on':
                                 if msg.to in ghost:
                                      msgs = "Ghost sudah aktif"
                                 else:
                                        ghost.append(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "Ghost Diaktifkan\nDi Group : " +str(ginfo.name)
                                 cl.sendMessage(msg.to, "ãDiaktifkanã\n" + msgs)
                             elif spl == 'off':
                                   if msg.to in ghost:
                                        ghost.remove(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "Ghost Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                   else:
                                        msgs = "Ghost Sudah Tidak Aktif"
                                   cl.sendMessage(msg.to, "ãDinonaktifkanã\n" + msgs)

                        elif 'Semua pro ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Semua pro ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = ""
                                  else:
                                       protectqr.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                      protectkick.append(msg.to)
                                  if msg.to in protectjoin:
                                      msgs = ""
                                  else:
                                      protectjoin.append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Semua protect sudah on\nDi Group : " +str(ginfo.name)
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Berhasil mengaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Berhasil menonaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                    else:
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Semua protect sudah off\nDi Group : " +str(ginfo.name)
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

#============================KICKOUT===============-=============#
                        elif ("Vc " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           G = cl.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           cl.updateGroup(G)
                                           invsend = 0
                                           Ticket = cl.reissueGroupTicket(msg.to)
                                           kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           kc.kickoutFromGroup(msg.to, [target])
                                           kc.leaveGroup(msg.to)
                                           X = cl.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           cl.updateGroup(X)
                                       except:
                                           pass

                        elif ("Bacok " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                           print ("kicker1 kick user")
                                       except:
                                           cl.sendMessage(msg.to,"Nothing Assist")
                        elif text.lower() == 'silentkiller':
                           if msg._from in owner or msg._from in admin or msg._from in staff:
                           	if msg.toType == 2:
                                  ginfo = cl.getGroup(msg.to)
                                  cl.sendMessage(msg.to, "Proses Cleanse....")
                                  cl.sendMessage(msg.to, "「 silentkiller 」\nmember : " +str(len(ginfo.members)) + " \nFuck you...")
                                  G = cl.getGroup(msg.to)
                                  G.preventedJoinByTicket = False
                                  cl.updateGroup(G)
                                  Ticket = cl.reissueGroupTicket(msg.to)
                                  ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  kb.acceptGroupInvitationByTicket(msg.to,Ticket) 
                                  sw.acceptGroupInvitationByTicket(msg.to,Ticket)                                                    
                                  _name = text.lower().replace('silentkiller','')
                                  gs = ki.getGroup(msg.to)
                                  gs = kk.getGroup(msg.to)
                                  gs = kc.getGroup(msg.to)
                                  gs = kb.getGroup(msg.to)
                                  gs = sw.getGroup(msg.to)
                                  targets = []
                                  for g in gs.members:
                                  	if _name in g.displayName:
                                  	   targets.append(g.mid)
                                  if targets == []:
                                  	cl.sendMessage(msg.to, "Limit bosku")
                                  else:
                                      for target in targets:
                                        if not target in Bots:
                                           if not target in admin:
                                              if not target in staff:
                                                 try:
                                                      random.choice(ABC).kickoutFromGroup(msg.to,[target])
                                                      G = cl.getGroup(msg.to)
                                                      G.preventedJoinByTicket = True
                                                      cl.updateGroup(G)
                                                      G.preventedJoinByTicket(G)
                                                      cl.updateGroup(G)
                                                 except:
                                                      pass


                        elif "Nuke" in msg.text:
                            if msg._from in admin:
                             if msg.toType == 2:
                                 print ("[ 19 ] KICK ALL MEMBER")
                                 _name = msg.text.replace("Nuke","")
                                 gs = cl.getGroup(msg.to)
                                 gs = ki.getGroup(msg.to)
                                 gs = kk.getGroup(msg.to)
                                 gs = kc.getGroup(msg.to)
                                 gs = kb.getGroup(msg.to)   
                                 cl.sendMessage(msg.to,"「 PΔPΔΨ SΨΔΠG 」")
                                 cl.sendMessage(msg.to,"「 r̸o̸o̸m̸ n̸y̸a̸ k̸a̸m̸i̸ s̸i̸t̸a̸ s̸e̸e̸ y̸o̸u̸ s̸l̸a̸m̸ d̸a̸r̸i̸ TΣΔM SILΣΠT βΩT」")
                                 targets = []
                                 for g in gs.members:
                                     if _name in g.displayName:
                                         targets.append(g.mid)
                                 if targets == []:
                                     cl.sendMessage(msg.to,"Limit boss")
                                 else:
                                     for target in targets:
                                       if not target in Bots:
                                          if not target in admin:
                                             if not target in staff:
                                                try:
                                                    klist = [ki,kk,kc,kb]
                                                    kicker=random.choice(klist)
                                                    kicker.kickoutFromGroup(msg.to,[target])
                                                    print (msg.to,[g.mid])
                                                except:
                                                    pass
                                                   
                        elif "Go" in msg.text:
                            if msg._from in admin:
                             if msg.toType == 2:
                                 print("ok")
                                 _name = msg.text.replace("Go","")
                                 gs = ki.getGroup(msg.to)
                                 gs = kk.getGroup(msg.to)
                                 gs = kc.getGroup(msg.to)
                                 gs = kb.getGroup(msg.to)
                                 cl.sendText(msg.to,"⚠ D̶A̶N̶G̶E̶R̶!!!⚠")
                                 cl.sendText(msg.to,"Proses cleanse....")
                                 cl.sendText(msg.to,"s̸l̸m̸ d̸r̸i̸ k̸a̸m̸i̸\n\n S̶̿͑̽į̷́̉l̸̛͋͋ẻ̶͇̮n̸̍̓̽ť̴̙͋ ̷̀̅̀T̸̑́͛é̶̊̏a̴̐́̂m̸͆̓͗ ̴̠͐̂B̷̛͋̀o̵̾̈́͒t̴̑̊̽\n\n")
                                 targets = []
                                 for g in gs.members:
                                     if _name in g.displayName:
                                         targets.append(g.mid)
                                 if targets == []:
                                     cl.sendText(msg.to,"l̸i̸m̸i̸t̸ b̸o̸s̸")
                                 else:
                                     for target in targets:
                                       if not target in Bots:
                                          if not target in admin:
                                            if not target in staff:
                                                try:
                                                    klist = [ki,kk,kc,kb,sw]
                                                    kicker=random.choice(klist)
                                                    kicker.kickoutFromGroup(msg.to,[target])
                                                    print (msg.to,[g.mid])
                                                except:
                                                    pass
#============================KICKOUT==========================#                                                    
                         
                        elif ("Adminadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin.append(target)
                                           cl.sendMessage(msg.to,"Berhasil menambahkan admin")
                                       except:
                                           pass

                        elif ("Staffadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           staff.append(target)
                                           cl.sendMessage(msg.to,"Berhasil menambahkan staff")
                                       except:
                                           pass

                        elif ("Botadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Bots.append(target)
                                           cl.sendMessage(msg.to,"Berhasil menambahkan bot")
                                       except:
                                           pass

                        elif ("Admindell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Saints:
                                       try:
                                           admin.remove(target)
                                           cl.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif ("Staffdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Saints:
                                       try:
                                           staff.remove(target)
                                           cl.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif ("Botdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Saints:
                                       try:
                                           Bots.remove(target)
                                           cl.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif cmd == "admin:on" or text.lower() == 'admin:on':
                            if msg._from in admin:
                                wait["addadmin"] = True
                                cl.sendMessage(msg.to,"Please send to contact...")

                        elif cmd == "admin:repeat" or text.lower() == 'admin:repeat':
                            if msg._from in admin:
                                wait["delladmin"] = True
                                cl.sendMessage(msg.to,"Please send to contact...")

                        elif cmd == "staff:on" or text.lower() == 'staff:on':
                            if msg._from in admin:
                                wait["addstaff"] = True
                                cl.sendMessage(msg.to,"Please send to contact...")

                        elif cmd == "staff:repeat" or text.lower() == 'staff:repeat':
                            if msg._from in admin:
                                wait["dellstaff"] = True
                                cl.sendMessage(msg.to,"Please send to contact...")

                        elif cmd == "bot:on" or text.lower() == 'bot:on':
                            if msg._from in admin:
                                wait["addbots"] = True
                                cl.sendMessage(msg.to,"Please send to contact...")

                        elif cmd == "bot:repeat" or text.lower() == 'bot:repeat':
                            if msg._from in admin:
                                wait["dellbots"] = True
                                cl.sendMessage(msg.to,"Please send to contact...")

                        elif cmd == "refresh" or text.lower() == 'refresh':
                            if msg._from in admin:
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
                                cl.sendMessage(msg.to,"Berhasil di Refresh...")

                        elif cmd == "contact admin" or text.lower() == 'contact admin':
                            if msg._from in admin:
                                ma = ""
                                for i in admin:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact staff" or text.lower() == 'contact staff':
                            if msg._from in admin:
                                ma = ""
                                for i in staff:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact bot" or text.lower() == 'contact bot':
                            if msg._from in admin:
                                ma = ""
                                for i in Bots:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

#===========COMMAND ON OFF============#
                        elif cmd == "notag on" or text.lower() == 'notag on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = True
                                cl.sendMessage(msg.to,"Notag diaktifkan")

                        elif cmd == "notag off" or text.lower() == 'notag off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["MentionKick"] = False
                                cl.sendMessage(msg.to,"Notag dinonaktifkan")

                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = True
                                cl.sendMessage(msg.to,"Deteksi contact diaktifkan")

                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = False
                                cl.sendMessage(msg.to,"Deteksi contact dinonaktifkan")

                        elif cmd == "respon on" or text.lower() == 'respon on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = True
                                cl.sendMessage(msg.to,"Auto respon diaktifkan")

                        elif cmd == "respon off" or text.lower() == 'respon off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = False
                                cl.sendMessage(msg.to,"Auto respon dinonaktifkan")
                                
                        elif cmd == "talkban on" or text.lower() == 'talkban on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["talkban"] = True
                                cl.sendMessage(msg.to,"Talk Ban diaktifkan")

                        elif cmd == "talkban off" or text.lower() == 'talkban off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["talkban"] = False
                                cl.sendMessage(msg.to,"Talk Ban dinonaktifkan")

                        elif cmd == "autojoin on" or text.lower() == 'autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = True
                                cl.sendMessage(msg.to,"Autojoin diaktifkan")

                        elif cmd == "autojoin off" or text.lower() == 'autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = False
                                cl.sendMessage(msg.to,"Autojoin dinonaktifkan")

                        elif cmd == "autoleave on" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = True
                                cl.sendMessage(msg.to,"Autoleave diaktifkan")

                        elif cmd == "autoleave off" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = False
                                cl.sendMessage(msg.to,"Autoleave dinonaktifkan")

                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = True
                                cl.sendMessage(msg.to,"Auto add diaktifkan")

                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = False
                                cl.sendMessage(msg.to,"Auto add dinonaktifkan")

                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = True
                                cl.sendMessage(msg.to,"Deteksi sticker diaktifkan")

                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = False
                                cl.sendMessage(msg.to,"Deteksi sticker dinonaktifkan")

                        elif cmd == "jointicket on" or text.lower() == 'jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinTicket"] = True
                                cl.sendMessage(msg.to,"Join ticket diaktifkan")

                        elif cmd == "jointicket off" or text.lower() == 'jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinTicket"] = False
                                cl.sendMessage(msg.to,"Join ticket dinonaktifkan")

#===========COMMAND BLACKLIST============#
                        elif ("Talkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["Talkblacklist"][target] = True
                                           cl.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Untalkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
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
                            if msg._from in admin:
                                wait["Talkwblacklist"] = True
                                cl.sendMessage(msg.to,"Please send to contact...")

                        elif cmd == "untalkban:on" or text.lower() == 'untalkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkdblacklist"] = True
                                cl.sendMessage(msg.to,"Please send to contact...")

                        elif ("Ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["blacklist"][target] = True
                                           cl.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Unban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
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
                            if msg._from in admin:
                                wait["wblacklist"] = True
                                cl.sendMessage(msg.to,"Please send to contact...")

                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["dblacklist"] = True
                                cl.sendMessage(msg.to,"Please send to contact...")

                        elif cmd == "banlist" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                cl.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"🦂 SILENT Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(wait["blacklist"]))))

                        elif cmd == "talkbanlist" or text.lower() == 'talkbanlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["Talkblacklist"] == {}:
                                cl.sendMessage(msg.to,"Tidak ada Talkban user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"🦂 SILENT Talkban User\n\n"+ma+"\nTotal「%s」Talkban User" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "blc" or text.lower() == 'blc':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                    cl.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = cl.getContact(i)
                                        cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "clearban" or text.lower() == 'clearban':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = cl.getContacts(wait["blacklist"])
                              mc = "「%i」User Blacklist" % len(ragets)
                              cl.sendMessage(msg.to,"Sukses membersihkan " +mc)
#===========COMMAND SET============#
                        elif 'Set pesan: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set pesan: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Pesan Msg")
                              else:
                                  wait["message"] = spl
                                  cl.sendMessage(msg.to, "「Pesan Msg」\nPesan Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set welcome: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set welcome: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Welcome Msg")
                              else:
                                  wait["welcome"] = spl
                                  cl.sendMessage(msg.to, "「Welcome Msg」\nWelcome Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set respon: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set respon: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag"] = spl
                                  cl.sendMessage(msg.to, "「Respon Msg」\nRespon Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set spam: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set spam: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Spam")
                              else:
                                  Setmain["SKmessage1"] = spl
                                  cl.sendMessage(msg.to, "「Spam Msg」\nSpam Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set sider: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set sider: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Sider Msg")
                              else:
                                  wait["mention"] = spl
                                  cl.sendMessage(msg.to, "「Sider Msg」\nSider Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif text.lower() == "cek pesan":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Pesan Msg」\nPesan Msg mu :\n\n「 " + str(wait["message"]) + " 」")

                        elif text.lower() == "cek welcome":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Welcome Msg」\nWelcome Msg mu :\n\n「 " + str(wait["welcome"]) + " 」")

                        elif text.lower() == "cek respon":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Respon Msg」\nRespon Msg mu :\n\n「 " + str(wait["Respontag"]) + " 」")

                        elif text.lower() == "cek spam":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Spam Msg」\nSpam Msg mu :\n\n「 " + str(Setmain["RAmessage1"]) + " 」")

                        elif text.lower() == "cek sider":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Sider Msg」\nSider Msg mu :\n\n「 " + str(wait["mention"]) + " 」")

#===========JOIN TICKET============
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                            if msg._from in admin:
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
                                     group1 = ki.findGroupByTicket(ticket_id)
                                     ki.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     ki.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group2 = kk.findGroupByTicket(ticket_id)
                                     kk.acceptGroupInvitationByTicket(group2.id,ticket_id)
                                     kk.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group3 = kc.findGroupByTicket(ticket_id)
                                     kc.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     kc.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group4 = kb.findGroupByTicket(ticket_id)
                                     kb.acceptGroupInvitationByTicket(group4.id,ticket_id)
                                     kb.sendMessage(msg.to, "Masuk : %s" % str(group.name))

    except Exception as error:
        print (error)


while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
               # bot(op)
                # Don't remove this line, if you wan't get error soon!
                oepoll.setRevision(op.revision)
                thread1 = threading.Thread(target=bot, args=(op,))#self.OpInterrupt[op.type], args=(op,)
                #thread1.daemon = True
                thread1.start()
                thread1.join()
    except Exception as e:
        pass

