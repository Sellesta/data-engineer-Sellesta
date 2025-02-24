import unittest
import sys
import time
from src.lru_cache import LRUCache

class TestLRUCache(unittest.TestCase):
    def test_has_nonexistent_key(self):
        lru_cache = LRUCache[str, str](capacity=10)
        lru_cache.set("foo", "bar")
        self.assertFalse(lru_cache.has("bar"))
        self.assertFalse(lru_cache.has(""))

    def test_has_existing_key(self):
        lru_cache = LRUCache[str, str](capacity=10)
        lru_cache.set("foo", "bar")
        self.assertTrue(lru_cache.has("foo"))

    def test_has_expired_key(self):
        lru_cache = LRUCache[str, str](capacity=1)
        lru_cache.set("foo", "bar")
        lru_cache.set("baz", "bar")
        self.assertFalse(lru_cache.has("foo"))
        self.assertTrue(lru_cache.has("baz"))

    def test_has_remove_least_recently_used_key_when_lru_was_inserted_last(self):
        lru_cache = LRUCache[str, str](capacity=2)
        lru_cache.set("foo", "bar")
        lru_cache.set("bar", "bar")
        lru_cache.has("foo")
        lru_cache.set("baz", "bar")
        self.assertTrue(lru_cache.has("foo"))
        self.assertFalse(lru_cache.has("bar"))
        self.assertTrue(lru_cache.has("baz"))

    def test_has_remove_least_recently_used_key_when_lru_was_inserted_first(self):
        lru_cache = LRUCache[str, str](capacity=2)
        lru_cache.set("foo", "bar")
        lru_cache.set("bar", "bar")
        lru_cache.has("foo")
        lru_cache.has("bar")
        lru_cache.set("baz", "bar")
        self.assertFalse(lru_cache.has("foo"))
        self.assertTrue(lru_cache.has("bar"))
        self.assertTrue(lru_cache.has("baz"))

    def test_has_recreated_key_after_expiration(self):
        lru_cache = LRUCache[str, str](capacity=1)
        lru_cache.set("foo", "bar")
        lru_cache.set("baz", "bar")
        lru_cache.set("foo", "bar")
        self.assertTrue(lru_cache.has("foo"))

    def test_has_many_existing_keys(self):
        lru_cache = LRUCache[str, str](capacity=10)
        lru_cache.set("foo", "bar")
        lru_cache.set("baz", "bar")
        self.assertTrue(lru_cache.has("foo"))
        self.assertTrue(lru_cache.has("baz"))

    def test_get_nonexistent_key(self):
        lru_cache = LRUCache[str, str](capacity=10)
        lru_cache.set("foo", "bar")
        self.assertIsNone(lru_cache.get("bar"))
        self.assertIsNone(lru_cache.get(""))

    def test_get_existing_key(self):
        lru_cache = LRUCache[str, str](capacity=10)
        lru_cache.set("foo", "bar")
        self.assertEqual(lru_cache.get("foo"), "bar")

    def test_get_expired_key(self):
        lru_cache = LRUCache[str, str](capacity=1)
        lru_cache.set("foo", "bar")
        lru_cache.set("baz", "bar")
        self.assertIsNone(lru_cache.get("foo"))
        self.assertEqual(lru_cache.get("baz"), "bar")

    def test_get_remove_least_recently_used_key_when_lru_was_inserted_last_get(self):
        lru_cache = LRUCache[str, str](capacity=2)
        lru_cache.set("foo", "bar")
        lru_cache.set("bar", "bar")
        lru_cache.get("foo")
        lru_cache.set("baz", "bar")
        self.assertEqual(lru_cache.get("foo"), "bar")
        self.assertIsNone(lru_cache.get("bar"))
        self.assertEqual(lru_cache.get("baz"), "bar")

    def test_get_remove_least_recently_used_key_when_lru_was_inserted_last_has(self):
        lru_cache = LRUCache[str, str](capacity=2)
        lru_cache.set("foo", "bar")
        lru_cache.set("bar", "bar")
        lru_cache.has("foo")
        lru_cache.set("baz", "bar")
        self.assertEqual(lru_cache.get("foo"), "bar")
        self.assertIsNone(lru_cache.get("bar"))
        self.assertEqual(lru_cache.get("baz"), "bar")

    def test_get_remove_least_recently_used_key_when_lru_was_inserted_last_set(self):
        lru_cache = LRUCache[str, str](capacity=2)
        lru_cache.set("foo", "bar")
        lru_cache.set("bar", "bar")
        lru_cache.set("foo", "bar")
        lru_cache.set("baz", "bar")
        self.assertEqual(lru_cache.get("foo"), "bar")
        self.assertIsNone(lru_cache.get("bar"))
        self.assertEqual(lru_cache.get("baz"), "bar")

    def test_get_remove_least_recently_used_key_when_lru_was_inserted_first(self):
        lru_cache = LRUCache[str, str](capacity=2)
        lru_cache.set("foo", "bar")
        lru_cache.set("bar", "bar")
        lru_cache.get("foo")
        lru_cache.get("bar")
        lru_cache.set("baz", "bar")
        self.assertIsNone(lru_cache.get("foo"))
        self.assertEqual(lru_cache.get("bar"), "bar")
        self.assertEqual(lru_cache.get("baz"), "bar")

    def test_get_recreated_key_after_expiration(self):
        lru_cache = LRUCache[str, str](capacity=1)
        lru_cache.set("foo", "bar")
        lru_cache.set("baz", "bar")
        lru_cache.set("foo", "bar")
        self.assertEqual(lru_cache.get("foo"), "bar")
        self.assertIsNone(lru_cache.get("baz"))

    def test_get_many_existing_keys(self):
        lru_cache = LRUCache[str, str](capacity=10)
        lru_cache.set("foo", "foo")
        lru_cache.set("baz", "baz")
        self.assertEqual(lru_cache.get("foo"), "foo")
        self.assertEqual(lru_cache.get("baz"), "baz")

    def test_ttl_expired_key(self):
        lru_cache = LRUCache[str, str](capacity=1, ttl=0.1)
        lru_cache.set("foo", "bar")
        time.sleep(0.2)  # Wait for TTL to expire
        self.assertFalse(lru_cache.has("foo"))
        self.assertIsNone(lru_cache.get("foo"))

    def test_ttl_not_expired_key(self):
        lru_cache = LRUCache[str, str](capacity=1, ttl=1.0)
        lru_cache.set("foo", "bar")
        self.assertTrue(lru_cache.has("foo"))
        self.assertEqual(lru_cache.get("foo"), "bar")

    def test_ttl_mixed_expiration(self):
        lru_cache = LRUCache[str, str](capacity=2, ttl=0.2)
        lru_cache.set("foo", "bar")
        time.sleep(0.1)
        lru_cache.set("baz", "qux")
        time.sleep(0.15)  # foo should expire, baz should not
        self.assertFalse(lru_cache.has("foo"))
        self.assertTrue(lru_cache.has("baz"))

    def test_ttl_refresh_on_set(self):
        lru_cache = LRUCache[str, str](capacity=1, ttl=0.2)
        lru_cache.set("foo", "bar")
        time.sleep(0.1)
        lru_cache.set("foo", "bar2")  # Should refresh TTL
        time.sleep(0.15)  # Original TTL would have expired
        self.assertTrue(lru_cache.has("foo"))
        self.assertEqual(lru_cache.get("foo"), "bar2")

    def test_no_ttl(self):
        lru_cache = LRUCache[str, str](capacity=1)  # No TTL specified
        lru_cache.set("foo", "bar")
        time.sleep(0.2)
        self.assertTrue(lru_cache.has("foo"))
        self.assertEqual(lru_cache.get("foo"), "bar")

if __name__ == "__main__":
    unittest.main()
    sys.exit(0)