import unittest

#Push pen state machine

class PushPen():

    brand = "Reynolds"

    def __init__(self, clr):
        self.tip_out = False
        self.color = clr
        print("Creating a " + clr + " pen !!")

    def push_pin(self):
        self.tip_out = not self.tip_out
        #print("Tip is out" if self.tip_out else "Tip is inside")

    def write(self):
        #print("push pin before writing....." if not self.tip_out else "ready to write .... ")
        return self.tip_out






### Tests

class PushPenTest(unittest.TestCase):


    def setUp(self):
        print("Runing -> ",  self._testMethodName)
        self.p = PushPen("green")

    def test_default_state(self):
        self.assertEqual("green", self.p.color)
        self.assertFalse(self.p.tip_out, "Tip should be inside when Pen is created")

    def test_one_push_ready_to_write(self):
        self.p.push_pin()
        self.assertTrue(self.p.tip_out, "One push should bring the tip out")

    def test_two_push_not_ready_to_write(self):
        self.p.push_pin()
        self.p.push_pin()
        self.assertFalse(self.p.tip_out, "Two push resets the tip back inside")


    def test_change_to_static_var_affects_all_objects(self):
        p1 = PushPen
        p2 = PushPen

        self.assertEqual("Reynolds", p1.brand)
        self.assertEqual("Reynolds", p2.brand)

        p2.brand = "Brand 2"

        self.assertEqual("Brand 2", p1.brand)
        self.assertEqual("Brand 2", p2.brand)

    def tearDown(self) -> None:
        pass


if __name__ == "__main__":
    unittest.main()