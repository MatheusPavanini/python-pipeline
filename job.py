import os, sys, time
def job():
    print("Now running")
    print("Now running2")
    print("Now running2")
def main():
    while True:
        job()
        time.sleep(5)
main()