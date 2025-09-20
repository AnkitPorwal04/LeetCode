class Router:
    def __init__(self, memoryLimit: int):
        self.size = memoryLimit
        self.packets = {}  # key -> [source, destination, timestamp]
        self.counts = defaultdict(list)  # destination -> sorted list of timestamps
        self.queue = deque()  # FIFO order of packets

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        key = self._encode(source, destination, timestamp)

        # Duplicate check
        if key in self.packets:
            return False

        # If memory full, forward oldest packet
        if len(self.packets) >= self.size:
            self.forwardPacket()

        # Add packet
        self.packets[key] = [source, destination, timestamp]
        self.queue.append(key)
        self.counts[destination].append(timestamp)

        return True

    def forwardPacket(self):
        if not self.packets:
            return []

        key = self.queue.popleft()
        packet = self.packets.pop(key)

        dest = packet[1]
        self.counts[dest].pop(0)  # remove the earliest timestamp

        return packet

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        timestamps = self.counts.get(destination, [])
        if not timestamps:
            return 0

        # Binary search for range
        left = bisect.bisect_left(timestamps, startTime)
        right = bisect.bisect_right(timestamps, endTime)

        return right - left

    def _encode(self, source: int, destination: int, timestamp: int) -> int:
        # Encode uniquely into 1 number
        return (source << 40) | (destination << 20) | timestamp
