from gendiff.get_difference import helper

from gendiff.generate_diff import generate_diff


def main():
    args = helper()
    result = generate_diff(args.first_argument, args.second_argument, args.format)
    print(result)


if __name__ == "__main__":
    main()
