Munin Multigraph Plugins using PyMunin
=========================================


About
-----

Munin Multigraph Plugins that make use of [_PyMunin_](https://pypi.python.org/pypi/PyMunin).

More detailed documentation for the project and sample graphs for plugins are published on the [PyMunin Project Web Page](https://aouyar.github.com/PyMunin/).

Regular Munin Plugins employ one-plugin one-graph logic and require the execution of a script for data retrieval for each graph. Multigraph plugins permit retrieval of data for multiple graphs in one execution run (one-plugin many-graphs), reducing the processing time and delay for the fetch cycle significantly.
More information on Multigraph Plugins can be found in the
[Munin Guide](https://guide.munin-monitoring.org/en/latest/):

* [Multigraph Plugins](https://munin-monitoring.org/wiki/MultigraphSampleOutput)
* [Multigraph Plugin Protocol](https://munin-monitoring.org/wiki/protocol-multigraph)

The plugins consist of the following components:

* The plugin logic is implemented in the plugin scripts in _pymunin.plugins_.
* The actual data retrieval logic is separated from the plugins to facilitate code reuse. Individual modules in _pymunin.sysinfo_ implement classes for getting the monitoring data and returning them in dictionary objects. The separation of the data retrieval logic should facilitate the use of the same code in other monitoring solutions.

Although the solution is focused on implementing _multigraph_ plugins the module also supports simple _single_ graph plugins.

For information on other projects you can check my [GitHub Personal Page](https://aouyar.github.io) and [GitHub Profile](https://github.com/aouyar).


Munin Plugins
-------------

Multigraph Munin Plugins for the following applications are included:

* Apache Tomcat
* Apache Web Server
* Asterisk Telephony Server
* Disk Usage
* Disk I/O
* FreeSWITCH Soft Switch
* Lighttpd Web Server
* Memcached
* MySQL Database
* Network Interface Traffic and Errors
* Network Connection Stats (netstat)
* Nginx Web Server
* NTP - Time Server
* PHP APC - PHP Cache
* PHP FPM (FastCGI Process Manager)
* PostgreSQL Database
* Processes and Threads
* Rackspace Cloud
* Redis Server
* System Resources
  (Load, CPU, Memory, Processes, Interrupts, Paging, Swapping, etc.)
* Sangoma Wanpipe Telephony Interfaces
* Varnish Cache Web Application Accelerator


Classes for retrieving stats are available, but no plugins have been developed yet for:

* Squid Web Proxy


Licensing
---------

_PyMuninPlugins_ is free software made available under the terms of the _GPL License Version 3_. See the _COPYING_ file that accompanies the code for full licensing information.


Download
--------

New versions of the code are published in [PyPI - the Python Package Index](https://pypi.python.org/pypi/PyMuninPlugins) periodically.

You can download the latest development version from [GitHub](https://github.com/aouyar/PyMuninPlugins) either
in [ZIP](https://github.com/aouyar/PyMuninPlugins/zipball/master)
or [TAR](https://github.com/aouyar/PyMuninPlugins/tarball/master)
format.

You can also get the latest development version of the code by cloning the [Git](http://git-scm.com) repository for the project by running:

    git clone git://github.com/aouyar/PyMuninPlugins


Installation
------------

The easiest way to install the code is to use [pip](https://www.pip-installer.org/).

Install the newest version from [PyPI](https://pypi.python.org/pypi/PyMuninPlugins):

    pip install PyMuninPlugins

Install the latest development version:

    pip install git+https://github.com/aouyar/PyMuninPlugins.git#egg=PyMuninPlugins

The other option is to download and uncompress the code manually and execute the included _setup.py_ script for installation:

    ./setup.py install


Collaboration
-------------

I would be happy to receive suggestions on improving the code for developing Munin Plugins. Alternatively you can use the _Issues_ functionality of _GitHub_ to document problems and to propose improvements. You can use the internal messaging system of _GitHub_ or my e-mail address in case you prefer to
contact me directly.

I hope that by sharing the code, the existing plugins will get more testing and receive improvements, and many more Multigraph plugins will be developed collaboratively.

I would be glad to receive some sample graphs from anyone using the plugins.


Credits
-------

_PyMuninPlugins_ has been developed by [aouyar](https://github.com/aouyar) (Ali Onur Uyar).

Changes for Python 3 and re-packaging as a namespace module separated from _PyMunin_ by [penguinpee](https://github.com/penguinpee) (Sandro).

Some of the people that have knowingly or unknowingly contributed with the development are:

* Initial packaging of the code was done by Mark Lavin ([mlavin](https://github.com/mlavin)). PyMuninPlugins is installable using pip / easy_install thanks to Mark. :-)
* The Rackspace Cloud plugin was initially developed by [Brian Welsh](https://github.com/palewire).
* [Sebastian Rojo](https://github.com/arpagon) has contributed many improvements to the Asterisk Plugin.
* [Preston Mason](https://github.com/pentie) has made significant contributions to the Varnish Cache and PHP APC Cache Plugins.
* Many plugins were inspired by existing _Munin Plugins_developed by other people. (Before developing any plugins, I always try to check existing solutions.)
* Many people have contributed by testing the plugins and identifying issues.

_I hope that more people will be using PyMunin for developing plugins in the future._
