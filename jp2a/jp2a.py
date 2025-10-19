#!/usr/bin/env python3
import argparse, shutil, sys, os, time
from PIL import Image, ImageOps, ImageFilter
import requests
from io import BytesIO
import subprocess
import threading

# ------------------- METADATA -------------------
DEFAULT_CHARS = "...',;:clodxkO0KXNWM"
VERSION = "1.3-python-jp2a"
COPYRIGHT = "© 2025 Gishan Krishka (https://t.me/KrishDev)"

# ------------------- OPTIONAL VIDEO SUPPORT -------------------
try:
    import cv2
    CV2_AVAILABLE = True
except ImportError:
    CV2_AVAILABLE = False

# ------------------- IMAGE LOADING -------------------
def load_image(path_or_url):
    try:
        if path_or_url == "-":
            return Image.open(sys.stdin.buffer).convert("RGBA")
        elif path_or_url.startswith(("http://","https://")):
            resp = requests.get(path_or_url)
            resp.raise_for_status()
            return Image.open(BytesIO(resp.content)).convert("RGBA")
        else:
            return Image.open(path_or_url).convert("RGBA")
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

# ------------------- TERMINAL SIZE -------------------
def get_terminal_size():
    size = shutil.get_terminal_size(fallback=(80,24))
    return size.columns, size.lines

# ------------------- ASCII CONVERSION -------------------
def image_to_ascii(
    img, width=None, height=None, size=None, color=False, charset=DEFAULT_CHARS,
    invert=False, highres=False, flipx=False, flipy=False, edges_only=False,
    edge_threshold=50, fill=False, border=False, html=False
):
    if img is None:
        return "Error: No image to convert."
    if flipx: img = ImageOps.mirror(img)
    if flipy: img = ImageOps.flip(img)

    if edges_only:
        img = img.convert("L").filter(ImageFilter.FIND_EDGES)
        if invert: img = ImageOps.invert(img)

    aspect_ratio = img.height / img.width
    if size:
        width, height = map(int, size.split('x'))
    elif width and not height:
        height = int(aspect_ratio * width * (2 if highres else 0.55))
    elif height and not width:
        width = int(height / (aspect_ratio * (2 if highres else 0.55)))
    elif not width and not height:
        width = 80
        height = int(aspect_ratio * width * (2 if highres else 0.55))

    img = img.resize((width, height))
    if invert:
        charset = charset[::-1]

    result = []
    step = 2 if highres else 1
    for y in range(0, img.height, step):
        line = ""
        for x in range(img.width):
            if highres and y+1 < img.height:
                r1,g1,b1,a1 = img.getpixel((x,y))
                r2,g2,b2,a2 = img.getpixel((x,y+1))
                if a1<128: r1=g1=b1=0
                if a2<128: r2=g2=b2=0
                if html and color:
                    line += f'<span style="color:rgb({r1},{g1},{b1});background-color:rgb({r2},{g2},{b2})">▀</span>'
                elif color:
                    line += f"\033[38;2;{r1};{g1};{b1}m\033[48;2;{r2};{g2};{b2}m▀\033[0m"
                else:
                    gray1 = int((r1+g1+b1)/3)
                    gray2 = int((r2+g2+b2)/3)
                    if invert: gray1, gray2 = 255-gray1, 255-gray2
                    line += "▀" if gray1>gray2 else "▄"
            else:
                r,g,b,a = img.getpixel((x,y))
                if a<128: r=g=b=0
                gray = int((r+g+b)/3)
                if invert: gray=255-gray
                char = charset[int(gray/(255)*(len(charset)-1))]
                if html and color:
                    line += f'<span style="color:rgb({r},{g},{b})">{char}</span>'
                elif color:
                    line += f"\033[38;2;{r};{g};{b}m{char}\033[0m"
                else:
                    line += char
        if border:
            line = "|" + line + "|"
        result.append(line)

    if border:
        top_bottom = "+" + "-"*len(result[0][1:-1]) + "+"
        result.insert(0, top_bottom)
        result.append(top_bottom)

    if html:
        return (
            "<pre style='line-height:90%;font-family:monospace;"
            "background-color:black;color:white;text-align:center;'>"
            + "\n".join(result) +
            "</pre>"
        )
    else:
        return "\n".join(result)

