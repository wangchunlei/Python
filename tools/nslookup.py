import os
import re
import subprocess

nslkp_domain = 'google.com'
nslkp_type = 'NS'
nslkp = 'nslookup'
out = subprocess.Popen([nslkp, nslkp_domain,
                        '8.8.8.8'], stdout=subprocess.PIPE).communicate()[0]

result = out.split("\n")
nslkp_result = {}
for data in result:
    if re.search('Address', data):
        data = data.split(":")
        ip = data[1]
        if '8.8.8.8' not in ip:
            times = [line.rpartition(
                '=')[-1] for line in subprocess.check_output(['ping', '-c', '3', 'localhost']).splitlines()[1:-4]]
            nslkp_result[ip] = times


print('Nameservers for domain :', nslkp_domain)
for ns, time in nslkp_result.items():
    print(ns + ":" + ','.join(time))
