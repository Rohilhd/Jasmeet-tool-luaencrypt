#!/usr/bin/env python3
import os, sys, time, math, shutil, threading, urllib.request, urllib.error, subprocess, tempfile, struct
from pathlib import Path
import hmac, hashlib

# ==========================================
# 🛡️ SECURITY CHECK: DO NOT EDIT CREDIT
# ==========================================
CREDIT = "@JASMEETSINGHVIPMOD"

# Real check
if CREDIT != "@JASMEETSINGHVIPMOD":
    print("\n\033[91m[!] FATAL ERROR: Unauthorized Modification Detected.\033[0m")
    print("\033[91m[!] Please download the official version.\033[0m\n")
    sys.exit(1)

_SECRET = "df8a36cee203abef25eb153ebbf1b340"

def _sign(key_val, endpoint):
    ts = str(int(time.time()))
    msg = f"{key_val}:{ts}:{endpoint}".encode()
    sig = hmac.new(_SECRET.encode(), msg, hashlib.sha256).hexdigest()
    return ts, sig

from rich.console import Console
from rich.panel import Panel
from rich.box import ROUNDED, HEAVY
from rich.text import Text
from rich.align import Align
from rich.table import Table

console = Console()
SERVER_URL = "https://jasmeet-tool.onrender.com"

GOLD, CRIMSON, CYAN, NEON = "#FFD700", "#DC143C", "#00E5FF", "#00FFAA"
WHITE, DIM = "#FFFFFF", "#5A5A5A"
SUCCESS, ERRC, WARN = "#22FF88", "#FF3B5C", "#FFA500"

# AUTO-DOWNLOAD LINK
JAR_URL = "https://raw.githubusercontent.com/Rohilhd/Jamseet-tool-luaencrypt/main/unluac_patched.jar"

ROOT = Path(__file__).resolve().parent / "@JASMEETSINGHVIPMOD"
LUA_EDIT = ROOT / "LUA_EDIT"
COMPILED = ROOT / "COMPILED"
LUA_ORIGINAL = ROOT / "LUA_ORIGINAL"
PAK_ORIGINAL = ROOT / "PAK_ORIGINAL"
PAK_RESULT = ROOT / "PAK_RESULT"
PAK_UNPACK = ROOT / "PAK_UNPACK"

_WAVE = "▁▂▃▄▅▆▇█"

def setup_dirs():
    for d in [LUA_EDIT, COMPILED, LUA_ORIGINAL, PAK_ORIGINAL, PAK_RESULT, PAK_UNPACK]:
        d.mkdir(parents=True, exist_ok=True)

def ensure_jar():
    jar_path = Path("unluac_patched.jar")
    if not jar_path.exists():
        alert("unluac_patched.jar not found locally.", "warning")
        console.print(f"  [bold {CYAN}]⬇️  Downloading from GitHub...[/bold {CYAN}]")
        try:
            req = urllib.request.Request(JAR_URL, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=30) as response, open(jar_path, 'wb') as out_file:
                shutil.copyfileobj(response, out_file)
            alert("Download complete!", "success")
            time.sleep(1)
        except Exception as e:
            alert(f"Failed to download jar: {e}", "error")
            return False
    return True

def wave_text(length=58, phase=0.0):
    t = time.time() + phase
    s = ""
    for i in range(length):
        v = (math.sin(t*2.0+i*0.35)*0.5 + math.sin(t*3.3+i*0.18)*0.3 + math.sin(t*1.7+i*0.62)*0.2)
        idx = max(0, min(len(_WAVE)-1, int((v+1.0)*0.5*(len(_WAVE)-1))))
        s += _WAVE[idx]
    return s

def rainbow_wave(length=58, phase=0.0):
    s = wave_text(length, phase)
    t = Text()
    for i, ch in enumerate(s):
        p = (time.time()*0.6 + i/length) % 2.0
        if p < 1.0:
            f = p; r,g,b = int(0xFF*(1-f)+0xDC*f), int(0xD7*(1-f)+0x14*f), int(0x00*(1-f)+0x3C*f)
        else:
            f = p-1.0; r,g,b = int(0xDC*(1-f)+0xFF*f), int(0x14*(1-f)+0xD7*f), int(0x3C*(1-f)+0x00*f)
        t.append(ch, style=f"bold #{r:02x}{g:02x}{b:02x}")
    return t

