#!/bin/sh

echo "+cpuset" >/sys/fs/cgroup/cgroup.subtree_control
chmod go+rx /run/user/1000
if [ ! -f "/dev/virtual_touchscreen" ]; then
  insmod /usr/src/virtual_touchscreen/virtual_touchscreen.ko abs_x_max=2560 abs_y_max=1440
  chmod 666 /dev/virtual_touchscreen
fi
export PULSE_SYSTEM=1
