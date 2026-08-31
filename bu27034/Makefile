# obj-m += bu27034-test.o bu27034-gpio-test.o

all: bu27034-test
bu27034-test: # bu27034-test.c bu27034-gpio-test.c
	make -C ${KERNEL_DIR} CROSS_COMPILE=${CC} ARCH=arm M=$(PWD) modules

clean:
	rm -rf bu27034_test.dtbo
install:
	cp bu27034_test.dtbo / ${CFG_BBB_NFS_ROOT}/.

debug_cfg:
	make -C ${KERNEL_DIR} CROSS_COMPILE=${CC} ARCH=arm M=$(PWD) CONFIG_DEBUG_SECTION_MISMATCH=y modules
