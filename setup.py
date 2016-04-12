import os
from setuptools import setup


def pkg_dir(path):
    return os.path.join(os.path.dirname(__file__), path)


with open(pkg_dir('VERSION'), 'r') as f:
    version = f.read().strip()


with open(pkg_dir('README.md'), 'r') as f:
    readme = f.read()


setup(
    name='elasticsearch-collectd-plugin',
    version=version,
    install_requires=[],
    py_modules=['elasticsearch-collectd'],
    author='',
    author_email='platforms@digital.justice.gov.uk',
    maintainer='MOJDS',
    url='https://github.com/ministryofjustice/elasticsearch-collectd-plugin',
    description='Collectd plugin to query stats from elasticsearch',
    long_description=readme,
    license='LICENSE',
    keywords=['python', 'ministryofjustice', 'collectd', 'elasticsearch'],
    test_suite='tests',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 1 - Alpha',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Monitoring',
        'Topic :: System :: Networking :: Monitoring',
        'Topic :: System :: Networking :: Time Synchronization']
)

