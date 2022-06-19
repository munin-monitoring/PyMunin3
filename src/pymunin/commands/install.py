#!/usr/bin/python3

import os, sys, shutil
import argparse
import pkgutil
import errno
# import glob
from setuptools import setup, find_packages, Command
from setuptools.command.install import install
import pymunin.plugins


INSTALL_PREFIX = '/usr'
MUNIN_PLUGIN_DIR = './share/munin/plugins'


def InstallPlugins():

    munin_plugin_dir = os.path.normpath(
        os.path.join(INSTALL_PREFIX, MUNIN_PLUGIN_DIR)
        )

    parser = argparse.ArgumentParser(
        description='Install Munin plugins from PyMuninPLugins. '
        'By default plugins will be installed in %s. '
        'Use the options below to adjust or set MUNIN_PLUGIN_DIR in your environment.'
        % munin_plugin_dir)

    parser.add_argument('--prefix', type=str,
                        help='prefix for plugin installation')
    parser.add_argument('--path', type=str,
                        help='full path for plugin installation')
    parser.add_argument('--dry-run', dest='dryrun', action='store_true',
                        help='show what would be done')

    args = parser.parse_args()

    if 'MUNIN_PLUGIN_DIR' in os.environ:
        munin_plugin_dir = os.environ.get('MUNIN_PLUGIN_DIR')
    elif args.path:
        munin_plugin_dir = args.path
    elif args.prefix:
        munin_plugin_dir = os.path.normpath(
            os.path.join(args.prefix, MUNIN_PLUGIN_DIR))

    modules = [modname for importer, modname, ispkg in
               pkgutil.iter_modules(pymunin.plugins.__path__)]

    plugins = []
    for module in modules:
        plugins.append(module)

    # Installing the plugins requires write permission to plugins directory
    # (/usr/share/munin/plugins) which is default owned by root.
    print("Munin plugin directory: %s" % munin_plugin_dir)
    if not os.path.exists(munin_plugin_dir):
        try:
            print("Directory does not exist, creating it")
            if not args.dryrun:
                old_umask = os.umask(0o022)
                os.makedirs(munin_plugin_dir, 0o755)
                os.umask(old_umask)
        except Exception as err:
            print("Unable to create directory: '%s' (%s)." % (munin_plugin_dir, err))
            return(1)
    try:
        for plugin in plugins:
            source = os.path.join(pymunin.plugins.__path__[0], plugin + '.py')
            destination = os.path.join(munin_plugin_dir, plugin)
            print("Installing %s in %s." % (plugin, munin_plugin_dir))
            if not args.dryrun:
                shutil.copy(source, destination)
                os.chmod(destination, 0o755)
    except IOError as e:
        if e.errno in  (errno.EACCES, errno.ENOENT):
            # Access denied or file/directory not found.
            if e.errno == errno.EACCES:
                print("You do not have permission to install the plugins to %s."
                       % munin_plugin_dir)
            if e.errno == errno.ENOENT:
                print("Failed installing the plugins to %s. "
                       "File or directory not found." % munin_plugin_dir)
            print()
            print("*" * 78)
            print("Use '--path' to specify an alternative location for plugin "
                  "installation")
            print("or run the command as root.")
            print()
            print("Use '%s --help' for more information."
                  % os.path.basename(sys.argv[0]))
            print("*" * 78)
            return(1)
        else:
            # Raise original exception
            raise
            return(1)

if __name__ == '__main__':
    sys.exit(InstallPlugins())
