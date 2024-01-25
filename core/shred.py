import subprocess
import sys
import os

from .common import pprint, get_pattern


def overwrite_data(target_path, passes, overwriting_pattern, interactive=False, chunk_size=2048):
	"""
	Overwrite the content of the specified target.

	Args:
		target_path (str): The path to the target which will be overwritten.
		passes (int): The number of passes for overwriting.
		overwriting_pattern (str): The pattern to use for overwriting ('0', '1', 'r').
		interactive (bool, optional): Checks if script is in interactive mode.
		chunk_size (int, optional): The size of each chunk read and overwritten during overwriting.

	Raises:
		OSError: If an error occurs during file overwriting.
		SystemExit: If the script exits due to an error.
	"""

	if not interactive:
		pattern = get_pattern(overwriting_pattern, chunk_size * passes)
	else:
		pattern = overwriting_pattern

	try:
		with open(target_path, "rb+") as file:
			for _ in range(passes):
				pattern = pattern[:chunk_size]
				while True:
					chunk = file.read(chunk_size)
					if not chunk:
						break
					file.seek(-len(chunk), os.SEEK_CUR)
					file.write(pattern * len(chunk))
	except OSError as e:
		pprint(f"Error {e} while overwriting file {target_path}", "red")
		sys.exit(1)
	else:
		pprint(f"'{target_path}' shredded!", "green")


def shred_file(file_path, passes, overwriting_pattern, interactive=False):
	"""
	Shred a single file by overwriting its content.

	Args:
		file_path (str): The path of the file to be shredded.
		passes (int): The number of passes for overwriting.
		overwriting_pattern (str): The pattern to use for overwriting ('0', '1', 'r').
		interactive (bool, optional): Checks if script is in interactive mode.

	Raises:
		SystemExit: If the script exits due to an error.
	"""

	if not os.path.isfile(file_path):
		pprint(f"Error: File '{file_path}' doesn't exist!", "red")
		sys.exit(1)

	overwrite_data(file_path, passes, overwriting_pattern, interactive)


def shred_directory(dir_path, passes, overwriting_pattern, excluded_extensions=None, interactive=False):
	"""
	Shred all files in a directory recursively.

	Args:
		dir_path (str): The path to the directory to be shredded.
		passes (int): The number of passes for overwriting.
		overwriting_pattern (str): The pattern to use for overwriting ('0', '1', 'r').
		excluded_extensions (list, optional): List of file extensions to exclude from shredding.
		interactive (bool, optional): Checks if script is in interactive mode.

	Raises:
		SystemExit: If the script exits due to an error.
	"""

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


def shred_partition(partition_path):
	"""
	"""

	raise NotImplementedError
