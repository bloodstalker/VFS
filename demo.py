#!/bin/python3
import ipfsapi

# the files are being stored on an rpi
file_list = ["QmcqWasAwrfnpGauWRakXyXYaMMss7puvPBR2LE7ZNcVR8",
             "Qmd2zCMyKZVLpbbvUUhcqChCCf8AqhUnRwtp8pQ35ZXiHH",
             "Qmdya7CCAg4t2hxvrW9qE8Afo3HBvfEPy1WDbaukdHvsPU", ]

def main():
    client = ipfsapi.connect('127.0.0.1', 5001)
    file0 = str()
    file1 = str()
    file2 = str()
    print("getting file 0:")
    print("hash: " + file_list[0])
    file0 = client.get(file_list[0])
    print(file0)
    print("getting file 1:")
    print("hash: " + file_list[1])
    file1 = client.get(file_list[1])
    print(file1)
    print("getting file 2:")
    print("hash: " + file_list[2])
    file2 = client.get(file_list[2])
    print(file2)

if __name__ == "__main__":
    main()
