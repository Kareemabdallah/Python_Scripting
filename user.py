#!/bin/python

user = { 'admin': True, 'active': True, 'name': 'Kevin' }

if user['admin'] and user['active']:
    print("ACTIVE - (ADMIN) %s" % user['name'])
elif user['active'] == True:
    print("ACTIVE %s" % user['name'])
elif user['admin'] == True:
    print("(ADMIN) %s" % user['name'])
else:
    print("%s" % user['name'])