# ------------------- FUNCTIONAL API -------------------
def convert_to_ascii(
    image_path_or_url,
    width=None,
    height=None,
    size=None,
    color=False,
    charset=DEFAULT_CHARS,
    invert=False,
    highres=False,
    flipx=False,
    flipy=False,
    edges_only=False,
    edge_threshold=50.0,
    fill=False,
    border=False,
    html=False
):
    img = load_image(image_path_or_url)
    if img is None: return "Error: Cannot load image."
    if width and not height:
        height = int((img.height/img.width) * width * (2 if highres else 0.55))
    elif height and not width:
        width = int(height / ((img.height/img.width) * (2 if highres else 0.55)))
    if highres: color = True
    return image_to_ascii(
        img,
        width=width,
        height=height,
        size=size,
        color=color,
        charset=charset,
        invert=invert,
        highres=highres,
        flipx=flipx,
        flipy=flipy,
        edges_only=edges_only,
        edge_threshold=edge_threshold,
        fill=fill,
        border=border,
        html=html
    )

# ------------------- AUDIO EXTRACTION & PLAYBACK -------------------
def extract_audio_from_video(video_path, temp_audio_path="temp_audio.wav", speed=1.0):
    """Extract audio from video using ffmpeg and adjust speed"""
    try:
        # Speed adjustment: 1.0 = normal, 0.8 = 20% slower, 0.5 = 50% slower
        cmd = [
            'ffmpeg', '-i', video_path, 
            '-q:a', '9', '-n', 
            '-af', f'atempo={speed}',  # Adjust audio tempo
            temp_audio_path, '-loglevel', 'error'
        ]
        result = subprocess.run(cmd, capture_output=True, timeout=60)
        if os.path.exists(temp_audio_path) and os.path.getsize(temp_audio_path) > 0:
            return temp_audio_path
        return None
    except subprocess.TimeoutExpired:
        print("Warning: Audio extraction timed out")
        return None
    except FileNotFoundError:
        print("Warning: FFmpeg not found. Install FFmpeg to enable audio playback.")
        return None
    except Exception as e:
        return None

def play_audio_background(audio_path):
    """Play audio in background thread using ffplay"""
    def _play():
        try:
            if sys.platform == 'win32':
                cmd = f'ffplay -nodisp -autoexit "{audio_path}"'
            elif sys.platform == 'darwin':
                cmd = f'ffplay -nodisp -autoexit "{audio_path}"'
            else:  # Linux
                cmd = f'ffplay -nodisp -autoexit "{audio_path}" 2>/dev/null'
            
            subprocess.Popen(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception as e:
            print(f"Error playing audio: {e}")
    
    audio_thread = threading.Thread(target=_play, daemon=True)
    audio_thread.start()
    return audio_thread

# ------------------- VIDEO ASCII -------------------
def play_video_ascii(video_path, color=False, charset=DEFAULT_CHARS, invert=False,
                     highres=False, flipx=False, flipy=False, edges_only=False,
                     edge_threshold=50.0, fill=False, border=False, clear=True,
                     fullscreen=False, width=None, height=None):
    try:
        import cv2, time, os

        if not os.path.exists(video_path):
            print(f"Video file not found: {video_path}")
            return

        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            print(f"Cannot open video: {video_path}")
            return

        fps = cap.get(cv2.CAP_PROP_FPS) or 25.0
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        print(f"Video ASCII mode: {video_path} at {fps:.2f} FPS ({frame_count} frames)")

        # Extract and play audio in background
        audio_thread = None
        temp_audio = "temp_audio.wav"
        audio_path = extract_audio_from_video(video_path, temp_audio, speed=0.8)
        audio_started = False
        if audio_path:
            print(f"Starting audio playback...")
            audio_thread = play_audio_background(audio_path)
            audio_started = True
            time.sleep(1.0)  # Give audio time to start

        try:
            frame_num = 0
            start_time = time.time()
            frame_delay = 1.0 / fps
            
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame).convert("RGBA")

                # Fullscreen or custom width/height handling
                term_w, term_h = get_terminal_size()
                aspect_ratio = img.height / img.width
                char_aspect = 0.55

                if fullscreen:
                    w = term_w
                    h = int(w * aspect_ratio * char_aspect)
                    if h > term_h:
                        h = term_h
                        w = int(h / (aspect_ratio * char_aspect))
                else:
                    w = width or img.width
                    h = height or int(w * aspect_ratio * char_aspect)
                    if w > term_w:
                        w = term_w
                        h = int(w * aspect_ratio * char_aspect)
                    if h > term_h:
                        h = term_h
                        w = int(h / (aspect_ratio * char_aspect))

                if highres:
                    color = True

                ascii_frame = image_to_ascii(
                    img,
                    width=w,
                    height=h,
                    color=color,
                    charset=charset,
                    invert=invert,
                    highres=highres,
                    flipx=flipx,
                    flipy=flipy,
                    edges_only=edges_only,
                    edge_threshold=edge_threshold,
                    fill=fill,
                    border=border
                )

                if clear:
                    os.system('cls' if os.name=='nt' else 'clear')
                print(ascii_frame)
                
                # Sync with audio: use exact frame timing from video
                elapsed_total = time.time() - start_time
                target_time = frame_num * frame_delay
                sleep_time = target_time - elapsed_total
                
                if sleep_time > 0.001:
                    time.sleep(sleep_time)
                elif sleep_time < -frame_delay:
                    # If we're too far behind, skip a frame to catch up
                    frame_num += 1
                    continue
                
                frame_num += 1
                
        except KeyboardInterrupt:
            print("\nVideo stopped by user.")
        finally:
            if audio_thread:
                try:
                    audio_thread.join(timeout=0.5)
                except:
                    pass
            time.sleep(0.5)
            if 'temp_audio' in locals() and os.path.exists(temp_audio):
                try:
                    os.remove(temp_audio)
                except:
                    pass
    except KeyboardInterrupt:
        print("\nVideo stopped by user.")
    finally:
        cap.release()
    

