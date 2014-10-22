#-------------------------------------------------------------------------------
# Copyright (c) 2012 Gael Honorez.
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the GNU Public License v3.0
# which accompanies this distribution, and is available at
# http://www.gnu.org/licenses/gpl.html
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#-------------------------------------------------------------------------------





# Initialize logging system
import logging
import util

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtNetwork import *

logger = logging.getLogger(__name__)
#logger.setLevel(logging.DEBUG)


# Initialize all important globals
LOBBY_HOST = 'faforever.tk'
LOBBY_PORT = 8001
LOCAL_REPLAY_PORT = 15000
GAME_PORT_DEFAULT = 6112

#Port on server for udp test
GAME_TEST_PORT = 8002

# Service URLs
AUTH_SERVICE_URL = "http://faforever.tk:44343/auth"
GAMES_SERVICE_URL = "http://faforever.tk:8080/games"

# Important URLs
MUMBLE_URL = "mumble://{login}@faforever.com/Games?version=1.2.0" 
FORUMS_URL = "http://faforever.com/forums"
WEBSITE_URL = "http://www.faforever.com"
UNITDB_URL = "http://www.faforever.com/faf/unitsDB/"
WIKI_URL = "http://www.faforever.com/mediawiki/index.php/Main_Page"
SUPPORT_URL = "http://www.faforever.com/forums/viewforum.php?f=3"
TICKET_URL = "https://gitreports.com/issue/FAForever/lobby"
STEAMLINK_URL = "http://www.faforever.com/faf/steam.php"
PASSWORD_RECOVERY_URL = "http://www.faforever.com/faf/forgotPass.php"
NAME_CHANGE_URL = "http://www.faforever.com/faf/userName.php"


networkAccessManager = QNetworkAccessManager()

class Banana(QObject):
    def __init__(self):
        super(Banana, self).__init__()

    def onSSLError(self, reply, errors):

        ret = QMessageBox.warning( 'SSL Error', errors[0].errorString(), QMessageBox.Ignore, QMessageBox.Cancel)

        if ret == QMessageBox.Ignore:
            reply.ignoreSslErrors()

banana = Banana()
networkAccessManager.sslErrors.connect(banana.onSSLError)

class ClientState:
    '''
    Various states the client can be in.
    '''
    SHUTDOWN  = -666  #Going... DOWN!
    DROPPED   = -2 # Connection lost
    REJECTED  = -1
    NONE      = 0
    ACCEPTED  = 1
    CREATED   = 2
    OUTDATED  = 9000
    UPTODATE  = 9001 #It's over nine thousaaand!



from ._clientwindow import ClientWindow as Client

instance = Client()
