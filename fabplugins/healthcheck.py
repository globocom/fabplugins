#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import with_statement
import sys
import time

from fabric.api import run, settings


def do_healthcheck(host, uri='healthcheck', body='WORKING'):
    sleeping_time = 1

    with settings(warn_only=True):
        print 'Waiting for server (%s)' % host
        while not run('curl -L %s/%s' % (host, uri)) == body:
            print '. (sleeping %d)' % sleeping_time
            time.sleep(sleeping_time)
            sleeping_time = sleeping_time * 2
            if sleeping_time >= 64:
                print 'Timeout trying to healthcheck'
                sys.exit(-1)
        return True
