#!/usr/bin/env python
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import os
import pip

cmd_update = "sudo apt-get update"
cmd_upgrade = "sudo apt-get upgrade"

print('Collecting updated PPA information...')
os.system(cmd_update)

print('Upgrading flagged software...')
os.system(cmd_upgrade)

dists = []
for dist in pip.get_installed_distributions():
    dists.append(dist.project_name)

dists = sorted(dists, key=lambda s: s.lower())
dists.insert(0, 'pip')  # let 'pip' be the first

for dist_name in dists:
    cmd = "sudo pip3 install -U {0}".format(dist_name)
    print('#', cmd)
    os.system(cmd)
