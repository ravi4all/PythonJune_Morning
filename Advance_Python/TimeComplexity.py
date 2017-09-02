import time

start = time.time()

a = []
for i in range(0,100000000):
    a.append(i)

##print(a)
end = time.time()

print("Time", end-start)
