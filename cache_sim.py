class cache_sim:
    def __init__(self, cache_size, block_size, map_tech):
        self.cache_size = cache_size
        self.block_size = block_size
        self.map_tech  = map_tech
        self.blocks = cache_size//block_size
        self.hits = 0
        self.miss = 0
        self.evictions = 0
        self.cache = -1*self.blocks  #initially empty cache


