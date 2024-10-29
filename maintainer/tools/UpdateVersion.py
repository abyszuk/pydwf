#! /usr/bin/env python3

import argparse
import re


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--update-version", type=str)
    args = parser.parse_args()

    update_version = args.update_version

    if not re.match(r"^[0-9]+(?:\.[0-9]+)*$", update_version):
        raise ValueError("Bad version string: {!r}".format(update_version))

    replacements = {
        "../../setup.cfg"                      : "version = $VERSION",
        "../../source/pydwf/__init__.py"       : "__version__ = \"$VERSION\"",
        "../../documentation/source/conf.py"   : "release = '$VERSION'",
        "../../README.md"                      : "The current release of *pydwf* is version $VERSION."
    }

    for (filename, linespec) in replacements.items():
        regexp_str = "^" + linespec.replace(".", r"\.").replace("*", r"\*").replace("$VERSION", r"[0-9]+(?:\.[0-9]+)*") + "$"
        regexp = re.compile(regexp_str)
        changed = False
        with open(filename, "r") as fi:
            lines = []
            for line in fi:
                if regexp.match(line):
                    if update_version is not None:
                        line_changed = linespec.replace("$VERSION", update_version) + "\n"
                    print("file {}:".format(filename))
                    print("    found ........... : {}".format(line.rstrip()))
                    if update_version is not None:
                        print("    changed to ...... : {}".format(line_changed.rstrip()))
                    if update_version is not None:
                        line = line_changed
                        changed = True
                lines.append(line)
            print()

        if changed:
            with open(filename, "w") as fo:
                fo.write("".join(lines))


if __name__ == "__main__":
    main()
