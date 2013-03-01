__author__ = 'uolter'


import OsmApi
import unittest


class MyTestCase(unittest.TestCase):

    def test_node_get_via_proxy(self):

        MyApi = OsmApi.OsmApi(
            api = "http://www.openstreetmap.org",
            proxy_host = 'proxy',
            proxy_port = 8080
        )

        node = MyApi.NodeGet(123)

        self.assertTrue( node['lon'] == 10.7899133)

    def test_no_proxy_fail(self):

        MyApi = OsmApi.OsmApi()

        node = MyApi.NodeGet(123)

        self.assertTrue(True, False)

if __name__ == '__main__':
    unittest.main()
