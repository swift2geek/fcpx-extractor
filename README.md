#  fcpx-extractor

### command line tool to extract chapters from Final Cut Pro xml files.

### Tested and worked on macos Ventura 13.2.1 with system ruby 
ruby 2.6.10p210 (2022-04-12 revision 67958) [universal.arm64e-darwin22]

## Usage
- Download fcpx_chapter_extractor.rb 
- Open a terminal window and navigate to the directory where the fcpx_chapter_extractor.rb file is saved.
- Run the following command to extract the chapters from an FCPX XML file:

```
ruby fcpx_chapter_extractor.rb /Users/swift2geek/Desktop/France.fcpxml
```
Replace "/Users/swift2geek/Desktop/France.fcpxml" with the path to the FCPX XML file you want to extract the chapters from.

- The app will output the name and start time of each chapter in the FCPX XML file.
