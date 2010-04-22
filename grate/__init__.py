from paste.request import parse_querystring
import urllib

class GrateMiddleware(object):
    def __init__(self, app, global_conf, mountpoint, content_type='text/html', protocol='http://'):
        self.app = app
        self.mountpoint = mountpoint
        self.content_type = content_type
        self.protocol = protocol
    
    def __call__(self, environ, start_response):
        path_info = environ.get('PATH_INFO')
        
        if path_info.startswith(self.mountpoint):
            # we need to act on the request
            url = path_info.replace(self.mountpoint, '')
            url = urllib.unquote(url)
            if not url.startswith(self.protocol):
                url = self.protocol + url
            qs = parse_querystring(environ)
            f = urllib.urlopen(url + '?' + urllib.urlencode(qs))
            body = f.read()
            f.close()
            start_response('200 OK', [('content-type', self.content_type),
                                      ('content-length', str(len(body)))])
            return [body]
            
        else:
            return self.app(environ, start_response)