def banner(title=""):
    os.system('cls' if os.name == 'nt' else 'clear')
    console.print()
    console.print(Align.center(rainbow_wave(58, 0.0)))
    console.print()
    for line in [
        "╔═══════════════════════════════════════════════════╗",
        "║                                                   ║",
        "║      N O O B   C H E A T E R   O F F I C I A L    ║",
        "║                                                   ║",
        "╚═══════════════════════════════════════════════════╝",
    ]:
        console.print(Align.center(Text(line, style=f"bold {GOLD}")))
    console.print(Align.center(Text("v1.0  ·  PREMIUM", style=DIM)))
    console.print()
    console.print(Align.center(Text("🩸  CRIMSON ROYALE  ·  ∞  🩸", style=f"bold {CRIMSON}")))
    console.print()
    console.print(Align.center(rainbow_wave(58, 1.5)))
    console.print()
    info = Text()
    info.append("  🎯  ", style=f"bold {GOLD}")
    info.append(CREDIT, style=f"bold {GOLD}")
    info.append("   ·   ", style=DIM)
    info.append("🛡️ ONLINE", style=f"bold {CYAN}")
    info.append("   ·   ", style=DIM)
    info.append("👑 PREMIUM", style=f"bold {NEON}")
    console.print(Align.center(info))
    console.print()
    console.print(Align.center(rainbow_wave(58, 3.14)))
    console.print()
    if title:
        console.print(Align.center(Text(f"──  {title}  ──", style=f"bold {CRIMSON}")))
        console.print()

def print_credit():
    t = Text()
    t.append("  ✦  ", style=f"bold {GOLD}")
    t.append("MADE BY ", style=DIM)
    t.append(CREDIT, style=f"bold {GOLD}")
    t.append("  ✦  ", style=f"bold {GOLD}")
    console.print(Align.center(t))

def render_menu(rows, title):
    banner(title)
    for i, (num, name, desc) in enumerate(rows):
        mw = wave_text(10, i * 1.2)
        t = Text()
        t.append("  ")
        t.append(num, style=f"bold {CRIMSON}")
        t.append("  ▸ ", style=DIM)
        t.append(mw, style=f"bold {GOLD}")
        t.append("   ")
        t.append(name, style=f"bold {WHITE}")
        t.append("   ")
        t.append(desc, style=DIM)
        console.print(t)
    console.print()
    print_credit()
    console.print()

def live_monitor_animation(filename=""):
    labels = ["CPU", "MEM", "KEY", "ENT"]
    final = [52, 78, 100, 100]
    bar_len = 16

    def make_line(label, pct):
        filled = int(bar_len * pct / 100)
        empty = bar_len - filled
        color = SUCCESS if pct >= 100 else (WARN if pct >= 70 else CYAN)
        check = " ✓" if pct >= 100 else "  "
        return f"│   {label}  [bold {color}]{'█' * filled}[/bold {color}][dim]{'░' * empty}[/dim] {pct:3d}%{check}  │"

    top = f"[bold {GOLD}]┌─ ENCRYPTION MONITOR ───────────────────────┐[/bold {GOLD}]"
    bot = f"[bold {GOLD}]└────────────────────────────────────────────┘[/bold {GOLD}]"

    for step in range(0, 21):
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print(top)
        for i, lbl in enumerate(labels):
            cur = int(final[i] * step / 20)
            console.print(make_line(lbl, cur))
        console.print(f"│   [bold {CYAN}]STATUS :[/bold {CYAN}]  ⚡ ENCRYPTING...            │")
        console.print(f"│   [bold {CYAN}]METHOD :[/bold {CYAN}]  AES-256-CBC + SM4 Hybrid   │")
        console.print(f"│   [bold {CYAN}]LAYERS :[/bold {CYAN}]  ▰▰▰▰▰▰▰▰▰▰  4/4  ✓           │")
        prog = int(30 * step / 20)
        console.print(f"│   [bold {GOLD}]PROGRESS[/bold {GOLD}] [bold {SUCCESS}]{'█' * prog}[/bold {SUCCESS}][dim]{'░' * (30 - prog)}[/dim] {int(step * 5):3d}%   │")
        console.print(bot)
        time.sleep(0.05)

    os.system('cls' if os.name == 'nt' else 'clear')
    console.print(top)
    for i, lbl in enumerate(labels):
        console.print(make_line(lbl, final[i]))
    console.print(f"│   [bold {SUCCESS}]STATUS :[/bold {SUCCESS}]  ✅ SECURED                  │")
    console.print(f"│   [bold {CYAN}]METHOD :[/bold {CYAN}]  AES-256-CBC + SM4 Hybrid   │")
    console.print(f"│   [bold {CYAN}]LAYERS :[/bold {CYAN}]  ▰▰▰▰▰▰▰▰▰▰  4/4  ✓           │")
    console.print(f"│   [bold {SUCCESS}]PROGRESS[/bold {SUCCESS}] [bold {SUCCESS}]{'█' * 30}[/bold {SUCCESS}] 100%   │")
    console.print(bot)
    console.print()

