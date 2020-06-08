#!/usr/bin/env python3.6 
import sys

args = sys.argv

t, c = sys.stdin.readline().strip().split("¥t")
title, count = t, int(c)
for line in sys.stdin:
  t, c = line.strip().split("¥t")
  if title != t:
   if count > int(args[1]):
       print(title, "¥t", count);
      title, count = t, int(c)
  else:
      count += int(c)
if count > int(args[1]):
    print(title, "¥t", count);
