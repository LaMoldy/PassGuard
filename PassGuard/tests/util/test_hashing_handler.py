from utils import HashingHandler

class TestHashingHandler:
    def test_hashing(self):
        input = "abc123"
        hash = HashingHandler.hash(input)
        assert input != hash

    def test_compare_hash_true(self):
        input = "abc123"
        hash = HashingHandler.hash(input)
        assert HashingHandler.compare_hash(input, hash)

    def test_compare_hash_false(self):
        input = "abc123"
        hash = HashingHandler.hash("def456")
        assert not HashingHandler.compare_hash(input, hash)
