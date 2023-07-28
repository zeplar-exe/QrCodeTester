# QrCodeTester

A simple project to test .png QR codes.

## Usage

Notes:
- It is expected that these commands are run in the extracted QrCodeTester directory. 
Otherwise, main.py must be replaced by a absolute or relative path to it.
- File paths here can be relative or absolute.

**Testing multiple files**

An entire directory (and all of its subdirectories, recursively) can be tested like so;

`py main.py -a DIR_PATH`

**Testing singular files**

Likewise, a single file can be tested like so;

`py main.py -s FILE_PATH`