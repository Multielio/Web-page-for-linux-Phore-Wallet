# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 20:15:56 2018

@author: Yo#1784
"""

import subprocess      
import json
import time
from time import gmtime, strftime
lasttime = time.time()
i=0
lastbalance = 0
while i ==0:
    if time.time()-lasttime >=60:
        lastime = time.time()
        p = subprocess.Popen(["phore-cli","getinfo"], stdout=subprocess.PIPE)
        output, err = p.communicate()
        o = json.loads(output)
        newbalance = o["balance"]
    	pa = '/var/www/html/phorec.json'
		with open(pa, 'w') as outfile:
			json.dump(o, outfile)
        if newbalance != lastbalance:
            fo = open("/var/www/html/history.txt", "a+")
            fo.write(strftime("%a, %d %b %Y %H:%M:%S", gmtime())+'  Balance: {0}'.format(newbalance)+'\n')
            fo.close()
            lastbalance = newbalance
		 