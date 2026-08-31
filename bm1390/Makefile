# obj-m += bm1390-test.o bm1390-gpio-test.o

all: bm1390-test
bm1390-test: # bm1390-test.c bm1390-gpio-test.c
	make -C ${KERNEL_DIR} CROSS_COMPILE=${CC} ARCH=arm M=$(PWD) modules

clean:
	rm -rf bm1390_test.dtbo
install:
	cp bm1390_test.dtbo / ${CFG_BBB_NFS_ROOT}/.

debug_cfg:
	make -C ${KERNEL_DIR} CROSS_COMPILE=${CC} ARCH=arm M=$(PWD) CONFIG_DEBUG_SECTION_MISMATCH=y modules
