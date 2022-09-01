#!/bin/bash

# prevent frame stuttering/drops
pkill picom
echo "killed picom..."

# disable turbo boost for lower temps
sudo echo 0 > /sys/devices/system/cpu/cpufreq/boost
echo "disabled turbo boost..."

# make osu! run at higher frames or lower frame time
sudo cpupower frequency-set -g performance
echo "set cpu governor to [performance]..."

