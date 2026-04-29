#!/usr/bin/env python3
"""Build thumbnail gallery site for GitHub Pages."""

import os
import shutil
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.parent
WALLPAPERS_DIR = REPO_ROOT / "wallpapers"
SITE_DIR = REPO_ROOT / "_site"
THUMB_SIZE = "256x256"
IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp"}

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
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 12px;
}
.thumb-wrap {
    position: relative;
    overflow: hidden;
    border-radius: 6px;
    background: #161b22;
    aspect-ratio: 1;
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


def make_thumb(src: Path, dest: Path):
    dest.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run([
        "convert", str(src),
        "-thumbnail", f"{THUMB_SIZE}^",
        "-gravity", "center",
        "-extent", THUMB_SIZE,
        str(dest),
    ], check=True, capture_output=True)


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


def folder_page(folder_name: str, images: list[Path], folder_path_in_site: str) -> str:
    thumbs_html = ""
    for img in sorted(images):
        rel_full = f"../../wallpapers/{folder_name}/{img.name}"
        rel_thumb = f"thumbs/{img.stem}.jpg"
        thumbs_html += f"""
<div class="thumb-wrap" data-full="{rel_full}" data-name="{img.name}">
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
    if SITE_DIR.exists():
        shutil.rmtree(SITE_DIR)
    SITE_DIR.mkdir()

    # Copy originals into _site/wallpapers/ so relative links work
    dest_wp = SITE_DIR / "wallpapers"
    print("Copying wallpapers...")
    shutil.copytree(WALLPAPERS_DIR, dest_wp)

    folders_info = []

    for folder in sorted(WALLPAPERS_DIR.iterdir()):
        if not folder.is_dir():
            continue
        images = [f for f in folder.iterdir() if f.suffix.lower() in IMAGE_EXTS]
        if not images:
            continue

        folder_site = SITE_DIR / "folders" / folder.name
        thumb_dir = folder_site / "thumbs"
        thumb_dir.mkdir(parents=True)

        print(f"  {folder.name}: {len(images)} images")
        for img in images:
            thumb_dest = thumb_dir / (img.stem + ".jpg")
            try:
                make_thumb(img, thumb_dest)
            except subprocess.CalledProcessError as e:
                print(f"    WARN: thumb failed for {img.name}: {e.stderr.decode()[:80]}")

        page_html = folder_page(folder.name, images, f"folders/{folder.name}")
        (folder_site / "index.html").write_text(page_html)
        folders_info.append((folder.name, len(images)))

    (SITE_DIR / "index.html").write_text(index_page(folders_info))
    print(f"Site built → {SITE_DIR}")


if __name__ == "__main__":
    build()
