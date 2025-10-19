# jp2a-python

<img width="500" height="500" alt="atGPT Image Aug 20, 2025, 07_09_35 PM" src="https://github.com/user-attachments/assets/a9fad732-07e3-47ed-ad36-4d8cf81f476f" />

> Python jp2a-like ASCII art converter with **image and video support** including **synchronized audio playback**.
> Turn any image or video into stunning ASCII directly in your terminal, with optional color, high-res blocks, and HTML output.

---

## Features

* Convert images and videos to ASCII art.
* **Automatic audio playback** for videos (runs in background thread).
* Supports **ANSI color** and **HTML output**.
* High-resolution Unicode half-block mode.
* Flip horizontally or vertically.
* Edge detection mode (`--edges-only`) for stylized ASCII.
* Terminal fullscreen mode with automatic resizing.
* Optional border and background fill for a polished look.
* Works with URLs, local files, or piped input.

---

## Installation

### Step 1: Install Python Package

Install the latest from **GitHub**:

```bash
pip install git+https://github.com/Gishankrishka/python-jp2a.git
```

Or install dependencies manually:

```bash
pip install opencv-python pillow requests
```

### Step 2: Install FFmpeg (Required for Video Audio)

FFmpeg is required for audio extraction and playback in video files.

#### Windows
```bash
# Using Chocolatey
choco install ffmpeg

# Or using Scoop
scoop install ffmpeg

# Or download from: https://ffmpeg.org/download.html
```

#### macOS
```bash
# Using Homebrew
brew install ffmpeg
```

#### Linux
```bash
# Ubuntu/Debian
sudo apt-get install ffmpeg

# Fedora
sudo dnf install ffmpeg

# Arch
sudo pacman -S ffmpeg
```

---

## Quick Usage

```bash
# Convert an image to ASCII
jp2a image.png --width 100 --color

or

python3 -m jp2a image.png --color

# Convert a video to ASCII in fullscreen high-res mode (with audio)
jp2a video.mp4 --fullscreen --highres

# Get HTML output
jp2a image.png --html --width 80

or

python -m jp2a image.png --html --width 80
```

---

## Example ASCII Output

**Original image:**

<img width="1212" height="650" alt="image" src="https://github.com/user-attachments/assets/69bc0bba-aa7b-48cb-9f0b-9d61b4b8d9f6" />

**ASCII Art Output:**

