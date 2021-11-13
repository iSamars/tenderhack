from main.parser import read_csv

if __name__ == "__main__":
    with open("stu.csv", "r") as file:
        read_csv(file)