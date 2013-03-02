PythonOsmApi
============

open street map python client with http proxy support 

this is basically a fork of the official Open Street Map python client where I added the possibility to use it going 
through a standard http proxy
This could be a very common needed when you are in a corporate network.

The official documentation and source code is available at this url: http://wiki.openstreetmap.org/wiki/PythonOsmApi

When you want to set the http proxy just set host (or ip)  and port in the object constructor like in the example below: 

```python
MyApi = OsmApi.OsmApi(
            api = "http://www.openstreetmap.org",
            proxy_host = 'myproxy',
            proxy_port = 8080
        )

        node = MyApi.NodeGet(123)

        print node

```

This software is available under the Open Database License and this is the [copyright page](http://www.openstreetmap.org/copyright)
