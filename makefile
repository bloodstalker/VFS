CC_FLAGS?=
LD_FLAGS?=
TARGET=testfs

.DEFAULT:all

.PHONY:all clean $(TARGET)

all:$(TARGET)

.c.o:
	$(CC) $(CC_FLAGS) -c $< -o $@

$(TARGET): $(TARGET).o
	$(CC) $^ $(LD_FLAGS) -o $@

clean:
	rm -f *.o *~ $(SYS_CALLS)
