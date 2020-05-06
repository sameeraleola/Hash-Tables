class HashTableEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, size):
            self.size = size
            self.storage = [None] * size
            

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """

    def djb2(self, key):
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash
      

    def hash_index(self, key):

        return self.djb2(key) % self.size

    def put(self, key, value):
        
        index = self.hash_index(key)
        entry = HashTableEntry(key, value)
        current = self.storage[index]
        
        if current is not None:
            self.storage[index] = entry
            self.storage[index].next = current
        else:
            self.storage[index] = entry

    def delete(self, key):
        
        index = self.hash_index(key)
        current = self.storage[index]
        prev = None
        

        if current.key == key:
            self.storage[index] = current.next
            return 
        
        while current != None:
            if current.key == key:
                prev.next = current.next
                self.storage[index].next = None
                return 
            
            prev = current
            current = current.next
        return


        


    def get(self, key):
       
       index = self.hash_index(key)
       current = self.storage[index]

       while current:
           if current.key == key:
               return current.value
           current = current.next
        
       return current


    def resize(self):
     self.storage = self.storage + [None] * self.size
     return self.storage
     

if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
