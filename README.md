# File Info Inspector

A Python tool to extract and display complete file information for digital forensics investigations.

## What it does

- Displays file name, extension, and size
- Shows creation and modification timestamps
- Calculates SHA256 hash for evidence integrity
- Detects real file type based on magic bytes, not just the extension

## Why magic bytes matter in forensics

Every file type has a unique sequence of bytes at the beginning, called magic bytes. A JPEG always starts with FF D8 FF. A PDF always starts with %PDF.

If someone renames malware.exe to photo.jpg, the operating system sees an image, but the magic byte reveals the truth. This tool catches that.

## Why it matters in forensics

Before analyzing any evidence, an investigator must document exactly what the file is, its identity, when it was last touched, and a hash to prove it was not altered. This tool automates that first step.

## Requirements

- Python 3

## Usage

python file_info_inspector.py

Options:
  [1] Inspect a file
  [0] Exit

When prompted, enter the full path of the file:

Windows: C:\Users\your-username\Downloads\file.jpg
Mac: /Users/your-username/Downloads/file.jpg

## Output example

  File      : teste.jpg
  Extension : .jpg
  Type      : JPEG Image
  Size      : 7.77 KB

  Created   : 2026-08-06 14:30:00
  Modified  : 2026-08-06 14:30:00

  SHA256    : 6bfdabd4fc33d112283c147acccc574e770bbe6fbdbc3d4da968ba7b606ecc2f