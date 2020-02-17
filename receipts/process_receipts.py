import glob
import os
import shutil
import json
import re
import math

try:
    os.mkdir("./processed")
except OSError:
    print("'processed' directory already exists")

# Get a list of receipts
# receipts = glob.glob('./new/receipt-[0-9]*.json')
receipts = [f for f in glob.iglob('./new/receipt-[0-9]*.json') 
        if re.match('./new/receipt-[0-9]*[02468].json', f)]

subtotal = 0.0
# Iterate of the receipts
for path in receipts:
    with open(path) as f:
        # read content and tally a subtotal
        content = json.load(f)
        subtotal +=  float(content['value'])
                                # split path with / and get the last name
    name = path.split('/')[-1]
                                #mv the file to the processed directory
    #destination = "./processed/%s" % name
    destination = path.replace('new', 'processed')
    shutil.move(path, destination)
                                 # print that we processed the file
    print("moved '%s' to dst '%s'" % (path, destination))

# print the subtotal of all processed receipts
print("Receipt subtotal: $%s" % round(subtotal, 2))