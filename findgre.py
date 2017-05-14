#! /bin/python3

import requests
import bs4 as bs

#cloud = str(input("Enter cloud name (zscaler.net, zscalertwo.net, zscloud.net, zscalerone.net, zscalerbeta.net) : "))

f = open("loca.txt", "r")



for line in f :
    if line in ['\n', '\r\n']:
        continue
    ip = line
    #print (ip)
    r = requests.post('https://tools.zscaler.com/findgre/?', data = {"import":"customer", "cloud_name":"zscalertwo.net", "tunnel":"public_cloud", "ip":ip})
    soup = bs.BeautifulSoup(r.text, 'html.parser')
    dc = soup.find_all('b', text=True)
    #print (type(dc))
    print ("IP adress: " + str(ip).replace('\n',''))
    print ("Primary DC: " + dc[0].text)
    print ("Secondary DC: " + dc[1].text)
    print ("====================================================")
    print ()

f.close()



