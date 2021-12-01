#!/usr/bin/python3

with open('input.txt') as f:
  input = [int(x) for x in f.read().splitlines()]

increased = 0
last = -1
for group in [input[i:i + 3] for i in range(0, len(input) - 2)]:
  if last == -1:
    last = sum(group)
    continue;
  current = sum(group)
  if current > last:
    increased += 1
  last = current
print(increased)
