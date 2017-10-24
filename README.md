# VFS

A scratchpad Meant for the Truebit interpreter's filesystem.<br/>
a virtual filesysetem in C along with the syscalls.<br/>
to run the test, just use the shell script. it will handle building and running
the tests:<br/>

```bash

./run.sh

```

you can also use emcc:
```bash

emcc testfs.c

```
then run `a.out.js` with node. that will also run the tests.<br/>

sys calls for swarm and ipfs.<br/>
the ipfs syscalls are in python just because im messing around with them.<br/>
im not oblivous to the fact that we dont have a Python-WASM pipe yet.<br/>
You can get the ipfs python api with pip:<br/>

```bash

pip install ipfsapi

```
