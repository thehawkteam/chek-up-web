import urllib.request
import time
x=2#time sleep
response=input("enter Url:")
response = urllib.request.urlopen(response)
time.sleep(x)
print("Facebook: -+-+-+--+-+-+-Haeder Jassem-+-+-+--+-+-+-")
print(response.info())
print(response.info()["content-type"])
