obj-m += bd72720-test.o bd72720-gpio-test.o

all: bd72720-test
bd72720-test: bd72720-test.c bd72720-gpio-test.c
	make -C ${KERNEL_DIR} CROSS_COMPILE=${CC} ARCH=arm M=$(PWD) modules

clean:
	rm -rf bd71828_test.dtbo
install:
	cp bd71828_test.dtbo / ${CFG_BBB_NFS_ROOT}/.
	cp bd72720-test.ko  ${CFG_BBB_NFS_ROOT}/.
	cp bd72720-gpio-test.ko  ${CFG_BBB_NFS_ROOT} /.

debug_cfg:
	make -C ${KERNEL_DIR} CROSS_COMPILE=${CC} ARCH=arm M=$(PWD) CONFIG_DEBUG_SECTION_MISMATCH=y modules
