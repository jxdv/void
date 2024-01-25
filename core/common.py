import secrets
import sys

PATTERN_DICT = {
	"0": b"0",
	"1": b"1",
}


class Colors:
	"""
	ANSI escape sequences for console text colors.
	"""

	RESET = "\033[0m"
	RED = "\033[91m"
	GREEN = "\033[92m"
	YELLOW = "\033[93m"


def pprint(msg, color):
	"""
	Print a formatted message with the specified color.

	Args:
		msg (str): The message to be printed.
		color (str): The color to use for printing.

	Raises:
		KeyError: If the specified color is not defined in Colors.
	"""

	color_code = getattr(Colors, color.upper(), "")
	if color_code:
		print(color_code + msg + Colors.RESET)
	else:
		print(msg)


def get_pattern(overwriting_pattern, chunk_size=2048):
	"""
	Get the overwriting pattern based on the user's choice.

	Args:
		overwriting_pattern (str): The user-specified overwriting pattenr ('0', '1', 'r')
		chunk_size (int): The size of the data chunk when generating a random pattern.

	Returns:
		bytes: The selected overwriting pattern.

	Raises:
		KeyError: If the specified overwriting pattern is not recognized.
	"""

	try:
		if overwriting_pattern == "r":
			return secrets.token_bytes(chunk_size)
		return PATTERN_DICT[overwriting_pattern]
	except KeyError:
		pprint("Error: Wrong overwriting pattern!", "red")
		sys.exit(1)
