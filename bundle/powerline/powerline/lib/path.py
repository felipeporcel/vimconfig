# vim:fileencoding=utf-8:noet
from __future__ import (unicode_literals, division, absolute_import, print_function)

import os


def realpath(path):
	return os.path.abspath(os.path.realpath(path))
