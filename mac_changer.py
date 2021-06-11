#!/usr/bin/env python

import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="INTERFACE TO CHANGE MAC ADD.")
    parser.add_option("-m", "--macadd", dest="new_mac", help="ENTER MAC ADD. TO CHANGE ")
    (options, arguments) =  parser.parse_args()
    if not options.interface :
        parser.error("[-] PLEASE ENTER INTERFACE, USE --help FOR MORE INFO")
    elif not options.new_mac :
        parser.error("[-] PLEASE ENTER NEW MAC ADDRESS, USE --help FOR MORE INFO")
    return options

def change_mac (interface , new_mac):
    print("[+] changing mac add. for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_add_search_re = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if mac_add_search_re:
        return mac_add_search_re.group(0)
    else:
        print("[-] Could not read mac address")

# parser = optparse.OptionParser()
# parser.add_option("-i" ,"--interface" , dest = "interface" , help="INTERFACE TO CHANGE MAC ADD.")
# parser.add_option("-m" ,"--macadd" , dest = "new_mac" , help="ENTER MAC ADD. TO CHANGE ")

# (options, arguments) = parser.parse_args()
# print("[+] changing mac add. for " + interface + " to " + new_mac)
# subprocess.call("ifconfig " + interface + " down" , shell = True)
# subprocess.call("ifconfig " + interface + " hw ether " + new_mac , shell = True)
# subprocess.call("ifconfig " + interface + " up" , shell = True)

# subprocess.call(["ifconfig", interface, "down"])
# subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
# subprocess.call(["ifconfig", interface, "up"])

options = get_arguments()
current_mac = get_current_mac(options.interface)
print("Current Mac = " + str(current_mac))
change_mac(options.interface , options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC address was successfully changed to " + current_mac )
else:
    print("[-] MAC address did not get changed")
