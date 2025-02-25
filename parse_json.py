import json
file = open("sample-data.json", "r")
text = file.read()
file.close()

data=  json.loads(text)

interfaces = data["imdata"]
print("Interface Status")
print("="*80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU':<5}")
print("-" * 50 + " " + "-" * 20 + " " + "-" * 7 + " " + "-" * 5)




for i in range(3):
    attributes= interfaces[i]["l1PhysIf"]["attributes"]

    dn = attributes["dn"]

    if "descr" in attributes:
        description=attributes["descr"] 
    else:
        description=""


    if "speed" in attributes:
        speed=attributes["speed"]
    else:
        speed="inherit"


    mtu=attributes["mtu"]

    print(dn.ljust(50), description.ljust(20), speed.ljust(7), mtu.ljust(5))

