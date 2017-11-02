#!/bin/python3
import ipfsapi

# the files/dirs that we will download
# im hosting these on my rpi, so if the sever is down lemme know
file_list = ["QmcqWasAwrfnpGauWRakXyXYaMMss7puvPBR2LE7ZNcVR8",
             "Qmd2zCMyKZVLpbbvUUhcqChCCf8AqhUnRwtp8pQ35ZXiHH",
             "Qmdya7CCAg4t2hxvrW9qE8Afo3HBvfEPy1WDbaukdHvsPU",
             "QmfNHgRYSqeWka8PtTspbGj9fRBgqzBtSZNFx2KKWE1q4Z",
             "QmfJbNp9CRcUz6oY9yTzvP8uY1gSB2bheU6r8QuQ8EUso1",
             "QmNfnaEN8gzWjdNvrKSZxySWUAWcoAJmSAmfufUWfZyD3S",
             "QmVdLyu2xSN24fidXnn4obJVBEHXgQw2SDswhJ3Ewpb9d7",
             "QmNfnaEN8gzWjdNvrKSZxySWUAWcoAJmSAmfufUWfZyD3S",
             "QmfNHgRYSqeWka8PtTspbGj9fRBgqzBtSZNFx2KKWE1q4Z",
             ]

def main():
    client = ipfsapi.connect('127.0.0.1', 5001)

    print("getting main.c:")
    print("hash: " + file_list[0])
    client.get(file_list[0])

    print("getting main.cpp:")
    print("hash: " + file_list[1])
    client.get(file_list[1])

    print("getting ps -aux dump:")
    print("hash: " + file_list[2])
    client.get(file_list[2])

    print("getting a python file now:")
    print("hash: " + file_list[3])
    client.get(file_list[3])

    print("getting a directory now:")
    print("hash: " + file_list[4])
    client.get(file_list[4])

    print("getting a lua file:")
    print("hash: " + file_list[5])
    client.get(file_list[5])

    print("getting dir1:")
    print("hash: " + file_list[6])
    client.get(file_list[6])

    print("getting main.lua:")
    print("hash: " + file_list[7])
    client.get(file_list[7])

    print("getting main.py:")
    print("hash: " + file_list[8])
    client.get(file_list[8])

if __name__ == "__main__":
    main()
