# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4 -*-
#
# Copyright (C) 2016 Canonical Ltd
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Author(s): David Planella <david.planella@ubuntu.com>

import os

import snapcraft
from snapcraft.plugins import nodejs
import sysconfig

class ElectronPlugin(nodejs.NodePlugin):

    def __init__(self, name, options, project):
        super().__init__(name, options, project)

    def build(self):
        """Build the source code as retrieved from the pull phase.

        We're simply running the commands required to build atom
        """

        super().build()

        if os.path.exists(os.path.join(self.builddir, 'package.json')):
            self.run(['npm', 'run', 'rebuild'])
