import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class RetailAnalyzer:
    def __init__(self):
        self.data = None

    # 1. Load Data
    def load_data(self, practicalexam):
        try:
            if not practicalexam.endswith(".csv"):
                print(" Please provide a CSV file.")
                return

            self.data = pd.read_csv(practicalexam)

            # Check required columns
            required_cols = ["Date", "Product", "Category", "Price", "Quantity Sold", "Total Sales"]
            for col in required_cols:
                if col not in self.data.columns:
                    print(f"Missing column: {col}")
                    return

            # Convert Date column
            self.data["Date"] = pd.to_datetime(self.data["Date"])

            print("Data loaded successfully!")

        except Exception as e:
            print(" Error loading file:", e)

    # 2. Calculate Metrics
    def calculate_metrics(self):
        if self.data is None:
            print(" No data loaded.")
            return

        total_sales = self.data["Total Sales"].sum()
        avg_sales = self.data["Total Sales"].mean()

        # Most popular product
        popular_product = self.data.groupby("Product")["Quantity Sold"].sum().idxmax()

        print("\n SALES METRICS")
        print("Total Sales:", total_sales)
        print("Average Sales:", round(avg_sales, 2))
        print("Most Popular Product:", popular_product)

    # 3. Filter Data
    def filter_data(self):
        if self.data is None:
            print("No data loaded.")
            return

        print("\nFilter Options:")
        print("1. By Category")
        print("2. By Date Range")

        choice = input("Enter choice: ")

        if choice == "1":
            category = input("Enter category: ")
            filtered = self.data[self.data["Category"] == category]
            print(filtered)

        elif choice == "2":
            start = input("Start date (YYYY-MM-DD): ")
            end = input("End date (YYYY-MM-DD): ")

            filtered = self.data[
                (self.data["Date"] >= start) &
                (self.data["Date"] <= end)
            ]
            print(filtered)

        else:
            print("Invalid choice")

    # 4. Display Summary
    def display_summary(self):
        if self.data is None:
            print("No data loaded.")
            return

        print("\nDATA SUMMARY")
        print(self.data.describe())
        print("\nMissing Values:\n", self.data.isnull().sum())

    # 5. Data Visualization
    def visualize_data(self):
        if self.data is None:
            print("No data loaded.")
            return

        while True:
            print("\nVisualization Menu")
            print("1. Bar Chart (Sales by Category)")
            print("2. Line Graph (Sales Over Time)")
            print("3. Heatmap (Correlation)")
            print("4. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                sales_by_cat = self.data.groupby("Category")["Total Sales"].sum()
                sales_by_cat.plot(kind='bar')
                plt.title("Total Sales by Category")
                plt.xlabel("Category")
                plt.ylabel("Sales")
                plt.show()

            elif choice == "2":
                sales_trend = self.data.groupby("Date")["Total Sales"].sum()
                sales_trend.plot()
                plt.title("Sales Trend Over Time")
                plt.xlabel("Date")
                plt.ylabel("Sales")
                plt.show()

            elif choice == "3":
                corr = self.data[["Price", "Quantity Sold", "Total Sales"]].corr()
                sns.heatmap(corr, annot=True)
                plt.title("Correlation Heatmap")
                plt.show()

            elif choice == "4":
                break

            else:
                print("Invalid choice")


# -------- MAIN PROGRAM -------- #

def main():
    analyzer = RetailAnalyzer()

    while True:
        print("\n====== Retail Sales Data Analyzer ======")
        print("1. Load Data")
        print("2. Calculate Metrics")
        print("3. Filter Data")
        print("4. Display Summary")
        print("5. Visualize Data")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            path = input("Enter CSV file path: ")
            analyzer.load_data(path)

        elif choice == "2":
            analyzer.calculate_metrics()

        elif choice == "3":
            analyzer.filter_data()

        elif choice == "4":
            analyzer.display_summary()

        elif choice == "5":
            analyzer.visualize_data()

        elif choice == "6":
            print("Exiting program...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()