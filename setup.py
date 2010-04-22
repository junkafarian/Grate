from setuptools import setup, find_packages

version = '0.0'

setup(name='grate',
      version=version,
      description="WSGI application for proxying http requests through the same domain",
      keywords='wsgi proxy gateway http',
      author='junkafarian',
      url='',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'Paste',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [paste.app_factory]
      grater = grate:make_app
      """,
      )
