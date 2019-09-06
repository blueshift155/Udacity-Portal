#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/catalog")

from __init__ import app as application

#application.secret_key = 'super_secret_key' 
application.secret_key = '7O32PoSksV2hMd6ZSZTv4zXp'
