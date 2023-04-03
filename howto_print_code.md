This follows the [tutorial](https://www.codementor.io/@carltashian/print-out-your-code-on-paper-w4pespmdn) by Carl Tashian

Basically, using the `enscript` program from command line. One has to use the following command
```bash
enscript -1rG --line-numbers -p out.ps --highlight=python -c inputfile.py
```

Enscript has a lot of options. Here are the most valuable options:

+ `-1 -2 -3 -4` number of columns per page
+ `-r` rotate (landscape mode)
+ `-G` fancy header (with filename, date & time)
+ `--color=1` if you have a color printer
+ `-w` html if you want HTML output instead of PostScript
+ `--help-highlight` will show which languages have syntax highlighting available
