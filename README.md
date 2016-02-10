ninekey
=======

A barebones hotkey/launcher application

Dependencies
------------

* python3
* pyqt5

Configuration
-------------

When you first run ninekey, an empty config file will be created in ~/.config/ninekey/ .

Odd numbered lines are the names of the commands to launch. These names will be displayed on the buttons.
Even numbered lines are the commands to run.

For example:

```
Launch Firefox
firefox
Compile
gcc ~/myproject/myprogram.c
```

will produce:

![ninekey screenshot](http://i.imgur.com/PbZV4rV.png)