```
...............................................................................'
...'................................',,,,'......................................
'..''............................,oOKK00K0Od;...................................
.'.'............................dKXKKKKKKKKKx..................................
''.............................OWXKKXKKKKKXKKX0.....................''..........
,.............................oNKXWN0O00O00XNXNl................................
.............'''..............0KKXX0XNNNNNKKNKK0................................
..............',....''.......'X0XX0KXXNNXXX0KK0K'...............................
...........''''.............,cKKX0xkk0XNKkkkkK00l,..............................
............''..............,dOXKkxoxKNNXxdkx0KOd,..............................
.......'...'''...............dKXKOXNNNXXNNNNOOK0x...............................
.......'....''....'...'.....'0KXOk0NNNXXNNN0xkK0K,...'..........................
........'...''...'..........cKKX0xd0XNXXNX0ook000O;.............................
............................O0KKOdoddOKKOdoodx00Oxd;............................
..........''............'..;KKXOkdxocldoccoodk0OKx,,............................
.........'',........''..'..kKKKOxdxc..l;.'ooxOkOXOx.............................
.....''...''........''....oKKKKkkxd'';cc,'';xOd0XKl,;...........................
......''...'''......'...''x0KKOxxOlc::,:ldcokxdOKX0ll,..........................
''....'','..'''........'od0OK0kkkd0XkclxK0OkdkOO0XXO,oc.........................
..'....'',..'''''.....,:o0KO00xkkkXNNXXNNNNXx0KOOKXKOko'........................
...''....'.'''.,;....':coOKOxkdOXNNN0XNNNNN0OXK0kKKK0k,:,'......................
...,,,'......'',;'..'c:oO0O0xxcxXNNKXXOxllddKXX0x0kKOdockc,'....................
...''',...'..''','';:;oOXOx0o:c',o0kl,'';o;kXXKkkOk0Ocdl0XOo:...................
...''''.......',,,;:;xXKXXOoo'','','.'';o,;0KOkxkx0Ox,;,c0x00kc.................
..;:cc;'.......',,'.oX0KXKx;:;.........l'.:OKK000kOkl;cllOO:,oOk:...............
.',;:cccc;..'.''''.:XO0XKdod:;...';:;'.:..:k0KK0kxdd'..'';KXx,.,lxo,............
;;,:;cc:cc;'.'''','kkdK0xodxx;,..lllc'.;..,x0KKKkOodl'.''':OXXx;.'lcdl,..'......
';;cc:c::;;c,.;llc:kcxKxdddxd;',.,c,..,,...,o0KXxxxddo'.''',o0XXx;,:,okd:''',,',
.',:c;c:,,;:;;ol;;dxxOOdkxxxd,,:.....;c''...lxO0Oxxodxc..';lllx0KXkdc,ck0d:;;,'.
'',:cc;;,';c,;,.:,lxkkkdkdxxl.,,'''''c,''..;dodkOxkkxxkc'cxx:,okO0KX0d:;dK0l,,,,
,',,,,,,,'':;'.'';;;oxxxkxoc..;''''';,.'...,ddodxkxkkkxko:';c'oxkOO0KXKkldKXx:cc
;,,,,,;:;',;;;:c,:,,,;okxkx,.;l'''',l,''....,ddoodxkkkkkkd;.;c;cddxkO0KXXO0XNk;;
,,'',;;,,;;,,:c,o00l',,oxloocc,'''',:'''''...:dddoodxkkOkkkx;':c:odxxdxO0KKXXXd;
.'',';'':c::cc,oKOOc;c';;:,',:''''';;''''';:,'cddddooddxkkkkOd:,::coxkxxdxk0K0Kx
,',ccc:,,;,:o:oXOxc;oxl'.,c';;''''':;'',;:;,;',oddxkxddodddxkkOd;,:;:lxkkxolclOK
,'',:ccc;',l;cNXo:cckxo'';c,:,''''':;';c,,:;,'':dooxkkkddddooxxOOo,;c,,;,,';codk
',:',;;,::::,0Xk;,,oOkc.,::c:'..''.:;::'::''::''ododkkkkkdododxxkOkl.'......';:c
',,,'.'';:o;kXXo;,'dOd'.,',,c,.....:c;':;'.,,...:ddoxkkkkkxddokkxkOkl',olloc'';l
.'..''',;,ckXKKlllckkd;,,'''','...'l;'',.'''''..;dxddxkkkkkkdodkxxkkkx,dkkkkkdlo
,';;:::;,,dX0OKl;:lkkddo,,',''''',c,..'''','''..;dxxodkkkkkkkdokkxxkxxxkxdxkkxxo
;;;;;;::::0KOkKl;:okxddo:'.'....;:'..,,''';'....;dxxooxkkkxkkkdkkdokkxodkxoxkxdd
.''',,,;;oOKOkOd::oOxddol''''........,''''''''..ldxxoodkkkkkkkdokkxxkxxxkxdxkkxxo
..',,;;:;dcXkkxx::oOxddoo;,''..'...'''''',''''.,ddkxoodkkkkxkdxocllokkkl::cllxdl
',,,;;;:;d;OOkkllcoxkxdooc'.''''..'''''''''....oddkxodokkkkdddol:::lxkdl:ccccooc
....''.,;:,:kkkd:co0dxxdoo;'.''''.''''''''''..;dddxxodoxkkkddxol;;::xxlcc::::cc;
```

*High-res color mode will show the ASCII with vibrant terminal colors.*

---

## CLI Options

* `--width`, `--height`: Output dimensions in characters.
* `--size`: Set both width and height (e.g., `120x60`)
* `--color`: Enable terminal ANSI color.
* `--html`: Export ASCII to HTML format.
* `--charset`: Custom ASCII character set.
* `--invert`: Invert brightness.
* `--highres`: Use Unicode half-blocks (enables color automatically).
* `--fullscreen`: Fit the ASCII art to your terminal window.
* `--flipx`, `--flipy`: Flip horizontally or vertically.
* `--edges-only`: Show only edges.
* `--edge-threshold`: Edge detection sensitivity (default: 50.0).
* `--fill`: Fill background in color mode.
* `--border` or `-b`: Draw a border around the output.
* `--clear`: Clear the terminal before drawing.
* `--output` or `-o`: Save output to a file.
* `--version` or `-V`: Show the version.

---

## Video Playback

