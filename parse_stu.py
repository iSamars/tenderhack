from main.parser import parse_category, parse_stu, parse_contracts

if __name__ == "__main__":
    with open("contracts.csv", "r", encoding='utf-8') as file:
        # parse_category(file)
        # parse_stu(file)
        parse_contracts(file)