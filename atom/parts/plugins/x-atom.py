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
        self._install_binary()

    def _install_binary(self):
        binary_installfile = 'atom.sh'
        command_name = os.path.splitext(binary_installfile)[0]
        binary_installdir = 'bin'
        module_installdir = os.path.join('lib', 'node_modules', 'atom')

        os.symlink(
            os.path.relpath(os.path.join(self.installdir, module_installdir,
                                         binary_installfile),
                            self.installdir),
            os.path.join(self.installdir, binary_installdir, command_name))
