# `simpletimer.py`

A simple MATLAB-like timing utility.  Example:

```
from simpletimer import tic, toc

...

tic()
call_something_expensive()
toc()
```

It is [not the "right" way to do this][so_dicussion], but may be
helpful for quick 'n dirty time measurement.

[so_discussion]: http://stackoverflow.com/questions/5849800/tic-toc-functions-analog-in-python "Stack Overflow discussion"

