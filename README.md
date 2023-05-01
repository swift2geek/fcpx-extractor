#  fcpx-extractor

### command line tool to extract chapters from Final Cut Pro xml files.

### Tested and worked on macos Ventura 13.2.1 with system python3 

## Usage
- Download fcpx_chapter_extractor.py 
- Open a terminal window and navigate to the directory where the fcpx_chapter_extractor.py file is saved.
- Run the following command to extract the chapters from an FCPX XML file:

```
python3 fcpx_chapter_extractor.py /Users/swift2geek/Desktop/Amsterdam.fcpxml
```
Replace "/Users/swift2geek/Desktop/France.fcpxml" with the path to the FCPX XML file you want to extract the chapters from.
There is Example file Amsterdam.fcpxml you can try on this on. 
You need to extract from Final Cut Pro markers in previous version 1.09, because new version is not an XML but a folder. 

- The app will output the name and start time of each chapter in the FCPX XML file.
