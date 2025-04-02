import sys
import os
import unittest
from unittest.mock import patch
from datetime import datetime
# Add the 'src' directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from input_handler import ExpenseManager

class TestInputHandler(unittest.TestCase):
    def setUp(self):
        """
        Set up a fresh instance of ExpenseManager before each test.
        """
        self.expense_manager = ExpenseManager()

    # === Test Cases for amount_validation ===

    def test_amount_validation_valid_input(self):
        """
        Test valid amount input.
        """
        with patch('builtins.input', return_value="100"):
            result = self.expense_manager.amount_validation()
            self.assertEqual(result, 100)

    def test_amount_validation_negative_input(self):
        """
        Test negative amount input.
        """
        with patch('builtins.input', return_value="-50"):
            with self.assertRaises(ValueError):  # Expect an exception after max retries
                self.expense_manager.amount_validation()

    def test_amount_validation_non_numeric_input(self):
        """
        Test non-numeric amount input.
        """
        with patch('builtins.input', return_value="abc"):
            with self.assertRaises(ValueError):  # Expect an exception after max retries
                self.expense_manager.amount_validation()

    def test_amount_validation_too_many_invalid_attempts(self):
        """
        Test too many invalid attempts for amount validation.
        """
        with patch('builtins.input', side_effect=["-1", "xyz", "-999"]):  # Three invalid inputs
            with self.assertRaises(ValueError):  # Expect an exception after max retries
                self.expense_manager.amount_validation()

    # === Test Cases for date_validation ===

    def test_date_validation_valid_input(self):
        """
        Test valid date input.
        """
        today = datetime.now().strftime("%Y-%m-%d")
        with patch('builtins.input', return_value=today):
            result = self.expense_manager.date_validation()
            self.assertEqual(result, today)

    def test_date_validation_future_date(self):
        """
        Test future date input.
        """
        future_date = "2050-01-01"
        with patch('builtins.input', return_value=future_date):
            with self.assertRaises(ValueError):  # Expect an exception after max retries
                self.expense_manager.date_validation()

    def test_date_validation_invalid_format(self):
        """
        Test invalid date format.
        """
        with patch('builtins.input', return_value="01-01-2023"):  # Incorrect format
            with self.assertRaises(ValueError):  # Expect an exception after max retries
                self.expense_manager.date_validation()

    def test_date_validation_too_many_invalid_attempts(self):
        """
        Test too many invalid attempts for date validation.
        """
        future_date = "2050-01-01"
        with patch('builtins.input', side_effect=[future_date, "abc", "xyz"]):  # Three invalid inputs
            with self.assertRaises(ValueError):  # Expect an exception after max retries
                self.expense_manager.date_validation()

    # === Test Cases for description_validation ===

    def test_description_validation_valid_input(self):
        """
        Test valid description input.
        """
        with patch('builtins.input', return_value="Groceries"):
            result = self.expense_manager.description_validation()
            self.assertEqual(result, "Groceries")

    def test_description_validation_invalid_length(self):
        """
        Test invalid description length (too short or too long).
        """
        with patch('builtins.input', side_effect=["A", "ThisIsTooLong", "AnotherInvalidInput"]):
            with self.assertRaises(ValueError):  # Expect an exception after max retries
                self.expense_manager.description_validation()

    def test_description_validation_invalid_characters(self):
        """
        Test invalid characters in the description.
        """
        with patch('builtins.input', side_effect=["Groceries123", "Groceries!", "Invalid@Input"]):
            with self.assertRaises(ValueError):  # Expect an exception after max retries
                self.expense_manager.description_validation()

    def test_description_validation_too_many_invalid_attempts(self):
        """
        Test too many invalid attempts for description validation.
        """
        with patch('builtins.input', side_effect=["A", "Groceries123", "Groceries!"]):  # Three invalid inputs
            with self.assertRaises(ValueError):  # Expect an exception after max retries
                self.expense_manager.description_validation()

    # === Test Cases for select_category ===

    @patch('src.input_handler.CategoryList.display_top_level_categories', return_value=["Food", "Transportation"])
    @patch('src.input_handler.CategoryList.get_category_by_index', side_effect=lambda categories, index: categories[index - 1])
    @patch('src.input_handler.CategoryList.display_subcategories', return_value={"Groceries": [], "Dining Out": []})
    def test_select_category_valid_input(self, mock_subcategories, mock_get_category, mock_top_level):
        """
        Test valid category selection.
        """
        with patch('builtins.input', side_effect=["1", "1"]):  # Select Food > Groceries
            result = self.expense_manager.select_category()
            self.assertEqual(result, "Food > Groceries")

    @patch('src.input_handler.CategoryList.display_top_level_categories', return_value=["Food", "Transportation"])
    @patch('src.input_handler.CategoryList.get_category_by_index', side_effect=lambda categories, index: None)
    def test_select_category_invalid_input(self, mock_get_category, mock_top_level):
        """
        Test invalid category selection.
        """
        with patch('builtins.input', side_effect=["99", "100", "999"]):  # Three invalid inputs
            with self.assertRaises(ValueError):  # Expect an exception after max retries
                self.expense_manager.select_category()


if __name__ == "__main__":
    unittest.main()