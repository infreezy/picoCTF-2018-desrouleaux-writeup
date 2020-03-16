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


"""bruteforcing socket script : 
import socket,time,re

port = 14079
host = "2018shell1.picoctf.com"
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))


def first(sock):
    res = sock.recv(250).decode('utf-8')
    sock.send('248.0.40.3\n'.encode('utf-8'))
    res = sock.recv(250).decode('utf-8')
    res = res.split('\n')
    return res
def which(ip):
    if ip == "159.244.90.48":
        return "3\n"
    if ip == "248.0.40.3":
        return "4\n"
    if ip == "109.165.249.213":
        return "2\n"
def second(sock, first_res):
    ip = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',first_res[-2]).group()
    ans = which(ip)
    sock.send(ans.encode('utf-8'))
    res = sock.recv(250).decode('utf-8')
    res.split('\n')
    return res
def third(sock, ans):
    ans = str(ans) + "\n"
    sock.send(ans.encode('utf-8'))
    res = sock.recv(250).decode('utf-8')
    res = res.split('\n')
    return res


for third_ans in [1.28, 1.29]:

    print("Trying", third_ans)

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as err:
        print("socket creation failed with error %s" % (err))
    sock.connect((host, port))

    first_res = first(sock)

    second_res = second(sock, first_res)

    third_res = third(sock, third_ans)
    print("THIRD----->", third_res)

    if third_res[0] == "Correct!":
        break

    sock.close()

    time.sleep(1.0)"""
