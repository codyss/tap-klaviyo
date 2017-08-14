#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='tap-klaviyo',
      version='0.0.1',
      description='Singer.io tap for extracting data from the GitHub API',
      author='Stitch',
      url='http://singer.io',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['CHANGEME'],
      install_requires=['singer-python==1.7.0',
                        'requests==2.13.0'],
      entry_points='''
          [console_scripts]
          tap-klaviyo=tap_klaviyo:main
      ''',
      packages=['tap_klaviyo'],
      package_data = {
          'tap_klaviyo/schemas': [
                "bounce.json",
                "click.json",
                "mark_as_spam.json",
                "open.json",
                "receive.json",
                "unsubscribe.json",
                "unsub_list.json",
                "subscribe_list.json",
                "update_email_preferences.json",
                "dropped_email.json",
                "lists.json",
                "global_exclusions.json"
              ]
         }
)
