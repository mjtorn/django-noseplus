# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from setuptools import setup, find_packages

NAME = 'django-noseplus'
VERSION = '0.0.1'

DESCR = """\
Mixin classes for pep8 test cases and to add more methods
"""

AUTHOR = u'Markus Törnqvist'
AUTHOR_EMAIL = 'mjt@fadconsulting.com'

URL = 'https://github.com/mjtorn/django-noseplus'

setup(
    name=NAME,
    version=VERSION,
    description=DESCR,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools'],
)

# EOF

