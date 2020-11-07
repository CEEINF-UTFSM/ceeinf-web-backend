from django.test import TestCase
from hashlib import sha3_256
from ..validators import validate_length


class TestHashingValidation(TestCase):

    def setUp(self) -> None:
        pass

    def test_correct_validation(self):
        new_str = sha3_256()
        new_str.update(b"ayy lmao")
        self.assertEqual(validate_length(new_str.hexdigest()), new_str.hexdigest())

    def test_failure(self):
        new_str = "eso es una locura? ESTO ES UNA LOCURA KJLADSLKJKJLADSKJL"
        with self.assertRaises(ValueError):
            validate_length(new_str)
