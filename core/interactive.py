import sys

from .shred import shred_file, shred_directory, shred_partition
from .common import pprint, get_pattern


def print_logo():
	pprint(r"""
                       __     
                __    /\ \    
 __  __    ___ /\_\   \_\ \   
/\ \/\ \  / __`\/\ \  /'_` \  
\ \ \_/ |/\ \L\ \ \ \/\ \L\ \ 
 \ \___/ \ \____/\ \_\ \___,_\
  \/__/   \/___/  \/_/\/__,_ /
                              
	""", "cyan")


def shred_single_file(passes, pattern):
	file_path = input("Enter file path:\nvoid> ")
	shred_file(file_path, passes, pattern, interactive=True)	


def shred_single_dir(passes, pattern, excluded_extensions):
	dir_path = input("Enter directory path:\nvoid> ")
	shred_directory(dir_path, passes, pattern, excluded_extensions, interactive=True)


def shred_single_partition(passes, pattern, excluded_extensions):
	partition = input("Partition name:\nvoid> ")
	shred_partition(partition, passes, pattern, excluded_extensions)


def view_shredding_config(passes, pattern, excluded_extensions):
	print("-"*70)
	print(f"Overwriting pattern: {pattern if pattern in [b'0', b'1'] else 'random bytes'}")
	print(f"File passes: {passes}")
	print(f"Excluded extensions (only used in recursive approach): {excluded_extensions}")
	print("-"*70)


def configure_shredding():
	print("Configure shredding options:")
	pattern_choice = input("Enter data overwriting pattern: (0/1/r)\nvoid> ").lower()
	overwriting_pattern = get_pattern(pattern_choice)

	try:
		passes = int(input("Enter Number of Passes (default is 3):\nvoid> ") or 3)
	except ValueError:
		pprint("Wrong data type!", "red")
		sys.exit(1)

	excluded_extensions_choice = input("Enter excluded extensions (comma-separated, leave empty for none):\nvoid> ")
	excluded_extensions_arr = excluded_extensions_choice.split(",") if excluded_extensions_choice else None

	return overwriting_pattern, passes, excluded_extensions_arr

def menu():
	pattern, passes, excluded_extensions = configure_shredding()

	choices = {
		1: lambda: shred_single_file(passes, pattern),
		2: lambda: shred_single_dir(passes, pattern, excluded_extensions),
		3: lambda: shred_single_partition(passes, pattern, excluded_extensions),
		4: lambda: view_shredding_config(passes, pattern, excluded_extensions),
		5: sys.exit
	}

	while True:
		print("""
1 - Shred a single file
2 - Shred a directory recursively
3 - Shred a partition recursively
4 - View shredding config
5 - Exit
		""")

		try:
			choice = int(input("void> "))
			if choice not in list(range(1, 6)):
				pprint("Wrong choice!", "red")
				sys.exit(1)
		except ValueError:
			pprint("Wrong data type!", "red")
			sys.exit(1)
		else:
			action = choices.get(choice)
			action()


def run():
	print_logo()
	menu()
