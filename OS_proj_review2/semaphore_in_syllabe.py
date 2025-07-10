import threading
import time
from collections import defaultdict

class Status:
    SUCCESS = 0
    FAILURE = 1

class Resource:
    def __init__(self, start, size, mask=0):
        self.start = start
        self.size = size
        self.mask = mask

class ResourceTree:
    def __init__(self):
        self.resources = []

    def add_resource(self, start, size, mask=0):
        self.resources.append(Resource(start, size, mask))

    def release_region(self, start, size):
        for resource in self.resources:
            if resource.start == start and resource.size == size:
                self.resources.remove(resource)
                print(f"Region [{start}, {size}] released")
                return Status.SUCCESS
        return Status.FAILURE

    def free_resource(self, start, mask):
        for resource in self.resources:
            if resource.start == start and resource.mask == mask:
                self.resources.remove(resource)
                print(f"Resource [{start}, Mask = {mask}] freed")
                return Status.SUCCESS
        return Status.FAILURE

    def print_resources(self):
        for resource in self.resources:
            print(f"Resource: Start = {resource.start}, Size = {resource.size}, Mask = {resource.mask}")

class Semaphore:
    def __init__(self, initial_count=1):
        self.semaphore = threading.Semaphore(initial_count)
        self.count = initial_count
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)
        self.wait_queue = []

class SemaphoreManager:
    def __init__(self):
        self.semaphores = {}
        self.next_id = 1
        self.lock = threading.Lock()

    def create_semaphore(self, initial_count=1):
        with self.lock:
            sem_id = self.next_id
            self.semaphores[sem_id] = Semaphore(initial_count)
            self.next_id += 1
        return sem_id

    def delete_semaphore(self, hSema):
        with self.lock:
            if hSema in self.semaphores:
                del self.semaphores[hSema]
                return Status.SUCCESS
            return Status.FAILURE

    def lock_semaphore_ex(self, hSema, nCount, nFlags, nTimeOut):
        if hSema not in self.semaphores:
            return Status.FAILURE
        
        sem = self.semaphores[hSema]
        acquired = sem.semaphore.acquire(timeout=nTimeOut)
        if acquired:
            with sem.lock:
                sem.count -= nCount
            return Status.SUCCESS
        return Status.FAILURE

    def lock_semaphore(self, hSema, nFlags, nTimeOut):
        return self.lock_semaphore_ex(hSema, 1, nFlags, nTimeOut)

    def unlock_semaphore_ex(self, hSema, nCount):
        if hSema not in self.semaphores:
            return Status.FAILURE
        
        sem = self.semaphores[hSema]
        with sem.lock:
            for _ in range(nCount):
                sem.semaphore.release()
            sem.count += nCount
        return Status.SUCCESS

    def unlock_semaphore(self, hSema):
        return self.unlock_semaphore_ex(hSema, 1)

    def unlock_and_suspend(self, hWaitQueue, hSema):
        if hWaitQueue not in self.semaphores or hSema not in self.semaphores:
            return Status.FAILURE
        
        wait_queue = self.semaphores[hWaitQueue]
        sem = self.semaphores[hSema]

        with wait_queue.lock:
            wait_queue.condition.notify_all()

        with sem.lock:
            sem.semaphore.release()
            sem.count += 1

        return Status.SUCCESS

    def spinunlock_and_suspend(self, hWaitQueue, psLock, nCPUFlags, nTimeOut):
        if hWaitQueue not in self.semaphores:
            return Status.FAILURE
        
        wait_queue = self.semaphores[hWaitQueue]

        with psLock:
            with wait_queue.lock:
                wait_queue.condition.notify_all()

        return Status.SUCCESS

    def reset_semaphore(self, hSema, nCount):
        if hSema not in self.semaphores:
            return Status.FAILURE
        
        sem = self.semaphores[hSema]
        with sem.lock:
            sem.semaphore = threading.Semaphore(nCount)
            sem.count = nCount
        return Status.SUCCESS

    def sleep_on_sem(self, hSema, nTimeOut):
        if hSema not in self.semaphores:
            return Status.FAILURE
        
        sem = self.semaphores[hSema]
        acquired = sem.semaphore.acquire(timeout=nTimeOut)
        if acquired:
            sem.semaphore.release()
            return Status.SUCCESS
        return Status.FAILURE

    def wakeup_sem(self, hSema, bAll):
        if hSema not in self.semaphores:
            return Status.FAILURE
        
        sem = self.semaphores[hSema]
        with sem.lock:
            if bAll:
                while sem.count < 1:
                    sem.semaphore.release()
                    sem.count += 1
            else:
                sem.semaphore.release()
                sem.count += 1

        return Status.SUCCESS

# Example usage
def main():
    manager = SemaphoreManager()
    resource_tree = ResourceTree()

    # Create some semaphores
    sem_id1 = manager.create_semaphore(1)
    sem_id2 = manager.create_semaphore(0)

    # Add resources to the resource tree
    resource_tree.add_resource(0, 100, 1)
    resource_tree.add_resource(10, 20, 2)
    resource_tree.add_resource(40, 30, 1)
    resource_tree.add_resource(80, 10, 2)

    print("Initial Resource Tree:")
    resource_tree.print_resources()

    # Perform some semaphore operations
    manager.lock_semaphore(sem_id1, 0, 5)
    manager.unlock_semaphore(sem_id1)
    manager.lock_semaphore_ex(sem_id1, 1, 0, 5)
    manager.unlock_semaphore_ex(sem_id1, 1)

    manager.unlock_and_suspend(sem_id2, sem_id1)
    manager.spinunlock_and_suspend(sem_id2, manager.semaphores[sem_id1].lock, 0, 5)
    manager.reset_semaphore(sem_id1, 2)
    manager.sleep_on_sem(sem_id2, 5)
    manager.wakeup_sem(sem_id2, True)

    print("After semaphore operations:")
    print(f"Semaphore {sem_id1}: Count = {manager.semaphores[sem_id1].count}")
    print(f"Semaphore {sem_id2}: Count = {manager.semaphores[sem_id2].count}")

    # Perform resource operations
    resource_tree.release_region(40, 30)
    resource_tree.free_resource(10, 2)

    print("Resource Tree after releasing and freeing resources:")
    resource_tree.print_resources()

if __name__ == "__main__":
    main()
