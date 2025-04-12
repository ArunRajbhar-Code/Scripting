import subprocess

cmd = 'winget list'
output = subprocess.run(cmd, shell=True, capture_output=True, text=True)
# subprocess.run(["echo", "Hello, World!"],shell=True)

print(output.stdout)
