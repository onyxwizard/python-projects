class CategoryList:
    def __init__(self, export_key=None):
        """
        Initialize the CategoryList with optional export_key for validation.
        """
        self.export_key = export_key  # Dependency injection for validation
        self.expense_categories = self.load_categories()  # Load predefined categories

    def load_categories(self):
        """
        Load the predefined expense categories.
        This can be extended to fetch data from a database or external source.
        """
        return {
            "Housing": {
                "Rent/Mortgage": [],
                "Utilities": ["Electricity", "Water", "Gas", "Internet", "Phone"],
                "Maintenance": ["Repairs", "Cleaning Supplies", "Gardening"],
                "Home Insurance": []
            },
            "Transportation": {
                "Public Transport": ["Bus", "Train", "Subway"],
                "Private Vehicle": ["Fuel", "Parking", "Tolls", "Maintenance", "Insurance"],
                "Ride Sharing": ["Uber", "Lyft"],
                "Vehicle Loan/Lease": []
            },
            "Food": {
                "Groceries": [],
                "Dining Out": ["Restaurants", "Cafes", "Fast Food"],
                "Snacks": []
            },
            "Healthcare": {
                "Insurance": [],
                "Doctor Visits": [],
                "Medications": [],
                "Fitness": ["Gym Membership", "Yoga Classes"]
            },
            "Personal Care": {
                "Haircuts": [],
                "Cosmetics": [],
                "Spa & Wellness": []
            },
            "Education": {
                "Tuition": [],
                "Books & Supplies": [],
                "Online Courses": []
            },
            "Entertainment": {
                "Streaming Services": ["Netflix", "Spotify", "Disney+"],
                "Movies & Events": ["Cinema", "Concerts", "Theater"],
                "Hobbies": []
            },
            "Shopping": {
                "Clothing": [],
                "Electronics": [],
                "Home Goods": [],
                "Gifts": []
            },
            "Travel": {
                "Flights": [],
                "Accommodation": [],
                "Local Transport": [],
                "Food & Activities": []
            },
            "Savings & Investments": {
                "Emergency Fund": [],
                "Retirement": [],
                "Stocks": [],
                "Cryptocurrency": []
            },
            "Debt Repayment": {
                "Credit Card Payments": [],
                "Loans": ["Student Loans", "Personal Loans"]
            },
            "Miscellaneous": {
                "Donations": [],
                "Pet Care": ["Food", "Vet Visits", "Toys"],
                "Other": []
            }
        }

    def display_top_level_categories(self):
        """
        Display only the top-level categories.
        :return: A list of top-level category names.
        """
        print("\nTop-Level Categories:")
        top_level_categories = list(self.expense_categories.keys())
        for index, category in enumerate(top_level_categories, start=1):
            print(f"[{index}] {category}")
        return top_level_categories

    def display_subcategories(self, category_name):
        """
        Display subcategories for a given top-level category.
        :param category_name: The name of the top-level category.
        :return: A dictionary of subcategories.
        """
        if category_name not in self.expense_categories:
            print(f"Category '{category_name}' does not exist.")
            return {}

        subcategories = self.expense_categories[category_name]
        print(f"\nSubcategories under '{category_name}':")
        for index, (subcat, items) in enumerate(subcategories.items(), start=1):
            print(f"[{index}] {subcat}")
            if isinstance(items, list) and items:
                for item in items:
                    print(f"  - {item}")
        return subcategories

    def get_category_by_index(self, categories, index):
        """
        Retrieve a category by its index.
        :param categories: A list or dictionary of categories.
        :param index: The 1-based index of the category.
        :return: The name of the category, or None if the index is invalid.
        """
        category_list = list(categories.keys()) if isinstance(categories, dict) else categories
        if 1 <= index <= len(category_list):
            return category_list[index - 1]
        return None