# dealRaw
Do you worry about the big RAW file to occupy disk space？
Deal with the RAW file is spending too much time？
The tool will Deal with the rating too low raw file and delete it,and help you save time

How to use:
Use Lightroom or other photo editor to rating for your photo
Build 'raw' folder and move your raw file to 'raw' folder
Use below command to deal with your raw file:
- python dealRaw.py //will use current path.
- python dealRaw.py path //use indicate the path.


The raw file delete Rule:
- Rating small than 4 will delete.
- JPG file doesn't exist will delete.