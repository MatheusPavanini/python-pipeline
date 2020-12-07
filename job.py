import os, sys, time
def job():
    print("Now running")
    print("Now running2")
    print("Now running3")
    print("Now running4")
    print("Now running5")
def main():
    while True:
        job()
        time.sleep(5)
main()