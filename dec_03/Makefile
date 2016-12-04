CC=cc
LD=ld
LINKER_FLAGS=-lc
REVERSE_LIB=reverse.h reverse.c
MAC_ARGUMENT=-macosx_version_min 10.11

noop:
	echo Must specify target

reverse_test:   OUTPUT=$@.out
reverse_test:   reverse.o reverse_test.o
	$(LD) -o $(OUTPUT) $(LINKER_FLAGS) $(MAC_ARGUMENT) $?
