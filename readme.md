# 🖼️ Wallpapers
This repository contains the wallpapers I use across all my devices—desktop, laptop, and phone. A few were designed by me and originally released on my [personal website](https://makc.co/downloads), but most were discovered (or commandeered) from far more talented artists and photographers online. Many of them also appear in videos on my [YouTube channel](https://www.youtube.com/@makc)—so if you’re here from there, thanks for watching!

If you’ve stumbled across this repo by chance—Welcome! Inside, you’ll find a curated collection of wallpapers mostly featuring:

- Nature & landscapes  
- Romantic, Russian, and Religious art (plus a few other types that break the alliteration)  
- Abstract visuals and subtle backgrounds that look good without stealing focus  
- Oceans, boats, and coastlines

## 🚀 Installation & Usage
This repo is structured for convenience—especially for scripts or terminal-based setups.

To clone the latest version of the wallpapers **without the full git history** (which can be large due to image sizes), run:

```bash
git clone --depth 1 https://github.com/makccr/wallpapers
```
⚠️ Each commit includes full-resolution image files—over time this makes the full history impractically large. Use ```--depth 1``` unless you have a reason not to.

### 📁 Folder Structure
After cloning, the structure will look like: ```📁 ~/XMediaFolder/wallpapers/wallpapers/Xcollection/```

Yes, there’s a duplicated ```wallpapers/``` folder. This is intentional. Tools like feh or pywal rely on recursive file discovery. Keeping image files one level deeper avoids issues with .git/ directories being mistaken for images.

**Example usage with feh:**

```
feh -r ~/photos/wallpapers/wallpapers/people --bg-scale
```

## 📚 Attributions
Sources and credits for the images are listed on the [Wiki page](https://github.com/makccr/wallpapers/wiki).

🛠️ Still, very much a work in progress—tracking down original sources for random images is more time-consuming than expected.
