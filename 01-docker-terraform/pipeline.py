import pandas as pd
import sys

print(sys.argv)


def get_date(args_date):
    print(f"args date is: {args_date}")


def main():
    day = sys.argv[1]
    get_date(day)


if __name__ == '__main__':
    main()
