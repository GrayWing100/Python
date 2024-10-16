import subprocess
import optparse
import re

#This should work properly for changing the MAC address. Make sure to run the script with appropriate permissions (e.g., using sudo).

def get_arguments():
    parser = optparse.OptionParser()
    # Komande koje mozes koristiti u terminalu, I i M suprecice
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) =  parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
    elif not options.new.mac:
        parser.error("[-] Please specify an new MAC, use --help for more info")
    return options

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    # Da zastiti od Terminala, da se nedodaju nove komande
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))

    if mac_address_search_result:
        return(mac_address_search_result(0))
    else:
        print("[-] Cloud not read MAC address.")

options = get_arguments()

current_mac = get_current_mac(options.interface)
print("[-] Current MAC : " + str(current_mac))

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[-] Mac address was successfully changed to " + current_mac)
else:
    print("[-] MAC address did not changed.")
