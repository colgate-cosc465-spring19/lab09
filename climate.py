#!/usr/bin/env python3

import requests
import re

# Examine each domain
with open('domains.txt', 'r') as df:
    for domain in df:
        domain = domain.strip()

        # Issue HTTP request
        # Set user-agent to Chrome, otherwise some sites refuse the request
        r = requests.get('http://' + domain + '/', headers={'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'})

        # Count the number of occurences of the word 'climate' in the page
        m = re.findall('climate', r.text, re.IGNORECASE)

        # If the word climate appears less than 10 times, assume the page is
        # about climate change denial
        if len(m) < 10:
            print(domain + ' DENIAL')
        else:
            print(domain + ' VALID')
