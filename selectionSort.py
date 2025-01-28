import time
def selection_sort(data, drawrectangle, delay):
    for i in range(len(data)):
        min_idx = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_idx]:
                min_idx = j
            drawrectangle(data, ['red' if x == j or x == min_idx else 'white' for x in range(len(data))])
            time.sleep(delay)
        data[i], data[min_idx] = data[min_idx], data[i]
        drawrectangle(data, ['green' for _ in range(len(data))])
