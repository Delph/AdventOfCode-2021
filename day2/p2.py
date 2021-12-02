#!/usr/bin/python3

#FILE = 'test.txt'
FILE = 'input.txt'

with open(FILE) as f:
  input = f.read().splitlines()


aim = 0
xpos = 0
depth = 0

for instruction in input:
  inst, amount = instruction.split(' ')
  if inst == 'forward':
    xpos += int(amount)
    depth += int(amount) * aim
  if inst == 'down':
    aim += int(amount)
  if inst == 'up':
    aim -= int(amount)

print(f'xpos: {xpos}, depth: {depth}, mult: {xpos*depth}')
