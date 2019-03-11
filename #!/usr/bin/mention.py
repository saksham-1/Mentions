#!/usr/bin/env python
from googlesearch import search
import urllib,re
string = raw_input("type something");
print(string);
for j in search(string,tld='com',lang='en',num=1,start=0,stop=1,pause=2.0):
    print(j);
url = urllib.urlopen(j);
content = url.read();
link = re.findall(r"(?:1[-.])*(?[2-9]\d{2})?[-. ]\d{3}[-. ]\d{4}",content);
print(link);
link = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",content);
print(link);
