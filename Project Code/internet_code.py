import requests  #import library



def check_internet():  #create function
    url = "https://www.youtube.com"       # what ever url we want to check
    timeout = 5 #after 5 seconds it will run
    try:
        _ = requests.get(url, timeout=timeout)  # request send 
        print("all good")
        return True
    except requests.ConnectionError: # except block
        print("please check internet connection")
    return False

check_internet() # function call






#loop_value = 1
#while loop_value:
 #   try:
  #      urlopen("https://google.com")
   # except urllib2.URLError:
    #    f.write("hey network is down!!")
    #else:
    #    print("hey you are on...")
     #   loop_value = 0
     
#print ("test 1")
#loop_value = 1
#while loop_value == 1:
#    print ("test 2")
#    try: urllib.request.urlopen("http://google.com")
#    except urllib.error.URLError as e:
#        print(e.reason)
#        f.write( "Network currently down." )
#        time.sleep(5)
#    else:
#         print( "Up and running." )
    
