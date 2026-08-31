# obj-m += bd79112-test.o bd79112-gpio-test.o

all: bd79112-test
bd79112-test: # bd79112-test.c bd79112-gpio-test.c
	make -C ${KERNEL_DIR} CROSS_COMPILE=${CC} ARCH=arm M=$(PWD) modules

clean:
	rm -rf bd79112_test.dtbo
install:
	cp bd79112_test.dtbo / ${CFG_BBB_NFS_ROOT}/.

debug_cfg:
	make -C ${KERNEL_DIR} CROSS_COMPILE=${CC} ARCH=arm M=$(PWD) CONFIG_DEBUG_SECTION_MISMATCH=y modules
