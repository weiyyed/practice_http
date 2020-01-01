import gevent
import gevent.pywsgi
import requests
import unittest
from . import api_server
import multiprocessing

class TestApiServer(unittest.TestCase):
    """
    Test case class that sets up an HTTP server which can be used within the tests
    """
    def setUp(self):
        super(TestApiServer, self).setUp()
        self.server_process=multiprocessing.Process(target=api_server.app.run)
        self.server_process.start()

    def tearDown(self):
        super(TestApiServer, self).tearDown()
        # self._api_server.stop_accepting()
        # self._api_server.stop()