* Works with `.mp4`, `.avi`, `.mov`, `.mkv`, `.webm`.
* **Audio plays automatically** in background while ASCII renders.
* Press `Ctrl+C` to stop playback.
* Fullscreen mode automatically adjusts to your terminal size.
* Audio sync maintains perfect timing with video frames.

### Requirements for Video Audio

Make sure **FFmpeg is installed** on your system for audio extraction:

```bash
# Check if FFmpeg is installed
ffmpeg -version
```

If FFmpeg is missing, install it using the commands above.

---

## Operating System Compatibility

### Installation Resources by OS

| OS | Package Manager | Install Command |
|---|---|---|
| **Windows** | Chocolatey | `choco install ffmpeg` |
| **Windows** | Scoop | `scoop install ffmpeg` |
| **macOS** | Homebrew | `brew install ffmpeg` |
| **Linux (Ubuntu/Debian)** | APT | `sudo apt-get install ffmpeg` |
| **Linux (Fedora)** | DNF | `sudo dnf install ffmpeg` |
| **Linux (Arch)** | Pacman | `sudo pacman -S ffmpeg` |

### Potential Issues by OS

| Issue | Linux | macOS | Windows |
|-------|-------|-------|---------|
| **FFmpeg Installation** | ✅ Easy via APT/DNF | ✅ Easy via Homebrew | ⚠️ Manual or Chocolatey |
| **Audio Playback** | ✅ Works with ffplay | ✅ Works with afplay | ✅ Works with Media.SoundPlayer |
| **Video Codec Support** | ✅ Good | ⚠️ May need codec fixes | ✅ Good |
| **Terminal Colors** | ✅ Full support | ✅ Full support | ⚠️ Older terminals may have issues |
| **Unicode Support** | ✅ Full support | ✅ Full support | ⚠️ Windows 7/8 may need config |
| **Fullscreen Mode** | ✅ Reliable | ✅ Reliable | ✅ Reliable |

### macOS-Specific Issues

**Issue:** Audio doesn't play  
**Solution:** Install FFmpeg via Homebrew
```bash
brew install ffmpeg
```

**Issue:** Video codec errors  
**Solution:** Convert video to H.264
```bash
ffmpeg -i input.avi -c:v libx264 output.mp4
```

### Windows-Specific Issues

**Issue:** `ffmpeg` command not found  
**Solution:** Add FFmpeg to PATH or use full path, or install via Chocolatey

**Issue:** Terminal color support  
**Solution:** Use Windows Terminal instead of Command Prompt for better ANSI support

### Linux-Specific Issues

**Issue:** Missing audio codec  
**Solution:** Install additional libraries
```bash
sudo apt-get install ffmpeg libavcodec-extra
```

**Issue:** Permission denied when playing audio  
**Solution:** Check audio device permissions
```bash
sudo usermod -a -G audio $USER
```

---

## Example Python Usage

You can also use it programmatically:

```python
from jp2a import convert_to_ascii

ascii_art = convert_to_ascii(
    "image.png",
    width=100,
    color=True,
    highres=True
)

print(ascii_art)
```

---

## Troubleshooting

### Audio not playing during video playback?
- Ensure FFmpeg is installed: `ffmpeg -version`
- Try converting video to standard codec: `ffmpeg -i video.mp4 -c:v libx264 -c:a aac output.mp4`
- Check system audio is working

### Video playback is slow?
- Reduce output width: `--width 80` instead of `--width 200`
- Disable color: remove `--color` flag
- Use `--highres` instead of custom charset for better performance

### Terminal not clearing properly?
- Ensure you're using a modern terminal emulator
- Try Windows Terminal on Windows instead of Command Prompt
- Use iTerm2 on macOS for best results

### Colors not showing?
- Add `--color` flag explicitly
- Use Windows Terminal on Windows for better ANSI support
- Verify terminal supports 24-bit true color

---

## License

MIT License © 2025 Gishan Krishka  
[Telegram](https://t.me/KrishDev)

---

## Contribution

Contributions welcome! Open an issue or pull request on [GitHub](https://github.com/GishanKrishka/python-jp2a).

---

## Screenshot / Demo GIF

![ScreencastFrom2025-08-1315-45-25-ezgif com-video-to-gif-converter (1) (1)](https://github.com/user-attachments/assets/fe2c1759-2a57-484a-9bf2-386d26525513)
