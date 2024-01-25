import argparse
import sys
import os

from .shred import shred_file, shred_directory, shred_partition
from .interactive import run
from .common import pprint


def parse_args():
	parser = argparse.ArgumentParser(
		description="Securely shred sensitive data to maximize your privacy.",
		epilog="Created by: github.com/jxdv"
	)
	parser.add_argument(
		"-i",
		"--interactive",
		action="store_true",
		help="Run void in interactive mode"
	)
	parser.add_argument(
		"-f",
		"--file",
		help="Path to file which will be shredded"
	)
	parser.add_argument(
		"-r",
		"--recursive",
		help="Path to directory which contents of will be shredded recursively"
	)
	parser.add_argument(
		"-p",
		"--passes",
		type=int,
		default=3,
		help="How many times to overwrite the file"
	)
	parser.add_argument(
		"-pr",
		"--partition",
		help="Partition name which will be shredded"
	)
	parser.add_argument(
		"-ee",
		"--exclude-extensions",
		nargs="+",
		help="File extensions to ignore"
	)
	parser.add_argument(
		"-ow",
		"--overwrite-pattern",
		choices=["0", "1", "r"],
		help="Data overwriting pattern to use"
	)
	args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])

	return args

def cli():
	args = parse_args()

	if args.overwrite_pattern and not (args.file or args.recursive or args.partition):
		pprint("Error: -ow has to be used with -f / -r / -pr", "red")
		sys.exit(1)

	if args.exclude_extensions and not (args.recursive or args.partition):
		pprint("Error: -ee arg can only be used along with -r / -pr", "red")
		sys.exit(1)

	if args.interactive:
		try:
			run()
		except (KeyboardInterrupt, EOFError):
			pprint("\nInterrupted, exiting..", "yellow")
			try:
				sys.exit(130)
			except SystemExit:
				os._exit(130)

	if args.file:
		shred_file(args.file, args.passes, args.overwrite_pattern)

	if args.recursive:
		shred_directory(args.recursive, args.passes, args.overwrite_pattern, excluded_extensions=args.exclude_extensions)

	if args.partition:
		raise NotImplementedError
		#shred_partition(args.partition, args.passes, args.overwrite_pattern, excluded_extensions=args.exclude_extensions)
