import json
file = open("incidents.json")
json_file = json.load(file)
src_ips =[]
hashes = set()
for i in range(9):
    src_ips.append(json_file['tickets'][i]['src_ip'])
    hashes.add(json_file['tickets'][i]['file_hash'])
print('Most common source IP is :',max(src_ips, key=src_ips.count))
ip = input('>')
if not ip:
    ip = max(src_ips, key=src_ips.count)
def uniq():
    unique_dest_ips = []
    for i in range(9):
        if json_file['tickets'][i]['src_ip'] == ip:
            unique_dest_ips.append(json_file['tickets'][i]['dst_ip'])
    return unique_dest_ips
print(f'Unique destination IP adresses for {ip} is : {len(uniq())}')
n = 0
for i in range(9):
    for hash in hashes:
        if json_file['tickets'][i]['file_hash'] == hash:
            n += 1
av = str(n/len(hashes))[:4]
print('Average is :',av)
