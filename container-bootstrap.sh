#!/bin/sh

echo "+cpuset" >/sys/fs/cgroup/cgroup.subtree_control
chmod go+rx /run/user/1000
