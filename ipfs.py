import ipfsapi
# the daemon should be running before running any of this
# run: ipfs init
# run: ipfs daemon

def ipfs_init():
    return (ipfsapi.connect('127.0.0.1', 5001))


def add_file(client, name):
    return client.add(name)

#open
def syscall_open(hash):
    pass
#seeking
def syscall_140():
    pass
#close
def syscall_6():
    pass
#read
def syscall_3():
    pass
#write
def syscall_4():
    pass
#dup
def syscall_41():
    pass
#dup2
def syscall_63():
    pass
#dup3
def syscall_330():
    pass
#readv
def syscall_145():
    pass
#preadv
def syscall_333():
    pass
#pwritev
def syscall_334():
    pass
#pread64
def syscall_180():
    pass
#pwrite64
def syscall_181():
    pass
#openat
def syscall_295():
    pass




#link
def syscall_9():
    pass
#unlink
def syscall_10():
    pass
#chdir
def syscall_12():
    pass
#rename
def syscall_38():
    pass
#mkdir
def syscall_39():
    pass
#rmdir
def syscall_40():
    pass
#symlink
def syscall_83():
    pass
#fchdir
def syscall_133():
    pass
#getcwd
def syscall_140():
    pass
#getcwd
def syscall_183():
    pass
#getdents
def syscall_220():
    pass
#mkdirat
def syscall_296():
    pass
#unlinkat
def syscall_301():
    pass
#renameat
def syscall_302():
    pass
#symlinkat
def syscall_304():
    pass


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
    #client.files_cp("/ipfs/"+res1[0]['Hash'], "/test1/test1.c")
    #client.files_cp("/ipfs/"+res2[0]['Hash'], "/test1/test2.cpp")
    #client.files_cp("/ipfs/"+res3[0]['Hash'], "/test1/test3.wasm")

    print(repr(res1))
    print(repr(res1[0]['Hash']))

    #print(client.pin_ls())
    client.repo_gc()
    #print(client.pin_ls())
    print(client.repo_stat())
    #print(client.swarm_peers())
    print(client.files_ls("/test1"))

    #print(client.cat("/test/" + res1[0]['Hash']))
    #print(client.cat("/test/" + res1[0]['Hash']))
    #print(client.cat("/test/" + res1[1]['Hash'] + "/test1.txt"))

    #print(repr(res1))
    #print(repr(res2))
    #print(repr(res3))
    #print(client.cat(res1['Hash']))
    #print(client.cat(res2['Hash']))
    #print(client.cat(res3['Hash']))


if __name__ == '__main__':
    main()

