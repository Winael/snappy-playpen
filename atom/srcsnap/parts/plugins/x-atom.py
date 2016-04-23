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

class AtomPlugin(nodejs.NodePlugin):

    def __init__(self, name, options, project):
        super().__init__(name, options, project)

    def build(self):
        """Build the source code as retrieved from the pull phase.

        We're simply running the commands required to build atom
        """

        super().build()

        scriptdir = os.path.join(self.builddir, 'script')
        buildscript = 'build'
        gruntscript = 'grunt'

        build_command = [os.path.join(scriptdir, buildscript),
                        '--build-dir', self.builddir]

        install_command = [os.path.join(scriptdir, gruntscript),
                        '--build-dir', self.builddir,
                        '--install-dir', self.installdir]

        self.run(build_command)
        self.run(install_command)

        # binary_file = 'atom.sh'
        # binary_dir = 'bin'
        #
        # os.makedirs(os.path.join(self.installdir, binary_dir))
        #
        # os.link(
        #     os.path.join(os.path.dirname(self.builddir), binary_dir,
        #                                  binary_file),
        #     os.path.join(self.installdir, binary_dir, binary_file))


        # binary_file = 'Notes'
        # binary_dir = 'bin'
        #
        # os.makedirs(os.path.join(self.installdir, binary_dir))
        #
        # os.link(
        #     os.path.join(os.path.dirname(self.builddir), binary_dir,
        #                                  binary_file),
        #     os.path.join(self.installdir, binary_dir, binary_file))
