from typing import TypeVar, Generic, Optional
from collections import OrderedDict

"""
A Least Recently Used (LRU) cache keeps items in the cache until it reaches its size
and/or item limit (only item in our case). In which case, it removes an item that was accessed
least recently.
An item is considered accessed whenever `has`, `get`, or `set` is called with its key.
Items can also expire based on their TTL (Time To Live) if specified.

Implement the LRU cache here and use the unit tests to check your implementation.
"""

# Type Variables
KT = TypeVar('KT')  # Key Type
VT = TypeVar('VT')  # Value Type

# TODO: Implement the LRUCache class
class LRUCache(Generic[KT, VT]):
    def __init__(self, capacity: int, ttl: Optional[float] = None):
        self.capacity = capacity
        self.ttl = ttl
        self.cache = OrderedDict() # we using the OrderedDict for LNU tracking

    def has(self, key: KT) -> bool:
        return key in self.cache
    
    def get(self, key: KT) -> Optional[VT]:
        if key not in self.cache:
            return None
        self.cache.move_to_end(key) # move to end on mostly used
        return self.cache[key]
            
    def set(self, key: KT, value: VT) -> None:
        if key in self.cache:
            self.cache.move_to_end(key) #update existing item's position
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False) # remove the least recently used item
        