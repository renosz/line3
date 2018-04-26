# -*- coding: utf-8 -*-
from linepy import *
import json, time, random, tempfile, os, sys, codecs
from gtts import gTTS
from googletrans import Translator

#==================TOKEN SET AUTO===============
readOpen = codecs.open("line3/token.json","r","utf-8")
token = json.load(readOpen)
#===================SELF========================
try:
    client = LineClient(authToken=str(token["renbot1"]))
except:
    client = LineClient()
    token["renbot1"] = str(token["renbot1"])
    f=codecs.open('token.json','w','utf-8')
    json.dump(token, f, sort_keys=True, indent=4,ensure_ascii=False)
channel = LineChannel(client)
poll = LinePoll(client)
#===================ASSIST========================
try:
    assist = LineClient(authToken=str(token["renbot2"]))
except:
    assist = LineClient()
    token["renbot2"] = str(token["renbot2"])
    f=codecs.open('token.json','w','utf-8')
    json.dump(token, f, sort_keys=True, indent=4,ensure_ascii=False)
assistchannel = LineChannel(assist)
assistpoll = LinePoll(assist)
#==================BOT LOGIN SUCCESS===============

#=================   BOT SETUP  ==================
clientMid = client.getProfile().mid
assistMid = assist.getProfile().mid
renBot = [clientMid,assistMid]
KCML = [client,assist]

vol = """Simple Command:

[+] ? <- Look command
[+] 1 <- Look your contact
[+] 2 <- Look speedbot
[+] 3 <- Tagall
[+] . <- Joined assist
[+] 9 <- Check reader
[+] 0 <- Stop check reader
[+] ; <- Restart bot

Protect command:

[#] Pkick:[on/off] <- Protectkick
[#] ! @tag <- Kick with tag

[ S E L F B O T ]"""

protect = {
    "kick":{}
}
cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

