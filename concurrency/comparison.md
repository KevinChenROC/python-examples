# Multithreading

## pros

- less costly to start a new thread than process

## cons

- GIL problem
  - GIL = global interpreter lock, a mutex to eliminate race condition, by requiring that only one thread can execute python codes at a time by acquring GIL first.
- Due to GIL, it is not suited for CPU-bound tasks.
- Non interruptable/killable
  - To kill a thread, we have to kill the process wrapping this thread.
  - The same mechanism applies to interrupt.

# Multiprocessing

## pros

- Great for CPU-bound tasks

## cons

- Slower to initiate a process
  - WHY? We need to update the process table in OS, intiate registers, etc.
