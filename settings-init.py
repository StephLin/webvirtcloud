#!/usr/bin/python
import random, string

config = ''

with open('./webvirtcloud/settings.py.template', 'r') as iFile:
    for line in iFile:
        config += line + "\n"
    haystack = string.ascii_letters + string.digits + string.punctuation
    config = config.replace("SECRET_KEY = ''", "SECRET_KEY = '" + ''.join([random.SystemRandom().choice(haystack) for _ in range(50)]) + "'")

with open('./webvirtcloud/settings.py', 'w') as oFile:
    oFile.write(config)

