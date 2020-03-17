import json
# loading json file
file = open("incidents.json")
json_file = json.load(file)

# question one
src_ips =[]
hashes = set()
for i in range(10):
    src_ips.append(json_file['tickets'][i]['src_ip'])
    hashes.add(json_file['tickets'][i]['file_hash'])
most_common_src_ip = max(src_ips, key=src_ips.count)
print('Most common source IP is :',most_common_src_ip)

# question two
ip = input('Unique destination IP adresses for : ')
if not ip:
    ip = most_common_src_ip
unique_dest_ips = []
for i in range(10):
    if json_file['tickets'][i]['src_ip'] == ip:
        unique_dest_ips.append(json_file['tickets'][i]['dst_ip'])
print(f'Unique destination IP adresses for {ip} is : {len(unique_dest_ips)}')

# question three
dhashes = dict.fromkeys(hashes,0)
for hash in hashes:
    hash_dst_list = []
    for i in range(10):
        if json_file['tickets'][i]['file_hash'] == hash:
            if json_file['tickets'][i]['dst_ip'] not in hash_dst_list:
                hash_dst_list.append(json_file['tickets'][i]['dst_ip'])
                dhashes[hash] = dhashes[hash]+1
number=0
for v in dhashes.values():
    number = number+v
av = str(number/len(hashes))[:4]
print('Average is :',av)
