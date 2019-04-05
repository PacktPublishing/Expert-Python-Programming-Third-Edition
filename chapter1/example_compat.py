"""This module provides compatibility layer for
selected things that have changed across Python
versions.
"""
import sys

if sys.version_info < (3, 0, 0):
    import urlparse  # noqa


    def is_string(s):
        """Return True if given value is considered string"""
        return isinstance(s, basestring)

else:
    # note: urlparse was moved to urllib.parse in Python 3
    from urllib import parse as urlparse  # noqa


    def is_string(s):
        """Return True if given value is considered string"""
        return isinstance(s, str)