import sys
import os


def _shred(file_path):
	pass


def shred_file(file_path, passes):
	is_file = os.path.isfile(file_path)
	file_exists = os.path.exists(file_path)
	if not (is_file or file_exists):
		sys.stderr.write(f"{file_path} either isn't a file or it doesn't exist!\n")
		sys.exit(1)


def shred_directory(dir_path, passes, excluded_extensions):
	if not os.path.isdir(dir_path):
		sys.stderr.write(f"{dir_path} isn't a directory!\n")
		sys.exit(1)

	for subdir, dirs, files in os.walk(dir_path):
		for file in files:
			file_path = os.path.join(subdir, file)
			if any(file_path.lower().endswith(ext) for ext in excluded_extensions):
				continue
			else:
				print(file_path)