from gendiff.get_difference import get_difference

from gendiff.generate_diff import generate_diff


def main():
    args = get_difference()
    generate_diff(args.first_argument, args.second_argument)
    result = generate_diff()
    print(result)


if __name__ == "__main__":
    main()
