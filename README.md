# dealRaw
Do you worry about the big RAW file to occupy disk space？

Deal with the RAW file is spending too much time？

The tool will Deal with the rating too low raw file and delete it,and help you save time.

### Environment:
- Install python 2.7
- pyexiv2, a python binding to exiv2 - https://goo.gl/Qp3E1

### How to use:
Use Lightroom or other photo editor to rating for your photo
Build 'raw' folder and move your raw file to 'raw' folder
Use below command to deal with your raw file:
- python dealRaw.py //will use current path.
- python dealRaw.py path //use indicate the path.

### Wdindows:
- dowload https://github.com/oknow23/dealRaw/raw/master/dist/dealRaw.exe
- Put dealRaw.exe and photos in the same folder and double click to execute it.

### The raw file delete Rule:
- Rating small than 4 will delete.
- Correspondece JPG file doesn't exist and will delete.

### The result like below:

		Find raw file:DSCF4882 - Copy
		Delete not exist G:\arrangeRawFile\dist\raw\DSCF4882 - Copy.raw


		Find raw file:DSCF4882
		G:\arrangeRawFile\dist\DSCF4882.jpg
		Photo Rating: None
		Delete low rating file: G:\arrangeRawFile\dist\raw\DSCF4882.raw

		Find raw file:DSCF5162-fix
		G:\arrangeRawFile\dist\DSCF5162-fix.jpg
		Photo Rating: 5
		請按任意鍵繼續 . . .


### Reffer:
odinho/gmg_localfiles: GNU MediaGoblin plugin for importing files from your filesystem without duplication. - https://goo.gl/G10TnJ
