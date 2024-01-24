import secrets
import sys
import os

PATTERN_DICT = {
	"zeroes": b"0",
	"ones": b"1",
}


def _get_pattern(overwriting_pattern, chunk_size):
	try:
		if overwriting_pattern == "random":
			return secrets.token_bytes(chunk_size)
		return PATTERN_DICT[overwriting_pattern]
	except KeyError:
		raise ValueError("Error occurred while choosing an overwriting pattern.")


def _shred(file_path, pattern, passes):
	chunk_size = 2048
	pass_pattern = _get_pattern(pattern, chunk_size * passes)

	try:
		with open(file_path, "rb+") as file:
			for _ in range(passes):
				pattern = pass_pattern[:chunk_size]
				while True:
					chunk = file.read(chunk_size)
					if not chunk:
						break
					file.seek(-len(chunk), os.SEEK_CUR)
					file.write(pattern * len(chunk))
	except OSError as e:
		raise OSError(f"Error {e} while overwriting file {file_path}")


def shred_file(file_path, passes, overwriting_pattern):
	if not os.path.isfile(file_path):
		raise FileNotFoundError(f"{file_path} either isn't a file or It doesn't exist!")

	_shred(file_path, overwriting_pattern, passes)


def shred_directory(dir_path, passes, overwriting_pattern, excluded_extensions=None):
	if not os.path.isdir(dir_path):
		raise NotADirectoryError(f"{dir_path} isn't a directory!")

	for subdir, dirs, files in os.walk(dir_path):
		for file in files:
			file_path = os.path.join(subdir, file)
			if excluded_extensions and any(file_path.lower().endswith(ext) for ext in excluded_extensions):
				continue
			_shred(file_path, overwriting_pattern, passes)
