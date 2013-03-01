PythonOsmApi
============

open street map python client with http proxy support 

this is basically a fork of the official Open Street Map python client where I added the possibility to use it going to 
a standard http proxy: very common needed when you are in a corporate network:

```python
MyApi = OsmApi.OsmApi(
            api = "http://www.openstreetmap.org",
            proxy_host = 'myproxy',
            proxy_port = 8080
        )

        node = MyApi.NodeGet(123)

        print node

```



