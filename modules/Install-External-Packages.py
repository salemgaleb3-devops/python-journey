#####   Modules  =>>  install external packages    ######3
## [1] modules vs package
## [2] external packages download from the internet
## [3] you can install package with python package manager PIP
## [4] PIP install the package and its dependency
## [5] module list "https://docs.python.org/3/py-modindex.html"
## [6] package and modules directory "https://pypi.org/"
## [7] PIP manual "https://pip.pypa.io/en/stable/reference/pip_install/"
####################################################################################33
### in terminal $ pip -- versin   $ pip list  $pip install

import pyfiglet, termcolor

print(pyfiglet.figlet_format("SALEM"))
print(termcolor.colored(pyfiglet.figlet_format("SALEM"), color="blue", force_color=True))

