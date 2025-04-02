import pandas as pd
import matplotlib.pyplot as plt
from storage import StorageManager


class VisualizationManager:
    def __init__(self, storage_manager=None):
        """
        Initialize the VisualizationManager with a StorageManager instance.
        :param storage_manager: An instance of StorageManager for loading expenses.
        """
        self.storage_manager = storage_manager or StorageManager()

    def load_expenses(self):
        """
        Load expenses from storage.
        :return: A list of expense dictionaries, or None if no expenses are found.
        """
        expenses = self.storage_manager.load_expenses()
        if not expenses:
            print("No expenses found.")
            return None
        return expenses

    def process_monthly_totals(self, expenses):
        """
        Process expenses to group them by month and calculate totals for the current year.
        :param expenses: A list of expense dictionaries.
        :return: A pandas DataFrame containing months and their total amounts.
        """
        df = pd.DataFrame(expenses)
        df["Amount"] = df["Amount"].astype(float)
        df["Date"] = pd.to_datetime(df["Date"])  # Convert Date column to datetime
        df["Year-Month"] = df["Date"].dt.to_period("M").astype(str)  # Extract YYYY-MM

        # Filter for the current year (or the most recent year in the data)
        current_year = df["Date"].dt.year.max()  # Get the most recent year
        df = df[df["Date"].dt.year == current_year]

        # Group by month and sum amounts
        monthly_totals = (
            df.groupby("Year-Month")["Amount"]
            .sum()
            .reindex([f"{current_year}-{str(i).zfill(2)}" for i in range(1, 13)], fill_value=0)
            .reset_index()
        )
        monthly_totals.columns = ["Month", "Total Amount"]
        return monthly_totals

    def plot_monthly_spending(self, monthly_totals):
        """
        Generate and display a bar chart of total expenses by month for the year.
        :param monthly_totals: A pandas DataFrame containing months and their total amounts.
        """
        plt.figure(figsize=(10, 6))
        colors = plt.cm.Blues(range(len(monthly_totals)))  # Use a colormap for distinct colors
        bars = plt.bar(monthly_totals["Month"], monthly_totals["Total Amount"], color=colors)

        plt.title(f"Monthly Spending for {monthly_totals['Month'][0][:4]}", fontsize=16)
        plt.xlabel("Month", fontsize=12)
        plt.ylabel("Amount ($)", fontsize=12)
        plt.xticks(rotation=45, ha="right", fontsize=10)
        plt.grid(axis="y", linestyle="--", alpha=0.7)

        # Add value labels on top of bars
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2, height + 5, f"${height:.2f}", ha="center", fontsize=10)

        plt.tight_layout()
        plt.show()

    def visualize_expenses(self):
        """
        Visualize monthly spending for the whole year.
        """
        # Step 1: Load expenses
        expenses = self.load_expenses()
        if not expenses:
            return

        # Step 2: Process expenses for monthly totals
        monthly_totals = self.process_monthly_totals(expenses)

        # Step 3: Plot the visualization
        print("\n=== Visualizing Monthly Spending for the Year ===")
        self.plot_monthly_spending(monthly_totals)