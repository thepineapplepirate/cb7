

import json


def main():
    with open("sedtest.top", mode="rt") as f1:
        source_list = [line for line in f1.readlines()]

    with open("tip3p.top", mode="rt") as f2:
        insert_list = [line for line in f2.readlines()]

    pos = [i for i, line in enumerate(source_list) if '<[ system ]>' in line][0]
    source_list[pos: pos] = insert_list

    with open("sedtest.top", mode="wt") as f1:
        f1.write("".join(source_list))


if __name__ == "__main__":
    main()
