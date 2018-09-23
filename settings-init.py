#!/usr/bin/python
import random, string

config = ''

with open('./webvirtcloud/settings.py.template', 'r') as iFile:
    for line in iFile:
        if "SECRET_KEY" in line:
            haystack = string.ascii_letters + string.digits + string.punctuation
            config += "SECRET_KEY = '" + ''.join([random.SystemRandom().choice(haystack) for _ in range(50)]).replace('"', '#').replace("'", '$') + "'\n"
            continue
        config += line

with open('./webvirtcloud/settings.py', 'w') as oFile:
    oFile.write(config)

