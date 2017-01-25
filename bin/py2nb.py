#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from pathlib import Path
import nbformat as nb
from nbformat import v3


def main(file, output, version):
    text = file.read_text()
    input = v3.reads_py(text)
    notebook = nb.convert(input, version)
    with open(str(output), 'w') as out:
        nb.write(notebook, out)
    print("Write {}".format(output))


if __name__ == "__main__":
    descr = "Convert python script to jupyter/ipython notebook"
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('file', type=str)
    parser.add_argument('--output', '-o', type=str)
    parser.add_argument('--version', '-v', type=int, default=4)
    args = parser.parse_args()
    f = Path(args.file).resolve()
    if not args.output:
        output = "{}.ipynb".format(Path(f.name).stem)
        output = f.parent / output

    main(f, output, args.version)
