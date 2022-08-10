#title = "This is a test sentence."
with open(r'/home/pi/title.txt', "r") as f:
    result = f.read().splitlines()
    print (result)