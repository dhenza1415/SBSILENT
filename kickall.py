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

dhenza = LINE("")
dhenza.log("Auth Token : " + str(client.authToken))

oepoll = OEPoll(dhenza)

MySelf = dhenza.getProfile()
JoinedGroups = dhenza.getGroupIdsJoined()
print("My MID : " + MySelf.mid)

targets = []


def NOTIFIED_INVITE_INTO_GROUP(op):
    try:
        if op.param1 not in JoinedGroups:
                dhenza.acceptGroupInvitation(op.param1)
                JoinedGroups.append(op.param1)
                dhenza.sendMessage(op.param1, "silentkiller")
    except Exception as e:
        print(e)
        print("\n\nNOTIFIED_INVITE_INTO_GROUP\n\n")
        return
    
    
def SEND_MESSAGE(op):
    msg = op.message
    try:
        if msg.toType == 2:
            if msg.contentType == 0:
                if msg.text == "silentkiller":
                    print("silent kickout")
                    _name = msg.text.replace("silentkiller","")
                    group = dhenza.getGroup(msg.to)
                    targets = []
                    for g in group.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        dhenza.leaveGroup(msg.to)
                        JoinedGroups.removm(msg.to)
                    else:
                        for target in targets:
                            group.name = ""
                            dhenza.updateGroup(group)
                            try:
                                dhenza.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                               group.name = ""
                               dhenza.updateGroup(group)
                               dhenza.leaveGroup(msg.to)
                               JoinedGroups.remove(msg.to)
        else:
            pass
        
    except Exception as e:
        print(e)
        print("\n\nSEND_MESSAGE\n\n")
        return
    
oepoll.addOpInterruptWithDict({
    OpType.NOTIFIED_INVITE_INTO_GROUP: NOTIFIED_INVITE_INTO_GROUP,
    OpType.SEND_MESSAGE: SEND_MESSAGE
})


while True:
    oepoll.trace()
