import heapq

def main():
    max_heap = []
    min_heap = []

    while True:
        x = input()
        if x == "":
            if len(max_heap)==0 and len(min_heap)==0:
                return 0
            mid = None

            if (len(max_heapa)+len(min_heap))&1==0:
                mid = (heapq.heappop(min_heap) - heapq.heappop(max_heap)) / 2
            else:
                mid = heapq.heappop(max_heap) * -1

            print("mid:",mid)
            return

        x = int(x)
        if (len(min_heap) + len(max_heap)) & 1 == 0:
            if len(min_heap) > 0:
                heapq.heappush(min_heap, x)
                x = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -1 * x) # 负数的原因是因为heapq是小根堆
        else:
            if len(max_heap) > 0:
                heapq.heappush(max_heap, -1 * x)
                x = -1 * heapq.heappop(max_heap)
            heapq.heappush(min_heap, x)