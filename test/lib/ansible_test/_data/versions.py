#!/usr/bin/env python
"""Show python and pip versions."""
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import os
import sys

try:
    import pip
except ImportError:
    pip = None

print(sys.version)

if pip:
    print('pip %s from %s' % (pip.__version__, os.path.dirname(pip.__file__)))
