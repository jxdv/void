import sys
import os

from .common import pprint, get_pattern


def overwrite_data(file_path, passes, overwriting_pattern, interactive=False):
	chunk_size = 2048

	if not interactive:
		pattern = get_pattern(overwriting_pattern, chunk_size * passes)
	else:
		pattern = overwriting_pattern

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
		pprint(f"Error: File '{file_path}' doesn't exist!", "red")
		sys.exit(1)

	overwrite_data(file_path, passes, overwriting_pattern, interactive)


def shred_directory(dir_path, passes, overwriting_pattern, excluded_extensions=None, interactive=False):
	if not os.path.exists(dir_path):
		pprint(f"Error: Directory '{dir_path}' doesn't exist!", "red")
		sys.exit(1)

	if not os.path.isdir(dir_path):
		pprint(f"Error: '{dir_path}' isn't a directory!", "red")
		sys.exit(1)

	for subdir, dirs, files in os.walk(dir_path):
		for file in files:
			file_path = os.path.join(subdir, file)
			if excluded_extensions and any(file_path.lower().endswith(ext) for ext in excluded_extensions):
				continue
			overwrite_data(file_path, passes, overwriting_pattern, interactive)


def shred_partition(partition, passes, overwriting_pattern, excluded_extensions=None, interactive=False):
	pass
