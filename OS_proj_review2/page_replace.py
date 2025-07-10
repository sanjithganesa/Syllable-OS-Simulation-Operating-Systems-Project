def find_lru(time, n):
    minimum = time[0]
    pos = 0
    for i in range(1, n):
        if time[i] < minimum:
            minimum = time[i]
            pos = i
    return pos

def lru_page_replacement(pages, n, m):
    frames = [-1] * m
    time = [0] * m
    page_faults = 0
    current_time = 0

    for i in range(n):
        flag1 = flag2 = False

        for j in range(m):
            if frames[j] == pages[i]:
                flag1 = flag2 = True
                time[j] = current_time
                break

        if not flag1:
            for j in range(m):
                if frames[j] == -1:
                    page_faults += 1
                    frames[j] = pages[i]
                    time[j] = current_time
                    flag2 = True
                    break

        if not flag2:
            pos = find_lru(time, m)
            frames[pos] = pages[i]
            time[pos] = current_time
            page_faults += 1

        current_time += 1
        print(f"Step {i + 1}: Frames: {frames}")

    print(f"Total page faults: {page_faults}")

def find_optimal(pages, frames, n, index):
    res = -1
    farthest = index
    for i in range(len(frames)):
        j = index
        while j < n:
            if frames[i] == pages[j]:
                if j > farthest:
                    farthest = j
                    res = i
                break
            j += 1
        if j == n:
            return i
    return 0 if res == -1 else res

def optimal_page_replacement(pages, n, m):
    frames = [-1] * m
    page_faults = 0

    for i in range(n):
        flag = False

        for j in range(m):
            if frames[j] == pages[i]:
                flag = True
                break

        if not flag:
            if -1 in frames:
                page_faults += 1
                frames[frames.index(-1)] = pages[i]
            else:
                pos = find_optimal(pages, frames, n, i + 1)
                frames[pos] = pages[i]
                page_faults += 1

        print(f"Step {i + 1}: Frames: {frames}")

    print(f"Total page faults: {page_faults}")

# Example usage
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3]
n = len(pages)
m = 3

print("LRU Page Replacement:")
lru_page_replacement(pages, n, m)

print("\nOptimal Page Replacement:")
optimal_page_replacement(pages, n, m)
