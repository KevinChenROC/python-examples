import subprocess

# Using subprocess.PIPE
process = subprocess.Popen(['echo' ,'hello world!'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
stdout, _ = process.communicate()
print(stdout)

# By default stdout and stderr use parent Python process's file handles
process = subprocess.Popen(['echo' ,'hello world!']) # You should see hello world! in your shell