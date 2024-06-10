# Micro:bit Stopwatch
# Mr. Scott
# June 7th

import microbit, time, random
# time.time() tells us how many seconds it has
# been since Jan 1st, 1970 at midnight GMT-0.

start_time = time.time() # 5 ... .. .10
while True:
    cur_time = time.time() # 5 6 7 8 9 10
    elapsed_time = cur_time - start_time
    print(elapsed_time)
    
    if microbit.button_a.was_pressed():
        start_time = time.time()