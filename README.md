rainbowbb
======
This Python script generates BBCode in rainbows.

How to use
======

TBD

Command-line arguments
======

**-b, --bounce**

>Sets **bounce** in rainbowbb.**colorize** to **True**.

**-c <CYCLENAME>, --cycle=<CYCLENAME>**

>Sets **cycle** in rainbowbb.**colorize** to **<CYCLENAME>**.

**-r, --reverse**

>Sets **reverse** in rainbowbb.**colorize** to **True**.

**-s <SIZE>, --size=<SIZE>**

>Sets **size** in rainbowbb.**size** to **<SIZE>**.

**-w, --by-word**

>Sets **by_char** in rainbowbb.**colorize** to **False**.

Methods
======

**rainbowbb**

>This is the main module.

rainbowbb.**cycles**

>This is a dictionary that contains preset color cycles for RainbowBB. Each
cycles is in the form of a tuple containing strings that represent hexadecimal
color codes. Currently, the preset cycles are "pastel" (default), "hard",
"grayscale", "fail", and "desaturated".

rainbowbb.**colorize**(text, cycle="pastel", reverse=False, by_char=True, bounce=False)

>This function takes a string as an argument and returns a copy with BBCode
[color] tags applied to it. If **text** is not a string, the function returns
**None**. **cycle** denotes the desired cycle; if a given cycle does not
exist, the function will return **None** and print out a list of valid cycles.
**reverse** is self-explanatory; it loads the cycle in reverse order.
**by_char** is the default behavior; if **False**, the cycle will apply to
individual words, not characters. **bounce** causes the cycle to reverse
upon reaching its end instead of starting over again.

rainbowbb.**size**(text, size=None)

>This function takes a string as an argument and returns a copy with BBCode
[size] tags applied to it. **size** denotes the desired size; if **None**,
the program simply returns the original string. 

Licensing
======
License is contained in the source code.
