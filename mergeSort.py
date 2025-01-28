import time
def merge_sort(data, drawrectangle, delay):
    def merge(left, right, start, mid, end):
        i, j, k = 0, 0, start
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1
            drawrectangle(data, ['red' if x == k else 'white' for x in range(len(data))])
            time.sleep(delay)

        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1

    def merge_sort_recursive(start, end):
        if start < end:
            mid = (start + end) // 2
            merge_sort_recursive(start, mid)
            merge_sort_recursive(mid + 1, end)
            merge(data[start:mid + 1], data[mid + 1:end + 1], start, mid, end)

    merge_sort_recursive(0, len(data) - 1)
    drawrectangle(data, ['green' for _ in range(len(data))])
