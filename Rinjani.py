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

botStart = time.time()
cl = LineClient(authToken='EokwoZ3iLj4USHMmSEF2.dgInDWWhfUrDRhkxlnH/iG.T9Bit+FaGq5CwB3V4zVYaTDaacTkt0dXGZ2G/erIHGw=')
cl.log("Auth Token : " + str(cl.authToken))
channel = LineChannel(cl)
cl.log("Channel Access Token : " + str(channel.channelAccessToken))

ki = LineClient(authToken='EnPikSj2k5Kw610SdvL0.4JH9B269AVZoWnkXc4HV8a.4BshV6dhnUKo8WitAp0Md6FpGqZUH4O7s3Y15hGEnAo=')
ki.log("Auth Token : " + str(ki.authToken))

kk = LineClient(authToken='EnglX9wnOWNPHTsbsNG4.2rFg3yOIB3WltnJBM85sfa.Mj3oTotl4+/+k1i88+JgVZR78BvQGbB9snuaPE1SofA=')
kk.log("Auth Token : " + str(kk.authToken))

kc = LineClient(authToken='EnxXpFG19Uvwe9OvGdfe.85aBcMuVNAjJX9KKPZidZG.J+FZNd+dQ+tCSurTD9S7Pb1fMF+bHWmLnVGBH/q94sU=')
kc.log("Auth Token : " + str(kc.authToken))

ks = LineClient(authToken='EnuFXhanijULkFFoP0sf.TFNjkysE9CP3h/sJLfoDJW.WOVC9zBGfdN8IgvCqua46CzbI6GGw0wuRAiFCRuMz+0=')
ks.log("Auth Token : " + str(ks.authToken))


settingsOpen = codecs.open("rinjani.json","r","utf-8")
poll = LinePoll(cl)
clientProfile = cl.getProfile()
clientSettings = cl.getSettings()

mid = cl.profile.mid
call = LineCall(cl)
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = ks.getProfile().mid
DEF = [ki,kk,cl,kc,ks]
KIC = [ki,kk,kc]
KAC = [ks,ki,kk,kc]
Bots = [mid,Amid,Bmid,Cmid,Dmid,"uc17663698bf499304c0b424c2dbaf754"]
protectname = []
protecturl = []
autocancel = {}
BlockACCESS = {}

settings = json.load(settingsOpen)
if settings["restartPoint"] != None:
    cl.sendMessage(settings["restartPoint"], "Bot kembali aktif")
contact = cl.getProfile()
backup = cl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
wait={
    "copy":False,
    "copy2":"target",
    "target":{}
}
cctv={
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

switch = {
    'winvite':False,
    'dinvite':False,
    'wblacklist':False,
    'dblacklist':False,
    'wrin':False,
    'drin':False,
    'cp1':False,
    'cp2':False,
    'cp3':False,
    'cp4':False,
    'changePicture':False
}


## -*- Script Start -*- ##
def restartBot():
    print ("[ INFO ] BOT RESETTED")
    python = sys.executable
    os.execl(python, python, *sys.argv)

def autoRestart():
    if time.time() - botStart > int(settings["timeRestart"]):
        backupData()
        time.sleep(5)
        restartBot()

def logError(text):
    cl.log("[ ERROR ] " + str(text))
    time = datetime.now()

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)

def download_page(url):
    try:
        headers = {}
        headers['User-Agent'] = random.choice(settings["userAgent"])
        req = urllib.request.Request(url, headers = headers)
        resp = urllib.request.urlopen(req)
        respData = str(resp.read())
        return respData
    except Exception as e:
        logError(e)
            
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content

def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)
            page = page[end_content:]
    return items

def translate(to_translate, to_language="auto"):
    bahasa_awal = "auto"
    bahasa_tujuan = to_language
    kata = to_translate
    url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
    agent = {'User-Agent':random.choice(settings["userAgent"])}
    cari_hasil = 'class="t0">'
    request = urllib.parse.Request(url, headers=agent)
    page = urllib.parse.urlopen(request).read()
    result = page[page.find(cari_hasil)+len(cari_hasil):]
    result = result.split("<")[0]
    return result

def sendMention(to, mid, firstmessage, lastmessage):
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
        sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "╔══[Mention {} User]\n╠ ".format(str(len(mid)))
        arr = []
        no = 1
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "╠ "
            else:
                try:
                    no = "╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))


def help():
    helpMessage = "╞[RINJANI BOT]" + "\n" + \
                  "\n" + "[Command Set]\n\n" + \
                  "╞[Main on/off" + "\n" + \
                  "╞[Block/Allow invite" + "\n" + \
                  "╞[Block/Allow url" + "\n" + \
                  "╞[Chat on/off" + "\n" + \
                  "╞[Greet on/off" + "\n" + \
                  "╞[Auto/Manual]respon" + "\n" + \
                  "╞[Auto/Manual] join" + "\n" + \
                  "╞[Rin normal/Rinjani" + "\n" + \
                  "╞[Kontak on/off" + "\n" + \
                  "╞[Name lock/unlock" + "\n" + \
                  "╞[Autoread" + "\n" + \
                  "╞[Manualread"
    return helpMessage

def help2():
    helpMessage2 = "╞[RINJANI BOT]" + "\n" + \
                  "\n" + "[Command Self]\n\n" + \
                  "╞[Sayang" + "\n" + \
                  "╞[Cok" + "\n" + \
                  "╞[Banlist" + "\n" + \
                  "╞[/Invite2:「GID」" + "\n" + \
                  "╞[Lihat grup" + "\n" + \
                  "╞[Respons" + "\n" + \
                  "╞[/Left:「GID」" + "\n" + \
                  "╞[/undang:「MID」" + "\n" + \
                  "╞[Mangat." + "\n" + \
                  "╞[Buka link" + "\n" + \
                  "╞[Tutup link" + "\n" + \
                  "╞[Nama bot/2-4:「NAMA」" + "\n" + \
                  "╞[All name:「NAMA」" + "\n" + \
                  "╞[Cancel" + "\n" + \
                  "╞[Cek sambutan" + "\n" + \
                  "╞[Cek left" + "\n" + \
                  "╞[Cek add" + "\n" + \
                  "╞[Undang orang 「SC」" + "\n" + \
                  "╞[Add ban 「SC」" + "\n" + \
                  "╞[Unban 「SC」" + "\n" + \
                  "╞[Pancal 「TAG」" + "\n" + \
                  "╞[Sikat 「TAG」" + "\n" + \
                  "╞[Sampul 「TAG」" + "\n" + \
                  "╞[Kepo 「TAG」" + "\n" + \
                  "╞[Status:「STATUS」" + "\n" + \
                  "╞[Gn:「NAMA」" + "\n" + \
                  "╞[Add wl「TAG」" + "\n" + \
                  "╞[Del wl「TAG」" + "\n" + \
                  "╞[Wl all" + "\n" + \
                  "╞[Ban all" + "\n" + \
                  "╞[Unban all" + "\n" + \
                  "╞[Tambah teman「SC」" + "\n" + \
                  "╞[Hapus teman「SC」" + "\n" + \
                  "╞[Temanku" + "\n" + \
                  "╞[Fbc「PESAN BC」" + "\n" + \
                  "╞[Gbc「PESAN BC」" + "\n" + \
                  "╞[Allbc「PESAN BC」" + "\n" + \
                  "╞[Cbot「TAG」" + "\n" + \
                  "╞[C1-4「TAG」" + "\n" + \
                  "╞[/Pundhut「TAG」" + "\n" + \
                  "╞[/Cipok「TAG」" + "\n" + \
                  "╞[PP 1-4「IMAGE」" + "\n" + \
                  "╞[@Bubar " + "\n" + \
                  "╞[Sikat lurrr" + "\n" + \
                  "╞[Takbir !!!" + "\n" + \
                  "╞[/Sambutan:「TEXT」" + "\n" + \
                  "╞[/Pesan left:「TEXT」" + "\n" + \
                  "╞[/Pesan add:「TEXT」" + "\n" + \
                  "╞[Ampuni 「TAG」" + "\n" + \
                  "╞[Bann 「TAG」"
    return helpMessage2

def help3():
    helpMessage3 = "╞[RINJANI BOT]" + "\n" + \
                  "\n" + "[Command Fun]\n\n" + \
                  "╞[Me" + "\n" + \
                  "╞[Sp" + "\n" + \
                  "╞[Ganti pp" + "\n" + \
                  "╞[Ganti pp grup" + "\n" + \
                  "╞[Mid 「TAG」" + "\n" + \
                  "╞[Runtime" + "\n" + \
                  "╞[My set" + "\n" + \
                  "╞[Deteksi cctv" + "\n" + \
                  "╞[Intip" + "\n" + \
                  "╞[,Pamit dulu ya" + "\n" + \
                  "╞[Gid" + "\n" + \
                  "╞[Midku" + "\n" + \
                  "╞[Creator" + "\n" + \
                  "╞[Empunya" + "\n" + \
                  "╞[/Ig「ID IG」" + "\n" + \
                  "╞[/Bilang「KALIMAT」" + "\n" + \
                  "╞[Jadwal sholat:「LOKASI」" + "\n" + \
                  "╞[Cuaca「LOKASI」" + "\n" + \
                  "╞[/Lirik「JUDUL LAGU」" + "\n" + \
                  "╞[/Film「TITLE」" + "\n" + \
                  "╞[/Wiki「KEYWORD」" + "\n" + \
                  "╞[.Crash" + "\n" + \
                  "╞[/Nonton:「JUDUL」" + "\n" + \
                  "╞[/music「JUDUL」" + "\n" + \
                  "╞[/mp3:「JUDUL」" + "\n" + \
                  "╞[/video:「JUDUL」" + "\n" + \
                  "╞[MIMIC]" + "\n" + \
                  "╞[Halo kak「TAG」" + "\n" + \
                  "╞[Kopi kak" + "\n" + \
                  "╞[Kopi abis" + "\n" + \
                  "╞[Udahan「TAG」" + "\n" + \
                  "╞[Targetku" + "\n" + \
                  "╞[Bacot lu」" + "\n" + \
                  "╞[Ginfo" + "\n" + \
                  "╞[Haloo" + "\n" + \
                  "╞[Cek lokasi「LOKASI」"

    return helpMessage3

