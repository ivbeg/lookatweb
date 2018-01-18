import re
import io
from setuptools import setup, find_packages

open_as_utf = lambda x: io.open(x, encoding='utf-8')

(__version__, ) = re.findall("__version__.*\s*=\s*[']([^']+)[']",
                             open('lookatweb/__init__.py').read())

readme = re.sub(r':members:.+|..\sautomodule::.+|:class:|:func:', '', open_as_utf('README.rst').read())
readme = re.sub(r'`Settings`_', '`Settings`', readme)
readme = re.sub(r'`Contributing`_', '`Contributing`', readme)
history = re.sub(r':mod:|:class:|:func:', '', open_as_utf('HISTORY.rst').read())



setup(
    name='lookatweb',
    version=__version__,
    description="Web technology identification",
    long_description=readme + '\n\n' + history,
    author='Ivan Begtin',
    author_email='ivan@begtin.tech',
    url='https://github.com/ivbeg/lookatweb',
    packages=find_packages(exclude=('tests', 'tests.*')),
    include_package_data=True,
    install_requires=[
        'lxml',
        'click'
    ],
    scripts=['bin/weblooker.py'],
    license="BSD",
    zip_safe=False,
    keywords='scraping htmlpatterns',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ]
)
