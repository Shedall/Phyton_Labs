import unittest
import sys
#sys.path.append("/home/floyk/Рабочий стол/IGI-Labs/Pyton4ik-labs/lab_3")
from data_test import my_func,my_func_2,factorial, my_decorator, for_dec, A, B,C
from Serialazer_Zakharanka_153505.xml_ser import XMLSerializer

class XMLTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.xml = XMLSerializer()
        
    def test_int(self):
        ser_obj = self.xml.dumps(12)
        des_obj = self.xml.loads(ser_obj)
        
        self.assertEqual(des_obj, 12)

    def test_float(self):
        ser_obj = self.xml.dumps(21.34)
        des_obj = self.xml.loads(ser_obj)

        self.assertEqual(des_obj, 21.34)

    def test_String(self):
        ser_obj = self.xml.dumps("Test")
        des_obj = self.xml.loads(ser_obj)

        self.assertEqual(des_obj, "Test")
        
    def test_list(self):
        ser_obj = self.xml.dumps([1, 2, [3, 5, "blue"], "pup"])
        des_obj = self.xml.loads(ser_obj)
        
        self.assertEqual(des_obj, [1, 2, [3, 5, "blue"], "pup"])

    def test_dict(self):
        ser_obj = self.xml.dumps({12: "Test"})
        des_obj = self.xml.loads(ser_obj)

        self.assertEqual(des_obj, {12: "Test"})

    def test_tuple(self):
        ser_obj = self.xml.dumps((1, 2, (34, 56), 3, "tru"))
        des_obj = self.xml.loads(ser_obj)

        self.assertEqual(des_obj, (1, 2, (34, 56), 3, "tru"))

    def test_set(self):
        ser_obj = self.xml.dumps({1, 2, 34.556, "tru"})
        des_obj = self.xml.loads(ser_obj)

        self.assertEqual(des_obj, {1, 2, 34.556, "tru"})

    def test_bytes(self):
        ser_obj = self.xml.dumps(bytes(range(10)))
        des_obj = self.xml.loads(ser_obj)

        self.assertEqual(des_obj, bytes(range(10)))

    def test_func(self):
        ser_obj = self.xml.dumps(my_func)
        des_obj = self.xml.loads(ser_obj)

        self.assertEqual(des_obj(5), my_func(5))

    def test_recurs_func(self):
        ser_obj = self.xml.dumps(factorial)
        des_obj = self.xml.loads(ser_obj)

        self.assertEqual(des_obj(5), factorial(5))

    def test_func_2(self):
        ser_obj = self.xml.dumps(my_func_2)
        des_obj = self.xml.loads(ser_obj)

        self.assertEqual(des_obj(1, 3, 4), my_func_2(1, 3, 4))
        
    def test_decorator(self):
        answ = my_decorator(for_dec)
        ser_obj = self.xml.dumps(my_decorator)
        des_obj = self.xml.loads(ser_obj)
        dec = des_obj(for_dec)
        
        self.assertEqual(answ(3), dec(3))
        
    def test_lambda(self):
        l = lambda b: b + 25
        ser_obj = self.xml.dumps(l)
        des_ob = self.xml.loads(ser_obj)
        
        self.assertEqual(l(2), des_ob(2))
        
    def test_static_method(self):
        ser_obj = self.xml.dumps(A)
        des_obj = self.xml.loads(ser_obj)
        
        self.assertEqual(des_obj.ret_bob(), A.ret_bob())
        
    def test_decorated_static_method(self):
        obj = B()
        ser_obj = self.xml.dumps(obj)
        des_obj = self.xml.loads(ser_obj)
        
        self.assertEqual(obj.another_method(5),des_obj.another_method(5))
        
    def test_method(self):
        obj = C()
        ser_obj = self.xml.dumps(obj)
        des_obj = self.xml.loads(ser_obj)
        
        self.assertEqual(obj.abobus(12), des_obj.abobus(12))

    def test_inheritance(self):
        obj = C()
        ser_obj = self.xml.dumps(obj)
        des_obj = self.xml.loads(ser_obj)

        self.assertEqual(obj.ret_bob(), des_obj.ret_bob())

    def test_class_metod(self):
        obj = A()
        ser_obj = self.xml.dumps(obj)
        des_obj = self.xml.loads(ser_obj)

        self.assertEqual(obj.ret_boby(), des_obj.ret_boby())
        
    def test_init(self):
        obj = C()
        ser_obj = self.xml.dumps(obj)
        des_obj = self.xml.loads(ser_obj)
        
        self.assertEqual(obj.coca, des_obj.coca)
        
        
if __name__ == "__main__":
    unittest.main()