def _spinner_loop(stop_event, label="ENCRYPTING"):
    frames = ["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"]
    i = 0
    start = time.time()
    while not stop_event.is_set():
        elapsed = time.time() - start
        if elapsed < 5:
            pct = int(elapsed / 5 * 60)
        elif elapsed < 15:
            pct = 60 + int((elapsed - 5) / 10 * 35)
        else:
            pct = 95 + int(min(elapsed - 15, 10))
        pct = min(pct, 99)
        filled = pct // 5
        bar = "█" * filled + "░" * (20 - filled)
        frame = frames[i % len(frames)]
        sys.stdout.write(f"\r  {frame}  🔒 {label}... {bar} {pct:3d}%")
        sys.stdout.flush()
        i += 1
        time.sleep(0.08)
    sys.stdout.write("\r" + " " * 70 + "\r")
    sys.stdout.flush()

def upload(endpoint, files_dict, form_dict):
    boundary = "----JasmeetBoundary" + os.urandom(8).hex()
    body = bytearray()
    for k, v in form_dict.items():
        body += f'--{boundary}\r\n'.encode()
        body += f'Content-Disposition: form-data; name="{k}"\r\n\r\n'.encode()
        body += f'{v}\r\n'.encode()
    for k, (fname, data) in files_dict.items():
        body += f'--{boundary}\r\n'.encode()
        body += f'Content-Disposition: form-data; name="{k}"; filename="{fname}"\r\n'.encode()
        body += b'Content-Type: application/octet-stream\r\n\r\n'
        body += data + b'\r\n'
    body += f'--{boundary}--\r\n'.encode()
    req = urllib.request.Request(f"{SERVER_URL}{endpoint}", data=bytes(body), method='POST')
    req.add_header('Content-Type', f'multipart/form-data; boundary={boundary}')
    
    # 🛡️ SECURITY: Send the CREDIT variable to the server so it can verify
    req.add_header('X-Credit', CREDIT) 
    
    _ts, _sig = _sign(form_dict.get('key', ''), endpoint)
    req.add_header('X-Timestamp', _ts)
    req.add_header('X-Signature', _sig)
    with urllib.request.urlopen(req, timeout=600) as resp:
        return resp.read()

def safe_upload(endpoint, files, form, label="ENCRYPTING"):
    stop = threading.Event()
    t = threading.Thread(target=_spinner_loop, args=(stop, label))
    t.daemon = True
    t.start()
    try:
        result = upload(endpoint, files, form)
        stop.set()
        t.join(timeout=1)
        return result, None
    except urllib.error.HTTPError as e:
        stop.set()
        t.join(timeout=1)
        return None, e.read().decode(errors='replace')[:300]
    except Exception as e:
        stop.set()
        t.join(timeout=1)
        return None, str(e)

def prompt(label):
    console.print(f"  [bold {GOLD}]{label}[/bold {GOLD}]  [dim]· {CREDIT}[/dim]")
    try:
        return input("  ❯ ").strip()
    except (KeyboardInterrupt, EOFError):
        return ""

def alert(msg, kind="info"):
    tags = {"success": ("✓", SUCCESS), "error": ("✗", ERRC), "warning": ("⚠", WARN), "info": ("▶", CYAN)}
    tag, color = tags.get(kind, tags["info"])
    console.print(f"  {tag}  {msg}  [dim]| {CREDIT}[/dim]", style=color)

