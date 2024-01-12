About
======================
A simple python script for sorting the current user's DOWNLOADS directory 
into folders corresponding to the extenstions of each file found in that directory.
(Windows 11)

The script only organizes top-level files in the directory.
(sub-directories and files within the sub-directories are ignored.)

**Disclaimer #1**: The script was only tested on machines running Windows OS.
Compatibility with other major operating systems is not guaranteed.
Use at your own risk.

**Disclaimer #2**: It is the user's responsibility to ensure that sorting any directory,
the default DOWNLOADS directory or otherwise, will not break something on their machine 
prior to executing the script.

Getting Started
======================

The default usage for the script is to sort the DOWNLOADS directory for a logged in user
operating on a Windows machine. Using the script without parameters will result in the user 
being asked if they are sure they would like to sort the downloads folder.

The confirmation dialog as well as the path being sorted can both be changed via the program's
command-line arguments as detailed in the **Path Argument (-p, --path)** and **No Dialog (-nd, --no_dialog)** sections.

**Default (No arguments)**
```
$ python DownloadOrganizerService.py
```

Path Argument (-p, --path)
---------------------

Using the path argument, the user is able to change the path where sorting occurs when
the script is executed.

**Path Arguments**
```
-p, --path
```

See example for usage:

`Path: C:\Users\developer\Documents\example`

**Command-line**
```
$ python DownloadOrganizerService.py -p C:\Users\developer\Documents\example
```

**Before Execution**
```
Structure: Documents\example\
                              example_text.txt
                              example_PDF.pdf
                              example_DOC.docx
```
**After Execution**
```
Structure: Documents\example\
                              TXT\example_text.txt
                              PDF\example_PDF.pdf
                              DOCX\example_DOC.docx
```

No Dialog Argument (-nd, --no_dialog)
---------------------

For safety purposes, the script by default will prompt the user with a dialog to confirm 
that they are sure that they want to sort whatever the current path is set as (either the 
default DOWNLOADS path or what is set in the path argument) after being executed.

This ensures that the user has a second change to review the currently set path. And if the incorrect path is selected, 
the user will have a chance to fix it before sorting the directory and possibly messing something up.

For automation purposes, the `no dialog` argument is provided so that a user
could in theory run the script periodically via some method without having the
confirmation dialog being prompted for each execution.

**No Dialog Arguments**
```
-nd, --no_dialog
```

**Command-line**
```
$ python DownloadOrganizerService.py -nd
```



