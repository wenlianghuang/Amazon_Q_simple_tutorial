import time
from multiprocessing import Process
from threading import Thread


def cpu_bound_task(n):
    """CPU-bound task - calculating sum of squares"""
    result = 0
    for i in range(n):
        result += i * i
    return result

def io_bound_task(seconds):
    """I/O-bound task - simulating I/O operations with sleep"""

def run_tasks_sequential(task, *args):
    start_time = time.time()
    for _ in range(4):  # Run 4 tasks
        task(*args)
    return time.time() - start_time

def run_tasks_multiprocess(task, *args):
    start_time = time.time()
    processes = []
    for _ in range(4):  # Run 4 processes
        p = Process(target=task, args=args)
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
    return time.time() - start_time

def run_tasks_multithread(task, *args):
    start_time = time.time()
    threads = []
    for _ in range(4):  # Run 4 threads
        t = Thread(target=task, args=args)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    return time.time() - start_time

if __name__ == '__main__':
    print("Comparing performance for CPU-bound tasks:")
    n = 10**7  # Number to calculate sum of squares up to
    
    sequential_time = run_tasks_sequential(cpu_bound_task, n)
    print(f"Sequential execution time: {sequential_time:.2f} seconds")
    
    multiprocess_time = run_tasks_multiprocess(cpu_bound_task, n)
    print(f"Multiprocess execution time: {multiprocess_time:.2f} seconds")
    
    multithread_time = run_tasks_multithread(cpu_bound_task, n)
    print(f"Multithread execution time: {multithread_time:.2f} seconds")
    
    print("\nComparing performance for I/O-bound tasks:")
    sleep_time = 1  # Seconds to sleep
    
    sequential_time = run_tasks_sequential(io_bound_task, sleep_time)
    print(f"Sequential execution time: {sequential_time:.2f} seconds")
    
    multiprocess_time = run_tasks_multiprocess(io_bound_task, sleep_time)
    print(f"Multiprocess execution time: {multiprocess_time:.2f} seconds")
    
    multithread_time = run_tasks_multithread(io_bound_task, sleep_time)
    print(f"Multithread execution time: {multithread_time:.2f} seconds")