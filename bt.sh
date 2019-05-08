#!/usr/bin/expect -f

set prompt "#"
spawn sudo bluetoothctl
sleep 1
expect -re $prompt
sleep 1
send "power on\r"
sleep 1
expect -re $prompt
send "discoverable on\r"
sleep 1
expect -re $prompt
send "pairable on\r"
sleep 1
expect -re $prompt
send "agent NoInputNoOutput\r"
sleep 2
expect -re $prompt
send "default-agent\r"
expect -re $prompt
sleep 3
interact
