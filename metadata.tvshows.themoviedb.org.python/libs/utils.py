# -*- coding: UTF-8 -*-
#
# Copyright (C) 2020, Team Kodi
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
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# pylint: disable=missing-docstring

"""Misc utils"""

from __future__ import absolute_import, unicode_literals

import xbmc
from xbmcaddon import Addon

try:
    from typing import Text, Optional, Any, Dict  # pylint: disable=unused-import
except ImportError:
    pass

ADDON_ID = 'metadata.tvshows.themoviedb.org.python'
ADDON = Addon()


class logger:
    log_message_prefix = '[{} ({})]: '.format(ADDON_ID, ADDON.getAddonInfo('version'))

    @staticmethod
    def log(message, level=xbmc.LOGDEBUG):
        # type: (Text, int) -> None
        if isinstance(message, str):
            message = message.decode('utf-8')
            prefix = logger.log_message_prefix
        if isinstance(message, unicode):
            message = message.encode('utf-8')
            prefix = logger.log_message_prefix.encode('utf-8')
        message = prefix + message
        xbmc.log(message, level)

    @staticmethod
    def info(message):
        # type: (Text) -> None
        logger.log(message, xbmc.LOGINFO)

    @staticmethod
    def error(message):
        # type: (Text) -> None
        logger.log(message, xbmc.LOGERROR)

    @staticmethod
    def debug(message):
        # type: (Text) -> None
        logger.log(message, xbmc.LOGDEBUG)


def safe_get(dct, key, default=None):
    # type: (Dict[Text, Any], Text, Any) -> Any
    """
    Get a key from dict

    Returns the respective value or default if key is missing or the value is None.
    """
    if key in dct and dct[key] is not None:
        return dct[key]
    return default

def fix_unicode(thestring):
    if isinstance(thestring, str):
        return thestring.decode('utf-8')
    if isinstance(thestring, unicode):
        return thestring.encode('utf-8')
