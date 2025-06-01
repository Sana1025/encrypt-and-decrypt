Caesar Cipher GUI

A simple Python-based GUI application to encrypt and decrypt text using the Caesar Cipher algorithm. This version supports letters, numbers, symbols, and all printable ASCII characters, with an easy-to-use graphical interface built using Tkinter.

How It Works   

The Caesar Cipher is a substitution cipher where each character is shifted by a certain number of positions in the character set.

This program:

=>Uses ord() and chr() to shift characters within ASCII printable range.

=>Wraps around using modulo % 127 to stay within bounds.

=>Includes encryption & decryption logic in a simple GUI.


✅ Prerequisites:

Python 3.x installed

