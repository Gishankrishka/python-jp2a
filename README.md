# jp2a-python

> Python jp2a-like ASCII art converter with **image and video support**.
> Turn any image or video into stunning ASCII directly in your terminal, with optional color, high-res blocks, and HTML output.

---

## Features

* Convert images and videos to ASCII art.
* Supports **ANSI color** and **HTML output**.
* High-resolution Unicode half-block mode.
* Flip horizontally or vertically.
* Edge detection mode (`--edges-only`) for stylized ASCII.
* Terminal fullscreen mode with automatic resizing.
* Optional border and background fill for a polished look.
* Works with URLs, local files, or piped input.

---

## Installation

Install via **PyPI**:

```bash
pip install jp2a-python
```

Or install the latest from **GitHub**:

```bash
pip install git+https://github.com/YourUser/python-jp2a.git
```

---

## Quick Usage

```bash
# Convert an image to ASCII
jp2a image.png --width 100 --color

# Convert a video to ASCII in fullscreen high-res mode
jp2a video.mp4 --fullscreen --highres

# Get HTML output
jp2a image.png --html --width 80
```

---

## Example ASCII Output

**Original image:**

![Sample Image](https://via.placeholder.com/120x60.png?text=Image)

**ASCII Art Output:**

```
@@@@@@@@@@@@@@%%%%%****++++++++======:::::;;;;;,,..  
@@@@@@@@@@@@@@%%%%%****++++++++======:::::;;;;;,,..  
@@@@@@@%%%%%%%****++++++++======:::::;;;;;,,....   
%%%%%%%****++++++++======:::::;;;;;,,.....        
****++++++++======:::::;;;;;,,.....              
++++++++======:::::;;;;;,,.....                  
======:::::;;;;;,,.....                          
:::::;;;;;,,.....                                 
```

*High-res color mode will show the ASCII with vibrant terminal colors.*

---

## CLI Options

* `--width`, `--height`: Output dimensions in characters.
* `--color`: Enable terminal color.
* `--html`: Export ASCII to HTML format.
* `--charset`: Custom ASCII character set.
* `--invert`: Invert brightness.
* `--highres`: Use Unicode half-blocks (enables color automatically).
* `--fullscreen`: Fit the ASCII art to your terminal window.
* `--flipx`, `--flipy`: Flip horizontally or vertically.
* `--edges-only`: Show only edges.
* `--fill`: Fill background in color mode.
* `--border` or `-b`: Draw a border around the output.
* `--clear`: Clear the terminal before drawing.
* `--output` or `-o`: Save output to a file.
* `--version` or `-V`: Show the version.

---

## Video Playback

* Works with `.mp4`, `.avi`, `.mov`, `.mkv`, `.webm`.
* Press `Ctrl+C` to stop playback.
* Fullscreen mode automatically adjusts to your terminal size.

---

## Example Python Usage

You can also use it programmatically:

```python
from jp2a.core import convert_to_ascii

ascii_art = convert_to_ascii(
    "image.png",
    width=100,
    color=True,
    highres=True
)

print(ascii_art)
```

---

## License

MIT License © 2025 Gishan Krishka
[Telegram](https://t.me/KrishDev)

---

## Contribution

Contributions welcome! Open an issue or pull request on [GitHub](https://github.com/GishanKrishka/python-jp2a).

---

## Screenshot / Demo GIF (Optional)

Add a small GIF showing an image or video converting in the terminal—it makes it look super premium.
