#!/usr/bin/python3

from pwn import *
import re
import json

r = remote('2018shell1.picoctf.com', 10493)

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

print(r.recv().decode())
r.send(most_common_src_ip+'\n')

# question two

result = r.recv().decode()
print(result)
ip = re.findall(r'\d+.\d+.\d+.\d+',result)[0]

unique_dest_ips = []
for i in range(10):
    if json_file['tickets'][i]['src_ip'] == ip:
        unique_dest_ips.append(json_file['tickets'][i]['dst_ip'])

r.send(str(len(unique_dest_ips))+'\n')
print(r.recv().decode())

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


r.send(av+'\n')
result = r.recv().decode()
flag = re.findall(r'picoCTF{.*}',result)[0]
print(f'flag is : {flag}')

r.close()
