# FCPX Chapter Marker Extractor

This tool extracts chapter markers from Final Cut Pro X (.fcpxml) files and outputs the markers as a formatted list of chapters. The tool can be used as a standalone Python script or as a Quick Action on macOS.

## Table of Contents

- [Requirements](#requirements)
- [Using the Python Script](#using-the-python-script)
- [Using the Quick Action on macOS](#using-the-quick-action-on-macos)
- [Installing the Quick Action](#installing-the-quick-action)
- [Troubleshooting](#troubleshooting)

## Requirements

- Python 3 (tested on Python 3.10)
- macOS (for the Quick Action)

## Using the Python Script

To use the Python script, follow these steps:

1. Clone or download this repository.

2. Open Terminal.

3. Navigate to the directory containing the script:

cd /path/to/script_directory

4. Run the script, providing the path to your .fcpxml file as an argument:

python3 fcpx_chapter_extractor.py /path/to/your/file.fcpxml

The script will parse the .fcpxml file and output the extracted chapter markers in the following format:

Chapters:  
00:00 Chapter 1   
00:22 Chapter 2   
01:30 Chapter 3   
...

## Using the Quick Action on macOS

The Quick Action allows you to extract chapter markers directly from the context menu in Finder.

1. Install the Quick Action (see [Installing the Quick Action](#installing-the-quick-action) below).

2. In Finder, right-click on a .fcpxml file.

3. In the context menu, go to "Quick Actions" and select the FCPX Chapter Marker Extractor Quick Action.

The chapter markers will be extracted and copied to the clipboard, allowing you to paste them into another application or YouTube video directly.

## Installing the Quick Action

To install the Quick Action on macOS, follow these steps:

1. Clone or download this repository.

2. Double-click on the exported Quick Action file (Get-FCPX-Chapters.workflow) to open it in Automator.

3. In Automator, click "Install" to install the Quick Action.

The Quick Action is now installed and ready to use.

## Troubleshooting

If you encounter any issues while using the script or the Quick Action, please check the following:

- Ensure you're using Python 3. The script may not work correctly with older versions of Python.
- Make sure the path to the .fcpxml file is correct when running the script.
- If using the Quick Action, ensure that the Quick Action is installed correctly and that the Python script is accessible on your system.

If you still encounter issues, please open a GitHub issue or contact the repository maintainer for assistance.
