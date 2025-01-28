import time
def quick_sort(data, drawrectangle, delay):
    def partition(low, high):
        pivot = data[high]
        i = low - 1
        for j in range(low, high):
            if data[j] < pivot:
                i += 1
                data[i], data[j] = data[j], data[i]
            drawrectangle(data, ['red' if x == j or x == i else 'white' for x in range(len(data))])
            time.sleep(delay)
        data[i + 1], data[high] = data[high], data[i + 1]
        return i + 1

    def quick_sort_recursive(low, high):
        if low < high:
            pi = partition(low, high)
            quick_sort_recursive(low, pi - 1)
            quick_sort_recursive(pi + 1, high)

    quick_sort_recursive(0, len(data) - 1)
    drawrectangle(data, ['green' for _ in range(len(data))])
