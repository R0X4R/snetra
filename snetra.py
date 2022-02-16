#!/usr/bin/env python3

'''
Author: Eshan Singh (R0X4R)
Version: 1.0
'''

#@> IMPORTING MODULES
import requests
import json
from sys import stdin, exit
from re import findall, match
from time import sleep

#@> READ STDIN
for host in stdin.readlines():
    if match("^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", str(host.strip())):
        try:
            header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"}
            link = str("https://internetdb.shodan.io/{}".format(host.strip()))
            response = requests.get(link, headers=header, timeout=20).text # SEND REQUEST
            data = json.loads(response) # FILTER RESULTS
            if findall(r"No information available", str(data.values())): # CHECK IF INFORMATION AVAILABLE OR NOT
                print("No information available for {}".format(str(host.strip())))
            else: # IF YES THEN
                #@> ASSIGNING VARIABLES TO RESULTS
                cpes = data["cpes"]
                hostnames = data["hostnames"]
                ip = data["ip"]
                ports = data["ports"]
                tags = data["tags"]
                vulns = data["vulns"]
                #@> PRINT RESULTS
                print("TARGET: {}".format(str(ip)))
                if len(ports) == 0:
                    print("PORTS: Not Found")
                else:
                    print("PORTS:", *ports, sep=" ")
                if len(hostnames) == 0:
                    print("HOSTNAMES: Not Found")
                else:
                    print("HOSTNAMES:", *hostnames, sep=" ")
                if len(cpes) == 0:
                    print("CPES: Not Found")
                else:
                    print("CPES:", *cpes, sep=" ")
                if len(tags) == 0:
                    print("TAGS: Not Found")
                else:
                    print("TAGS:", *tags, sep=" ")
                if len(vulns) == 0:
                    print("VULNS: Not Found \n")
                else:
                    print("VULNS:", *vulns, sep=" ")
                    print("\n")
            sleep(2) # SLEEP 2s
        except requests.Timeout: # IF REQUEST GET TIMEOUT ERROR THEN
            pass
        except KeyboardInterrupt: # IF CTRL+C PRESSED THEN
            print("\nCTRL+C, pressed... Exiting")
            exit(0)
        except requests.ConnectionError: # IF REQUEST CONNECTION ERROR THEN
            pass
        except: # IF ANYOTHER ERROR THEN
            pass
    else:
        print("Invalid IP:", str(host.strip()))
        print("\n")