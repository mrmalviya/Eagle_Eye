import os
import subprocess
import time
import urllib
import urllib.request
import json


def ip_finder():
                user_input = input("\033[1;91m[+] Provide Domain or IP Address: \033[1;m").lower()
                url = ("http://ip-api.com/json/")
                response = urllib.request.urlopen(url + user_input)
                data = response.read()
                json_data_output = json.loads(data)
                os.system("reset")
                print("\033[34m[~] Searching IP Location Finder: \033[0m".format(url) + user_input)
                time.sleep(1.5)

                print("\n [+] \033[34mUrl: " + user_input + "\033[0m")
                print(" [+] " + "\033[34m" + "IP: " + json_data_output["query"] + "\033[0m")
                print(" [+] " + "\033[34m" + "Status: " + json_data_output["status"] + "\033[0m")
                print(" [+] " + "\033[34m" + "Region: " + json_data_output["regionName"] + "\033[0m")
                print(" [+] " + "\033[34m" + "Country: " + json_data_output["country"] + "\033[0m")
                print(" [+] " + "\033[34m" + "City: " + json_data_output["city"] + "\033[0m")
                print(" [+] " + "\033[34m" + "ISP: " + json_data_output["isp"] + "\033[0m")
                print(" [+] " + "\033[34m" + "Lat & Lon: " + str(json_data_output['lat']) + " & " + str(json_data_output['lon']) + "\033[0m")
                print(" [+] " + "\033[34m" + "Zipcode: " + json_data_output["zip"] + "\033[0m")
                print(" [+] " + "\033[34m" + "TimeZone: " + json_data_output["timezone"] + "\033[0m")
                print(" [+] " + "\033[34m" + "AS: " + json_data_output["as"] + "\033[0m" + "\n") 

