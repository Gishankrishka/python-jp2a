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

install the latest from **GitHub**:

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

<img width="1212" height="650" alt="image" src="https://github.com/user-attachments/assets/69bc0bba-aa7b-48cb-9f0b-9d61b4b8d9f6" />


**ASCII Art Output:**

```
...............................................................................'
...'................................',,,,'......................................
'..''............................,oOKK00K0Od;...................................
.'.'............................dKXKKKKKKKKKKx..................................
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
.''',,,;;oOKOkOd::oOxddol''''........,''''''''..ldxxoodkkkxxkxdkoooxkkd;codoxxdo
..',,;;:;dcXkkxx::oOxddoo;,''..'...'''''',''''.,ddkxoodkkkkxkdxocllokkkl::cllxdl
',,,;;;:;d;OOkkllcoxkxdooc'.''''..'''''''''....oddkxodokkkkdddol:::lxkdl:ccccooc
....''.,;:,:kkkd:co0dxxdoo;'.''''.''''''''''..;dddxxodoxkkkddxol;;::xxlcc::::cc;
                               
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

## License

MIT License © 2025 Gishan Krishka
[Telegram](https://t.me/KrishDev)

---

## Contribution

Contributions welcome! Open an issue or pull request on [GitHub](https://github.com/GishanKrishka/python-jp2a).

---

## Screenshot / Demo GIF 

![ScreencastFrom2025-08-1315-45-25-ezgif com-video-to-gif-converter (1) (1)](https://github.com/user-attachments/assets/fe2c1759-2a57-484a-9bf2-386d26525513)

