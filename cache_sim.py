class cache_sim:
    def __init__(self, cache_size, block_size, map_tech):
        self.cache_size = cache_size
        self.block_size = block_size
        self.map_tech  = map_tech
        self.blocks = cache_size//block_size
        self.hits = 0
        self.misses = 0
        self.evictions = 0
        self.cache = [-1]*self.blocks  #initially empty cache(-1)

    def direct(self, index, tag):
        if self.cache[index] == tag:
            print(f"Hit pa: {hex(tag*(self.block_size*self.blocks)+index*self.block_size)}")
            self.hits += 1
        else:
            print(f"Miss pa: {hex(tag*(self.block_size*self.blocks)+index*self.block_size)}")
            self.misses += 1
            self.cache[index] = tag #replacement

    def set_associative(self, index, tag):
        setindex = index%(self.blocks//2) #Two way set-associative
        if self.cache[setindex] == tag or self.cache[setindex+1] == tag:
            print(f"Hit pa: {hex(tag*(self.block_size*self.blocks)+index*self.block_size)}")
            self.hits += 1
        else:
            print(f"Miss pa: {hex(tag*(self.block_size*self.blocks)+index*self.block_size)}")
            self.misses += 1

            if self.cache[setindex] == -1:
                self.cache[setindex] = tag #replace first element
            elif self.cache[setindex+1] == -1:
                self.cache[setindex+1] = tag #replace second element
            else:
                if self.cache[setindex]<self.cache[setindex+1]:
                    self.cache[setindex+1] = tag
                else:
                    self.cache[setindex] = tag
                self.evictions += 1 #value evicted and replced with tag since both are non-empty(uses LRU)

    def associative(self, tag):
        if tag in self.cache:
            print(f"Hit pa: {hex(tag*(self.block_size*self.blocks))}")
            self.hits += 1
        else:
            print(f"Miss pa: {hex(tag*(self.block_size*self.blocks))}")
            self.misses += 1

            self.cache[0] = tag #replacement

    def address(self, address):
        offset = address%self.block_size
        index = (address//self.block_size)%(self.blocks)
        tag = (address)//(self.block_size*self.blocks)

        if self.map_tech == "Direct":
            self.direct(index, tag)
        elif self.map_tech == "Set Associative":
            self.set_associative(index, tag)
        elif self.map_tech == "Associative":
            self.associative(tag)
        else:
            print("Invalid mapping technique")

def main():
    cache_size = int(input("Enter cache size(bytes):"))
    block_size = int(input("Enter block size(bytes):"))
    map_tech = input("Enter mapping technique:(Direct/Set Associative/Associative):")

    cache = cache_sim(cache_size, block_size, map_tech)

    while True:
        user_input = input("Enter memory address(comma separated decimal values), type(Q/q) to quit:")
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

if __name__ == "__main__":
    main()
