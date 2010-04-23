from setuptools import setup, find_packages

version = '0.2'

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
      [paste.filter_app_factory]
      grater = grate:GrateMiddleware
      """,
      )
