import time
import re

file = open('/var/log/nginx/access.log')
file.seek(-1,2)

while True:
        where=file.tell()
        line=file.readline()
        if not line:
                time.sleep(0.5)
                file.seek(where)
        else:
                print(line)
                i = re.findall("HTTP/1.1\" (.*?) \"-\"", line)
                if len(i)>0:
                        statusCode = i[0][:3]
                        print(statusCode)
                        if statusCode > 405:
                                print("error")
