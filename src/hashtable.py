"""Hash table module...."""


class HashTable(object):
    """Hash table with multiple hashing functions."""

    def __init__(self, size=1024, hash_func='additive'):
        """Set up hash with specified hash function and size."""
        self.nums = [10, 6, 3, 11, 15]
        self.size = size
        self.count = 0
        self.buckets = []
        self.hash_funcs = {
            'additive': self._additive_hash,
            'oat': self._oat_hash,
            'oneatatime': self._oat_hash,
            'fnv': self._fnv_hash,
            'custom': self._custom_oat_hash
        }

        inpt = hash_func.lower().replace('-', '')
        try:
            self.hash_func = self.hash_funcs[inpt]
        except KeyError:
            raise NameError("Hash function, " + hash_func + ", is not an option.")

        for i in range(size):
            self.buckets.append([])

    def get(self, key):
        """Retrieve the given val using the given key."""
        bucket = self._get_bucket(key)
        idx = self._get_sub_bucket_idx(key, bucket)
        if idx is not None:
            return bucket[idx][1]
        else:
            raise KeyError('Key not found in hash table.')

    def set(self, key, val):
        """Store the given val using the given key."""
        bucket = self._get_bucket(key)
        idx = self._get_sub_bucket_idx(key, bucket)
        if idx is not None:
            bucket[idx] = (key, val)
        else:
            self.count += 1
            bucket.append((key, val))

    def _get_bucket(self, key):
        idx = self._hash(key) % self.size
        return self.buckets[idx]

    def _get_sub_bucket_idx(self, key, bucket):
        for idx, kv_pair in enumerate(bucket):
            if kv_pair[0] == key:
                return idx

    def _hash(self, key):
        """Hash the provided key."""
        if type(key) is str:
            return self.hash_func(key)
        else:
            raise TypeError('Key must be a string.')

    def _oat_hash(self, key):
        h = 0

        for i in range(len(key)):
            h += ord(key[i])
            h += h << 10
            h ^= h >> 6
        h += h << 3
        h ^= h >> 11
        h += h << 15

        return h

    def _additive_hash(self, key):
        h = 0
        for i in range(len(key)):
            h += ord(key[i])
        return h

    def _fnv_hash(self, key):
        h = 2166136261
        for i in range(len(key)):
            h = (h * 16777619) ^ ord(key[i])
        return h

    def _custom_oat_hash(self, key):
        h = 0

        for i in range(len(key)):
            h += ord(key[i])
            h += h << self.nums[0]
            h ^= h >> self.nums[1]
        h += h << self.nums[2]
        h ^= h >> self.nums[3]
        h += h << self.nums[4]

        return h

    def __getitem__(self, key):
        """Try to find and return item."""
        return self.get(key)

    def __setitem__(self, key, data):
        """Set a kv pair of (key, data)."""
        self.set(key, data)

    def __len__(self):
        """Return the number of items in table."""
        return self.count


def findbest(nums=None, loops=100, ht_size=500):
    """Try to find better values for the oat hash."""
    import random
    best_len_empty = 1000
    bestnums = None
    if nums is None:
        nums = [10, 6, 3, 11, 15]
    for i in range(loops):
        ht = HashTable(size=ht_size, hash_func='custom')
        ht.nums = nums
        for i in range(ht.size):
            ht.set('key' + str(i), i)
        len_empty = len([x for x in ht.buckets if len(x) == 0])
        if len_empty < best_len_empty:
            best_len_empty = len_empty
            bestnums = ht.nums[:]
        for idx, num in enumerate(ht.nums):
            if random.randint(0, 1):
                ht.nums[idx] -= random.randint(0, num)
            else:
                ht.nums[idx] += random.randint(0, 9)
        nums = ht.nums[:]
    return bestnums, best_len_empty


if __name__ == '__main__':  # pragma: no cover
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == 'test':

        ht_add = HashTable()
        ht_oat = HashTable(hash_func='oat')
        ht_fnv = HashTable(hash_func='fnv')
        for i in range(1024):
            ht_add.set('key' + str(i), i)
            ht_oat.set('key' + str(i), i)
            ht_fnv.set('key' + str(i), i)

        stats = []
        stats.append(len([x for x in ht_add.buckets if not x]))
        stats.append(len(max(ht_add.buckets, key=lambda x: len(x))))
        stats.append(len([x for x in ht_oat.buckets if not x]))
        stats.append(len(max(ht_oat.buckets, key=lambda x: len(x))))
        stats.append(len([x for x in ht_fnv.buckets if not x]))
        stats.append(len(max(ht_fnv.buckets, key=lambda x: len(x))))

        results = '''\nHash tables of size 1024, with 1024 key-value pairs:')
                 \n\nADDITIVE HASH:
                 \nEmpty buckets: {}
                 \nLargest bucket size: {}
                 \n\nONE AT A TIME:
                 \nEmpty buckets: {}
                 \nLargest bucket size: {}
                 \n\nFNV:
                 \nEmpty buckets: {}
                 \nLargest bucket size: {}\n'''
        print(results.format(*[x for x in stats]))
