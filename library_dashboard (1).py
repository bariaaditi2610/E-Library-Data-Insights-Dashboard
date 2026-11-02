import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class LibraryDashboard:
    def __init__(self):
        self.data = None

    def load_data(self, file_name):
        try:
            self.data = pd.read_csv(file_name)
            print("Data loaded successfully!")
        except FileNotFoundError:
            print("File not found!")
        except Exception as e:
            print("Error:", e)

    def calculate_statistics(self):
        if self.data is None:
            print("Please load the data first!")
            return
        d = self.data["Borrowing_Duration"]
        print("\n----- Statistics -----")
        print("Total Transactions:", len(d))
        print("Average Duration:", np.mean(d))
        print("Maximum Duration:", np.max(d))
        print("Minimum Duration:", np.min(d))
        print("Standard Deviation:", np.std(d))

    def filter_transactions(self):
        if self.data is None:
            print("Please load the data first!")
            return
        genre = input("Enter Genre: ")
        f = self.data[self.data["Genre"].str.lower() == genre.lower()]
        print(f if not f.empty else "No records found!")

    def generate_report(self):
        if self.data is None:
            print("Please load the data first!")
            return
        print(self.data.groupby("Genre")["Borrowing_Duration"].mean())

    def plot_bar_chart(self):
        self.data["Genre"].value_counts().plot(kind="bar")
        plt.title("Transactions by Genre")
        plt.show()

    def plot_line_graph(self):
        self.data["Date"] = pd.to_datetime(self.data["Date"])
        self.data.groupby("Date").size().plot()
        plt.title("Transactions by Date")
        plt.xticks(rotation=45)
        plt.show()

    def plot_pie_chart(self):
        self.data["Genre"].value_counts().plot(kind="pie", autopct="%1.1f%%")
        plt.ylabel("")
        plt.show()

    def plot_heatmap(self):
        h = self.data.pivot_table(values="Borrowing_Duration", index="Genre", aggfunc="mean")
        sns.heatmap(h, annot=True, cmap="YlGnBu")
        plt.show()

if __name__ == "__main__":
    library = LibraryDashboard()
    while True:
        print("\n1.Load Data\n2.Statistics\n3.Filter\n4.Report\n5.Bar Chart\n6.Line Graph\n7.Pie Chart\n8.Heatmap\n9.Exit")
        ch = input("Enter choice: ")
        if ch == "1":
            library.load_data(input("Enter CSV file name: "))
        elif ch == "2":
            library.calculate_statistics()
        elif ch == "3":
            library.filter_transactions()
        elif ch == "4":
            library.generate_report()
        elif ch == "5":
            library.plot_bar_chart()
        elif ch == "6":
            library.plot_line_graph()
        elif ch == "7":
            library.plot_pie_chart()
        elif ch == "8":
            library.plot_heatmap()
        elif ch == "9":
            break
        else:
            print("Invalid choice")
