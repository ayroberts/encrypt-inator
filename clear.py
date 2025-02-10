# clears folders created by encryptinate and decryptinate
# that means be careful dawg

import os
import shutil

def clear(f):
    for r, d, files in os.walk(f, topdown=False):
        for file in files:
            os.remove(os.path.join(r, file))
        for dir in d:
            shutil.rmtree(os.path.join(r, dir))

if __name__ == "__main__":
    for folder in ["secret", "key", "vulnerable"]:
        if os.path.exists(folder):
            clear(folder)
