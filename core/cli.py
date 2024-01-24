import argparse
import sys

from .shred import shred_file, shred_directory
from .interactive import run


def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("-i", "--interactive", action="store_true", help="Run void in interactive mode")
	parser.add_argument("-f", "--file", help="Path to file which will be overwritten")
	parser.add_argument("-r", "--recursive", help="Path to directory which contents of will be overwritten recursively")
	parser.add_argument("-p", "--passes", type=int, default=3, help="How many times to overwrite the file")
	parser.add_argument("-ee", "--exclude-extensions", nargs="+", help="File extensions to ignore")
	parser.add_argument("-ow", "--overwrite-pattern", choices=["zeroes", "ones", "random"], help="Data overwriting pattern to use")
	args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])

	return args

def cli():
	args = parse_args()

	if args.interactive:
		run()

	if args.overwrite_pattern and not (args.file or args.recursive):
		sys.stderr.write("-ow has to be used with -f or -r\n")
		sys.exit(1)

	if args.exclude_extensions and not args.recursive:
		sys.stderr.write("-ee arg can only be used along with -r\n")
		sys.exit(1)

	if args.file:
		shred_file(args.file, args.passes, args.overwrite_pattern)

	if args.recursive:
		shred_directory(args.recursive, args.passes, args.overwrite_pattern, excluded_extensions=args.exclude_extensions)
