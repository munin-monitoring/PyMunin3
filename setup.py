#!/usr/bin/python3

# import errno
import os
# import pkgutil
# import shutil
# import glob
from setuptools import setup, find_packages
from setuptools import Command
import pkgutil


PYMUNIN_SCRIPT_FILENAME_PREFIX = 'pymuninplugins'
MUNIN_PLUGIN_DIR = './share/munin/plugins'


class InstallPlugins(Command):

    description = "Install Munin plugins"
    user_options = [
                    ('path=', None, 'full path for plugin installation')
                    ]

    def initialize_options(self):
        self.path = None

    def finalize_options(self):
        if self.path:
            assert os.path.isdir(self.path), (
                'Path (%s) does not exist or is not a directory.' % self.path)

    def run(self):
        if self.path:
            munin_plugin_dir = self.path
        elif 'MUNIN_PLUGIN_DIR' in os.environ:
            munin_plugin_dir = os.environ.get('MUNIN_PLUGIN_DIR')
        elif self.root is None:
            munin_plugin_dir = os.path.normpath(
                os.path.join(
                    self.prefix,MUNIN_PLUGIN_DIR))
        else:
            munin_plugin_dir = os.path.normpath(
                os.path.join(self.root,os.path.relpath(self.prefix, '/')
                             ,MUNIN_PLUGIN_DIR))

        pkgutil.get_loader(pymunin.plugins)
        modules = [modname for importer, modname, ispkg in
                   pkgutil.iter_modules(pymunin.plugins.__path__)]
        print(module for module in modules)

        console_scripts = []
        plugin_names = []
        for modname in modules:
            params = {
                'script_name': '%s-%s' % (PYMUNIN_SCRIPT_FILENAME_PREFIX, modname),
                'script_path': '%s.%s' % (pymuninplugins.__name__,  modname),
                'entry': 'main',
            }
            plugin_names.append(modname)
            console_scripts.append('%(script_name)s = %(script_path)s:%(entry)s' % params)
        print(script for script in console_scripts)

        # Installing the plugins requires write permission to plugins directory
        # (/usr/share/munin/plugins) which is default owned by root.
        print("Munin Plugin Directory: %s" % munin_plugin_dir)
        if os.path.exists(munin_plugin_dir):
            try:
                for name in plugin_names:
                    source = os.path.join(
                        self.install_scripts,
                        '%s-%s' % (PYMUNIN_SCRIPT_FILENAME_PREFIX, name)
                    )
                    destination = os.path.join(munin_plugin_dir, name)
                    print("Installing %s to %s." % (name, munin_plugin_dir))
                    shutil.copy(source, destination)
            except IOError as e:
                if e.errno in  (errno.EACCES, errno.ENOENT):
                    # Access denied or file/directory not found.
                    print("*" * 78)
                    if e.errno == errno.EACCES:
                        print(("You do not have permission to install the plugins to %s."
                               % munin_plugin_dir))
                    if e.errno == errno.ENOENT:
                        print(("Failed installing the plugins to %s. "
                               "File or directory not found." % munin_plugin_dir))
                    # script = os.path.join(self.install_scripts, 'pymunin-install')
                    # f = open(script, 'w')
                    # try:
                    #     f.write('#!/bin/sh\n')
                    #     for name in plugin_names:
                    #         source = os.path.join(
                    #             self.install_scripts,
                    #             '%s-%s' % (PYMUNIN_SCRIPT_FILENAME_PREFIX, name)
                    #         )
                    #         destination = os.path.join(munin_plugin_dir, name)
                    #         f.write('cp %s %s\n' % (source, destination))
                    # finally:
                    #     f.close()
                    # os.chmod(script, 0o755)
                    print(("You will need to copy manually using the script: %s\n"
                           "Example: sudo %s"
                           % (script, script)))
                    print("*" * 78)
                else:
                    # Raise original exception
                    raise


setup(
    cmdclass={'install_plugins': InstallPlugins},
)
