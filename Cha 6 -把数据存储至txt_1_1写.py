title = '\t'.join(['name','title','age','gender'])
with open('/home/pi/test.txt', "a+") as f:
    f.write(title)
    f.close()