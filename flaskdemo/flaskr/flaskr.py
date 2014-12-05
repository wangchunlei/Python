# all the imports
from subprocess import check_output
import os

out = check_output(["mkdir wangcl"], shell=True)

print out
