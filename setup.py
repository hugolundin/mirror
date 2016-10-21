from distutils.core import setup

setup(
  name='mirror',
  version='0.1dev',
  packages=['mirror'],
  entry_points={
  'console_scripts': ['mirror = mirror.main:main'],
  },
  install_requires=['click', 'watchdog'],
  license='Creative Commons Attribution-Noncommercial-Share Alike license',
  long_description=open('README.md').read()
)

