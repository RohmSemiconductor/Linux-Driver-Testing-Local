COMMON_NAME := bd9573-demo

#obj-m := ${COMMON_NAME}.o
obj-m := bd9573-test.o

all:
	make -C ${KERNEL_DIR} CROSS_COMPILE=${CC} ARCH=arm M=$(PWD) modules
clean:
	make -C ${KERNEL_DIR} CROSS_COMPILE=${CC} ARCH=arm M=$(PWD) clean
	rm -rf bd9573_test.dtbo
install:
	cp bd9573-test.ko ${CFG_BBB_NFS_ROOT}/.
	cp bd9573_test.dtbo ${CFG_BBB_NFS_ROOT}/.

debug_cfg:
	make -C ${KERNEL_DIR} CROSS_COMPILE=${CC} ARCH=arm M=$(PWD) CONFIG_DEBUG_SECTION_MISMATCH=y modules