while True:
    try:
        ops=poll.singleTrace(count=50)
        if ops != None:
          for op in ops:
            if op.type == 19:
                if op.param1 in protect["kick"]:
                    if op.param2 in renBot:
                        pass
                    else:
                        random.choice(KCML).kickoutFromGroup(op.param1, [op.param2])
                else:
                    pass
            if op.type == 19:
                if op.param3 in clientMid:
                    if op.param2 not in renBot:
                        assist.kickoutFromGroup(op.param1, [op.param2])
                        P = assist.getGroup(op.param1)
                        P.preventedJoinByTicket = False
                        assist.updateGroup(P)
                        invsend = 0
                        Ticket = assist.reissueGroupTicket(op.param1)
                        client.acceptGroupInvitationByTicket(op.param1, Ticket)
                        A = assist.getGroup(op.param1)
                        A.preventedJoinByTicket = False
                        assist.updateGroup(A)
                if op.param3 in assistMid:
                    if op.param2 not in renBot:
                        client.kickoutFromGroup(op.param1, [op.param2])
                        P = client.getGroup(op.param1)
                        P.preventedJoinByTicket = False
                        client.updateGroup(P)
                        invsend = 0
                        Ticket = client.reissueGroupTicket(op.param1)
                        assist.acceptGroupInvitationByTicket(op.param1, Ticket)
                        A = client.getGroup(op.param1)
                        A.preventedJoinByTicket = False
                        client.updateGroup(A)
            if op.type == 25:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                msg.from_ = msg._from
                try:
                    if msg.contentType == 0:
                        if msg.toType in [0,2]:
                            contact = client.getContact(sender)
                            if text.lower() == '?':
                                client.sendText(receiver, vol)
                            elif text.lower() == '1':
                                client.sendMessage(receiver, None, contentMetadata={'mid': sender}, contentType=13)
                            elif text.lower() == '2':
                                start = time.time()
                                client.sendText(receiver, "[ C H E C K ] : [sendText]")
                                elapsed_time = time.time() - start
                                client.sendText(receiver, "[T I M E Response] : \n%s" % (elapsed_time))
                            elif text.lower() == '3':
                                group = client.getGroup(receiver)
                                nama = [contact.mid for contact in group.members]
                                nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                                if jml <= 100:
                                    client.mention(receiver, nama)
                                if jml > 100 and jml < 200:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    client.mention(receiver, nm1)
                                    for j in range(101, len(nama)):
                                        nm2 += [nama[j]]
                                    client.mention(receiver, nm2)
                                if jml > 200 and jml < 300:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    client.mention(receiver, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    client.mention(receiver, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    client.mention(receiver, nm3)
                                if jml > 300 and jml < 400:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    client.mention(receiver, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    client.mention(receiver, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    client.mention(receiver, nm3)
                                    for l in range(301, len(nama)):
                                        nm4 += [nama[l]]
                                    client.mention(receiver, nm4)
                                if jml > 400 and jml < 501:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    client.mention(receiver, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    client.mention(receiver, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    client.mention(receiver, nm3)
                                    for l in range(301, len(nama)):
                                        nm4 += [nama[l]]
                                    client.mention(receiver, nm4)
                                    for m in range(401, len(nama)):
                                        nm5 += [nama[m]]
                                    client.mention(receiver, nm5)             
                            elif text.lower() == '.':
                                try:
                                    G = client.getGroup(receiver)
                                    G.preventedJoinByTicket = False
                                    client.updateGroup(G)
                                    invsend = 0
                                    Ticket = client.reissueGroupTicket(receiver)
                                    assist.acceptGroupInvitationByTicket(receiver, Ticket)
                                    X = client.getGroup(receiver)
                                    X.preventedJoinByTicket = True
                                    client.updateGroup(X)
                                except Exception as axsd:
                                    print(axsd)
                            elif text.lower() == '9':
                                try:
                                    del cctv['point'][receiver]
                                    del cctv['sidermem'][receiver]
                                    del cctv['cyduk'][receiver]
                                    client.sendText(receiver, "Cek sider on!")
                                except:
                                    pass
                                cctv['point'][receiver] = msg.id
                                cctv['sidermem'][receiver] = ""
                                cctv['cyduk'][receiver]=True
                            elif text.lower() == '0':
                                if msg.to in cctv['point']:
                                    cctv['cyduk'][receiver]=False
                                    client.sendText(receiver, "Check reader off!")
                                else:
                                    client.sendText(receiver, "Type 9 to get data siders")
                            elif text.lower() == ';':
                                restart_program()
                            elif text.lower().startswith("!"):
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    if target not in renBot:
                                        random.choice(KCML).kickoutFromGroup(receiver, [target])
                            elif text.lower().startswith("pkick"):
                                pset = text.split(":")
                                pk = text.replace(pset[0] + ":","")
                                if pk == "on":
                                    if receiver in protect["kick"]:
                                        client.sendText(receiver, "Protect kick already On!")
                                    else:
                                        protect["kick"][receiver] = True
                                        client.sendText(receiver, "Protect kick set On!")
                                if pk == "off":
                                    if receiver in protect["kick"]:
                                        del protect["kick"][receiver]
                                        client.sendText(receiver, "Protect kick set Off!")
                                    else:
                                        client.sendText(receiver, "Protect kick already Off!")
                except Exception as e:
                    client.log("[SEND_MESSAGE] ERROR : " + str(e))
            elif op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = client.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n~ " + Name
                                pref=['eh ada','hai kak','aloo..','nah','lg ngapain','halo','sini kak']
                                client.sendText(op.param1, str(random.choice(pref))+' '+Name)
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

            else:
                pass
#=========================================================================================================================================#
            # Don't remove this line, if you wan't get error soon!
            poll.setRevision(op.revision)
            
    except Exception as e:
        client.log("[SINGLE_TRACE] ERROR : " + str(e))
