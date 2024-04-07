class cache_sim:
    def __init__(self, cache_size, block_size, map_tech):
        self.cache_size = cache_size
        self.block_size = block_size
        self.map_tech  = map_tech
        self.blocks = cache_size//block_size
        self.hits = 0
        self.miss = 0
        self.evictions = 0
        self.cache = -1*self.blocks  #initially empty cache(-1)


def main():
    cache_size = int(input("Enter cache size(bytes)"))
    block_size = int(input("Enter block size(bytes)"))
    map_tech = input("Enter mapping technique")
    user_input = ("Enter comma separated values").split(",")

    cache = cache_sim(cache_size, block_size, map_tech)

    print("Total Hits:", cache.hits)
    print("Total Misses:", cache.miss)
    print("Total Evictions:", cache.evictions)

if __name__ == "__main__":
    main()
