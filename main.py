from fileinput import filename
import sys


def convert(file, delimeter=''):
    file = file.read().split('\n')
    # print(file)

    content = []

    for item in file:
        item = item.strip().split(delimeter)
        item[-1], item[-2] = item[-2], item[-1]
        content.append(" ".join(item))
    return content


def main():
    if len(sys.argv) > 3:
        input_file = sys.argv[1]
        delimeter = sys.argv[2]
        output_file = sys.argv[3]

        with open(input_file) as file:
            data = convert(file, delimeter=delimeter)
            with open(output_file, "w") as file:
                for i in data:
                    print(i)
                    file.write(i)
                file.flush()
    else:
        print(
            f"[ERROR] Enter input with: python main.py [filename] [delimeter]")


if __name__ == '__main__':
    main()