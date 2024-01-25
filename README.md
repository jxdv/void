# void

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

----

## Install

```shell
$ git clone https://github.com/jxdv/void.git && cd void/
$ chmod +x install.sh
$ ./install.sh
```

## Usage

```shellSession
$ void -h
usage: void [-h] [-i] [-f FILE] [-r RECURSIVE] [-p PASSES] [-pr PARTITION]
               [-ee EXCLUDE_EXTENSIONS [EXCLUDE_EXTENSIONS ...]] [-ow {0,1,r}]

options:
  -h, --help            show this help message and exit
  -i, --interactive     Run void in interactive mode
  -f FILE, --file FILE  Path to file which will be shredded
  -r RECURSIVE, --recursive RECURSIVE
                        Path to directory which contents of will be shredded
                        recursively
  -p PASSES, --passes PASSES
                        How many times to overwrite the file
  -pr PARTITION, --partition PARTITION
                        Partition name which will be shredded
  -ee EXCLUDE_EXTENSIONS [EXCLUDE_EXTENSIONS ...], --exclude-extensions EXCLUDE_EXTENSIONS [EXCLUDE_EXTENSIONS ...]
                        File extensions to ignore
  -ow {0,1,r}, --overwrite-pattern {0,1,r}
                        Data overwriting pattern to use
```

## Examples

<b>Run interactively</b>

```shell
$ void -i
```

<b>Overwrite with random bytes</b>

```shell
$ void -f file.txt -ow r
```

<b>Overwrite file 10 times with zeroes</b>

```shell
$ void -f file.txt -ow 0 -p 10
```

<b>Recursively overwrite directory with ones</b>

```shell
$ void -r target_dir/ -ow 1
```

<b>Ignore files with .c and .o extensions</b>

```shell
$ void -r target_dir/ -ow 1 -ee .c .o
```
