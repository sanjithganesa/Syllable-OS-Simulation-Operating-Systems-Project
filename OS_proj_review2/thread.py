#implementing threads for syllable OS 
#Notes:
#syllable is monolithic
#syllable is single thread

import threading
import time

class Kernel:
    def __init__(self):
        self.threads = []
        self.lock = threading.Lock()

    def create_thread(self, thread_id, target, args=()):
        thread = threading.Thread(target=self.thread_wrapper, args=(thread_id, target, *args))
        self.threads.append(thread)
        return thread

    def thread_wrapper(self, thread_id, target, *args):
        print(f"Kernel: Initializing thread {thread_id}")
        with self.lock:
            print(f"Kernel: Thread {thread_id} has acquired the lock")
            target(*args)
            print(f"Kernel: Thread {thread_id} is releasing the lock")
        print(f"Kernel: Thread {thread_id} has finished execution")

    def start_all_threads(self):
        for thread in self.threads:
            thread.start()

    def join_all_threads(self):
        for thread in self.threads:
            thread.join()
        print("Kernel: All threads have finished execution")

# Define the function to be executed by each thread
def thread_function(thread_id):
    print(f"Thread {thread_id} is running")
    time.sleep(1)  # Simulate some work
    print(f"Thread {thread_id} is finished")

# Simulate a monolithic kernel handling threading
def main():
    kernel = Kernel()

    # Create threads
    for i in range(5):
        kernel.create_thread(i, thread_function, (i,))

    # Start all threads
    kernel.start_all_threads()

    # Wait for all threads to complete
    kernel.join_all_threads()

if __name__ == "__main__":
    main()
