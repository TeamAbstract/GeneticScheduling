import sys

if sys.version_info < (3, 0):
	raise EnvironmentError("Outdated version update to V3")
else:
	print("System check fine")
