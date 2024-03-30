import subprocess
import time

def _runtime(pin):

    start_time = time.time()

    command = "./chall"

    with subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True) as process:
        process.stdin.write(pin.ljust(10, '0') + "\n")
        process.stdin.flush()  # Flush the input buffer
        output, _ = process.communicate()
    end_time = time.time()
    runtime = end_time - start_time

    return runtime, output

max_runtime = 0
pin = ''
for i in range(10):
    curr_pin = pin
    for j in range(10):
        curr_t, out = _runtime(curr_pin + str(j))
        if max_runtime < curr_t:
            max_runtime = curr_t 
            pin = curr_pin + str(j)
    print(pin)
print(pin)
