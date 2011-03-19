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

from tlog.test import test_tlog

if __name__ == "__main__":
    #print "basedir:%s" % (basedir,)
    #print "sys.path:%s" % (sys.path,)
    test_tlog()
