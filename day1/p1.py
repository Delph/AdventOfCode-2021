#!/usr/bin/python3

with open('input.txt') as f:
  input = [int(x) for x in f.read().splitlines()]

increased = 0
last = -1
for reading in input:
  if last == -1:
    last = reading
    continue
  if reading > last:
    increased += 1
  last = reading
print(increased)
