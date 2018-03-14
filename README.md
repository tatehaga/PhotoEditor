# PhotoEditor
* Command line image randomizer built on Python3
* Supports BMP, PNG, JPG, TIFF with RGB and RGBA channels

### Usage:

main.py [-h] filename [-o OUTPUT] [-v] [-ns] [-nd] [-r RANDOMNESS] 

~~~
>> chmod +x main.py
>> main.py truck.png
~~~
Files save as {input_filename}\_RandomNoise_{randomnessvalue}.{input_filetype} (unless -o flag is used)


### Commands:

commands | usage
------|--------
-r, -\-randomness | changes the color values of a given pixel by this value (±)
-v, -\-verbose | returns information about the provided file
-o, -\-output | name of output file
-ns, -\-nosave | runs without saving a copy to memory
-nd, -\-nodisplay | runs without displaying both the input and altered file
-h, -\-help | displays help message and exits
