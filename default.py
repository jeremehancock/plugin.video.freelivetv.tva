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

from resources.lib.modules.channels import *

import xbmcplugin

mode = FreeLiveTV().plugin_queries['mode']

if mode is "main":
    tvaddons_branding()
    Channels.section_list()

elif mode == "All Channels":
    Channels.channel_list()

elif mode == "Genres":
    Channels.genres_list()

elif mode in m7lib.Common.get_genres():
    Channels.genre_list(mode)

else:
    Channels.get_channel(mode)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
