import pytest
from app.calc import Calculator

class TestCals:

    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 10, 2) == 12

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 5, 1) == 4

    def test_multiply_success(self):
        assert self.calc.multiply(self, 3, 4) == 12

    def test_division_success(self):
        assert self.calc.division(self, 10, 2) == 5

    def teardown(self):
        print('Выполнение метода Teardown')