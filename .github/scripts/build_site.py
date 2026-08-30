#!/usr/bin/env python3
"""Build thumbnail gallery site."""

import shutil
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from PIL import Image

REPO_ROOT = Path(__file__).parent.parent.parent
WALLPAPERS_DIR = REPO_ROOT / "wallpapers"
SITE_DIR = REPO_ROOT / "_site"
CACHE_DIR = REPO_ROOT / ".thumb-cache"
THUMB_PX = 256
IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp"}
GITHUB_RAW = "https://raw.githubusercontent.com/makccr/wallpapers/master/wallpapers"

SITE_CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
    font-family: system-ui, sans-serif;
    background: #0d1117;
    color: #e6edf3;
    min-height: 100vh;
}
header {
    padding: 2rem;
    border-bottom: 1px solid #21262d;
    display: flex;
    align-items: center;
    gap: 1rem;
}
header h1 { font-size: 1.5rem; font-weight: 600; }
header a { color: #e6edf3; text-decoration: none; }
header a:hover { color: #58a6ff; }
.breadcrumb { font-size: 0.9rem; color: #8b949e; }
.breadcrumb span { color: #58a6ff; }

main { padding: 2rem; }

/* folder grid */
.folders { display: flex; flex-wrap: wrap; gap: 1rem; margin-bottom: 2rem; }
.folder-card {
    background: #161b22;
    border: 1px solid #21262d;
    border-radius: 8px;
    padding: 1rem 1.5rem;
    cursor: pointer;
    transition: border-color 0.15s, background 0.15s;
    text-decoration: none;
    color: #e6edf3;
    display: flex;
    align-items: center;
    gap: 0.6rem;
    font-size: 0.95rem;
}
.folder-card:hover { border-color: #58a6ff; background: #1c2128; }
.folder-card .icon { font-size: 1.2rem; }
.folder-card .count { color: #8b949e; font-size: 0.8rem; }

/* image grid */
.grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
    gap: 12px;
}
.thumb-wrap {
    position: relative;
    overflow: hidden;
    border-radius: 6px;
    background: #161b22;
    aspect-ratio: 16 / 9;
    cursor: pointer;
}
.thumb-wrap img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.2s;
    display: block;
}
.thumb-wrap:hover img { transform: scale(1.05); }
.thumb-wrap .label {
    position: absolute;
    bottom: 0; left: 0; right: 0;
    background: linear-gradient(transparent, rgba(0,0,0,0.7));
    padding: 1.5rem 0.5rem 0.4rem;
    font-size: 0.7rem;
    color: #ccc;
    opacity: 0;
    transition: opacity 0.2s;
    word-break: break-all;
}
.thumb-wrap:hover .label { opacity: 1; }

/* lightbox */
#lb {
    display: none;
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,0.92);
    z-index: 100;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    gap: 1rem;
}
#lb.open { display: flex; }
#lb img { max-width: 90vw; max-height: 85vh; border-radius: 4px; }
#lb-close {
    position: absolute;
    top: 1rem; right: 1.5rem;
    font-size: 2rem;
    cursor: pointer;
    color: #ccc;
    background: none;
    border: none;
    line-height: 1;
}
#lb-dl {
    color: #58a6ff;
    font-size: 0.85rem;
    text-decoration: none;
}
#lb-dl:hover { text-decoration: underline; }
"""

LIGHTBOX_JS = """
const lb = document.getElementById('lb');
const lbImg = document.getElementById('lb-img');
const lbDl = document.getElementById('lb-dl');
document.querySelectorAll('.thumb-wrap').forEach(w => {
    w.addEventListener('click', () => {
        lbImg.src = w.dataset.full;
        lbDl.href = w.dataset.full;
        lbDl.download = w.dataset.name;
        lb.classList.add('open');
    });
});
document.getElementById('lb-close').addEventListener('click', () => lb.classList.remove('open'));
lb.addEventListener('click', e => { if (e.target === lb) lb.classList.remove('open'); });
document.addEventListener('keydown', e => { if (e.key === 'Escape') lb.classList.remove('open'); });
"""

THUMB_W = 320
THUMB_H = 180

def make_thumb(src: Path, dest: Path):
    """Generate 320x180 centre-cropped thumbnail using Pillow."""
    cache_path = CACHE_DIR / src.relative_to(WALLPAPERS_DIR).with_suffix(".jpg")
    if not cache_path.exists():
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        with Image.open(src) as img:
            img = img.convert("RGB")
            
            target_ratio > target_ratio: 
            w, h = img.size
            img_ratio = w /h 

            if img_ratio > target_ratio: 
                new_h = THUMB_H * 2
                new_w = int(new_h * img_ratio)
            else:
                new_w = THUMB_W * 2
                new_h = int(new_w /img_ratio)

            img = img.resize((new_w, new_h), Image.LANCZOS)

            left = (new_w - THUMB_W * 2) // 2
            top = (new_h - THUMB_H * 2) // 2
            img = img.crop((left, top, left + THUMB_W * 2, top + THUMB_H *2))

            img = img.resize ((THUMB_W, THUMB_H), Image.LANCZOS)
            img.save(cache_path, "JPEG", quality=85, optimize=True)

    shutil.copy2(cache_path, dest)


def _thumb_task(src: Path, dest: Path) -> tuple[str, str | None]:
    try:
        make_thumb(src, dest)
        return (src.name, None)
    except Exception as e:
        return (src.name, str(e)[:100])


def html_page(title: str, breadcrumb_html: str, body_html: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<style>{SITE_CSS}</style>
</head>
<body>
<header>
  <div>
    <div style="margin-bottom:.3rem">{breadcrumb_html}</div>
    <h1>{title}</h1>
  </div>
</header>
<main>
{body_html}
</main>
<div id="lb">
  <button id="lb-close">&times;</button>
  <img id="lb-img" src="" alt="">
  <a id="lb-dl" href="">&#x2193; Download original</a>
</div>
<script>{LIGHTBOX_JS}</script>
</body>
</html>
"""


