# HashMap class creates a hash table that stores package objects
class HashMap:
    def __init__(self):
        self.size = 40
        self.map = [None] * self.size

    # This creates a hash key - O(1)
    def create_hash_key(self, key):
        return key % self.size

    # This is the 'insert function' that adds the package to the hash table - O(N)
    def add(self, key, package):
        hash_key = self.create_hash_key(key)
        key_value = [key, package]

        if self.map[hash_key] is None:
            self.map[hash_key] = list([key_value])
            return True
        else:
            for pair in self.map[hash_key]:
                if pair[0] == key:
                    pair[1] = package
                    return True
            # This is a self-adjusting data structure that implements chaining
            self.map[hash_key].append(key_value)
            return True

    # This is the 'lookup function' that gets the package from the hash table, per requirements - O(N)
    def get(self, key):
        key_hash = self.create_hash_key(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    # This is the remove function that deletes a package from the hash table - O(N)
    def delete(self, key):
        key_hash = self.create_hash_key(key)

        if self.map[key_hash] is None:
            return False
        for i in range (0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True