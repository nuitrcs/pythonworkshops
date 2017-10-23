#The shebang line in any script determines the script's ability to be executed like an standalone executable without typing python beforehand in the terminal or when double clicking it in a file manager(when configured properly). It isn't necessary but generally put there so when someone sees the file opened in an editor, they immediately know what they're looking at. However, which shebang line you use IS important; Correct usage is

#using env gives maximum flexibility in that the user can select the interpreter to use by changing the PATH. Often this flexibility is not required though and the downside is that linux for example can't use the script name for the name of the process in ps and reverts to "python". When packaging python apps for distros for example I would advise not to use env

#If you have several versions of Python installed, /usr/bin/env will ensure the interpreter used is the first one on your environment's $PATH. The alternative would be to hardcode something like #!/usr/bin/python; that's ok, but less flexible.
#In Unix, an executable file that's meant to be interpreted can indicate what interpreter to use by having a #! at the start of the first line, followed by the interpreter (and any flags it may need).
#If you're talking about other platforms, of course, this rule does not apply (but that "shebang line" does no harm, and will help if you ever copy that script to a platform with a Unix base, such as Linux, Mac, etc).

#In computing, a shebang (also called a hashbang, hashpling, pound bang, or crunchbang) refers to the characters "#!" when they are the first two characters in an interpreter directive as the first line of a text file. In a Unix-like operating system, the program loader takes the presence of these two characters as an indication that the file is a script, and tries to execute that script using the interpreter specified by the rest of the first line in the file.

#/usr/bin/env python
#/usr/bin/python
#/usr/local/bin/python
#python

#python

import math

print(math.sqrt(4))
