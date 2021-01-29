import sys
import time

print(f'{"="*10} Output without Flush {"="*10}')
# It will take 10 sec to print the output as print 
# takes the data into buffer and then when the buffer gets 
# full it prints the data.
for i in range(10):
    print(i, end=' ')
    time.sleep(1)

print("\n")
print(f'{"="*10} Output with Flush {"="*10}')
# Now it won't store the data into buffer and
# directly print the output

for i in range(10):
    print(i, end=' ', flush=True)
    time.sleep(1)