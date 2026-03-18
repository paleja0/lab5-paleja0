import os
import math

current_dir = os.getcwd()
print(f"Current working directory: {current_dir}")

num = int(input("Enter an integer: "))

log_value = math.log2(num)
print(f"Log base 2 of {num} is: {log_value}")

floor_val = math.floor(log_value)
ceil_val = math.ceil(log_value)

print(f"Floor: {floor_val}")
print(f"Ceiling: {ceil_val}")