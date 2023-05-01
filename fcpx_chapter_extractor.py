import xml.etree.ElementTree as ET
import argparse
import os
import subprocess

def get_time_from_offset(offset_str):
    if offset_str and 's' in offset_str:
        numerator = offset_str.split('/')[0] if '/' in offset_str else offset_str.rstrip('s')
        denominator = offset_str.split('/')[1].rstrip('s') if '/' in offset_str else 1
        time_in_seconds = int(numerator) / int(denominator)
        return time_in_seconds
    else:
        return None

def format_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    if hours > 0:
        return "{:02d}:{:02d}:{:02d}".format(int(hours), int(minutes), int(seconds))
    else:
        return "{:d}:{:02d}".format(int(minutes), int(seconds))

def parse_fcpxml(file_path):
    # Load and parse the XML data
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Find all asset-clips
    asset_clips = root.findall(".//asset-clip")
    markers_list = []

    for asset_clip in asset_clips:
        # Find the corresponding 'chapter-marker' which is a child of this 'asset-clip'
        chapter_marker = asset_clip.find(".//chapter-marker")
        if chapter_marker is not None:
            value = chapter_marker.attrib.get('value')
            offset_str = asset_clip.attrib.get('offset')
            offset_seconds = get_time_from_offset(offset_str)
            if offset_seconds is not None:
                formatted_offset = format_time(offset_seconds)
                markers_list.append((formatted_offset, value))

    return markers_list

def format_chapters_to_clipboard(chapters):
    formatted_chapters = "Chapters:\n"
    for offset, value in chapters:
        formatted_chapters += "{} {}\n".format(offset, value)

    # Copy to clipboard (MacOS specific)
    process = subprocess.Popen('pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(formatted_chapters.encode())

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', help='The filepath of the .fcpxml file')
    args = parser.parse_args()

    chapters = parse_fcpxml(args.filepath)
    format_chapters_to_clipboard(chapters)

if __name__ == "__main__":
    main()
