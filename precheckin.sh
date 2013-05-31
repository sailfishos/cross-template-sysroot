#!/bin/sh
ARCHS="armv6l armv7l armv7hl armv7thl armv7tnhl mipsel i486 i586"

for x in $ARCHS; do
	cp cross-template-sysroot.spec cross-$x-sysroot.spec
	sed -i "s/@TARGET_CPU@/$x/g" cross-$x-sysroot.spec
	sed -i "s/ExclusiveArch:  none/ExclusiveArch:  %ix86/g" cross-$x-sysroot.spec
	case $x in
		arm*) sed -i "s/@GNU@/gnueabi/g" cross-$x-sysroot.spec ;;
		*) sed -i "s/@GNU@/gnu/g" cross-$x-sysroot.spec ;;
	esac
done