# ------------------- MAIN -------------------
def main():
    parser = argparse.ArgumentParser(
        description=f"jp2a-like Python ASCII converter\n{COPYRIGHT}",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="""Examples:
  python jp2a.py image.png --width 100 --color
  python jp2a.py video.mp4 --fullscreen --highres
"""
    )

    parser.add_argument("image", nargs='?', help="Path, URL, or '-' for stdin")
    parser.add_argument("--width", type=int, help="Output width in chars")
    parser.add_argument("--height", type=int, help="Output height in chars")
    parser.add_argument("--size", type=str, help="Output WxH, e.g., 120x60")
    parser.add_argument("--color", action="store_true", help="Enable ANSI color")
    parser.add_argument("--html", action="store_true", help="Return HTML output")
    parser.add_argument("--charset", type=str, default=DEFAULT_CHARS, help="Custom ASCII set")
    parser.add_argument("--invert", action="store_true", help="Invert brightness")
    parser.add_argument("--highres", action="store_true", help="Unicode half-block highres (enables color automatically)")
    parser.add_argument("--fullscreen", action="store_true", help="Fit full terminal")
    parser.add_argument("--flipx", action="store_true", help="Flip horizontally")
    parser.add_argument("--flipy", action="store_true", help="Flip vertically")
    parser.add_argument("--edges-only", action="store_true", help="Show edges only")
    parser.add_argument("--edge-threshold", type=float, default=50.0, help="Edge threshold")
    parser.add_argument("--fill", action="store_true", help="Fill background in color mode")
    parser.add_argument("--border", "-b", action="store_true", help="Draw border")
    parser.add_argument("--clear", action="store_true", help="Clear terminal before drawing")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    parser.add_argument("--debug", "-d", action="store_true", help="Debug info")
    parser.add_argument("--output", "-o", type=str, help="Write output to file")
    parser.add_argument("--version", "-V", action="store_true", help="Print version")

    args = parser.parse_args()

    if args.version:
        print(f"jp2a.py {VERSION}\n{COPYRIGHT}")
        return

    if args.clear:
        os.system('cls' if os.name=='nt' else 'clear')

    if args.image is None:
        print("Error: no image or video provided")
        return

    # If video
    if CV2_AVAILABLE and args.image.lower().endswith(('.mp4','.mov','.avi','.mkv','.webm')):
        play_video_ascii(
            args.image,
            width=args.width,
            highres=args.highres,
            color=args.color,
            invert=args.invert,
            charset=args.charset,
            fullscreen=args.fullscreen
        )
        return

    img = load_image(args.image)
    if img is None:
        return

    if args.fullscreen:
        term_w, term_h = get_terminal_size()
        args.width = term_w
        args.height = int((img.height/img.width)*term_w*(2 if args.highres else 0.55))

    if args.highres:
        args.color = True

    ascii_art = image_to_ascii(
        img,
        width=args.width,
        height=args.height,
        size=args.size,
        color=args.color,
        charset=args.charset,
        invert=args.invert,
        highres=args.highres,
        flipx=args.flipx,
        flipy=args.flipy,
        edges_only=args.edges_only,
        edge_threshold=args.edge_threshold,
        fill=args.fill,
        border=args.border,
        html=args.html
    )

    if args.output:
        try:
            with open(args.output,"w",encoding="utf-8") as f:
                f.write(ascii_art)
        except Exception as e:
            print(f"Error writing output: {e}")
    else:
        print(ascii_art)

if __name__=="__main__":
    main()
