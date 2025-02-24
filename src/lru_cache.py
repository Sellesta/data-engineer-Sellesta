from typing import TypeVar, Generic, Optional
from collections import OrderedDict
import time

# Type Variables
KT = TypeVar('KT')  # Key Type
VT = TypeVar('VT')  # Value Type

class LRUCache(Generic[KT, VT]):
    def __init__(self, capacity: int, ttl: Optional[float] = None):
        """
        Initialize LRU Cache
        
        Args:
            capacity: Maximum number of items in cache
            ttl: Time to live in seconds for cache items (None means no expiration)
        """
        self.capacity = capacity
        self.ttl = ttl
        self.cache = OrderedDict()
        self.timestamps = {}  # Stores insertion timestamps for TTL handling

    def has(self, key: KT) -> bool:
        """
        Args:
            key: The key to look up
            
        Returns:
            True or False
        """
        if key in self.cache:
            if self._is_expired(key):
                self._remove(key)
                return False
            self.cache.move_to_end(key)  # Mark as recently used
            return True
        return False
    
    def get(self, key: KT) -> Optional[VT]:
        """
        Args:
            key: The key to look up
            
        Returns:
            The value associated with the key, or None
        """
        if key in self.cache:
            if self._is_expired(key):
                self._remove(key)
                return None
            self.cache.move_to_end(key)  # Mark as recently used
            return self.cache[key]
        return None
            
    def set(self, key: KT, value: VT) -> None:
        """        
        Args:
            key: The key to store
            value: The value to store
        """
        if key in self.cache:
            self.cache.move_to_end(key)  # Mark as recently used
        elif len(self.cache) >= self.capacity:
            self._evict()
        
        self.cache[key] = value
        self.timestamps[key] = time.time()
    
    def _evict(self):
        """Remove the least recently used item from the cache."""
        oldest_key, _ = self.cache.popitem(last=False)
        self.timestamps.pop(oldest_key, None)
    
    def _is_expired(self, key: KT) -> bool:
        """Check if a key has expired based on TTL."""
        if self.ttl is None:
            return False
        return (time.time() - self.timestamps.get(key, 0)) > self.ttl
    
    def _remove(self, key: KT):
        """Remove a key from the cache and timestamps."""
        self.cache.pop(key, None)
        self.timestamps.pop(key, None)
