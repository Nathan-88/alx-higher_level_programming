#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

n = len(sys.argv)
if n < 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
#for i in range(1, n):
 #   operator = sys.argv[2]
  #  if operator == "+":
   #     print("{} + {} = {}".format(sys.argv[1], sys.argv[3], add(sys.argv[1], sys.argv[3])
