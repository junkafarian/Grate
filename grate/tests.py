import unittest

class TestTopLevelFuncs(unittest.TestCase):
    def test_make_grater(self):
        from grate import GrateMiddleware
        app = object()
        grate = GrateMiddleware(app, None,
                                mountpoint='/foo/',
                                content_type='application/rss+xml',
                                protocol='https://')
        self.assertEqual(grate.app, app)
        self.assertEqual(grate.mountpoint, '/foo/')
        self.assertEqual(grate.content_type, 'application/rss+xml')
        self.assertEqual(grate.protocol, 'https://')

class TestErrorLogging(unittest.TestCase):
    
    def _makeOne(self, *arg, **kw):
        from grate import GrateMiddleware
        return GrateMiddleware(*arg, **kw)
    
    def test_call_app(self):
        app = DummyApplication()
        instance = self._makeOne(app, None, mountpoint='/foo/')
        env = {'PATH_INFO':'/somewhere/else', 'wsgi.url_scheme':'http',
               'SERVER_NAME':'localhost', 'SERVER_PORT':'8080'}
        self.assertEqual(instance(env, None), app(env, None))
    
    def test_call_grate(self):
        app = DummyApplication()
        instance = self._makeOne(app, None, mountpoint='/foo/')
        env = {'PATH_INFO':'/foo/www.google.com', 'wsgi.url_scheme':'http',
               'SERVER_NAME':'localhost', 'SERVER_PORT':'8080'}
        def start_response(code, headers):
            pass
        
        res = instance(env, start_response)
        s = ''.join(res)
        self.assertNotEqual(res, app(env, None))
        self.assert_('google' in s)
        

class DummyApplication:
    def __call__(self, environ, start_response):
        self.environ = environ
        self.start_response = start_response
        return ['hello world']
