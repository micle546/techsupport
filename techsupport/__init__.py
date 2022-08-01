"""
The flask application package.
"""

from mongita import MongitaClientDisk

from flask import Flask
app = Flask(__name__)
app.secret_key = b'\xf7\xd1\xd6\x80\xc6Vl\xd3\x0bs5\xf2*a3\x03'

#database
client = MongitaClientDisk(host="./.mongita")
db = client.db
users = db.users

from . import views
#import techsupport.views
