class HashRing:
    def __init__(self,size = 4):
        self.servers = [[] for i in range(size)]

    def view_server_keys(self):
        for idx, server in enumerate(self.servers):
            print(f"Index: {idx} has the following contents \n{server}")
    
    def add_key(self,key_val):
        # key values are in integers
        # assign key to servers
        hash_val = key_val % len(self.servers)
        self.servers[hash_val].append(key_val)
        print("Key is added")
    
    def add_server(self):
        # add servers to the hash ring; clockwise check
        previous_hash = len(self.servers) - 1
        self.servers.append([])
        self.servers[-1], self.servers[previous_hash] = self.servers[previous_hash], self.servers[-1]
        print("Server is added!")

    def delete_server(self,idx):
        if idx < len(self.servers):
            print("Invalid index!")
            return
        
        # check edge cases
        # 'first' server in the ring -> last server goes to second
        if idx == 0:
            affected_idx = -1
            target_idx = 1
        # 'last' server in the ring -> second last server goes to idx 0
        elif idx == len(self.servers) - 1:
            affected_idx = idx - 1
            target_idx = 0
        else:
            affected_idx = idx - 1
            target_idx = idx + 1
            
        # move all the keys (from deleted server) to the next server (relative clockwise)
        affected_keys = self.servers[affected_idx]
        self.servers[target_idx] += affected_keys
        
        # delete server to the hash ring
        del self.servers[affected_idx]
        print("Server is deleted!")
    