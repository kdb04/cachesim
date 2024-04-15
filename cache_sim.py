class cache_sim:
    def __init__(self, cache_size, block_size, map_tech):
        self.cache_size = cache_size
        self.block_size = block_size
        self.map_tech = map_tech
        self.blocks = cache_size // block_size
        self.hits = 0
        self.misses = 0
        self.evictions = 0
        self.cache = [-1] * self.blocks  # initially empty cache(-1)
        self.total = 0 #total memory accesses

    def direct(self, index, tag):
        physical_address = tag * (self.block_size * self.blocks) + index * self.block_size
        if self.cache[index] == tag:
            print(f"Hit pa: {physical_address}")
            self.hits += 1
        else:
            print(f"Miss pa: {physical_address}")
            self.misses += 1
            self.cache[index] = tag  # replacement


    def set_associative(self, index, tag):
        set_size = 2  # Two-way set-associative
        setindex = index % (self.blocks // set_size)
        set_start = setindex * set_size
        physical_address = tag * (self.block_size * self.blocks) + index * self.block_size

        if self.cache[set_start] == -1 or self.cache[set_start + 1] == -1:
            if self.cache[set_start] == -1:
                self.cache[set_start] = tag  # First block
            else:
                self.cache[set_start + 1] = tag  #Second block
            print(f"Miss pa: {physical_address}")
            self.misses += 1
        elif tag in (self.cache[set_start], self.cache[set_start+1]):
            print(f"Hit pa: {physical_address}")
            self.hits+=1
        else: #LRU replacement
            if self.cache[set_start] < self.cache[set_start+1]: #First block accesed more frequently as its tag value is lesser
                lru_block = set_start
            else:
                lru_block = set_start + 1
            evicted_tag = self.cache[lru_block]
            self.cache[lru_block] = tag
            print(f"Miss pa: {physical_address}")
            print(f"Evicted tag: {evicted_tag}")
            self.misses+=1
            self.evictions+=1

    def fully_associative(self, tag):
        physical_address = tag * (self.block_size * self.blocks)
        if tag in self.cache:
            print(f"Hit pa: {physical_address}")
            self.hits += 1
        else:
            print(f"Miss pa: {physical_address}")
            self.misses += 1
            if -1 in self.cache:
                self.cache[self.cache.index(-1)] = tag
            else:   #LRU replacement
                lru_index = self.cache.index(min(self.cache))
                evicted_tag = self.cache[lru_index]
                print(f"Evicting tag: {evicted_tag}")
                self.cache[lru_index] = tag

    def address(self, address):
        offset = address % self.block_size
        index = (address // self.block_size) % (self.blocks)
        tag = (address) // (self.block_size * self.blocks)
        self.total += 1
        if self.map_tech == "Direct":
            self.direct(index, tag)
        elif self.map_tech == "Set Associative":
            self.set_associative(index, tag)
        elif self.map_tech == "Fully Associative":
            self.fully_associative(tag)
        else:
            print("Invalid mapping technique")

    def hit_rate(self):
        if self.total>0:
            return self.hits/self.total
        else:
            return 0

    def miss_rate(self):
        if self.total>0:
            return self.misses/self.total
        else:
            return 0

def main():
    cache_size = int(input("Enter cache size(bytes):"))
    block_size = int(input("Enter block size(bytes):"))
    map_tech = input("Enter mapping technique:(Direct/Set Associative/Fully Associative):")
    cache = cache_sim(cache_size, block_size, map_tech)
    while True:
        user_input = input("Enter memory address, type(Q/q) to quit:")
        if user_input.lower() == "q":
            break
        else:
            try:
                addr = int(user_input)
                cache.address(addr)
            except ValueError:
                print("Enter valid decimal value")
    print("Total Hits:", cache.hits)
    print("Total Misses:", cache.misses)
    print("Total Evictions:", cache.evictions)
    print("Hit Rate:", cache.hit_rate())
    print("Miss Rate:", cache.miss_rate())

if __name__ == "__main__":
    main()
