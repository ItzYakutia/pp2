import os

pa = os.getcwd()

print(f"Existence check: {os.access(pa + '/test.py', os.F_OK)}")
print(f"Readability check: {os.access(pa, os.R_OK)}")
print(f"Writability check: {os.access(pa, os.W_OK)}")
print(f"Executability check: {os.access(pa, os.X_OK)}")