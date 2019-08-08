import time

source = 'reportLine += 1'

reportLine = 0

start = time.time()
for i in range(10000):
    exec(source)
stop = time.time()
time_not_compiled = stop - start

start = time.time()
sourceComplited = compile(source,'internal variablesource', 'exec')

for i in range(10000):
    exec(sourceComplited)
stop = time.time()
time_compiled = stop - start

print(time_not_compiled)
print(time_compiled)
print(time_not_compiled/time_compiled)

print(reportLine)