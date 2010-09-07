from geoportal import utils, admin, templatetags, forms

VERSION = (0, 4, 3)


def get_version():
    version = '%s.%s' % (VERSION[0], VERSION[1])
    if len(VERSION) > 2:
        version = '%s.%s' % (version, VERSION[2])
    return version

__all__ = ['utils', 'admin', 'templatetags', 'forms']
