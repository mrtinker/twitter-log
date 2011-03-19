#!/usr/bin/env python

#import site
import sys, os

basedir = os.path.realpath(__file__).split('/')
#print "__file__:%s" % (__file__,)
#print "basedir:%s" % (basedir,)
basedir.pop()
basedir.pop()
basedir = '/'.join(basedir)

#for virtualenv:
activate_this = "%s/pyvirt/bin/activate_this.py" % (basedir,)
execfile(activate_this, dict(__file__=activate_this))

sys.path.insert(0, '%s/src/python' % (basedir,))


import string
import random

import twitter

from tlog.test import test_tlog

consumer_key = '************************'
consumer_secret = '************************'
access_token = '************************'
access_token_secret = '************************'
user = 'asdasdasdasd'

def random_tweet():
    """
    returns 140 character alnum string
    """
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(140))

if __name__ == "__main__":
    #print "basedir:%s" % (basedir,)
    #print "sys.path:%s" % (sys.path,)
    test_tlog()



    #api = twitter.Api()
    api = twitter.Api(consumer_key=consumer_key,
                      consumer_secret=consumer_secret, 
                      access_token_key=access_token, 
                      access_token_secret=access_token_secret) 

    print api.VerifyCredentials() 
    statuses = api.GetUserTimeline(user)
    print [s.text for s in statuses]



    
    status = api.PostUpdate(random_tweet())
    print status.text
