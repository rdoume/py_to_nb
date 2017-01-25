# Installation

## Using pip

Installation using `pip`

```bash
pip install https://github.com/chicham/py2nb.git
```

# Usage

## Default

Once installed a script name `py2nb.py` is added to your PATH. Just type

```bash
py2nb.py myscript.py
```

To generate a `myscript.ipynb` readable by jupyter.

## With output name

```bash
py2nb.py myscript.py -o name.ipynb
```


## With ipython/jupyter version specification

```bash
py2nb.py myscript.py -v 3
```

To generate a notebook compatible with the version 3 of the ipython API. By default the version 4 is used.


# Python file

In order to be converted the python source file some comments must be add to the source file.

## Markdown block

```python
# <markdowncell>
# My text in
# the markdowncell
```

## Raw block

```python
# <rawcell>
# A raw cell
```

## Code block

```python
# <codecell>

from numpy.random import randint

randint(0, 5, (3, 5))
```