def backupData():
    try:
        backup = settings
        f = codecs.open('rinjani.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False

groupParam = ""
def SiriGetOut(targ):
    cl.kickoutFromGroup(groupParam,[targ])
def byuh(targ):
    random.choice(KAC).kickoutFromGroup(groupParam,[targ])
def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 5:
            print ("[ 5 ] NOTIFIED ADD CONTACT")
            if settings["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
            cl.sendMessage(op.param1, "Makasih {} dah add ya\n\n".format(str(cl.getContact(op.param1).displayName)) + settings["cot"])
            arg = "   New Friend : {}".format(str(cl.getContact(op.param1).displayName))
            print (arg)
        if op.type == 11:
            if op.param3 == "1":
                if op.param1 in settings['pname']:
                    try:
                        G = cl.getGroup(op.param1)
                    except:
                        pass
                    G.name = settings['pro_name'][op.param1]
                    if op.param2 in Bots:
                        pass
                        print("[admin] Ubah nama")
                    else:
                        try: 
                            cl.updateGroup(G)
                        except:
                           pass
                    if op.param2 in Bots:
                        pass
                        print("Bot mengubah nama")
                    elif op.param2 in settings["Rinjani"]:
                        pass
                        print("whitelist mengubah nama")
                    else:
                        try:
                           ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            pass
                            cl.sendMessage(op.param1,"Nama grup di kunci")
                            c = Message(to=op.param1, _from=None, text=None, contentType=13)
                            c.contentMetadata={'mid':op.param2}
                            cl.sendMessage(c)
                            print("Nama grup diubah")
        if op.param3 == "1":
            if op.param1 in protectname:
                group = cl.getGroup(op.param1)
                try:
                    group.name = settings["pro_name"][op.param1]
                    cl.updateGroup(group)
                    cl.sendMessage(op.param1, "nama grup di kunci")
                    settings["blacklist"][op.param2] = True
                except Exception as e:
                    print(e)
                    pass
        if op.param3 == "4":
          if op.param1 in settings["protecturl"]:
            if op.param1 in settings["main"]:
             if op.param2 in Bots or op.param2 in settings["Rinjani"]:
                pass
             else:
                 random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                 settings["blacklist"][op.param2] = True
                 cl.reissueGroupTicket(op.param1)
                 X = cl.getGroup(op.param1)
                 X.preventedJoinByTicket = True
                 cl.updateGroup(X)
                 settings["blacklist"][op.param2] = True
            else:
             if op.param2 in Bots or op.param2 in settings["Rinjani"]:
                pass
             else:
                 cl.reissueGroupTicket(op.param1)
                 X = cl.getGroup(op.param1)
                 X.preventedJoinByTicket = True
                 cl.updateGroup(X)

        if op.type == 13:
            if mid in op.param3:
              if op.param2 in Bots:
                cl.acceptGroupInvitation(op.param1)
              else:
                G = cl.getGroup(op.param1)
                if settings['autoJoin'] == True:
                    cl.acceptGroupInvitation(op.param1)
                else:
                  print("[NOTIF] AUTO JOIN OFF BOS")
            if Amid in op.param3:
              if op.param2 in Bots:
                G = ki.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    if settings["autocancel"]["on"] == True:
                        if len(G.members) <= settings["autocancel"]["members"]:
                            ki.rejectGroupInvitation(op.param1)
                        else:
                            ki.acceptGroupInvitation(op.param1)
                            print("Bot 2 masuk")
                    else:
                        ki.acceptGroupInvitation(op.param1)
                        print("Bot 2 masuk")
                elif settings["autocancel"]["on"] == True:
                    if len(G.members) <= settings["autocancel"]["members"]:
                        ki.rejectGroupInvitation(op.param1)
                        print("Bot 2 autocancel")
            if Bmid in op.param3:
              if op.param2 in Bots:
                G = kk.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    if settings["autocancel"]["on"] == True:
                        if len(G.members) <= settings["autocancel"]["members"]:
                            kk.rejectGroupInvitation(op.param1)
                        else:
                            kk.acceptGroupInvitation(op.param1)
                            print("Bot 3 masuk")
                    else:
                        kk.acceptGroupInvitation(op.param1)
                        print("Bot 3 masuk")
                elif settings["autocancel"]["on"] == True:
                    if len(G.members) <= settings["autocancel"]["members"]:
                        kk.rejectGroupInvitation(op.param1)
                        print("Bot 3 autocancel")

            if Cmid in op.param3:
              if op.param2 in Bots:
                G = kc.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    if settings["autocancel"]["on"] == True:
                        if len(G.members) <= settings["autocancel"]["members"]:
                            kc.rejectGroupInvitation(op.param1)
                        else:
                            kc.acceptGroupInvitation(op.param1)
                            print("Bot 4 masuk")
                    else:
                        kc.acceptGroupInvitation(op.param1)
                        print("Bot 4 masuk")
                elif settings["autocancel"]["on"] == True:
                    if len(G.members) <= settings["autocancel"]["members"]:
                        kc.rejectGroupInvitation(op.param1)
                        print("Bot 4 autocancel")

            if Dmid in op.param3:
              if op.param2 in Bots:
                G = ks.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    if settings["autocancel"]["on"] == True:
                        if len(G.members) <= settings["autocancel"]["members"]:
                            ks.rejectGroupInvitation(op.param1)
                        else:
                            ks.acceptGroupInvitation(op.param1)
                            print("Bot 5 masuk")
                    else:
                        ks.acceptGroupInvitation(op.param1)
                        print("Bot 5 masuk")
                elif settings["autocancel"]["on"] == True:
                    if len(G.members) <= settings["autocancel"]["members"]:
                        ks.rejectGroupInvitation(op.param1)
                        print("Bot 5 autocancel")
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in settings["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    ki.cancelGroupInvitation(op.param1, matched_list)
                    kk.cancelGroupInvitation(op.param1, matched_list)
                    kc.cancelGroupInvitation(op.param1, matched_list)
                    ks.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 13:
         if op.param1 in settings["autocancel"]:
          if op.param1 in settings["main"]:
            if op.param2 in Bots or op.param2 in settings["Rinjani"]:
               pass
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                contact = cl.getContact(op.param2)
                cl.cancelGroupInvitation(op.param1,InviterX)
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                settings["blacklist"][op.param2] = True
          else:
            if op.param2 in Bots or op.param2 in settings["Rinjani"]:
               pass
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                contact = cl.getContact(op.param2)
                cl.cancelGroupInvitation(op.param1,InviterX)

        if op.type == 15:
            if settings['greet'] == True:
                if op.param2 in Bots:
                    return
                cl.sendMessage(op.param1,settings["left"])

        if op.type == 17:
            if settings['greet'] == True:
              ginfo = cl.getGroup(op.param1)
              cl.sendMessage(op.param1, "Selamat datang di " + str(ginfo.name))
              cl.sendMessage(op.param1, settings["greeting"])
        if op.type == 17:
            if op.param1 in BlockACCESS:
              if op.param2 not in Bots or op.param2 not in settings["Rinjani"]:
                    random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
                    settings["blacklist"][op.param2] = True
              else:
                  pass
            else:
                pass


        if op.type == 17:
            if mid in op.param3:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in settings["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendMessage(msg.to,"tidak ada yang diblacklist")
                        return
                    for jj in matched_list:
                        random.choice(DEF).kickoutFromGroup(msg.to,[jj])
                    cl.sendMessage(msg.to,"done")
        if op.type == 17:
            if op.param2 in settings["blacklist"]:
               try:
                   random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
               except:
                     random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
                     print("[Notif]Blacklist User Kick")
            else:
                pass
                print("[Wong] Join")

        if op.type == 19:
            if mid in op.param3:
                print("Bots1 has been kicked")
                if op.param2 in Bots:
                    X = ki.getGroup(op.param1)
                    X.preventedJoinByTicket = False
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventedJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                else:
                    settings["blacklist"][op.param2] = True
                    print("Kicker has been blacklist")
                    try:
                        X = ki.getGroup(op.param1)
                        X.preventedJoinByTicket = False
                        ki.updateGroup(X)
                        Ti = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ti)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        kk.acceptGroupInvitationByTicket(op.param1,Ti)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        ks.acceptGroupInvitationByTicket(op.param1,Ti)
                        X = cl.getGroup(op.param1)
                        X.preventedJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        print("Bots1 Joined openqr")
                    except:
                        try:
                            kc.inviteIntoGroup(op.param1,[op.param3])
                            cl.acceptGroupInvitation(op.param1)
                            ks.kickoutFromGroup(op.param1,[op.param2])
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
                                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                G = cl.getGroup(op.param1)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                                Ticket = ki.reissueGroupTicket(op.param1)
                                print("Bots1 Joined Open Qr 1")
                            except:
                                G = ks.getGroup(op.param1)
                                G.preventedJoinByTicket = False
                                ks.updateGroup(G)
                                Ticket = ks.reissueGroupTicket(op.param1)
                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
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
                    Ti = cl.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventedJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                else:
                    settings["blacklist"][op.param2] = True
                    print("Kicker has been blacklist")
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        X = kc.getGroup(op.param1)
                        X.preventedJoinByTicket = False
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        ks.kickoutFromGroup(op.param1,[op.param2])
                        cl.acceptGroupInvitationByTicket(op.param1,Ti)
                        kk.acceptGroupInvitationByTicket(op.param1,Ti)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        ks.acceptGroupInvitationByTicket(op.param1,Ti)
                        X = cl.getGroup(op.param1)
                        X.preventedJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        print("Bots2 Joined openqr")
                    except:
                        try:
                            kk.inviteIntoGroup(op.param1,[op.param3])
                            ki.acceptGroupInvitation(op.param1)
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            print("Bots2 Joined Invite 2")
                        except:
                            try:
                                ks.kickoutFromGroup(op.param1,[op.param2])
                                G = cl.getGroup(op.param1)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                Ticket = cl.reissueGroupTicket(op.param1)
                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
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
                                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
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
                    Ti = cl.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventedJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                else:
                    settings["blacklist"][op.param2] = True
                    print("Kicker has been blacklist")
                    try:
                        X = ks.getGroup(op.param1)
                        X.preventedJoinByTicket = False
                        ks.updateGroup(X)
                        Ti = ks.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,Ti)
                        cl.acceptGroupInvitationByTicket(op.param1,Ti)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        ks.acceptGroupInvitationByTicket(op.param1,Ti)
                        X = cl.getGroup(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        X.preventedJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        print("Bots3 Joined openqr")
                    except:
                        try:
                            cl.inviteIntoGroup(op.param1,[op.param3])
                            kk.acceptGroupInvitation(op.param1)
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            print("Bots3 Joined Invite 2")
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                G = ki.getGroup(op.param1)
                                G.preventedJoinByTicket = False
                                ki.updateGroup(G)
                                Ticket = ki.reissueGroupTicket(op.param1)
                                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                G = ki.getGroup(op.param1)
                                G.preventedJoinByTicket = True
                                ki.updateGroup(G)
                                Ticket = ki.reissueGroupTicket(op.param1)
                                print("Bots3 Joined Open Qr 1")
                            except:
                                G = kc.getGroup(op.param1)
                                G.preventedJoinByTicket = False
                                kc.updateGroup(G)
                                Ticket = kc.reissueGroupTicket(op.param1)
                                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                G = cl.getGroup(op.param1)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                                ks.kickoutFromGroup(op.param1,[op.param2])
                                Ticket = cl.reissueGroupTicket(op.param1)
                                print("Bots3 Joined Open Qr 2")

            if Cmid in op.param3:
                print("Bots4 has been kicked")
                if op.param2 in Bots:
                    X = cl.getGroup(op.param1)
                    X.preventedJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventedJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                else:
                    settings["blacklist"][op.param2] = True
                    print("Kicker has been blacklist")
                    try:
                        X = kk.getGroup(op.param1)
                        X.preventedJoinByTicket = False
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        cl.acceptGroupInvitationByTicket(op.param1,Ti)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        kk.acceptGroupInvitationByTicket(op.param1,Ti)
                        ks.acceptGroupInvitationByTicket(op.param1,Ti)
                        X = kk.getGroup(op.param1)
                        X.preventedJoinByTicket = True
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)
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
                                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                G = ki.getGroup(op.param1)
                                G.preventedJoinByTicket = True
                                ki.updateGroup(G)
                                Ticket = ki.reissueGroupTicket(op.param1)
                                print("Bots4 Joined Open Qr 1")
                            except:
                                G = ks.getGroup(op.param1)
                                G.preventedJoinByTicket = False
                                ks.updateGroup(G)
                                Ticket = ks.reissueGroupTicket(op.param1)
                                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
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
                    Ti = cl.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventedJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                else:
                    settings["blacklist"][op.param2] = True
                    print("Kicker has been blacklist")
                    try:
                        X = kc.getGroup(op.param1)
                        X.preventedJoinByTicket = False
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                        ks.acceptGroupInvitationByTicket(op.param1,Ti)
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        cl.acceptGroupInvitationByTicket(op.param1,Ti)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        kk.acceptGroupInvitationByTicket(op.param1,Ti)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        X = kk.getGroup(op.param1)
                        X.preventedJoinByTicket = True
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)
                        print("Bots4 Joined openqr")
                    except:
                        try:
                            kk.inviteIntoGroup(op.param1,[op.param3])
                            ks.acceptGroupInvitation(op.param1)
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            print("Bots4 Joined Invite 2")
                        except:
                            try:
                                ki.kickoutFromGroup(op.param1,[op.param2])
                                G = kk.getGroup(op.param1)
                                G.preventedJoinByTicket = False
                                kk.updateGroup(G)
                                Ticket = kk.reissueGroupTicket(op.param1)
                                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
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
                                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
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

            if op.param3 in settings["Rinjani"]:
                print("admin was kicked")
                if op.param2 in Bots or op.param2 in settings["Rinjani"]:
                   kk.findAndAddContactsByMid(op.param3)
                   kk.inviteIntoGroup(op.param1,[op.param3])
                else:
                    cl.findAndAddContactsByMid(op.param3)
                    cl.inviteIntoGroup(op.param1,[op.param3])
                    settings["blacklist"][op.param2] = True
                    cl.kickoutFromGroup(op.param1,[op.param2])

            if op.param2 not in Bots or op.param2 not in settings["Rinjani"]:
             if op.param1 in settings["main"]:
                random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
                settings["blacklist"][op.param2] = True
             else:
                pass
        if op.type == 22:
            print ("[ 22 ] NOTIFIED INVITE INTO ROOM")
            if settings["autoLeave"] == True:
                cl.sendMessage(op.param1, "Kampret invite aku")
                cl.leaveRoom(op.param1)

        if op.type == 24:
            print ("[ 24 ] NOTIFIED LEAVE ROOM")
            if settings["autoLeave"] == True:
                cl.sendMessage(op.param1, "Apaan ini Goblok")
                cl.leaveRoom(op.param1)

        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from

            # Check if in group chat or personal chat
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                # Check if only text message
                if msg.contentType == 13:
                   if switch["winvite"] == True:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 cl.sendMessage(msg.to,"Wonge " + _name + " Wis nang kene")
                                 break
                             elif invite in settings["blacklist"]:
                                 cl.sendMessage(msg.to,"Sepurane lurr " + _name + " iku wong bejat")
                                 break
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     kk.findAndAddContactsByMid(target)
                                     kk.inviteIntoGroup(msg.to,[target])
                                     cl.sendMessage(msg.to,"Done bro " + _name)
                                     switch["winvite"] = False
                                     break
                                 except:
                                     try:
                                         ki.findAndAddContactsByMid(invite)
                                         ki.inviteIntoGroup(op.param1,[invite])
                                         switch["winvite"] = False
                                     except:
                                         cl.sendMessage(msg.to,"Sepurane limit lurr")
                                         switch["winvite"] = False
                                         break
                   elif switch["wblacklist"] == True:
                       if msg.contentMetadata["mid"] in settings["blacklist"]:
                            cl.sendMessage(msg.to,"Termasuk orang bejat")
                            switch["wblacklist"] = False
                            print("MID Already in the Blacklist")
                       else:
                            settings["blacklist"][msg.contentMetadata["mid"]] = True
                            switch["wblacklist"] = False
                            cl.sendMessage(msg.to,"sampun dititeni")
                            print([msg.contentMetadata["mid"]] + " Ditambahkan ke daftar orang bejat")

                   elif switch["dblacklist"] == True:
                       if msg.contentMetadata["mid"] in settings["blacklist"]:
                            del settings["blacklist"][msg.contentMetadata["mid"]]
                            cl.sendMessage(msg.to,"sampun diampuni")
                            switch["dblacklist"] = False
                            print([msg.contentMetadata["mid"]] + " Diampuni dosa2nya")

                       else:
                            switch["dblacklist"] = False
                            cl.sendMessage(msg.to,"Dia tak berdosa")
                            print("MID not in blacklist")
                   elif switch["wrin"] == True:
                       if msg.contentMetadata["mid"] in settings["Rinjani"]:
                            cl.sendMessage(msg.to,"Kita udah temenan")
                            switch["wrin"] = False
                            print("MID Already in the wl")
                       else:
                            settings["Rinjani"][msg.contentMetadata["mid"]] = True
                            switch["wrin"] = False
                            cl.sendMessage(msg.to,"Sudah dijadikan teman")
                            print([msg.contentMetadata["mid"]] + " Ditambahkan ke daftar teman")

                   elif switch["drin"] == True:
                       if msg.contentMetadata["mid"] in settings["Rinjani"]:
                            del settings["Rinjani"][msg.contentMetadata["mid"]]
                            cl.sendMessage(msg.to,"Teman terlupakan")
                            switch["drin"] = False
                            print([msg.contentMetadata["mid"]] + " dilupakan")

                       else:
                            switch["drin"] = False
                            cl.sendMessage(msg.to,"Dia bukan temanmu")
                            print("MID not in wl")
                   elif settings["detailsContact"] == True:
                        msg.contentType = 0
                        cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                        if 'displayName' in msg.contentMetadata:
                            contact = cl.getContact(msg.contentMetadata["mid"])
                            try:
                                cu = cl.channel.getCover(msg.contentMetadata["mid"])
                            except:
                                cu = ""
                            cl.sendMessage(msg.to,"[Name]:\n ->" + msg.contentMetadata["displayName"] + "\n[MID]:\n ->" + msg.contentMetadata["mid"] + "\n[Biography]:\n ->" + contact.statusMessage + "\n[Profile Picture]:\n ->http://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[Cover Picture]:\n ->" + str(cu))
                        else:
                            contact = cl.getContact(msg.contentMetadata["mid"])
                            try:
                                cu = cl.channel.getCover(msg.contentMetadata["mid"])
                            except:
                                cu = ""
                            try:
                                cl.sendImageWithURL(msg.to, "http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                                time.sleep(0.02)
                            except:
                                pass
                            cl.sendMessage(msg.to,"[Name]:\n ->" + msg.contentMetadata["displayName"] + "\n[MID]:\n ->" + msg.contentMetadata["mid"] + "\n[Biography]:\n ->" + contact.statusMessage + "\n[Profile Picture]:\n ->http://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[Cover Picture]:\n ->" + str(cu))


                if msg.contentType == 0:
                    if settings["autoRead"] == True:
                        cl.sendChatChecked(to, msg_id)
                    if text is None:
                        return
                    else:
                        # Basic command
                        if text.lower() == "help1":
                            helpMessage = help()
                            cl.sendMessage(to, str(helpMessage))
                        if text.lower() == "help2":
                            helpMessage2 = help2()
                            cl.sendMessage(to, str(helpMessage2))
                        if text.lower() == "help3":
                            helpMessage3 = help3()
                            cl.sendMessage(to, str(helpMessage3))
                        elif text.lower() == "me":
                            cl.sendContact(to, sender)
                        elif text.lower() == "reboot":
                            cl.sendMessage(to, "Sabat mblo")
                            settings["restartPoint"] = to
                            restartBot()
                        elif text.lower() == "sp":
                            start = time.time()
                            cl.sendMessage("u78643d09e42a36836a17cc918963a8b7", '.')
                            elapsed_time = time.time() - start
                            cl.sendMessage(to, "%s♻Detik♻" % (elapsed_time))
                            start = time.time()
                            ki.sendMessage("u78643d09e42a36836a17cc918963a8b7", '.')
                            elapsed_time = time.time() - start
                            ki.sendMessage(to, "%s♻Detik♻" % (elapsed_time))
                            start = time.time()
                            kk.sendMessage("u78643d09e42a36836a17cc918963a8b7", '.')
                            elapsed_time = time.time() - start
                            kk.sendMessage(to, "%s♻Detik♻" % (elapsed_time))
                            start = time.time()
                            kc.sendMessage("u78643d09e42a36836a17cc918963a8b7", '.')
                            elapsed_time = time.time() - start
                            kc.sendMessage(to, "%s♻Detik♻" % (elapsed_time))
                            start = time.time()
                            ks.sendMessage("u78643d09e42a36836a17cc918963a8b7", '.')
                            elapsed_time = time.time() - start
                            ks.sendMessage(to, "%s♻Detik♻" % (elapsed_time))
                        elif text.lower() == "sp1":
                            start = time.time()
                            cl.sendMessage("u78643d09e42a36836a17cc918963a8b7", '.')
                            elapsed_time = time.time() - start
                            cl.sendMessage(to, "%s♻Detik♻" % (elapsed_time))
                        elif text.lower() == ",pamit dulu ya":
                            if msg.toType == 2:
                                cl.sendMessage(to, "Kangen PC aja")
                                cl.leaveGroup(to)
                        elif 'mid ' in text.lower():
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                ret_ = "[ Mid User ]"
                                for ls in lists:
                                    ret_ += "\n{}".format(str(ls))
                                cl.sendMessage(to, str(ret_))
                        elif 'sikat ' in text.lower():
                            if msg.contentMetadata is not None:
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    try:
                                        klist=[kk,kc,ks,ki]
                                        kicker=random.choice(klist)
                                        kicker.kickoutFromGroup(msg.to,[target])
                                    except:
                                        kicker.kickoutFromGroup(msg.to,[target])
                                else:
                                    pass
                        elif 'pancal ' in text.lower():
                            if msg.contentMetadata is not None:
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    try:
                                        cl.kickoutFromGroup(msg.to,[target])
                                    except:
                                        cl.sendMessage(to, "jancok limit")                                
                                else:
                                    pass
                        elif text.lower() == "takbir...":
                            gs = cl.getGroup(msg.to)
                            sirilist = [i.mid for i in gs.members if any(word in i.displayName for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん"])]
                            if sirilist != []:
                                groupParam = msg.to
                                try:
                                    p = Pool(40)
                                    p.map(SiriGetOut,sirilist)
                                    p.close()
                                except:
                                    p.close()
                        elif text.lower() == "@gulung ":
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                   groupParam = msg.to
                                   try:
                                       p = Pool(40)
                                       p.map(byuh,targets)
                                       p.close()
                                       p.terminate()
                                       p.join
                                   except Exception as error:
                                       p.close()
                                       return
                        elif 'sikat ' in text.lower():
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        random.choice(KAC).kickoutFromGroup(to, ls)
                                    except:
                                        cl.sendMessage(to, "cok, limit")
                        elif text.lower() == "gid":
                            cl.sendMessage(msg.to,msg.to)
                
                        elif text.lower() == "midku":
                            cl.sendMessage(msg.to,msg._from)

                        elif '/bilang ' in text.lower():
                            sep = text.split(" ")
                            audio = text.replace(sep[0] + " ","")
                            tts = gTTS(text=audio, lang='id')
                            tts.save('ra.mp3')
                            cl.sendAudio(msg.to,'ra.mp3')
                            print("[Notif] Send Text To Audio Sucess")

                        elif '/ig ' in text.lower():
                            sep = text.split(" ")
                            instagram = text.replace(sep[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                html = web.get("https://www.instagram.com/" + instagram + "/")
                                soup = BeautifulSoup(html.text, 'html5lib')
                                data = soup.find_all('meta', attrs={'property':'og:description'})
                                text = data[0].get('content').split()
                                data1 = soup.find_all('meta', attrs={'property':'og:image'})
                                text1 = data1[0].get('content').split()
                                user = "Name: " + text[-2] + "\n"
                                user1 = "Username: " + text[-1] + "\n"
                                followers = "Followers: " + text[0] + "\n"
                                following = "Following: " + text[2] + "\n"
                                post = "Post: " + text[4] + "\n"
                                link = "Link: " + "https://instagram.com/" + instagram
                                cl.sendImageWithURL(msg.to, text1[0])
                                cl.sendMessage(msg.to, user + user1 + followers + following + post + link)
                                print("[Notif] Search Instagram Sucess")



                        elif 'ambilin ' in text.lower():
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    path = "http://dl.profile.line-cdn.net/" + cl.getContact(ls).pictureStatus
                                    if settings["server"] == "VPS":
                                        cl.sendImageWithURL(to, str(path))
                                    else:
                                        urllib.urlretrieve(path, "steal.jpg")
                                        cl.sendImage(to, "steal.jpg")
                        elif 'sampul ' in text.lower():
                            if channel != None:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        path = channel.getProfileCoverURL(ls)
                                        path = str(path)
                                        if settings["server"] == "VPS":
                                            cl.sendImageWithURL(to, str(path))
                                        else:
                                            urllib.urlretrieve(path, "steal.jpg")
                                            cl.sendImage(to, "steal.jpg")
                            else:
                                cl.sendMessage(to, "gak masuk channel bos")
                        elif 'kepo ' in text.lower():
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                    cl.sendMessage(to, "Curhatannya \n{}".format(str(contact.statusMessage)))
                        elif text.lower() == "ganti pp":
                            switch["changePicture"] = True
                            cl.sendMessage(to, "Kirimen gambare")
                        elif text.lower() == "pp 1":
                            switch["cp1"] = True
                            cl.sendMessage(to, "Kirimen gambare")
                        elif text.lower() == "pp 2":
                            switch["cp2"] = True
                            cl.sendMessage(to, "Kirimen gambare")
                        elif text.lower() == "pp 3":
                            switch["cp3"] = True
                            cl.sendMessage(to, "Kirimen gambare")
                        elif text.lower() == "pp 4":
                            switch["cp4"] = True
                            cl.sendMessage(to, "Kirimen gambare")

                        elif text.lower() == "kill ban":
                            group = cl.getGroup(msg.to)
                            gMembMids = [contact.mid for contact in group.members]
                            matched_list = []
                            for tag in wait["blacklist"]:
                                matched_list+=filter(lambda str: str == tag, gMembMids)
                            if matched_list == []:
                                cl.sendMessage(msg.to,"Tak ada yang berdosa")
                                return
                            for jj in matched_list:
                                try:
                                    random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                                    print((msg.to,[jj]))
                                except:
                                    pass

                        elif 'status: ' in text.lower():
                          sep = text.split(": ")
                          string = text.replace(sep[0] + ": ","")
                          if len(string) <= 500:
                             profile_B = ki.getProfile()
                             profile_C = kk.getProfile()
                             profile_D = kc.getProfile()
                             profile_E = ks.getProfile()
                             profile_B.statusMessage = string
                             profile_C.statusMessage = string
                             profile_D.statusMessage = string
                             profile_E.statusMessage = string
                             ki.updateProfile(profile_B)
                             kk.updateProfile(profile_B)
                             kc.updateProfile(profile_B)
                             ks.updateProfile(profile_B)
                             cl.sendMessage(msg.to,"Status yang ditampilkan : " + string )
                        elif 'gn: ' in text.lower():
                            if msg.toType == 2:
                                X = cl.getGroup(msg.to)
                                sep = text.split(": ")
                                iki = text.replace(sep[0] + ": ","")
                                X.name = iki
                                cl.updateGroup(X)
                                print("[Command]GN executed")
                        elif text.lower() == "botku":		
                            cl.sendContact(to, Amid)
                            cl.sendContact(to, Bmid)
                            cl.sendContact(to, Cmid)
                            cl.sendContact(to, Dmid)
                            cl.sendContact(to, "u78643d09e42a36836a17cc918963a8b7")

                        elif text.lower() == "ginfo":
                            if msg.toType == 2:
                                ginfo = cl.getGroup(msg.to)
                                try:
                                    gCreator = ginfo.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if ginfo.invitee is None:
                                    sinvitee = "0"
                                else:
                                    sinvitee = str(len(ginfo.invitee))
                                if ginfo.preventedJoinByTicket == True:
                                    u = "Close"
                                else:
                                    u = "Open"
                                cl.sendMessage(msg.to,"[Group Name]\n ->" + str(ginfo.name) + "\n[Group ID]\n ->" + msg.to + "\n[Group Creator]\n ->" + gCreator + "\n[Group Profile]\n ->http://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n[Members]\n ->" + str(len(ginfo.members)) + "\n[Members Pending]\n ->" + sinvitee + "\n[Join by URL]\n ->" + u)
                            else:
                                cl.sendMessage(msg.to,"Hanya bisa di grup.")
                        elif text.lower() == "sikat lurrr":
                            if msg.toType == 2:
                                gs = cl.getGroup(msg.to)
                                targets = []
                                for g in gs.members:
                                    targets.append(g.mid)
                                targets.remove(mid)
                                if targets == []:
                                    cl.sendMessage(msg.to,"Amit lurrr")
                                else:
                                    for target in targets:			
                                      if target not in settings["Rinjani"]:
                                        try:
                                            cl.kickoutFromGroup(msg.to,[target])
                                        except:
                                           print("cleanse executed")
                        elif text.lower() == "takbir !!!":
                            if msg.toType == 2:
                                gs = cl.getGroup(msg.to)
                                targets = []
                                for g in gs.members:
                                    targets.append(g.mid)
                                targets.remove(mid)
                                if targets == []:
                                    cl.sendMessage(msg.to,"Amit lurrr")
                                else:
                                    for target in targets:
                                      if target not in settings["PEKI"]:
                                        try:
                                            random.choice(KAC).kickoutFromGroup(msg.to,[target])
                                        except:
                                           try:
                                              random.choice(KAC).kickoutFromGroup(msg.to,[target])
                                           except:
                                              try:
                                                 random.choice(KAC).kickoutFromGroup(msg.to,[target])
                                              except:
                                                 try:
                                                     random.choice(KAC).kickoutFromGroup(msg.to,[target])
                                                 except:
                                                      print("cleanse executed")

                        elif '/pundhut ' in text.lower():
                           ulti0 = msg.text.replace("/pundhut ","")
                           ulti1 = ulti0.lstrip()
                           ulti2 = ulti1.replace("@","")
                           ulti3 = ulti2.rstrip()
                           _name = ulti3
                           gs = cl.getGroup(msg.to)
                           ginfo = cl.getGroup(msg.to)
                           gs.preventedJoinByTicket = False
                           cl.updateGroup(gs)
                           invsend = 0
                           Ticket = cl.reissueGroupTicket(msg.to)
                           ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                           time.sleep(0.2)
                           targets = []
                           for s in gs.members:
                               if _name in s.displayName:
                                  targets.append(s.mid)
                           if targets == []:
                               sendMessage(msg.to,"minggat")
                               pass
                           else:
                               for target in targets:
                                    try:
                                        ki.kickoutFromGroup(msg.to,[target])
                                        print((msg.to,[g.mid]))
                                    except:
                                        ki.leaveGroup(msg.to)
                                        gs = cl.getGroup(msg.to)
                                        gs.preventedJoinByTicket = True
                                        cl.updateGroup(gs)
                                        gs.preventedJoinByTicket(gs)
                                        cl.updateGroup(gs)

                        elif '/cipok ' in text.lower():
                           ulti0 = msg.text.replace("/cipok ","")
                           ulti1 = ulti0.lstrip()
                           ulti2 = ulti1.replace("@","")
                           ulti3 = ulti2.rstrip()
                           _name = ulti3
                           gs = cl.getGroup(msg.to)
                           ginfo = cl.getGroup(msg.to)
                           gs.preventedJoinByTicket = False
                           cl.updateGroup(gs)
                           invsend = 0
                           Ticket = cl.reissueGroupTicket(msg.to)
                           kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                           time.sleep(0.2)
                           targets = []
                           for s in gs.members:
                               if _name in s.displayName:
                                  targets.append(s.mid)
                           if targets == []:
                               sendMessage(msg.to,"minggat")
                               pass
                           else:
                               for target in targets:
                                    try:
                                        kk.kickoutFromGroup(msg.to,[target])
                                        print((msg.to,[g.mid]))
                                    except:
                                        kk.leaveGroup(msg.to)
                                        gs = cl.getGroup(msg.to)
                                        gs.preventedJoinByTicket = True
                                        cl.updateGroup(gs)
                                        gs.preventedJoinByTicket(gs)
                                        cl.updateGroup(gs)

                        elif text.lower() == "@bubar":
                            if msg.toType == 2:
                                gs = cl.getGroup(msg.to)
                                gs.preventedJoinByTicket = False
                                cl.updateGroup(gs)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ks.acceptGroupInvitationByTicket(msg.to,Ticket)
                                time.sleep(0.1)
                                targets = []
                                for g in gs.members:
                                    targets.append(g.mid)
                                targets.remove(mid)
                                if targets == []:
                                    cl.sendMessage(msg.to,"Amit lurrr")
                                else:
                                    for target in targets:
                                      if target not in settings["Rinjani"]:
                                        try:
                                            random.choice(KAC).kickoutFromGroup(msg.to,[target])
                                        except:
                                           try:
                                              random.choice(KAC).kickoutFromGroup(msg.to,[target])
                                           except:
                                              try:
                                                 random.choice(KAC).kickoutFromGroup(msg.to,[target])
                                              except:
                                                 try:
                                                     random.choice(KAC).kickoutFromGroup(msg.to,[target])
                                                 except:
                                                      print("cleanse executed")
                        elif "cbot @" in text.lower():
                            print("[COPY] Ok")
                            _name = msg.text.replace("cbot @","")
                            _nametarget = _name.rstrip(' ')
                            gs = cl.getGroup(msg.to)
                            targets = []
                            for g in gs.members:
                                if _nametarget == g.displayName:
                                    targets.append(g.mid)
                            if targets == []:
                                cl.sendMessage(msg.to, "wonge raono")
                            else:
                                for target in targets:
                                     try:
                                        ki.cloneContactProfile(target)
                                        kk.cloneContactProfile(target)
                                        kc.cloneContactProfile(target)
                                        ks.cloneContactProfile(target)
                                        cl.sendMessage(msg.to, "Semua Bot Profil sukses copy profil")
                                     except Exception as e:
                                         print(e)
                        elif "c1 @" in text.lower():
                            print("[COPY] Ok")
                            _name = msg.text.replace("c1 @","")
                            _nametarget = _name.rstrip(' ')
                            gs = cl.getGroup(msg.to)
                            targets = []
                            for g in gs.members:
                                if _nametarget == g.displayName:
                                    targets.append(g.mid)
                            if targets == []:
                                cl.sendMessage(msg.to, "wonge raono")
                            else:
                                for target in targets:
                                     try:
                                        ki.cloneContactProfile(target)
                                        cl.sendMessage(msg.to, "Bot 1 sukses copy")
                                     except Exception as e:
                                         print(e)
                        elif "c2 @" in text.lower():
                            print("[COPY] Ok")
                            _name = msg.text.replace("c2 @","")
                            _nametarget = _name.rstrip(' ')
                            gs = cl.getGroup(msg.to)
                            targets = []
                            for g in gs.members:
                                if _nametarget == g.displayName:
                                    targets.append(g.mid)
                            if targets == []:
                                cl.sendMessage(msg.to, "wonge raono")
                            else:
                                for target in targets:
                                     try:
                                        kk.cloneContactProfile(target)
                                        cl.sendMessage(msg.to, "Bot 2 sukses copy")
                                     except Exception as e:
                                         print(e)
                        elif "c3 @" in text.lower():
                            print("[COPY] Ok")
                            _name = msg.text.replace("c3 @","")
                            _nametarget = _name.rstrip(' ')
                            gs = cl.getGroup(msg.to)
                            targets = []
                            for g in gs.members:
                                if _nametarget == g.displayName:
                                    targets.append(g.mid)
                            if targets == []:
                                cl.sendMessage(msg.to, "wonge raono")
                            else:
                                for target in targets:
                                     try:
                                        kc.cloneContactProfile(target)
                                        cl.sendMessage(msg.to, "Bot 3 sukses copy")
                                     except Exception as e:
                                         print(e)
                        elif "c4 @" in text.lower():
                            print("[COPY] Ok")
                            _name = msg.text.replace("c2 @","")
                            _nametarget = _name.rstrip(' ')
                            gs = cl.getGroup(msg.to)
                            targets = []
                            for g in gs.members:
                                if _nametarget == g.displayName:
                                    targets.append(g.mid)
                            if targets == []:
                                cl.sendMessage(msg.to, "wonge raono")
                            else:
                                for target in targets:
                                     try:
                                        kk.cloneContactProfile(target)
                                        cl.sendMessage(msg.to, "Bot 1 sukses copy")
                                     except Exception as e:
                                         print(e)

                        elif text.lower() == "ganti pp grup":
                            if msg.toType == 2:
                                if to not in settings["changeGroupPicture"]:
                                    settings["changeGroupPicture"].append(to)
                                cl.sendMessage(to, "Ndi cok")
                        elif text.lower() == "haloo":
                            if msg.toType == 0: 	
                                mentionMembers(to, to)
                            elif msg.toType == 2:
                                group = cl.getGroup(to)
                                contact = [mem.mid for mem in group.members]
                                mentionMembers(to, contact)
                        elif text.lower() == "gambar grup":
                            if msg.toType == 2:
                                try:
                                    group = cl.getGroup(msg.to)
                                    try:
                                        images = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                    except:
                                        images = "https://www.1and1.co.uk/digitalguide/fileadmin/DigitalGuide/Teaser/not-found-t.jpg"
                                    try:
                                        cl.sendImageWithURL(msg.to,images)
                                    except Exception as error:
                                        cl.sendMessage(msg.to,(error))
                                        pass
                                except:
                                    cl.sendMessage(msg.to,"Error!")
                        elif text.lower().startswith("gbc "):
                            sep = text.split(" ")
                            txt = text.replace(sep[0] + " ","")
                            groups = cl.groups
                            for group in groups:
                                cl.sendMessage(group, "[ Broadcast ]\n{}".format(str(txt)))
                            cl.sendMessage(to, "Berhasil broadcast ke {} group".format(str(len(groups))))
                        elif text.lower().startswith("fbc "):
                            sep = text.split(" ")
                            txt = text.replace(sep[0] + " ","")
                            friends = cl.friends
                            for friend in friends:
                                cl.sendMessage(friend, "[ Broadcast ]\n{}".format(str(txt)))
                            cl.sendMessage(to, "Berhasil broadcast ke {} teman".format(str(len(friends))))
                        elif text.lower().startswith("allbc "):
                            sep = text.split(" ")
                            txt = text.replace(sep[0] + " ","")
                            friends = cl.friends
                            groups = cl.groups
                            for group in groups:
                                cl.sendMessage(group, "[ Broadcast ]\n{}".format(str(txt)))
                            cl.sendMessage(to, "Berhasil broadcast ke {} group".format(str(len(groups))))
                            for friend in friends:
                                cl.sendMessage(friend, "[ Broadcast ]\n{}".format(str(txt)))
                            cl.sendMessage(to, "Berhasil broadcast ke {} teman".format(str(len(friends))))

                        elif text.lower() == "creator":
                            cl.sendContact(to, "╞u78643d09e42a36836a17cc918963a8b7")
                            cl.sendMessage(msg.to,"[TEAM RINJANI BOT")  
                       # elif text.lower() == "empunya":		
                           # cl.sendContact(to, "u4d28c76d0e3abd959b575fcac821e15f")
                          #  cl.sendContact(to, "uc17663698bf499304c0b424c2dbaf754")
                           # cl.sendContact(to, "u3608fe707f0c172ce936fe90cc5d8341")
                           # cl.sendContact(to, "ua7a787fe059eed9f2a65a4dea2528b3b")
                            #cl.sendMessage(msg.to,"TEAM RINJANI BOT")
                        elif text.lower() == "danyange":
                            try:
                                group = cl.getGroup(msg.to)
                                GS = group.creator.mid
                                cl.sendContact(to, GS)
                                cl.sendMessage(msg.to,"Niki sing Bahu rekso") 
                            except:
                                W = group.members[0].mid
                                cl.sendContact(to, W)
                                cl.sendMessage(msg.to,"Niki sing Bahu rekso") 
                        elif text.lower() == "grupku":
                            groups = cl.groups
                            ret_ = "[ Groupku INI ]"
                            no = 0
                            for gid in groups:
                                group = cl.getGroup(gid)
                                ret_ += "\n {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                                no += 1
                            ret_ += "[ Total {} Grup ]".format(str(len(groups)))
                            cl.sendMessage(to, str(ret_))
                        elif text.lower() == "tolak angin":
                            ginvited = cl.ginvited
                            if ginvited != [] and ginvited != None:
                                for gid in ginvited:
                                    cl.rejectGroupInvitation(gid)
                                cl.sendMessage(to, "Undangan segini {} udah ditolak".format(str(len(ginvited))))
                            else:
                                cl.sendMessage(to, "Gak da yg undang")

                        elif 'del wl ' in text.lower():
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        del settings["Rinjani"][ls]
                                        cl.sendMessage(msg.to,"Teman telah dilupakan")
                                        print("[Notif] Delete wl Success")
                                    except:
                                        cl.sendMessage(msg.to,"Bukan temanmu")
  
                        elif 'add wl ' in text.lower():
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        settings["Rinjani"][ls] = True
                                        cl.sendMessage(msg.to,"Teman ditambahkan")
                                        print("[Notif] WL Success")
                                    except:
                                        cl.sendMessage(msg.to,"Sudah menjadi teman")

                        elif text.lower() == "wl all":
                            if msg.toType == 2:
                                gs = cl.getGroup(msg.to)
                                targets = []
                                for g in gs.members:
                                    targets.append(g.mid)
                                targets.remove(mid)
                                if targets == []:
                                    cl.sendMessage(msg.to,"gak ada orang")
                                else:
                                    for target in targets:
                                         if target not in settings["Rinjani"]:
                                            try:
                                                settings["Rinjani"][target] = True
                                                cl.sendMessage(msg.to,"Teman ditambahkan")
                                            except:
                                                pass
                        elif text.lower() == "ban all":
                            if msg.toType == 2:
                                gs = cl.getGroup(msg.to)
                                targets = []
                                for g in gs.members:
                                    targets.append(g.mid)
                                targets.remove(mid)
                                if targets == []:
                                    cl.sendMessage(msg.to,"gak ada orang")
                                else:
                                    for target in targets:
                                         if target not in settings["Rinjani"] or target not in Bots:
                                            try:
                                                settings["blacklist"][target] = True
                                                cl.sendMessage(msg.to,"Anda ternoda")
                                            except:
                                                pass
                        elif text.lower() == "unban all":
                            if msg.toType == 2:
                                gs = cl.getGroup(msg.to)
                                targets = []
                                for g in gs.members:
                                    targets.append(g.mid)
                                targets.remove(mid)
                                if targets == []:
                                    cl.sendMessage(msg.to,"gak ada orang")
                                else:
                                    for target in targets:
                                            try:
                                                del settings["blacklist"][target]
                                                cl.sendMessage(msg.to,"Anda ternoda")
                                            except:
                                                pass
                        elif 'ampuni ' in text.lower():
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        del settings["blacklist"][ls]
                                        cl.sendMessage(msg.to,"Dosa telah diampuni")
                                        print("[Notif] Delete Blacklist Success")
                                    except:
                                        cl.sendMessage(msg.to,"Error")
  
                        elif 'bann ' in text.lower():
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        settings["blacklist"][ls] = True
                                        cl.sendMessage(msg.to,"Dia telah ternoda")
                                        print("[Notif] Blacklist Success")
                                    except:
                                        cl.sendMessage(msg.to,"Error")
                        elif text.lower() == "dulurrr":
                            G = cl.getGroup(msg.to)
                            ginfo = cl.getGroup(msg.to)
                            G.preventedJoinByTicket = False
                            cl.updateGroup(G)
                            invsend = 0
                            Ticket = cl.reissueGroupTicket(msg.to)
                            ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                            kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                            kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                            ks.acceptGroupInvitationByTicket(msg.to,Ticket)
                            G = cl.getGroup(msg.to)
                            G.preventedJoinByTicket = True
                            cl.updateGroup(G)
                            G.preventedJoinByTicket(G)
                            cl.updateGroup(G)
                        elif text.lower() == "cok":
                            ki.leaveGroup(msg.to)
                            kk.leaveGroup(msg.to)
                            kc.leaveGroup(msg.to)
                            ks.leaveGroup(msg.to)

                        elif text.lower() == 'pasang cctv':
                                try:
                                    del cctv['point'][msg.to]
                                    del cctv['sidermem'][msg.to]
                                    del cctv['cyduk'][msg.to]
                                except:
                                    pass
                                cctv['point'][msg.to] = msg.id
                                cctv['sidermem'][msg.to] = ""
                                cctv['cyduk'][msg.to]=True
                        elif text.lower() == 'intip':
                                if msg.to in cctv['point']:
                                    cctv['cyduk'][msg.to]=False
                                    cl.sendMessage(msg.to, cctv['sidermem'][msg.to])
                                else:
                                    cl.sendMessage(msg.to, "Lum dipasang cctvnya")
                        elif text.lower() == "invgc":
                            if msg.toType == 2:
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                call.acquireGroupCallRoute(to)
                                call.inviteIntoGroupCall(to, contactIds=members)
                                cl.sendMessage(to, "Berhasil mengundang kedalam telponan group")
                        elif text.lower() == "removeallachat":
                            cl.removeAllMessages(op.param2)
                            cl.sendMessage(to, "Berhasil hapus semua chat")

                        elif text.lower() == 'banlist':
                                if settings["blacklist"] == {}:
                                    cl.sendMessage(msg.to,"Gak ada orang bejat")
                                else:
                                    cl.sendMessage(msg.to,"Ini daftar orang2 bejat:")
                                    mc = "●Jancokers● \n\n"
                                    for mi_d in settings["blacklist"]:
                                        mc += "~  " +cl.getContact(mi_d).displayName + "\n"
                                    cl.sendMessage(msg.to,mc)
                        elif text.lower() == 'temanku':
                                if settings["Rinjani"] == {}:
                                    cl.sendMessage(msg.to,"Kamu gak punya teman :(")
                                else:
                                    cl.sendMessage(msg.to,"Ini daftar temanmu:")
                                    mc = "●Sahabat Rinjani● \n\n"
                                    for mi_d in settings["PEKI"]:
                                        mc += "~  " +cl.getContact(mi_d).displayName + "\n"
                                    cl.sendMessage(msg.to,mc)
                        elif text.lower() == 'undang orang':
                             switch["winvite"] = True
                             cl.sendMessage(msg.to,"mana kontaknya ?")
                        elif text.lower() == 'add ban':
                            switch["wblacklist"] = True
                            cl.sendMessage(msg.to,"kirim kontak orangnya")
                        elif text.lower() == 'unban':
                            switch["dblacklist"] = True
                            cl.sendMessage(msg.to,"Mana yang mau diampuni ?")
                        elif text.lower() == 'tambah teman':
                            switch["wrin"] = True
                            cl.sendMessage(msg.to,"kirim kontak orangnya")
                        elif text.lower() == 'hapus teman':
                            switch["drin"] = True
                            cl.sendMessage(msg.to,"Mana yang mau dilupakan ?")
                       #-------------------------------------------------------#
                        elif "/invite2: " in msg.text.lower():
                            sep = text.split(": ")
                            gid = text.replace(sep[0] + ": ","")
                            if gid == "":
                                ki.sendMessage(msg.to,"Invalid group id")
                            else:
                                try:
                                    ki.findAndAddContactsByMid(msg._from)
                                    ki.inviteIntoGroup(gid,[msg._from])
                                except:
                                    ki.sendMessage(msg.to,"aku wes ra nek kono")
                        elif text.lower() == 'lihat grup':
                            gid = ki.getGroupIdsJoined()
                            g = ""
                            for i in gid:
                                g += "[%s] :%s\n" % (ki.getGroup(i).name,i)
                            ki.sendMessage(msg.to,g)

                        elif text.lower() == ".crash":
                            cl.sendContact(to, msg.to+"',")

                        elif "/nonton: " in text.lower():
                            try:
                                sep = text.split(": ")
                                textToSearch = text.replace(sep[0] + ": ","")
                                query = urllib.parse.quote(textToSearch)
                                url = "https://www.youtube.com/results?search_query=" + query
                                response = urllib.request.urlopen(url)
                                html = response.read()
                                soup = BeautifulSoup(html, "html.parser")
                                results = soup.find(attrs={'class':'yt-uix-tile-link'})
                                cl.sendMessage(msg.to,'https://www.youtube.com' + results['href'])
                                print("[Command] Search Youtube Success")
                            except:
                                cl.sendMessage(msg.to,"gk ketemu")
                        elif "/mp3: " in text.lower():
                            try:
                                cl.sendText(msg.to,"Sabar lagi donlod...")
                                textToSearch = (msg.text).replace('/mp3: ', "").strip()
                                query = urllib.parse.quote(textToSearch)
                                url = "https://www.youtube.com/results?search_query=" + query
                                response = urllib.request.urlopen(url)
                                html = response.read()
                                soup = BeautifulSoup(html, "html.parser")
                                results = soup.find(attrs={'class':'yt-uix-tile-link'})
                                dl = 'https://www.youtube.com' + results['href']
                                vid = pafy.new(dl)
                                stream = vid.audiostreams
                                for s in stream:
                                    start = timeit.timeit()
                                    vin = s.url
                                    img = vid.bigthumbhd
                                    hasil = vid.title
                                    hasil += '\n\nPenulis : ' +str(vid.author)
                                    hasil += '\nDurasi   : ' +str(vid.duration)+ ' (' +s.quality+ ') '
                                    hasil += '\nRating   : ' +str(vid.rating)
                                    hasil += '\nDitonton    : ' +str(vid.viewcount)+ 'x '
                                    hasil += '\nDiterbitkan : ' +vid.published
                                    hasil += '\n\nTime taken : %s' % (start)
                                    hasil += '\n\n Tunggu encoding selesai...'
                                cl.sendAudioWithURL(msg.to,vin)
                                cl.sendImageWithURL(msg.to,img)
                                cl.sendMessage(msg.to,hasil)
                                print("[Notif] Search Youtube Mp3 Success")
                            except:
                                cl.sendMessage(msg.to,"Gagal Mencari...")

                        elif "/video: " in text.lower():
                            try:
                                cl.sendMessage(msg.to,"Sabar lagi donlod...")
                                textToSearch = (msg.text).replace('/video: ', "").strip()
                                query = urllib.parse.quote(textToSearch)
                                url = "https://www.youtube.com/results?search_query=" + query
                                response = urllib.request.urlopen(url)
                                html = response.read()
                                soup = BeautifulSoup(html, "html.parser")
                                results = soup.find(attrs={'class':'yt-uix-tile-link'})
                                dl = 'https://www.youtube.com' + results['href']
                                vid = pafy.new(dl)
                                stream = vid.streams
                                for s in stream:
                                    vin = s.url
                                    hasil = 'Informasi\n\n'
                                    hasil += 'Judul:\n ' + vid.title
                                    hasil += '\n Tunggu encoding selesai...'
                                cl.sendVideoWithURL(msg.to,vin)
                                cl.sendText(msg.to,hasil)
                                print("[Notif] Search Youtube Success")

                            except:
                                cl.sendMessage(msg.to,"Gagal Mencari...")

                        elif text.lower() == "respons":
                            s = cl.getProfile()
                            s1 = ki.getProfile()
                            s2 = kk.getProfile()
                            s3 = kc.getProfile()
                            s4 = ks.getProfile()
                            cl.sendMessage(msg.to, s.displayName + " ON")
                            ki.sendMessage(msg.to, s1.displayName + " ON")
                            kk.sendMessage(msg.to, s2.displayName + " ON")
                            kc.sendMessage(msg.to, s3.displayName + " ON")
                            ks.sendMessage(msg.to, s4.displayName + " ON")
                        elif "/left: " in text.lower():
                            gids = msg.text.replace("Left: ","")
                            gid = cl.getGroup(gids)
                            try:
                                ki.leaveGroup(gids)
                                kk.leaveGroup(gids)
                                kc.leaveGroup(gids)
                                ks.leaveGroup(gids)
                                print("[BOT LEAVE] dari suatu room")
                            except:
                                ki.sendMessage(msg.to,"Berhasil keluar dari wilayah " + gids.name)
                        elif "/undang: " in text.lower():
                            sep = text.split(": ")
                            midd = text.replace(sep[0] + ": ","")
                            cl.findAndAddContactsByMid(midd)
                            cl.inviteIntoGroup(msg.to,[midd])
                        elif text.lower() == "mangat.":
                            if msg.toType == 2:
                                group = cl.getGroup(msg.to)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    cl.cancelGroupInvitation(msg.to,[_mid])
                        elif text.lower() == "vakum dari line...":
                            gid = cl.getGroupIdsJoined()
                            for i in gid:
                                cl.leaveGroup(i)
                                print("[BOT LEAVE] DARI SEMUA ROOM")
                        elif text.lower() == "buka link":
                            if msg.toType == 2:
                                X = cl.getGroup(msg.to)
                                X.preventedJoinByTicket = False
                                cl.updateGroup(X)
                                Ticket = cl.reissueGroupTicket(msg.to)
                                cl.sendMessage(msg.to,"http://line.me/R/ti/g/" + Ticket)
                            else:
                                cl.sendMessage(msg.to,"Hanya bisa di grup.")
                        elif text.lower() == "tutup link":
                            if msg.toType == 2:
                                X = cl.getGroup(msg.to)
                                X.preventedJoinByTicket = True
                                cl.updateGroup(X)
                                cl.sendMessage(msg.to,"Link ditutup")
                            else:
                                cl.sendMessage(msg.to,"Hanya bisa di grup.")
                        elif "nama bot: " in text.lower():
                            sep = text.split(": ")
                            string = text.replace(sep[0] + ": ","")
                            if len(string) <= 20:
                                profile = ki.getProfile()
                                profile.displayName = string
                                ki.updateProfile(profile)
                                ki.sendMessage(msg.to,"Nama " + string + " Berhasil diubah")
                        elif "nama bot2: " in text.lower():
                            sep = text.split(": ")
                            string = text.replace(sep[0] + ": ","")
                            if len(string) <= 20:
                                profile = kk.getProfile()
                                profile.displayName = string
                                kk.updateProfile(profile)
                                kk.sendMessage(msg.to,"Nama " + string + " Berhasil diubah")
                        elif "nama bot3: " in text.lower():
                            sep = text.split(": ")
                            string = text.replace(sep[0] + ": ","")
                            if len(string) <= 20:
                                profile = kc.getProfile()
                                profile.displayName = string
                                kc.updateProfile(profile)
                                kc.sendMessage(msg.to,"Nama " + string + " Berhasil diubah")
                        elif "nama bot4: " in text.lower():
                            sep = text.split(": ")
                            string = text.replace(sep[0] + ": ","")
                            if len(string) <= 20:
                                profile = ks.getProfile()
                                profile.displayName = string
                                ks.updateProfile(profile)
                                ks.sendMessage(msg.to,"Nama " + string + " Berhasil diubah")
                        elif "all name: " in text.lower():
                            sep = text.split(": ")
                            string = text.replace(sep[0] + ": ","")
                            if len(string) <= 20:
                                profile = ki.getProfile()
                                profile = kk.getProfile()
                                profile = kc.getProfile()
                                profile = ks.getProfile()
                                profile.displayName = string
                                ki.updateProfile(profile)
                                kk.updateProfile(profile)
                                kc.updateProfile(profile)
                                ks.updateProfile(profile)
                                cl.sendMessage(msg.to,"Nama " + string + " Berhasil diubah")


                        elif text.lower() == "/balikin":
                            try:
                                cl.updateProfilePicture(backup.pictureStatus)
                                cl.updateProfile(backup)
                                cl.sendMessage(msg.to,"Sudah balik cakep lagi")
                            except Exception as e:
                                cl.sendMessage(msg.to, str (e))
                        elif text.lower() == "runtime":
                            timeNow = time.time()
                            runtime = timeNow - botStart
                            runtime = waktu(runtime)
                            resetTime = timeNow - int(settings["timeRestart"])
                            resetTime = waktu(resetTime)
                            cl.sendMessage(to, "Bot sudah berjalan selama {}.".format(str(runtime)))

                        elif "/ti/g/" in msg.text.lower():
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
                                    cl.sendMessage(to, "Berhasil masuk ke group %s" % str(group.name))
                        # Check viewers command
                        elif text.lower() == "cctv on":
                            tz = pytz.timezone("Asia/Jakarta")
                            timeNow = datetime.now(tz=tz)
                            day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                            hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                            bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                            hr = timeNow.strftime("%A")
                            bln = timeNow.strftime("%m")
                            for i in range(len(day)):
                                if hr == day[i]: hasil = hari[i]
                            for k in range(0, len(bulan)):
                                if bln == str(k): bln = bulan[k-1]
                            readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                            if to in read["readPoint"]:
                                cl.sendMessage(to, "Cctv sudah aktif ketik {}Cctv result untuk menampilkan hasil".format(str(settings["keyCommand"])))
                            else:
                                try:
                                    read["readPoint"][to] = True
                                    read["readMember"][to] = {}
                                    read["readTime"][to] = readTime
                                    read["ROM"][to] = {}
                                except:
                                    pass
                        elif text.lower() == "cctv off":
                            if to in read["readPoint"]:
                                try:
                                    del read["readPoint"][to]
                                    del read["readMember"][to]
                                    del read["readTime"][to]
                                    del read["ROM"][to]
                                    cl.sendMessage(to, "Berhasil matikan cctv")
                                except:
                                    pass
                            else:
                                cl.sendMessage(to, "Cctv belum diaktifkan ngapain di matikan?")
                        elif text.lower() == "cctv reset":
                            tz = pytz.timezone("Asia/Jakarta")
                            timeNow = datetime.now(tz=tz)
                            day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                            hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                            bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                            hr = timeNow.strftime("%A")
                            bln = timeNow.strftime("%m")
                            for i in range(len(day)):
                                if hr == day[i]: hasil = hari[i]
                            for k in range(0, len(bulan)):
                                if bln == str(k): bln = bulan[k-1]
                            readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                            if to in read["readPoint"]:
                                try:
                                    read["readPoint"][to] = True
                                    read["readMember"][to] = {}
                                    read["readTime"][to] = readTime
                                    read["ROM"][to] = {}
                                except:
                                    pass
                            else:
                                cl.sendMessage(to, "Cctv belum diaktifkan ngapain di reset?")
                        elif text.lower() == "cctv result":
                            if to not in read["readPoint"]:
                                cl.sendMessage(to, "Cctv belum diaktifkan udah main result aja")
                            else:
                                ret_ = "╔══[ Reader ]"
                                reader = {}
                                reader["name"] = ""
                                if read["readMember"][to] == {}:
                                    reader["name"] += "\n╠ Belum ada yang membaca chat"
                                else:
                                    for a in read["readMember"][to]:
                                        reader["name"] += "\n╠ {}".format(str(read["readMember"][to][a]))
                                time = read["readTime"][to]
                                ret += reader["name"]
                                ret += "\n╠══[ Siders ]"
                                sider = {}
                                sider["name"] = ""
                                if read["ROM"][to] == {} and read["readMember"][to] != {}:
                                    sider["name"] += "\n╠ Semua reader aktif chatting"
                                elif read["ROM"][to] == {} and read["readMember"][to] == {}:
                                    pass
                                else:
                                    for a in read["ROM"][to]:
                                        sider["name"] += "\n╠ {}".format(str(read["ROM"][to][a]))
                                ret_ += sider["name"]
                                ret_ += "\n╚══[ Total {} Siders From {} Viewers ]".format(str(len(read["ROM"])), str(len(read["readMember"])))
                                ret_ += "\nPoint Set On : \n{}".format(str(time))
                        # Example remote command
                        elif text.lower() == "settings":
                                 md = "   Rinjani bot \n\n"
                                 if settings["chat"] == True: md+=" ♻􀔃􀆑lock􏿿 Bot chat      → ON\n"
                                 else: md+=" ♻ ⛔ Bot chat      → OFF\n"
                                 if wait["copy"] == True: md+=" ♻􀔃􀆑lock􏿿 Copy      → ON\n"
                                 else: md+=" ♻ ⛔ Copy      → OFF\n"
                                 if settings["autoAdd"] == True: md+=" ♻􀔃􀆑lock􏿿 Auto add      → ON\n"
                                 else: md+=" ♻ ⛔ Auto add      → OFF\n"
                                 if settings["dm"] == True: md+=" ♻􀔃􀆑lock􏿿 Auto respon   → ON\n"
                                 else: md+=" ♻ ⛔ Auto respon   → OFF\n"
                                 if settings["autoJoin"] == True: md+=" ♻􀔃􀆑lock􏿿 Auto Join     → ON\n"
                                 else: md+=" ♻ ⛔ Auto Join     → OFF\n"
                                 if settings["greet"] == True: md+=" ♻􀔃􀆑lock􏿿 Sambutan      → ON\n"
                                 else: md+=" ♻ ⛔ Sambutan      → OFF\n"
                                 if settings["autoRead"] == True: md+=" ♻􀔃􀆑lock􏿿 Auto Read     → ON\n"
                                 else: md+=" ♻ ⛔ Auto Read     → OFF\n"
                                 if msg.to in settings["autocancel"]: md+=" ♻􀔃􀆑lock􏿿 Auto Cancel   → ON\n"
                                 else: md+=" ♻ ⛔ Auto Cancel   → OFF\n"
                                 if msg.to in settings["protecturl"]: md+=" ♻􀔃􀆑lock􏿿 URL Protect   → ON\n"
                                 else: md+=" ♻ ⛔ URL Protect   → OFF\n"
                                 if msg.to in settings["BlockACCESS"]: md+=" ♻􀔃􀆑lock􏿿 Block Join    → ON\n"
                                 else: md+=" ♻ ⛔ Block Join    → OFF\n"
                                 if msg.to in settings["main"]: md+=" ♻􀔃􀆑lock􏿿 Main Protect  → ON\n"
                                 else: md+=" ♻ ⛔ Main Protect  → OFF\n"
                                 if settings["detailsContact"] == True: md+=" ♻􀔃􀆑lock􏿿 Contact read  → ON\n"
                                 else: md+=" ♻ ⛔ Contact read  → OFF\n"
                                 if msg.to in settings['pname']: md+=" ♻􀔃􀆑lock􏿿 NameLOCK      → ON"
                                 else: md+=" ♻ ⛔ NameLOCK      → OFF\n"
                                 cl.sendMessage(msg.to,md + "\n       [TEAM RINJANI BOT   ")

                        elif text.lower() == "autoread":
                          if settings["autoRead"] == True:
                             cl.sendMessage(to, "Auto read sudah aktif")
                          else: 
                            settings["autoRead"] = True
                            cl.sendMessage(to, "Auto read diaktifkan")
                        elif text.lower() == "manualread":
                          if settings["autoRead"] == False:
                             cl.sendMessage(to, "Auto read belum diaktifkan")
                          else: 
                            settings["autoRead"] = False
                            cl.sendMessage(to, "Auto read dimatikan")
                        elif text.lower() == "kontak on":
                          if settings["detailsContact"] == True:
                             cl.sendMessage(to, "Membaca detil kontak sudah aktif")
                          else: 
                            settings["detailsContact"] = True
                            cl.sendMessage(to, "Membaca detil kontak diaktifkan")
                        elif text.lower() == "kontak off":
                          if settings["detailsContact"] == False:
                             cl.sendMessage(to, "Detil kontak belum diaktifkan")
                          else: 
                            settings["detailsContact"] = False
                            cl.sendMessage(to, "Detil kontak dimatikan")
                        elif text.lower() == "kopi kak":
                            wait["copy"] = True
                            cl.sendMessage(msg.to,"biar gak stress")
                        elif text.lower() == "kopi abis":
                            wait["copy"] = False
                            cl.sendMessage(msg.to,"biar gak stress")
                        elif text.lower() == "auto join":
                          if settings["autoJoin"] == True:
                             cl.sendMessage(to, "Auto join sudah aktif")
                          else: 
                             settings["autoJoin"] = True
                             cl.sendMessage(to, "Auto join diaktifkan")
                        elif text.lower() == "manual join":
                          if settings["autoJoin"] == False:
                             cl.sendMessage(to, "Auto join belum diaktifkan")
                          else: 
                            settings["autoJoin"] = False
                            cl.sendMessage(to, "Auto join dimatikan")
                        elif text.lower() == "auto add":
                          if settings["autoAdd"] == True:
                             cl.sendMessage(to, "Auto add sudah aktif")
                          else: 
                             settings["autoAdd"] = True
                             cl.sendMessage(to, "Auto add diaktifkan")
                        elif text.lower() == "manual add":
                          if settings["autoAdd"] == False:
                             cl.sendMessage(to, "Auto add belum diaktifkan")
                          else: 
                            settings["autoAdd"] = False
                            cl.sendMessage(to, "Auto add dimatikan")
                        elif text.lower() == "greet on":
                          if settings["greet"] == True:
                             cl.sendMessage(to, "Sambutan sudah aktif")
                          else: 
                             settings["greet"] = True
                             cl.sendMessage(to, "Sambutan diaktifkan")
                        elif text.lower() == "greet off":
                          if settings["greet"] == False:
                             cl.sendMessage(to, "Sambutan belum diaktifkan")
                          else: 
                            settings["greet"] = False
                            cl.sendMessage(to, "Sambutan dimatikan")
                        elif text.lower() == "auto respon":
                          if settings["dm"] == True:
                             cl.sendMessage(to, "Auto respon sudah aktif")
                          else: 
                            settings["dm"] = True
                            cl.sendMessage(to, "Auto respon diaktifkan")
                        elif text.lower() == "manual respon":
                          if settings["dm"] == False:
                             cl.sendMessage(to, "Auto respon belum diaktifkan")
                          else: 
                            settings["dm"] = False
                            cl.sendMessage(to, "Auto respon dimatikan")
                        elif text.lower() == "chat on":
                          if settings["chat"] == True:
                             cl.sendMessage(to, "Auto chat sudah aktif")
                          else: 
                            settings["chat"] = True
                            cl.sendMessage(to, "Auto chat diaktifkan")
                        elif text.lower() == "chat off":
                          if settings["chat"] == False:
                             cl.sendMessage(to, "Auto chat belum diaktifkan")
                          else: 
                            settings["chat"] = False
                            cl.sendMessage(to, "Auto chat dimatikan")
                        elif text.lower() == "block url":
                                settings["protecturl"][msg.to] = True
                                cl.sendMessage(msg.to,"Link/QR dilindungi")
                                print("[Perintah]block url")

                        elif text.lower() == "allow url":
                                try:
                                    del settings["protecturl"][msg.to]
                                    cl.sendMessage(msg.to,"Link/QR dibebaskan")
                                except:
                                    cl.sendMessage(msg.to,"Link/QR Proteksi Sudah dimatikan")
                                    print("[Perintah]Allow url")
                        elif text.lower() == "name lock":
                            if msg.to in settings['pname']:
                                cl.sendMessage(msg.to,"Nama grup diamankan")
                            else:
                                cl.sendMessage(msg.to,"Sudah diaktifkan")
                                settings['pname'][msg.to] = True
                                settings['pro_name'][msg.to] = cl.getGroup(msg.to).name
                        elif text.lower() == "name unlock":
                            if msg.to in settings['pname']:
                                cl.sendMessage(msg.to,"Nama grup dibebaskan")
                                del settings['pname'][msg.to]
                            else:
                                cl.sendMessage(msg.to,"Siap dimatikan")          
                        elif text.lower() == "block invite":
                                settings["autocancel"][msg.to] = True
                                cl.sendMessage(msg.to,"Akses invite dibatasi")
                                print("[Perintah]block invite")

                        elif text.lower() == "allow invite":
                                try:
                                    del settings["autocancel"][msg.to]
                                    cl.sendMessage(msg.to,"Akses invite dibebaskan")
                                except:
                                    cl.sendMessage(msg.to,"Akses invite sudah dibebaskan")
                                    print("[Perintah]Allow invite")

                        elif text.lower() == 'rinjani agresif':
                             try:
                                settings["BlockACCESS"][msg.to] = True
                                cl.sendMessage(msg.to,"Proteksi mode agresif")
                                print("[Perintah]block kses")
                             except:
                                cl.sendMessage(msg.to,"Proteksi sudah ditingkatkan")
                        elif text.lower() == 'Rinjani normal':
                                try:
                                    del settings["BlockACCESS"][msg.to]
                                    cl.sendMessage(msg.to,"Keamanan mode normal")
                                except:
                                    cl.sendMessage(msg.to,"Keamanan mode normal")
                                    print("[Perintah]Allow join")
                        elif text.lower() == 'main on':
                             try:
                                settings["main"][msg.to] = True
                                cl.sendMessage(msg.to,"Proteksi kick diaktifkan")
                                print("[Perintah]block kick")
                             except:
                                cl.sendMessage(msg.to,"Proteksi kick sudah aktif")
                
                        elif text.lower() == 'main off':
                                try:
                                    del settings["main"][msg.to]
                                    cl.sendMessage(msg.to,"Proteksi kick dimatikan")
                                except:
                                    cl.sendMessage(msg.to,"Proteksi kick sudah mati")
                                    print("[Perintah]Allow kick")

                        # Bonus fun command
                        elif text.lower().startswith("searchimage "):
                            start = time.time()
                            sep = text.split(" ")
                            query = text.replace(sep[0] + " ","")
                            url = "https://www.google.com/search?q=" + query.replace(" ","") + "&espv=2&biw=1366&bih=667&site=webhp&source=lnms&tbm=isch&sa=X&ei=XosDVaCXD8TasATItgE&ved=0CAcQ_AUoAg"
                            raw_html = (download_page(url))
                            items = []
                            items = items + (_images_get_all_items(raw_html))
                            path = random.choice(items)
                            if settings["server"] == "VPS":
                                cl.sendImageWithURL(to, str(path))
                            else:
                                urllib.urlretrieve(path, "imgresult.jpg")
                                cl.sendImage(to, "imgresult.jpg")
                            ass = items.index(path)
                            ast = len(items)
                            elapsed_time = time.time() - start
                            cl.sendMessage(to, "[ Image Search ]\nGambar ke {}\nTotal gambar {}\nKecepatan : {} detik".format(str(ass), str(ast), str(elapsed_time)))
                        elif text.lower() == "liststicker":
                            with open('sticker.json','r') as fp:
                                stickers = json.load(fp)
                            ret_ = "╔══[ List Sticker ]"
                            for sticker in stickers:
                                ret_ += "╠ " + sticker.title()
                            ret_ += "╚══[ Total {} Stickers ]".format(str(len(stickers)))
                            cl.sendMessage(to, ret_)
                        elif text.lower().startswith("spamsticker "):
                            sep = text.split(" ")
                            text = text.replace(sep[0] + " ","")
                            cond = text.split(" ")
                            jml = int(cond[0])
                            stickername = str(cond[1]).lower()
                            with open('sticker.json','r') as fp:
                                stickers = json.load(fp)
                            if stickername in stickers:
                                sid = stickers[stickername]["STKID"]
                                spkg = stickers[stickername]["STKPKGID"]
                            else:
                                return
                            for x in range(jml):
                                cl.sendSticker(to, spkg, sid)
                        elif '/sambutan: ' in text.lower():
                            sep = text.split(": ")
                            sambut = text.replace(sep[0] + ": ","")
                            settings["greeting"] = sambut
                            cl.sendMessage(msg.to,"Pesan sambutan diubah.")
                        elif text.lower() == 'cek sambutan':
                            cl.sendMessage(msg.to,"Pesan sambutan yang dipakai:\n\n" + settings["greeting"])

                        elif '/pesan left: ' in text.lower():
                            sep = text.split(": ")
                            sambut = text.replace(sep[0] + ": ","")
                            settings["left"] = sambut
                            cl.sendMessage(msg.to,"Pesan left diubah.")
                        elif '/pesan add: ' in text.lower():
                            sep = text.split(": ")
                            sambut = text.replace(sep[0] + ": ","")
                            settings["cot"] = sambut
                            cl.sendMessage(msg.to,"Pesan add diubah.")
                        elif 'wordban: ' in text.lower():
                            sep = text.split(": ")
                            sambut = text.replace(sep[0] + ": ","")
                            settings["bahaya"][sambut] = True
                        elif text.lower() == 'cek add':
                            cl.sendMessage(msg.to,"Pesan add yang dipakai:\n\n" + settings["cot"])
                        elif text.lower() == 'cek left':
                            cl.sendMessage(msg.to,"Pesan left yang dipakai:\n\n" + settings["left"])
                        elif text.lower() == 'clear ban':
                            settings["blacklist"] = {}
                            cl.sendMessage(msg.to,"Resik mbah")
                        elif text.lower() == 'clear wl':
                            settings["PEKI"] = {}
                            cl.sendMessage(msg.to,"Resik mbah")
                        elif 'jadwal sholat: ' in text.lower():
                            sep = text.split(": ")
                            location = text.replace(sep[0] + ": ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                if data[1] != "Subuh : " and data[2] != "Dzuhur : " and data[3] != "Ashr : " and data[4] != "Maghrib : " and data[5] != "Isha : ":
                                    ret_ = "[ Jadwal Sholat ]"
                                    ret_ += "\n Location : " + data[0]
                                    ret_ += "\n " + data[1]
                                    ret_ += "\n " + data[2]
                                    ret_ += "\n " + data[3]
                                    ret_ += "\n " + data[4]
                                    ret_ += "\n " + data[5]
                                    ret_ += "\n[ Done ]"
                                else:
                                    ret_ = "[ Jadwal Sholat ] Error : Lokasi tidak ditemukan" 
                                cl.sendMessage(to, str(ret_))

                        elif '/lirik ' in text.lower():
                            sep = text.split(" ")
                            judul = text.replace(sep[0] + " ","")
                            url = "http://rahandiapi.herokuapp.com/lyricapi?key=betakey&q="
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                content = web.get(url + judul).json()
                                lirik = content["lyric"]
                                judul = content["title"]
                                hasil = str(judul)
                                hasil += "\n\n"
                                hasil += str(lirik)
                                cl.sendMessage(msg.to,hasil)

                        elif '/film ' in text.lower():
                            sep = text.split(" ")
                            proses = text.replace(sep[0] + " ","")
                            prosess = proses.split()
                            title = prosess[0]
                            tahun = prosess[1]
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://www.omdbapi.com/?t="+title+"&y="+tahun+"&plot=full&apikey=4bdd1d70")
                                data=r.text
                                data=json.loads(data)
                                hasil = "Informasi \n" +str(data["Title"])+ " (" +str(data["Year"])+ ")"
                                hasil += "\n\n " +str(data["Plot"])
                                hasil += "\n\nDirector : " +str(data["Director"])
                                hasil += "\nActors   : " +str(data["Actors"])
                                hasil += "\nRelease : " +str(data["Released"])
                                hasil += "\nGenre    : " +str(data["Genre"])
                                hasil += "\nRuntime   : " +str(data["Runtime"])
                                img = data["Poster"]
                                cl.sendImageWithURL(msg.to,img)
                                cl.sendMessage(msg.to,hasil)
                                print("[Notif] Search Info Film Success")


                        elif '/wiki ' in text.lower():
                            try:
                                sep = text.split(" ")
                                wiki = text.replace(sep[0] + " ","")
                                wikipedia.set_lang("id")
                                pesan="Title ("
                                pesan+=wikipedia.page(wiki).title
                                pesan+=")\n\n"
                                pesan+=wikipedia.summary(wiki, sentences=1)
                                pesan+="\n"
                                pesan+=wikipedia.page(wiki).url
                                cl.sendMessage(msg.to, pesan)
                                print("[Notif] Search Artikel Id Wikipedia Sucess")
                            except:
                                try:
                                    sep = text.split(" ")
                                    wiki = text.replace(sep[0] + " ","")
                                    wikipedia.set_lang("en")
                                    pesan="Title ("
                                    pesan+=wikipedia.page(wiki).title
                                    pesan+=")\n\n"
                                    pesan+=wikipedia.summary(wiki, sentences=1)
                                    pesan+="\n"
                                    pesan+=wikipedia.page(wiki).url
                                    cl.sendMessage(msg.to, pesan)
                                    print("[Notif] Search Artikel En Wikipedia Sucess")
                                except:
                                    try:
                                        pesan="Melebihi Batas. Silahkan Click link ini\n"
                                        pesan+=wikipedia.page(wiki).url
                                        cl.sendMessage(msg.to, pesan)
                                        print("[Notif] Text Full Wikipedia Sucess")
                                    except Exception as e:
                                        cl.sendMessage(msg.to, str(e))

                        elif '/gambar ' in text.lower():
                            start = timeit.timeit()
                            sep = msg.text.split(" ")
                            query = msg.text.replace(sep[0] + " ","")
                            url = "https://www.google.com/search?q=" + query.replace(" ","") + "&espv=2&biw=1366&bih=667&site=webhp&source=lnms&tbm=isch&sa=X&ei=XosDVaCXD8TasATItgE&ved=0CAcQ_AUoAg"
                            raw_html =  (download_page(url))
                            items = []
                            items = items + (_images_get_all_items(raw_html))
                            path = random.choice(items)
                            try:
                                cl.sendImageWithURL(msg.to,path)
                                cl.sendMessage(msg.to, "「Google Image」\nType: Search Image\nTime taken: %s" % (start) +"\nTotal Image Links = "+str(len(items)))
                                print("[Notif] Search Image Google Sucess")
                            except Exception as e:
                                cl.sendMessage(msg.to, str(e))

                        elif '/zodiak ' in text.lower():
                            sep = msg.text.split(" ")
                            proses = msg.text.replace(sep[0] + " ","")
                            prosess = proses.split()
                            nama = prosess[0]
                            tanggal = prosess[1]
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama='+nama+ '&tanggal='+tanggal")
                                data=r.text
                                data=json.loads(data)
                                lahir = data["data"]["lahir"]
                                usia = data["data"]["usia"]
                                ultah = data["data"]["ultah"]
                                zodiak = data["data"]["zodiak"]
                                cl.sendMessage(msg.to,"Tgl lahir : "+lahir+"\nUmur     : "+usia+"\nUltah   : "+ultah+"\nZodiak : "+zodiak)









                        elif '/music ' in text.lower():
                            cl.sendMessage(msg.to, "sabar lagi nyari")
                            sep = text.split(" ")
                            songname = text.replace(sep[0] + " ","")
                            params = {'songname': songname}
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?" + urllib.parse.urlencode(params))
                                data = r.text
                                data = json.loads(data)
                                for song in data:
                                  hasil = "Monggo lurrr \n\n"
                                  hasil += "Judul : " + song [0]
                                  hasil += "\nDurasi : " + song[1]
                                  hasil += "\nDownload link : " + song[4]
                                  hasil += "\n Lirik :\n " + song[5]
                                  cl.sendAudioWithURL(msg.to,song[3])
                                  cl.sendMessage(msg.to, hasil)
                                  print("[Command] Search Music Success")

                        elif 'cuaca ' in text.lower():
                            sep = text.split(" ")
                            location = text.replace(sep[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                if "result" not in data:
                                    ret_ = "[ Weather Status ]"
                                    ret_ += "\n Lokasi : " + data[0].replace("Temperatur di kota ","")
                                    ret_ += "\n Suhu : " + data[1].replace("Suhu : ","")
                                    ret_ += "\n Kelembaban : " + data[2].replace("Kelembaban : ","")
                                    ret_ += "\n Tekanan Udara : " + data[3].replace("Tekanan udara : ","")
                                    ret_ += "\n Kecepatan Angin : " + data[4].replace("Kecepatan angin : ","")
                                    ret_ += "\n[ Done ]"
                                else:
                                    ret_ = "[ Weather Status ] Error : Lokasi tidak ditemukan"
                                cl.sendMessage(to, str(ret_))

                        elif text.lower() == "cancel":
                            if msg.toType == 2:
                                X = cl.getGroup(msg.to)
                                cl.sendMessage(msg.to,"Sorry gua cancel pendingannya")
                                if X.invitee is not None:
                                    gInviMids = [contact.mid for contact in X.invitee]
                                    cl.cancelGroupInvitation(msg.to, gInviMids)
                                else:
                                    cl.sendMessage(msg.to,"Pendingan kosong")
           
                        elif 'cek lokasi: ' in text.lower():
                            sep = text.split(": ")
                            location = text.replace(sep[0] + ": ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                if data[0] != "" and data[1] != "" and data[2] != "":
                                    link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                    ret_ = "[ Info Lokasi ]"
                                    ret_ += "\n Lokasi : " + data[0]
                                    ret_ += "\n Google Maps : " + link
                                    ret_ += "\n[ Sampun ]"
                                else:
                                    ret_ = "[ Details Location ] Error : Lokasi tidak ditemukan"
                                cl.sendMessage(to,str(ret_))


                        elif msg._from in wait["target"] and wait["copy"] == True and wait["copy2"] == "target":
                            for i in range(1):
                                cl.sendMessage(msg.to,msg.text)
                                wait["copy"] = False
                            wait["copy"] = True

                        elif 'halo kak @' in text.lower():
                                target = msg.text.replace("halo kak @","")
                                gc = cl.getGroup(msg.to)
                                targets = []
                                for member in gc.members:
                                    if member.displayName == target.rstrip('  '):
                                        targets.append(member.mid)
                                if targets == []:
                                    cl.sendMessage(msg.to, "oiii")
                                else:
                                    for t in targets:
                                        wait["target"][t] = True
                                    cl.sendMessage(msg.to,"oii")

                        elif 'udahan ' in text.lower():
                                target = msg.text.replace("udahan @","")
                                gc = cl.getGroup(msg.to)
                                targets = []
                                for member in gc.members:
                                    if member.displayName == target.rstrip('  '):
                                        targets.append(member.mid)
                                if targets == []:
                                    cl.sendMessage(msg.to, "gak kenal")
                                else:
                                    for t in targets:
                                        del wait["target"][t]
                                    cl.sendMessage(msg.to,"capek")

                        elif text.lower() == "targetku":
                                    if wait["target"] == {}:
                                        cl.sendMessage(msg.to,"gak tau")
                                    else:
                                        mc = "Targetmu ini\n"
                                        for mi_d in wait["target"]:
                                            mc += "* "+cl.getContact(mi_d).displayName + "\n"
                                        cl.sendMessage(msg.to,mc)
                          
                # Check if only image
                elif msg.contentType == 1:
                    if switch["changePicture"] == True:
                        path = cl.downloadObjectMsg(msg_id)
                        switch["changePicture"] = False
                        cl.updateProfilePicture(path)
                        cl.sendMessage(to, "PP diganti")
                    if msg.toType == 2:
                        if to in settings["changeGroupPicture"]:
                            path = cl.downloadObjectMsg(msg_id)
                            settings["changeGroupPicture"].remove(to)
                            cl.updateGroupPicture(to, path)
                            cl.sendMessage(to, "Berhasil mengubah foto group")
                    if switch["cp1"] == True:
                        path = cl.downloadObjectMsg(msg_id)
                        switch["cp1"] = False
                        ki.updateProfilePicture(path)
                        cl.sendMessage(to, "PP bot 1 diganti")
                    if switch["cp2"] == True:
                        path = cl.downloadObjectMsg(msg_id)
                        switch["cp2"] = False
                        kk.updateProfilePicture(path)
                        cl.sendMessage(to, "PP bot 2 diganti")
                    if switch["cp3"] == True:
                        path = cl.downloadObjectMsg(msg_id)
                        switch["cp3"] = False
                        kc.updateProfilePicture(path)
                        cl.sendMessage(to, "PP bot 3 diganti")
                    if switch["cp4"] == True:
                        path = cl.downloadObjectMsg(msg_id)
                        switch["cp4"] = False
                        ks.updateProfilePicture(path)
                        cl.sendMessage(to, "PP bot 4 diganti")



        if op.type == 32:
          if op.param1 in settings["main"]:
            if op.param2 in Bots:
                pass
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                contact = cl.getContact(op.param2)
                random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
                cl.kickoutFromGroup(op.param1,[op.param2])
                settings["blacklist"][op.param2] = True

        if op.type == 26:
            msg = op.message
            if msg._from in settings["blacklist"]:
               try:
                  cl.kickoutFromGroup(msg.to,[msg._from])
               except:
                    random.choice(KAC).kickoutFromGroup(msg.to,[msg._from])

            elif msg._from in wait["target"] and wait["copy"] == True and wait["copy2"] == "target":
                for i in range(1):
                    cl.sendMessage(msg.to,msg.text)
                    wait["copy"] = False
                wait["copy"] = True

        if op.type == 26:
           msg = op.message
           if settings["chat"] == True:
            if "Berapa besar cinta " in msg.text:
                tanya = msg.text.replace("Berapa besar cinta ","")
                jawab = ("10%","20%","30%","40%","50%","60%","70%","80%","90%","100%")
                jawaban = random.choice(jawab)
                cl.sendMessage(msg.to,"Besar cinta " + tanya + " adalah " + jawaban)

            elif "Berapa besar dosa " in msg.text:
                tanya = msg.text.replace("Berapa besar dosa ","")
                jawab = ("10%","20%","30%","40%","50%","60%","70%","80%","90%","100%")
                jawaban = random.choice(jawab)
                cl.sendMessage(msg.to,"Besar dosa " + tanya + " adalah " + jawaban + " sampai saat ini")

            elif "Kerang ajaib " in msg.text:
                tanya = msg.text.replace("Kerang ajaib ","")
                jawab = ("TIDAK","YA")
                jawaban = random.choice(jawab)
                cl.sendMessage(msg.to,"Demi Neptunus dan samudra ini")
                cl.sendMessage(msg.to,"Akan aku jawab " + jawaban)

            elif msg.text in ["Assalamualaikum","assalamualaikum","asalamualaikum","Asalamualaikum"]:
                if msg.toType == 2:
                 cl.sendMessage(msg.to, "Wa'alaikum salam...")

            elif msg.text in ["pagi","selamat pagi","Selamat pagi","Pagi"]:
                if msg.toType == 2:
                 cl.sendMessage(msg.to, "Selamat pagi kak, jangan lupa sarapan yak")

            elif msg.text in ["malam","Malam","malem","met malem","Met malem"]:
                if msg.toType == 2:
                 cl.sendMessage(msg.to, "Selamat malam kak, gimana tadi harinya ?")

            elif msg.text in ["Sepi","sepi","kok sepi","Kok sepi","tumben sepi"]:
                if msg.toType == 2:
                 cl.sendMessage(msg.to, "Ramein dong kalo sepi, drpd read doang")

            elif msg.text in ["sayang","beb","Sayang","Sayangku"]:
                if msg.toType == 2:
                 cl.sendMessage(msg.to, "iya sayang, ada apa")
                 cl.sendMessage(msg.to, "kangen aku ya")
            elif msg.text in ["iya kangen","anen banget","Iya kangen","Anen banget"]:
                if msg.toType == 2:
                 cl.sendMessage(msg.to, "Tabahkan hatimu kak")
                 cl.sendMessage(msg.to, "Terima kenyataanmu")

            elif msg.text in ["salken","Salken","salken kak","Salken kak"]:
                if msg.toType == 2:
                 cl.sendMessage(msg.to, "Salam kenal kak")
                 cl.sendMessage(msg.to, "moga betah disini yak")

            elif msg.text in ["Sarapan","jangan lupa sarapan","Jgn lupa sarapan","sarapan","jan lupa sarapan"]:
                if msg.toType == 2:
                 cl.sendMessage(msg.to, "Iya kak, aku tau kok senyum gak bisa buat kenyang")
                 cl.sendMessage(msg.to, "Jadinya aku sarapan :')")

            elif msg.text in ["Galau","Galon","aku galau","Aku galau","galau","bikin galau","galon"]:
                if msg.toType == 2:
                 cl.sendMessage(msg.to, "Sabar kak, semua cobaan")
                 cl.sendMessage(msg.to, "tabahkan hatimu")

            elif msg.text in ["sinyal baper","Sinyal baper","Sinyal sue","sinyal jelek","Sinyal jelek","jelek sinyalnya","sinyal sue"]:
                if msg.toType == 2:
                 cl.sendMessage(msg.to, "Kalo beli hp sama sinyalnya")
                 cl.sendMessage(msg.to, "Hp bagus kok gak da sinyal")
           else:
             pass






        if op.type == 26:
                msg = op.message
                if msg.text != None:
                    if msg.toType == 2:
                      if settings["dm"] == True:
                        may = cl.getProfile().mid
                        if may in str(msg.contentMetadata) and 'MENTION' in str(msg.contentMetadata):
                            pilih = ['hmm, di tag lagi','jan tag lah, pm lgsg aja','nah loh, aku ter-tag','gak da kerjaan ya, ngetag mele','ter-tag entah lu orang atau bot']
                            rslt = random.choice(pilih)
                            cl.sendMessage(msg.to, str(rslt))
                        else:
                            pass
                      else:
                          pass
                    else:
                        pass
                else:
                    pass

        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = sender
                elif msg.toType == 2:
                    to = receiver
                if settings["autoRead"] == True:
                    cl.sendChatChecked(to, msg_id)
                if to in cctv['point']:
                    if sender in cctv['sidermem'][to]:
                        del cctv['sidermem'][to][sender]

        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = cl.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n~ " + Name
                                #cl.mention(op.param1, op.param2)
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        cl.sendMessage(op.param1, 'Cie yang lagi baca '+nick[0])
                                    else:
                                        cl.sendMessage(op.param1, 'Haloo, sini dong chat '+nick[1])
                                else:
                                    cl.sendMessage(op.param1, 'Keluar dong '+Name + ' Jan sider mele')
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

        backupData()
    except Exception as error:
        logError(error)

while True:
    try:
        autoRestart()
        ops = poll.singleTrace(count=1)
        if ops is not None:
            for op in ops:
               # bot(op)
                # Don't remove this line, if you wan't get error soon!
                poll.setRevision(op.revision)
                thread1 = threading.Thread(target=bot, args=(op,))#self.OpInterrupt[op.type], args=(op,)
                thread1.daemon = True
                thread1.start()
    except Exception as e:
        logError(e)
