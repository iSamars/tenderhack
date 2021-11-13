from main.parser import parse_category, parse_stu, test

if __name__ == "__main__":
    with open("stu.csv", "r", encoding='utf-8') as file:
        # parse_category(file)
        parse_stu(file)
        # test()