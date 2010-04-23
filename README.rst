Grate
=====

``Grate`` is a simple WSGI filter application, allowing cross domain
requests to be made from any application further down the pipeline.

Configuration
-------------

It can be configured through ``PasteDeploy`` with the following
options::
    
    [filter:grate]
    use = egg:grate#grater
    mountpoint = /grate/
    
    # Optional attributes
    content_type = text/html
    protocol = http://
    
    [pipeline:main]
    pipeline =
             ...
             grate
             ...

Usage
-----

You can then make requests to remote sites after the mountpoint::
    
    http://mywsgiapp.com/grate/www.google.com => http://google.com
    http://mywsgiapp.com/grate/www.google.com?foo=bar => http://google.com/?foo=bar
    http://mywsgiapp.com/www.google.com => Passed down the pipeline
