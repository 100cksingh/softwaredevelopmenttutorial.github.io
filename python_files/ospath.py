# problem not working 
import os
from os import path
import datetime
from datetime import date,time,timedelta
import time
from traceback import print_tb

def main():
    print(os.name)

    # print("Item exists:"+str(path.exists("textfile.txt")))
    # print("Item is a file:"+str(path.isfile("textfile.txt")))
    # print("Item is a directory:"+str(path.isdir("textfile.txt")))


    # print("Item is path:"+str(path.realpath("textfile.txt")))
    # print("Item path and name:"+str(path.split(path.realpath("textfile.txt"))))
    
    # t=time.ctime(path.getatime("textfile.txt"))
    # print(t)
    # print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))

    td=datetime.datetime.now()-datetime.datetime.fromtimestamp(
        path.getmtime("textfile.txt")
    )
    print("It has been "+str(td)+"since the file was modified")
    print("Or,"+str(td.total_seconds())+" seconds")

    if __name__=="__main__":
        main()