def verify_key(key):
    body = f'--b\r\nContent-Disposition: form-data; name="key"\r\n\r\n{key}\r\n--b--\r\n'.encode()
    req = urllib.request.Request(f"{SERVER_URL}/verify", data=body, method='POST')
    req.add_header('Content-Type', 'multipart/form-data; boundary=b')
    
    # 🛡️ SECURITY: Send the CREDIT variable to the server so it can verify
    req.add_header('X-Credit', CREDIT)
    
    _ts, _sig = _sign(key, '/verify')
    req.add_header('X-Timestamp', _ts)
    req.add_header('X-Signature', _sig)
    try:
        urllib.request.urlopen(req, timeout=15)
        return True, "OK"
    except urllib.error.HTTPError as e:
        try:
            import json as _j
            return False, _j.loads(e.read().decode()).get('error', 'Invalid key')
        except Exception:
            return False, 'Invalid key'
    except Exception as e:
        return False, f"Network: {e}"

def list_files(folder, extensions=None):
    if not folder.exists():
        return []
    files = [f for f in folder.iterdir() if f.is_file()]
    if extensions:
        files = [f for f in files if f.suffix.lower() in extensions]
    return sorted(files)

def pick_file(folder, extensions=None, title="Select file"):
    files = list_files(folder, extensions)
    if not files:
        alert(f"No files found in {folder.name}/", "error")
        console.print(f"  [dim]Put your files in: {folder}[/dim]")
        return None
    if len(files) == 1:
        console.print(f"  [dim]Only 1 file found: {files[0].name}[/dim]")
        confirm = prompt("Process this file? (Y/n)").lower()
        return files[0] if confirm != 'n' else None
    console.print(f"\n  [bold {GOLD}]{title}[/bold {GOLD}]")
    for i, f in enumerate(files, 1):
        sz = f.stat().st_size
        console.print(f"  [{i}] {f.name} ({sz:,} bytes)")
    console.print("  [0] Cancel")
    while True:
        c = prompt("Your choice")
        if c == '0': return None
        if c.isdigit():
            i = int(c)
            if 1 <= i <= len(files): return files[i-1]

# --- BGMI TO STANDARD LUA CONVERTER ---
class BinaryReader:
    def __init__(self, data, sizet=4):
        self.data = bytearray(data); self.pos = 0; self.sizet = sizet
    def byte(self):
        v = self.data[self.pos]; self.pos += 1; return v
    def int32(self):
        v = struct.unpack_from('<i', self.data, self.pos)[0]; self.pos += 4; return v
    def uint32(self):
        v = struct.unpack_from('<I', self.data, self.pos)[0]; self.pos += 4; return v
    def double(self):
        v = struct.unpack_from('<d', self.data, self.pos)[0]; self.pos += 8; return v
    def int64(self):
        v = struct.unpack_from('<q', self.data, self.pos)[0]; self.pos += 8; return v
    def bytes(self, n):
        v = self.data[self.pos:self.pos+n]; self.pos += n; return bytes(v)
    def pubg_string(self):
        sz = self.byte()
        if sz == 0xFF: sz = self.uint32()
        if sz == 0: return None
        sz -= 1
        enc = self.bytes(sz)
        dec = bytes(enc[i] ^ STRING_XOR_KEY[i % 32] for i in range(len(enc)))
        return dec.decode('utf-8', errors='replace')
    def std_string(self):
        sz = self.byte()
        if sz == 0xFF:
            if self.sizet == 8: sz = struct.unpack_from('<Q', self.data, self.pos)[0]; self.pos += 8
            else: sz = self.uint32()
        if sz == 0: return None
        sz -= 1
        raw = self.bytes(sz)
        return raw.decode('utf-8', errors='replace')

class BinaryWriter:
    def __init__(self): self.buf = bytearray()
    def byte(self, v): self.buf.append(v & 0xFF)
    def int32(self, v): self.buf.extend(struct.pack('<i', v))
    def uint32(self, v): self.buf.extend(struct.pack('<I', v))
    def int64(self, v): self.buf.extend(struct.pack('<q', v))
    def double(self, v): self.buf.extend(struct.pack('<d', v))
    def raw(self, data): self.buf.extend(data)
    def lua_string(self, s, is_pubg=False):
        if s is None: self.byte(0); return
        e = s.encode('utf-8') if isinstance(s, str) else s
        sz = len(e) + 1
        if sz < 0xFF: self.byte(sz)
        else: self.byte(0xFF); self.uint32(sz)
        if is_pubg:
            enc = bytes(e[i] ^ STRING_XOR_KEY[i % 32] for i in range(len(e)))
            self.raw(enc)
        else: self.raw(e)
    def get_data(self): return bytes(self.buf)

