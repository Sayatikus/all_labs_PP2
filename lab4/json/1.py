import json

file_path = "/Users/zhaulybek7icloud.com/Documents/pp2_all_labs/labs/lab4/json/sample_data.json"


with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

if "imdata" not in data:
    print("Ошибка: ключ 'imdata' отсутствует в файле JSON.")
    exit()

interfaces = data["imdata"]

print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<10} {:<10}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

for interface in interfaces:
    attributes = interface.get("l1PhysIf", {}).get("attributes", {})

    dn = attributes.get("dn", "N/A")
    description = attributes.get("descr", "")  
    speed = attributes.get("speed", "inherit") 
    mtu = attributes.get("mtu", "N/A")  

    print("{:<50} {:<20} {:<10} {:<10}".format(dn, description, speed, mtu))