import os
  
  
# Create a child process
# using os.fork() method 
pid = os.fork()
  
# pid greater than 0 represents
# the parent process 
if pid > 0 :
    print("I am parent process:")
    print("Process ID:", os.getpid())
    print("Child's process ID:", pid)
  
# pid equal to 0 represents
# the created child process
elif pid == 0:
    print("\nI am child process. pid = " + str(pid))
    print("Process ID:", os.getpid())
    print("Parent's process ID:", os.getppid())
  
  
# If any error occurred while
# using os.fork() method
# OSError will be raised