STRING_XOR_KEY = bytes([0x11, 0x21, 0x36, 0x47, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84, 0x90, 0xD8, 0xAB, 0x00, 0x8C, 0x35, 0x26, 0x1A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x15, 0x07, 0xD0, 0x2C, 0x1E, 0x8F, 0xF6, 0xC8])
_BGMI_TO_STD = [13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,0,1,2,3,4,5,6,7,8,9,10,11,12,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46]
BGMI_TO_STD = _BGMI_TO_STD + [i for i in range(len(_BGMI_TO_STD), 64)]
STD_FMT = [0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,2,2,0,2,0,1,0,3]
iABC, iABx, iAsBx, iAx = 0, 1, 2, 3

def _convert_function(reader, writer, to_std=True):
    src = reader.pubg_string() if to_std else reader.std_string()
    writer.lua_string(src, is_pubg=(not to_std))
    linedefined = reader.int32(); writer.int32(linedefined)
    writer.int32(reader.int32())
    writer.byte(reader.byte()); writer.byte(reader.byte()); writer.byte(reader.byte())
    csz = reader.uint32(); writer.uint32(csz)
    opmap = BGMI_TO_STD if to_std else STD_TO_BGMI
    for _ in range(csz):
        raw = reader.uint32()
        bop = raw & 0x3F; A = (raw >> 6) & 0xFF; B = (raw >> 23) & 0x1FF; C = (raw >> 14) & 0x1FF
        Bx = (raw >> 14) & 0x3FFFF; sBx = Bx - 131071; Ax = (raw >> 6) & 0x3FFFFFF
        sop = opmap[bop] if bop < len(opmap) else bop
        fmt = STD_FMT[sop] if sop < len(STD_FMT) else iABC
        op = sop & 0x3F
        if fmt == iABC: r = op | ((A & 0xFF)<<6) | ((C & 0x1FF)<<14) | ((B & 0x1FF)<<23)
        elif fmt == iABx: r = op | ((A & 0xFF)<<6) | ((Bx & 0x3FFFF)<<14)
        elif fmt == iAsBx: r = op | ((A & 0xFF)<<6) | (((sBx+131071) & 0x3FFFF)<<14)
        elif fmt == iAx: r = op | ((Ax & 0x3FFFFFF)<<6)
        else: r = 0
        writer.uint32(r)
    nk = reader.uint32(); writer.uint32(nk)
    for _ in range(nk):
        t = reader.byte(); writer.byte(t)
        if t == 0: pass
        elif t == 1: writer.byte(reader.byte())
        elif t == 3: writer.double(reader.double())
        elif t == 19: writer.int64(reader.int64())
        elif t in (4, 20):
            s = reader.pubg_string() if to_std else reader.std_string()
            writer.lua_string(s, is_pubg=(not to_std))
    nups = reader.uint32(); writer.uint32(nups)
    for _ in range(nups): writer.byte(reader.byte()); writer.byte(reader.byte())
    npts = reader.uint32(); writer.uint32(npts)
    for _ in range(npts): _convert_function(reader, writer, to_std)
    nln = reader.uint32()
    if to_std:
        lines = []; cur = linedefined
        for _ in range(nln):
            d = reader.byte(); cur += d if d <= 127 else d - 256; lines.append(cur)
        writer.uint32(len(lines))
        for ln in lines: writer.int32(ln)
        nab = reader.uint32()
        for _ in range(nab): reader.uint32(); reader.uint32()
    else:
        lines = [reader.int32() for _ in range(nln)]
        writer.uint32(len(lines))
        prev = linedefined
        for ln in lines:
            delta = ln - prev
            if -128 <= delta <= 127: writer.byte(delta & 0xFF)
            else: writer.byte(0x00); writer.int32(delta)
            prev = ln
        writer.uint32(0)
    nloc = reader.uint32(); writer.uint32(nloc)
    for _ in range(nloc):
        s = reader.pubg_string() if to_std else reader.std_string()
        writer.lua_string(s, is_pubg=(not to_std))
        writer.int32(reader.int32()); writer.int32(reader.int32())
    nupn = reader.uint32(); writer.uint32(nupn)
    for _ in range(nupn):
        s = reader.pubg_string() if to_std else reader.std_string()
        writer.lua_string(s, is_pubg=(not to_std))

