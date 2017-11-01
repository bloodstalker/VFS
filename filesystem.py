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
def syscall_3(path):
    client.files_read(path)
#write
def syscall_4(path, bytes, create):
    client_write(path, bytes, create)
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
