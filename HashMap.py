class HashMap:
    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for _ in range(size)]
        
    def set_val(self, key, val):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]
        
        for index, (record_key, _) in enumerate(bucket):
            if record_key == key:
                bucket[index] = (key, val)
                return 
        bucket.append((key,val))
            
    def get_val(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]

        for record_key, record_val in bucket:
            if record_key == key:
                return record_val
        return "No record found"        
    
    def delete_val(self, key):
        hashed_key = hash(key)%self.size
        bucket = self.hash_table[hashed_key]
        
        for index, (record_key, _) in enumerate(bucket):
            if record_key == key:
                bucket.pop(index)
                return
    
    def __str__(self):
        return "".join(str(bucket) for bucket in self.hash_table)
    
ht = HashMap(10)
print(ht)

ht.set_val('apple', 10)
ht.set_val('banana', 20)
ht.set_val('cherry', 30)

print("Hash Table:", ht)

print("Value for 'banana':", ht.get_val('banana'))
print("Value for 'apple':", ht.get_val('apple'))

ht.set_val('apple', 50)
print("Updated Hash Table:", ht)

ht.delete_val('banana')
print("After Deletion:", ht)

print("Value for 'banana':", ht.get_val('banana'))