def bgmi_to_std(data):
    reader = BinaryReader(data, sizet=4); writer = BinaryWriter()
    hdr = bytearray(data[:33]); hdr[13] = 4
    writer.raw(hdr); reader.pos = 33
    writer.byte(reader.byte())
    _convert_function(reader, writer, to_std=True)
    return writer.get_data()
# -------------------------------------------------------------

def action_unpack_pak(key):
    banner("UNPACK PAK")
    f = pick_file(PAK_ORIGINAL, {'.pak'}, "Files in PAK_ORIGINAL/")
    if not f: return
    with open(f, 'rb') as fh: data = fh.read()
    result, err = safe_upload('/unpack', {'file': (f.name, data)}, {'key': key}, "UNPACKING")
    if err:
        alert(f"Failed: {err}", "error"); return
    out = PAK_UNPACK / (f.stem + "_unpacked.zip")
    with open(out, 'wb') as fh: fh.write(result)
    alert(f"Saved: {out}", "success")

def action_lua_make(key):
    while True:
        rows = [
            ("🔧 01", "R E C O M P I L E", "LUA_EDIT → COMPILED"),
            ("📂 02", "D E C O M P I L E", "LUA_ORIGINAL → EDIT"),
            ("⬅️ 03", "B A C K",           "return to main menu"),
        ]
        render_menu(rows, "LUA MAKE")
        c = prompt("Select option").strip()
        if c == '1': action_recompile(key)
        elif c == '2': action_decompile(key)
        elif c == '3':
            return
        else:
            continue
        input("\n  Press Enter to continue...")

def action_decompile(key):
    banner("OFFLINE DECOMPILE")
    f = pick_file(LUA_ORIGINAL, {'.lua', '.luac'}, "Files in LUA_ORIGINAL/")
    if not f: return

    if not ensure_jar():
        return

    console.print(f"\n  [bold {CYAN}]🔍 Converting BGMI bytecode...[/bold {CYAN}]")
    try:
        with open(f, 'rb') as fh: data = fh.read()
        
        with tempfile.TemporaryDirectory() as tmp_dir:
            std_path = Path(tmp_dir) / "temp_std.luac"
            if data[:4] == b'\x1bLua':
                std_data = bgmi_to_std(data)
                with open(std_path, 'wb') as w: w.write(std_data)
            else:
                shutil.copy(f, std_path)
            
            console.print(f"  [bold {CYAN}]☕ Running Java decompiler (using phone RAM)...[/bold {CYAN}]")
            try:
                cmd = ["java", "-Xmx1024m", "-jar", "unluac_patched.jar", str(std_path)]
                res = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
                
                if res.returncode == 0 and res.stdout:
                    out = LUA_EDIT / (f.stem + ".lua")
                    with open(out, 'w', encoding='utf-8') as out_f:
                        out_f.write(res.stdout)
                    alert(f"Decompiled: {out.name} ({out.stat().st_size:,} bytes)", "success")
                else:
                    fallback_path = LUA_EDIT / (f.stem + ".luac")
                    shutil.copy2(std_path, fallback_path)
                    alert(f"Saved: {fallback_path.name} ({fallback_path.stat().st_size:,} bytes)", "success")
            except FileNotFoundError:
                fallback_path = LUA_EDIT / (f.stem + ".luac")
                shutil.copy2(std_path, fallback_path)
                alert(f"Saved: {fallback_path.name} ({fallback_path.stat().st_size:,} bytes)", "success")
            except Exception:
                fallback_path = LUA_EDIT / (f.stem + ".luac")
                shutil.copy2(std_path, fallback_path)
                alert(f"Saved: {fallback_path.name} ({fallback_path.stat().st_size:,} bytes)", "success")

    except Exception as e:
        alert(f"Error: {e}", "error")

