import time
def insertion_sort(data, drawrectangle, delay):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
            drawrectangle(data, ['red' if x == j or x == j + 1 else 'white' for x in range(len(data))])
            time.sleep(delay) #this is same as the sorting speed we decided 
        data[j + 1] = key
        drawrectangle(data, ['green' for _ in range(len(data))])