def folder_page(folder_name: str, images: list[Path]) -> str:
    thumbs_html = ""
    for img in sorted(images):
        raw_url = f"{GITHUB_RAW}/{folder_name}/{img.name}"
        rel_thumb = f"thumbs/{img.stem}.jpg"
        thumbs_html += f"""
<div class="thumb-wrap" data-full="{raw_url}" data-name="{img.name}">
  <img src="{rel_thumb}" alt="{img.stem}" loading="lazy">
  <div class="label">{img.name}</div>
</div>"""
    breadcrumb = '<a href="../../index.html">Home</a> / <span>' + folder_name + '</span>'
    body = f'<div class="grid">{thumbs_html}\n</div>'
    return html_page(folder_name, breadcrumb, body)


def index_page(folders: list[tuple[str, int]]) -> str:
    cards = ""
    for name, count in sorted(folders):
        cards += f"""
<a class="folder-card" href="folders/{name}/index.html">
  <span class="icon">&#x1F5BC;</span>
  <span>{name}</span>
  <span class="count">{count} images</span>
</a>"""
    breadcrumb = '<span>Wallpapers</span>'
    body = f'<div class="folders">{cards}\n</div>'
    return html_page("Wallpapers Gallery", breadcrumb, body)


def build():
    CACHE_DIR.mkdir(exist_ok=True)
    if SITE_DIR.exists():
        shutil.rmtree(SITE_DIR)
    SITE_DIR.mkdir()

    folders_info = []
    tasks = []

    for folder in sorted(WALLPAPERS_DIR.iterdir()):
        if not folder.is_dir():
            continue
        images = [f for f in folder.iterdir() if f.suffix.lower() in IMAGE_EXTS]
        if not images:
            continue

        thumb_dir = SITE_DIR / "folders" / folder.name / "thumbs"
        thumb_dir.mkdir(parents=True)

        for img in images:
            tasks.append((img, thumb_dir / (img.stem + ".jpg"), folder.name, images))

        folders_info.append((folder.name, images))

    # Generate all thumbnails in parallel
    print(f"Generating {len(tasks)} thumbnails...")
    with ThreadPoolExecutor() as pool:
        futures = {pool.submit(_thumb_task, src, dest): src for src, dest, _, _ in tasks}
        done = 0
        for fut in as_completed(futures):
            name, err = fut.result()
            done += 1
            if err:
                print(f"  WARN {name}: {err}")
        print(f"  {done} done")

    # Write HTML pages
    seen = {}
    for _, _, folder_name, images in tasks:
        if folder_name not in seen:
            seen[folder_name] = images
    for folder_name, images in seen.items():
        page_html = folder_page(folder_name, images)
        (SITE_DIR / "folders" / folder_name / "index.html").write_text(page_html)

    (SITE_DIR / "index.html").write_text(index_page([(n, len(imgs)) for n, imgs in seen.items()]))
    print(f"Site built → {SITE_DIR}")


if __name__ == "__main__":
    build()