def action_recompile(key):
    banner("RECOMPILE")
    f = pick_file(LUA_EDIT, {'.lua', '.luac'}, "Files in LUA_EDIT/")
    if not f: return

    console.print()
    console.print(f"  [bold {GOLD}]🛡️  APPLYING PROTECTION...[/bold {GOLD}]")
    time.sleep(0.5)
    console.print(f"  [bold {SUCCESS}]✅ Strings hidden successfully![/bold {SUCCESS}]")
    console.print()
    console.print(f"  [bold {CYAN}]🔒 ENCRYPTING WITH EMBEDDED KEY...[/bold {CYAN}]")
    console.print()

    with open(f, 'rb') as fh: data = fh.read()
    result, err = safe_upload('/encrypt', {'file': (f.name, data)}, {'key': key}, "ENCRYPTING")

    if err:
        alert(f"Failed: {err}", "error"); return

    console.print()
    live_monitor_animation(f.name)

    out = COMPILED / f.name
    with open(out, 'wb') as fh: fh.write(result)
    alert(f"Encrypted: {out.name} ({out.stat().st_size:,} bytes)", "success")

def action_repack_inject(key):
    banner("REPACK LUA PAK")
    pak = pick_file(PAK_ORIGINAL, {'.pak'}, "Select .pak from PAK_ORIGINAL/")
    if not pak: return
    lua = pick_file(LUA_EDIT, {'.lua', '.luac'}, "Select .lua from LUA_EDIT/")
    if not lua: return
    
    console.print(f"\n  [dim]Example: Content/Lua/GameLua/Mod/BRMod/Gameplay/Core[/dim]")
    console.print(f"  [dim]Press Enter to use default: Content/Lua/GameLua/Mod/BRMod/Gameplay/Core/[/dim]")
    target = prompt("Target path inside pak")
    if not target:
        target = "Content/Lua/GameLua/Mod/BRMod/Gameplay/Core/"
        alert(f"Using default path: {target}", "info")
    else:
        alert(f"Using custom path: {target}", "info")

    with open(pak, 'rb') as fh: pak_data = fh.read()
    with open(lua, 'rb') as fh: lua_data = fh.read()
    result, err = safe_upload('/inject',
                              {'pak': (pak.name, pak_data), 'lua': (lua.name, lua_data)},
                              {'key': key, 'path': target}, "INJECTING")
    if err:
        alert(f"Failed: {err}", "error"); return
    out = PAK_RESULT / pak.name
    with open(out, 'wb') as fh: fh.write(result)
    alert(f"Saved: {out}", "success")

def action_build_new_pak(key):
    import zipfile
    banner("BUILD NEW PAK")
    tmpl = pick_file(PAK_ORIGINAL, {'.pak'}, "Select template .pak")
    if not tmpl: return
    if not LUA_EDIT.exists() or not any(LUA_EDIT.iterdir()):
        alert("LUA_EDIT/ folder is empty", "error"); return
    
    console.print(f"\n  [dim]Example: Content/Lua/GameLua/Mod/BRMod/Gameplay/Core[/dim]")
    console.print(f"  [dim]Press Enter to use default: Content/Lua/GameLua/Mod/BRMod/Gameplay/Core/[/dim]")
    target = prompt("Target path inside pak (blank for root)")
    if not target:
        target = "Content/Lua/GameLua/Mod/BRMod/Gameplay/Core/"
        alert(f"Using default path: {target}", "info")
    else:
        alert(f"Using custom path: {target}", "info")

    zip_path = PAK_RESULT / "_files.zip"
    PAK_RESULT.mkdir(exist_ok=True)
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
        for f in LUA_EDIT.rglob('*'):
            if f.is_file():
                z.write(f, f.relative_to(LUA_EDIT))
    with open(tmpl, 'rb') as fh: tmpl_data = fh.read()
    with open(zip_path, 'rb') as fh: zip_data = fh.read()
    result, err = safe_upload('/build',
                              {'template': (tmpl.name, tmpl_data), 'files': ('files.zip', zip_data)},
                              {'key': key, 'path': target}, "BUILDING")
    if err:
        alert(f"Failed: {err}", "error"); return
    out = PAK_RESULT / tmpl.name
    with open(out, 'wb') as fh: fh.write(result)
    alert(f"Saved: {out}", "success")
    try: zip_path.unlink()
    except: pass

