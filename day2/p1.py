#!/usr/bin/python3

#FILE = 'test.txt'
FILE = 'input.txt'

with open(FILE) as f:
  input = f.read().splitlines()


xpos = 0
depth = 0

for instruction in input:
  inst, amount = instruction.split(' ')
  if inst == 'forward':
    xpos += int(amount)
  if inst == 'down':
    depth += int(amount)
  if inst == 'up':
    depth -= int(amount)

print(f'xpos: {xpos}, depth: {depth}, mult: {xpos*depth}')
