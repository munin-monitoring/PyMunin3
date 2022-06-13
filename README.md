PyMunin - Python Multigraph Munin Plugins
=========================================


About
-----

Python Module for developing Munin Multigraph Monitoring Plugins.

More detailed documentation for the project and sample graphs for plugins are
published in the [PyMunin Project Web Page](http://aouyar.github.io/PyMunin/).

Regular Munin Plugins employ one-plugin one-graph logic and require the
execution of a script for data retrieval for each graph.
Multigraph plugins permit retrieval of data for multiple graphs in one execution
run (one-plugin many-graphs), reducing the processing time and delay for the
fetch cycle significantly.
More information on Multigraph Plugins can be found in the
[Munin Guide](https://guide.munin-monitoring.org/en/latest/index.html):

* [Multigraph Plugins](http://guide.munin-monitoring.org/en/latest/plugin/multigraphing.html)
* [Multigraph Protocol Extension](http://guide.munin-monitoring.org/en/latest/plugin/protocol-multigraph.html)

The plugins consist of the following components:

* The _pymunin_ module _(./pymunin)_ implements the base classes for
  developing Munin plugins.
* The plugin logic is implemented in the plugin scripts in _./pymunin/plugins_.
* The actual data retrieval logic is separated from the plugins to facilitate
  code reuse. Individual modules in the directory _./pysysinfo_ implement classes
  for getting the monitoring data and returning them in dictionary objects.
  The separation of the data retrieval logic should facilitate the use of the
  same code in other monitoring solutions.

Although the solution is focused on implementing _Multigraph Plugins_ the module
also supports simple single graph plugins.

For information on other projects you can check
my [GitHub Personal Page](http://aouyar.github.io)
and [GitHub Profile](https://github.com/aouyar).


Licensing
---------

_PyMunin_ is copyrighted free software made available under the terms of the
_GPL License Version 3_ or later.

See the _COPYING_ file that accompanies the code for full licensing information.


Download
--------

New versions of the code are be published for download
at [PyPI - the Python Package Index](http://pypi.python.org/pypi/PyMunin)
periodically.

You can download the latest development version of this code that is hosted
at [GitHub](https://github.com/aouyar/PyMunin) either
in [ZIP](https://github.com/aouyar/PyMunin/zipball/master)
or [TAR](https://github.com/aouyar/PyMunin/tarball/master)
format.

You can also get the latest development version of the code by cloning
the [Git](http://git-scm.com) repository for the project by running:

    git clone git://github.com/aouyar/PyMunin


Installation
------------

The easiest way to install the code is to use [pip](https://pip.pypa.io/en/stable/).

Install the newest version from [PyPI](http://pypi.python.org/pypi/PyMunin):

    pip install PyMunin

Install the latest development version:

    pip install git+https://github.com/aouyar/PyMunin.git#egg=PyMunin

The other option is to download and uncompress the code manually and execute the
included _setup.py_ script for installation:

    ./setup.py install


Collaboration
-------------

I would be happy to receive suggestions on improving the code for developing
Munin Plugins. Alternatively you can use the _Issues_ functionality of _GitHub_
to document problems and to propose improvements. You can use the internal
messaging system of _GitHub_ or my e-mail address in case you prefer to
contact me directly.

I hope that by sharing the code, the existing plugins will get more testing and
receive improvements, and many more Multigraph plugins will be developed
collaboratively.

I would be glad to receive some sample graphs from anyone using the plugins.


Credits
-------

_PyMunin_ has been developed
by [aouyar](https://github.com/aouyar) (Ali Onur Uyar).

Some of the people that have knowingly or unknowingly contributed with the
development are:

* Initial packaging of the code was done by Mark Lavin
([mlavin](https://github.com/mlavin)).
PyMunin is installable pip / easy_install thanks to Mark. :-)
* _PyMunin_ has been packaged for _Fedora_ and _Red Hat Enterprise Linux_ by
  [Matthias Runge](http://www.matthias-runge.de).
* The initial design of the solution was inspired by
[python-munin](https://github.com/samuel/python-munin)
by [Samuel Stauffer](https://github.com/samuel).
* The Rackspace Cloud plugin was initially developed
  by [Ben Welsh](https://github.com/palewire).
* [Sebastian Rojo](https://github.com/arpagon) has contributed
many improvements to the Asterisk Plugin.
* [Preston Mason](https://github.com/pentie) has made significant contributions to
the Varnish Cache and PHP APC Cache Plugins.
* Many plugins were inspired by existing _Munin Plugins_developed by other
  people. (Before developing any plugins, I always try to check existing
  solutions.)
* Many people have contributed by testing the plugins and identifying issues.

_I hope that more people will be using PyMunin for developing plugins in the
future._
