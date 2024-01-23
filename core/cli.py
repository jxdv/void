import argparse
import sys

from .shred import shred_file, shred_directory


def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("-f", "--file", help="Path to file which will be overwritten")
	parser.add_argument("-r", "--recursive", help="Path to directory which contents of will be overwritten recursively")
	parser.add_argument("-p", "--passes", type=int, default=3, help="How many times to overwrite the file")
	parser.add_argument("-ee", "--exclude-extensions", nargs="+", help="File extensions to ignore")
	args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])

	return args

def cli():
	args = parse_args()

	if args.file:
		shred_file(args.file, args.passes)

	if args.recursive:
		shred_directory(args.recursive, args.passes, excluded_extensions=args.exclude_extensions)

	if args.exclude_extensions and not args.recursive:
		sys.stderr.write("-ee arg can only be used along with -r\n")
		sys.exit(1)
