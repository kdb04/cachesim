class cache_sim:
    def __init__(self, cache_size, block_size, map_tech):
        self.cache_size = cache_size
        self.block_size = block_size
        self.map_tech  = map_tech
        self.blocks = cache_size//block_size
        self.hits = 0
        self.misses = 0
        self.evictions = 0
        self.cache = -1*self.blocks  #initially empty cache(-1)

    def direct(self, index, tag):
        if self.cache[index] == tag:
            print("Hit pa!")
            self.hits += 1
        else:
            print("Miss pa!")
            self.misses += 1
            self.cache[index] = tag #replacement

    def set_associative(self, index, tag):
        setindex = index%(self.blocks//2) #Two way set-associative
        if self.cache[setindex] == tag or self.cache[setindex+1] == tag:
            print("Hit pa!")
            self.hits += 1
        else:
            print("Miss pa!")
            self.misses += 1

            if self.cache[setindex] == -1:
                self.cache[setindex] = tag #replace first element
            elif self.cache[setindex+1] == -1:
                self.cache[setindex+1] = tag #replace second element
            else:
                self.cache[setindex] = tag
                self.evictions += 1 #value evicted and replced with tag since both are non-empty(uses LRU)

    def associative(self, tag):
        if tag in self.cache:
            print("Hit pa!")
            self.hits += 1
        else:
            print("Miss pa!")
            self.misses += 1

            self.cache[0] = tag #replacement

def main():
    cache_size = int(input("Enter cache size(bytes)"))
    block_size = int(input("Enter block size(bytes)"))
    map_tech = input("Enter mapping technique")
    user_input = ("Enter comma separated values").split(",")

    cache = cache_sim(cache_size, block_size, map_tech)

    print("Total Hits:", cache.hits)
    print("Total Misses:", cache.misses)
    print("Total Evictions:", cache.evictions)

if __name__ == "__main__":
    main()
