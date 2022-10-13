import time

symbol = ["-", "/", "|", "\\"]

def spinning_cursor():
    while True:
        for cursor in symbol:
            print("\r"+("Processing..."+cursor), end="")
            time.sleep(0.2)

spinning_cursor()