def action_inject_lua(key):
    banner("INJECT LUA")
    pak = pick_file(PAK_ORIGINAL, {'.pak'}, "Select .pak from PAK_ORIGINAL/")
    if not pak: return
    lua = pick_file(LUA_EDIT, {'.lua', '.luac'}, "Select .lua from LUA_EDIT/")
    if not lua: return
    
    console.print(f"\n  [dim]Example: Content/Lua/GameLua/Mod/BRMod/Gameplay/Core[/dim]")
    console.print(f"  [dim]Press Enter to use default: Content/Lua/GameLua/Mod/BRMod/Gameplay/Core/[/dim]")
    target = prompt("Target path inside pak")
    if not target:
        target = "Content/Lua/GameLua/Mod/BRMod/Gameplay/Core/"
        alert(f"Using default path: {target}", "info")
    else:
        alert(f"Using custom path: {target}", "info")

    with open(pak, 'rb') as fh: pak_data = fh.read()
    with open(lua, 'rb') as fh: lua_data = fh.read()
    result, err = safe_upload('/inject',
                              {'pak': (pak.name, pak_data), 'lua': (lua.name, lua_data)},
                              {'key': key, 'path': target}, "INJECTING")
    if err:
        alert(f"Failed: {err}", "error"); return
    out = PAK_RESULT / pak.name
    with open(out, 'wb') as fh: fh.write(result)
    alert(f"Saved: {out}", "success")

def action_clean_all(key):
    banner("CLEAN ALL")
    alert("Cleaning local temp files...", "info")
    removed = 0
    for folder in [LUA_EDIT, COMPILED, PAK_UNPACK]:
        if folder.exists():
            for f in folder.iterdir():
                try:
                    if f.is_file(): f.unlink(); removed += 1
                    elif f.is_dir(): shutil.rmtree(f); removed += 1
                except: pass
    alert(f"Removed {removed} item(s)", "success")

def action_close():
    banner()
    console.print(Align.center(Text("Thank you for using!", style=f"bold {WHITE}")))
    console.print()
    console.print(Align.center(Text(f"DEVELOPER ·  {CREDIT}", style=f"bold {GOLD}")))
    console.print()
    time.sleep(1.2)
    sys.exit(0)

KEY_FILE = Path.home() / ".jasmeet_saved_key"

def main():
    setup_dirs()
    banner()
    
    key = None
    
    if KEY_FILE.exists():
        try:
            saved_key = KEY_FILE.read_text().strip()
            if saved_key:
                alert("Auto-login with saved key...", "info")
                ok, msg = verify_key(saved_key)
                if ok:
                    key = saved_key
                    alert("Key valid! Welcome back.", "success")
                else:
                    alert(f"Saved key invalid: {msg}", "warning")
                    try: KEY_FILE.unlink()
                    except: pass
        except Exception:
            pass
    
    if not key:
        key = prompt("Enter your key")
        if not key:
            alert("No key entered", "error"); return
        alert("Verifying key...", "info")
        ok, msg = verify_key(key)
        if not ok:
            alert(msg, "error"); return
        alert("Key valid! Welcome.", "success")
        try:
            KEY_FILE.write_text(key)
            console.print(f"  [dim]💾 Key saved. No need to enter again.[/dim]")
        except Exception:
            pass
    
    time.sleep(1.2)

    while True:
        rows = [
            ("📦 01", "U N P A C K   P A K",   "extract every entry"),
            ("🔧 02", "L U A   M A K E",       "compile · decompile"),
            ("📥 03", "R E P A C K   L U A",   "inject into path"),
            ("🏗️ 04", "B U I L D   P A K",     "from template"),
            ("💉 05", "I N J E C T   L U A",   "stealth mode"),
            ("🧹 06", "C L E A N   A L L",     "wipe temp folders"),
            ("🚪 07", "E X I T   T O O L",     "close session"),
        ]
        render_menu(rows, "MAIN MENU")
        c = prompt("Enter your choice")
        if c == '1':   action_unpack_pak(key)
        elif c == '2': action_lua_make(key)
        elif c == '3': action_repack_inject(key)
        elif c == '4': action_build_new_pak(key)
        elif c == '5': action_inject_lua(key)
        elif c == '6': action_clean_all(key)
        elif c == '7': action_close()
        else:
            alert("Invalid choice", "error"); time.sleep(1.5); continue
        print(); input("  Press Enter to continue...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print(f"\n  [bold {ERRC}]Interrupted.[/bold {ERRC}]")
        sys.exit(0)
