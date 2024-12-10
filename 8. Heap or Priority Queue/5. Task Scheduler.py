class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)
        time = 0
        q = deque()

        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                c = 1 + heapq.heappop(maxHeap)
                if c:
                    q.append([c, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time