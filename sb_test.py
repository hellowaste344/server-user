import subprocess
import sys
try:
    answer = subprocess.check_output(["python", "--version"], text=True)
    print(answer)
except subprocess.CalledProcessError as e:
    print(f"Command failed with return code {e.returncode}")

# Popen starts a new OS process 
lsProcess = subprocess.Popen(["ls"], stdout=subprocess.PIPE, text=True)
grepProcess = subprocess.Popen(
    ["grep", "banana"], stdin=lsProcess.stdout,
    stdout=subprocess.PIPE, text=True)
output, error = grepProcess.communicate()

print(output)
print(error)

ans = subprocess.call(["python", "--version"])
try:
    if ans == 0:
        print("Command executed")
except subprocess.CalledProcessError as e:
    sys.stdout.write("Command failed {0}".format(e.returncode))