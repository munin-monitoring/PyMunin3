---
title: Proposal for releasing a Python 3 compatible version of PyMunin
author: Sandro (@penguinpee)
email: devel@penguinpee.nl
date: 2022-06-10
version: 0.1
---

# Proposal for releasing a Python 3 compatible version of PyMunin

Python 2 has been replaced by Python 3. After an extended transition period, support for Python 2 has finally stopped. The final version of Python 2, 2.7.18, was released in April 2020.

Munin Monitoring no longer accepts plugins written in Python 2[^1]. Transitioning PyMunin to Python 3 is therefore mandatory to allow plugin developers to write plugins in Python using the PyMunin framework.

## Dropping Python 2 support

I propose to drop Python 2 support from PyMunin entirely. In my opinion the effort needed for a dual stack approach is wasted. For legacy plugins, the current release of PyMunin will remain available in PyPI. Plugins that still require it can define a specific version dependency.

## Separating PyMunin from the plugins

Currently PyMunin is released together with a number of plugins. These plugins showcase the usefulness of the framework and can also serve as reference or starting point for plugin development.

However, these plugins come with their own dependencies, which are only necessary for the plugin in question. For PyMunin to be accepted as a framework for writing Munin plugins, it should be possible to install just PyMunin, without any extras. That keeps the number of dependencies for the framework, and thus plugins using it, small.

It will also mean less effort for package maintainers including PyMunin as they would object to including Munin plugins from a variety of sources.

### Future development of PyMunin plugins

I propose to move the plugins to a separate package, say `PyMuninPlugins`.

I haven't taken a close look at all plugins, yet, and what graphs they produce. Keeping the plugins in the current release and re-releasing them on their own, would also be an option, I suppose.

I think it's worth the effort to compare the existing plugins to whats on offer in Munin core (master[^2] and stable[^3]) and contrib [^4]. The plugins now in PyMunin may be a good addition, replacement or merge candidate for plugins published there. It appears that quite a number of plugins in the contrib repository are not being looked after.

At the same time the plugins get the exposure they deserve and, by entailment, so does the PyMunin module.

## Housekeeping
It's a bit off-topic, but I wanted it to be mentioned at least.

The information available on GitHub[^5], PyPI[^6] and the Project Site[^7] need some looking after. Some of the links are broken due to Munin Monitoring having a new home as well as GitHub's move to the `github.io` domain for user pages.

---

**Ali Onur Uyar (@aouyar)**: *''I hope that more people will be using PyMunin for developing plugins in the future.''*

Let's make it happen!

---

[^1]: http://guide.munin-monitoring.org/en/latest/develop/plugins/advanced-topics.html?highlight=python#python-plugins
[^2]: https://github.com/munin-monitoring/munin/tree/master/plugins
[^3]: https://github.com/munin-monitoring/munin/tree/stable-2.0/plugins
[^4]: https://github.com/munin-monitoring/contrib/tree/master/plugins
[^5]: https://github.com/aouyar/PyMunin
[^6]: https://pypi.org/project/PyMunin/
[^7]: https://aouyar.github.io/PyMunin/
