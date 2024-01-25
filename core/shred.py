import sys
import os

from .common import pprint, get_pattern


def _shred(file_path, pattern, passes, interactive=False):
	chunk_size = 2048

	if not interactive:
		pattern = get_pattern(pattern, chunk_size * passes)

	try:
		with open(file_path, "rb+") as file:
			for _ in range(passes):
				pattern = pattern[:chunk_size]
				while True:
					chunk = file.read(chunk_size)
					if not chunk:
						break
					file.seek(-len(chunk), os.SEEK_CUR)
					file.write(pattern * len(chunk))
	except OSError as e:
		pprint(f"Error {e} while overwriting file {file_path}", "red")
		sys.exit(1)


def shred_file(file_path, passes, overwriting_pattern, interactive=False):
	if not os.path.isfile(file_path):
		pprint(f"{file_path} either isn't a file or doesn't exist!", "red")
		sys.exit(1)

	_shred(file_path, overwriting_pattern, passes, interactive)


def shred_directory(dir_path, passes, overwriting_pattern, excluded_extensions=None, interactive=False):
	if not os.path.isdir(dir_path):
		pprint(f"{dir_path} either isn't a directory or doesn't exist!", "red")
		sys.exit(1)

	for subdir, dirs, files in os.walk(dir_path):
		for file in files:
			file_path = os.path.join(subdir, file)
			if excluded_extensions and any(file_path.lower().endswith(ext) for ext in excluded_extensions):
				continue
			_shred(file_path, overwriting_pattern, passes, interactive)


def shred_partition(partition, passes, overwriting_pattern, excluded_extensions=None, interactive=False):
	pass
