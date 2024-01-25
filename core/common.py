import secrets
import sys

PATTERN_DICT = {
	"0": b"0",
	"1": b"1",
}


class Colors:
	RESET = "\033[0m"
	RED = "\033[91m"
	GREEN = "\033[92m"
	CYAN = "\033[96m"
	YELLOW = "\033[93m"


def pprint(msg, color):
	color_code = getattr(Colors, color.upper(), "")
	if color_code:
		print(color_code + msg + Colors.RESET)
	else:
		print(msg)


def get_pattern(overwriting_pattern, chunk_size=2048):
	try:
		if overwriting_pattern == "r":
			return secrets.token_bytes(chunk_size)
		return PATTERN_DICT[overwriting_pattern]
	except KeyError:
		print(Colors.RED + "Wrong overwriting pattern!" + Colors.RESET)
		sys.exit(1)
