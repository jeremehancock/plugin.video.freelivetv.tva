"""
    Free Live TV Add-on
    Developed by mhancoc7

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

try:
    # Python 3
    from resources.lib.modules.common import *
except ImportError:
    # Python 2
    from common import *

import m7lib

class Channels:

    @staticmethod
    def section_list():
        try:
            #Generate Section List
            for section in sorted(m7lib.Common.get_sections()):
                m7lib.Common.add_section(section, m7lib.Common.get_logo(section, "section"), fanart)
        except StandardError:
            dlg_oops(addon_name)

    @staticmethod
    def genres_list():
        try:
            # Generate Genre List
            for genre in sorted(m7lib.Common.get_genres()):
                m7lib.Common.add_section(genre, m7lib.Common.get_logo(genre, "genre"), fanart)
        except StandardError:
            dlg_oops(addon_name)

    @staticmethod
    def genre_list(genre):
        try:
            # Generate Channel List within given genre
            for channel in m7lib.Common.get_channels():
                if genre in channel["genre"]:
                    m7lib.Common.add_channel(channel["slug"], channel["endpoints"]["poster"], fanart, channel["name"], True)
        except StandardError:
            dlg_oops(addon_name)

    @staticmethod
    def channel_list():
        try:
            # Generate Channel List
            for channel in m7lib.Common.get_channels():
                m7lib.Common.add_channel(channel["slug"], channel["endpoints"]["poster"], fanart, channel["name"], True)
        except StandardError:
            dlg_oops(addon_name)

    @staticmethod
    def get_channel(mode):
        try:
            m7lib.Common.get_stream_and_play(mode)
        except StandardError:
            dlg_oops(addon_name)

