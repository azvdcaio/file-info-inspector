import os
import hashlib
import datetime
import struct

def color(text, code):
    return f"\033[{code}m{text}\033[0m"

def calculate_sha256(path):
    sha256 = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

def detect_file_type(path):
    signatures = {
        b'\xff\xd8\xff': 'JPEG Image',
        b'\x89PNG': 'PNG Image',
        b'GIF8': 'GIF Image',
        b'%PDF': 'PDF Document',
        b'PK\x03\x04': 'ZIP Archive',
        b'MZ': 'Windows Executable',
        b'\x7fELF': 'Linux Executable',
        b'RIFF': 'WAV Audio / AVI Video',
        b'\x00\x00\x00\x18': 'MP4 Video',
        b'ID3': 'MP3 Audio',
    }

    with open(path, "rb") as f:
        header = f.read(16)

    for signature, filetype in signatures.items():
        if header.startswith(signature):
            return filetype

    return "Unknown / Plain Text"

def format_size(size):
    if size < 1024:
        return f"{size} bytes"
    elif size < 1024 * 1024:
        return f"{size / 1024:.2f} KB"
    else:
        return f"{size / (1024 * 1024):.2f} MB"

def inspect_file(path):
    try:
        stat = os.stat(path)
    except FileNotFoundError:
        print(color("\n  ✗ File not found. Check the path and try again.\n", "1;31"))
        return

    filename = os.path.basename(path)
    extension = os.path.splitext(filename)[1] or "No extension"
    size = format_size(stat.st_size)
    created = datetime.datetime.fromtimestamp(stat.st_ctime).strftime("%Y-%m-%d %H:%M:%S")
    modified = datetime.datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
    filetype = detect_file_type(path)
    sha256 = calculate_sha256(path)

    print("\n" + color("="*60, "36"))
    print(color("       FILE INFO INSPECTOR — Forensic Tool", "1;36"))
    print(color("="*60, "36"))
    print(f"  {color('File      :', '33')} {filename}")
    print(f"  {color('Extension :', '33')} {extension}")
    print(f"  {color('Type      :', '33')} {filetype}")
    print(f"  {color('Size      :', '33')} {size}")
    print(color("-"*60, "36"))
    print(f"  {color('Created   :', '33')} {created}")
    print(f"  {color('Modified  :', '33')} {modified}")
    print(color("-"*60, "36"))
    print(f"  {color('SHA256    :', '32')} {sha256}")
    print(color("="*60, "36") + "\n")

def menu():
    print("\n" + color("="*60, "36"))
    print(color("       FILE INFO INSPECTOR — Forensic Tool", "1;36"))
    print(color("="*60, "36"))
    print(f"  {color('[1]', '33')} Inspect a file")
    print(f"  {color('[0]', '33')} Exit")
    print(color("-"*60, "36"))

while True:
    menu()
    option = input(color("  Choose an option: ", "36"))

    if option == "1":
        path = input(color("  Enter file path: ", "33"))
        inspect_file(path)

    elif option == "0":
        print(color("\n  Exiting. Stay sharp.\n", "36"))
        break

    else:
        print(color("\n  ✗ Invalid option. Try again.\n", "1;31"))