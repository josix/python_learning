# In python2, the modules of server and client are scattered.
# In python3, it conculde these modules in two packages
# http is used to deal with managing all HTTP details of client and server
#   client  ->      for client's work
#   server  ->      help you write the python web server
#   cookies and cookjar  ->     help you manage cookiem use it for storing data when you visit the same page several times

# urllib will be executed on the http 
#   request  ->     for dealing with request of the client-end
#   response ->     for dealing with response of the server-end
#   parse   ->      for dismantling URL's every part

import urllib.request as ur
url = "http://bit.ly/httpresponse-docs"
conn = ur.urlopen(url) # conn is a HTTPResponse object
# this will open a TCP/IP connection ->  make a HTTP request -> take a HTTP response( HTML format) 
print(conn)

# this object has lots of method like read() to provide the data of page
data = conn.read()
print(data) 

# the HTTP status code:
#   1xx(information)  server recieve a request, but there is other information shoud be deliver to client-end
#   2xx(success)    it succeed, other status code will deliver information to client except 200
#   3xx(redirection)    the source is moved, so the response will return a new URL to client
#   4xx(client error)   there are some error at client-end, like 404(not found)
#   5xx(server error)   500 is general code 
print(conn.status)

print(conn.getheader('Content-Type')) # get the content type of the header (the data format is usually assigned by the content-type of header in HTTP response)
# other thing that HTTP header will deliver
print()
for key, value in conn.getheaders():
    print(key, value)
