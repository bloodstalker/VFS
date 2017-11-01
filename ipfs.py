#!/bin/python3
import ipfsapi
# the daemon should be running before running any of this
# run: ipfs init
# run: ipfs daemon
# note to self: you cant cat a copy. you can read it though.


# blob > list > tree > commit

def ipfs_init():
    return (ipfsapi.connect('127.0.0.1', 5001))


def add_file(client, name):
    return client.add(name)


def main():
    client = ipfsapi.connect('127.0.0.1', 5001)

    client.files_mkdir("/test", parents=True)
    client.files_mkdir("/test1", parents=True)

    res1 = client.add('test1.c', wrap_with_directory=True)
    res2 = client.add('test2.cpp', wrap_with_directory=True)
    res3 = client.add('test3.wasm', wrap_with_directory=True)

    file1_ipfs_addr = res1[1]['Hash'] + "/" + "test1.c"
    file2_ipfs_addr = res2[1]['Hash'] + "/" + "test2.cpp"
    file3_ipfs_addr = res3[1]['Hash'] + "/" + "test3.wasm"
    print(client.cat(file1_ipfs_addr))
    print(client.cat(file2_ipfs_addr))
    #client.files_cp("/test/"+res1[0]['Hash'], "/test1")
    try:
        pass
        client.files_cp("/ipfs/"+res1[0]['Hash'], "/test1/test1.c")
        client.files_cp("/ipfs/"+res2[0]['Hash'], "/test1/test2.cpp")
        client.files_cp("/ipfs/"+res3[0]['Hash'], "/test1/test3.wasm")
    except ipfsapi.exceptions.StatusError:
        print("status error raised by cp")
        pass
    except requests.exceptions.HTTPError:
        print("http error raised by cp")
        pass

    print(client.files_read("/test1/test1.c"))

    print(repr(res1))
    print(repr(res1[0]['Hash']))

    client.repo_gc()
    print(client.repo_stat())
    print(client.files_ls("/test1"))

    try:
        print(client.cat("/test/" + res1[0]['Hash']))
        print(client.cat("/test/" + res1[0]['Hash']))
        print(client.cat("/test/" + res1[1]['Hash'] + "/test1.c"))
    except ipfsapi.exceptions.StatusError:
        print("cat cp failed.")
        pass

    dir1_ipfs_hash = client.files_stat("/test1")
    dir0_ipfs_hash = client.files_stat("/test")
    print(dir1_ipfs_hash['Hash'])
    print(dir0_ipfs_hash['Hash'])
    print(client.files_stat("/test1/test1.c"))
    print(client.files_stat("/test1/test2.cpp"))
    print(client.files_stat("/test1/test3.wasm"))
    print(client.files_read("/test1/test3.wasm"))

    print(repr(res1))
    print(repr(res2))
    print(repr(res3))
    print(client.cat(res1[0]['Hash']))
    print(client.cat(res2[0]['Hash']))
    print(client.cat(res3[0]['Hash']))


if __name__ == '__main__':
    main()

