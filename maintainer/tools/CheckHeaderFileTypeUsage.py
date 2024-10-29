#! /usr/bin/env python3

from collections import Counter

from pydwf.core.auxiliary.dwf_function_signatures import dwf_function_signatures


def report_type_usage():

    class typespec_count_attributes:
        def __init__(self):
            self.counter = Counter()

        def __getattr__(self, name):
            self.counter[name] += 1

    typespec = typespec_count_attributes()

    function_signatures = dwf_function_signatures(typespec)

    print("API summary: types used in API function signatures")
    print("==================================================")
    print()

    for (index, (name, num_occurrences)) in enumerate(typespec.counter.most_common(), 1):
        print("{:2}  {:37}  {:3}".format(index, name, num_occurrences))

    print()


def main():
    report_type_usage()


if __name__ == "__main__":
    main()
