# bounce.py
#
# Exercise 1.5
reduction_value = 0.6
num_bounces = 10
height = 100

for bounce in range(1, num_bounces + 1):
    height = height * reduction_value
    print(bounce, round(height, 4))