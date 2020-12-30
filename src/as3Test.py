
import sys
import subprocess

if __name__ == '__main__':
        for i in ['a', 'b','c','d','e']:
            print(f"\n\ntesting exercise {i}")
            subprocess.call(['python', 'cs_1807572.py', i])
