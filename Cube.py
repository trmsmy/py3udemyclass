import unittest

class Cube() :

    def __init__(self, length):
        self.length = length

    def volume(self):
        return self.length ** 3

    def surface(self):
        return self.length ** 2 * 6



class CubeTest(unittest.TestCase):

    def setUp(self) -> None:
        self.c = Cube(3)

    def test_volume_and_surface(self):
        self.assertEqual(27, self.c.volume())
        self.assertEqual(54, self.c.surface())




if __name__ == "__main__":
    unittest.main()
