import os, sys, time
def job():
    print("Now running")

def main():
    while True:
        job()
        time.sleep(5)
main()