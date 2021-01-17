# Treasure

Treasure is a cli program that aims at providing a safe and fast method to encrypt and decrypt data



# Usage and Arguments

```bash
cli.py [-h] [-k] [-i INPUT] [-o OUTPUT] (-l | -u)
```



| optional argument      | description                                                      |
| ---------------------- | ---------------------------------------------------------------- |
| -h, --help             | show this help message and exit                                  |
| -k, --keep             | keep the original file when encrypting or decrypting from a file |
| -i FILE, --input FILE  | input file/directory path                                        |
| -o FILE, --output FILE | output file/directory path                                       |

| action argument | description     |
| --------------- | --------------- |
| -l, --lock      | encrypt content |
| -u, --unlock    | decrypt content |

# Demo

## Encryption

From stdin to stdout:

```bash
$ echo test|python cli.py -l
Enter treasure(s) password:
p2MSoYSBTInkBeAGOeGcWLQ2bFM4lR4vFE2qoDPJmd33z0skfWm0wmybtoHlwaHLZ9VD/joHHxgIV2nw
```



## Decryption

from stdin:

```bash
echo p2MSoYSBTInkBeAGOeGcWLQ2bFM4lR4vFE2qoDPJmd33z0skfWm0wmybtoHlwaHLZ9VD/joHHxgIV2nw|python cli.py -u
Enter stdin treasure password:
test
```