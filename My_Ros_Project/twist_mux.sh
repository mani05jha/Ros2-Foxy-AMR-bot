#!/bin/bash
ros2 run twist_mux twist_mux --ros-args --params-file ./my_bot/src/my_bot/config/twist_mux.yaml -r cmd_vel_out:=diff_cont/cmd_vel_unstamped