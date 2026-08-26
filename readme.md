<a href="https://wallpapers.makc.co">
    <img src="https://makc.co/images/github-header.svg" alt="MAKC lgoo" title="MAKC" align="right" height="50" />
</a>

# [Wallpapers](https://wallpapers.makc.co)
This repository contains the wallpapers I use across all my devices—desktop, laptop, and phone. A few were designed by me and originally released on my [personal website](https://makc.co/downloads), but most were discovered (or commandeered) from far more talented artists and photographers online. Many of them also appear in videos on my [YouTube channel](https://www.youtube.com/@makc)—so if you’re here from there, thanks for watching!

If you’ve stumbled across this repo by chance—Welcome! Inside, you’ll find a curated collection of wallpapers featuring but not not limited to:

- Nature & landscapes  
- Romantic, Russian, and Religious art (plus a few other types that break the alliteration)  
- Abstract visuals and subtle backgrounds that look good without stealing focus  
- Oceans, boats, and coastlines
- Some general nature goodness

## Browsing

## Installation & Usage
This repo is structured for convenience—especially for scripts or terminal-based setups. To clone the latest version of the wallpapers **without the full git history**, run:
```bash
git clone --depth 1 https://github.com/makccr/wallpapers
```
**Note**: Each commit includes full-resolution image files. Git actually handles this surprisingly well, as the full size of the repository (as of July 2025) is just a bit over 1gb. However I would still reccommend using ```--depth 1``` unless you have a reason not to. This flag simply tells git to only pull the most recent commit, as opposed to the entire history of the repository. 

### Folder Structure
After cloning, the structure will look like: ```~/XMediaFolder/wallpapers/wallpapers/Xcollection/``` Yes, there’s a duplicated ```/wallpapers/``` folder. This is intentional. Tools like [feh](https://wiki.archlinux.org/title/Feh), [nitrogen](https://wiki.archlinux.org/title/Nitrogen) or [pywal](https://github.com/dylanaraps/pywal) rely on recursive file discovery. Keeping image files one level deeper avoids issues with ```.git/``` files & directories being mistaken for images.

**Example usage with feh:**
```bash
awww img ~/Pictures/wallpapers/wallpapers/abstract/neon-dream.jpg
```

#### Setting a Random Wallpaper in a Directory
Some image setting applications (particularly minimal ones) are pretty bad at parsing a directory, the following find command will let you bypass limitations: 

```bash
image-setter "$(find PATH -type f | shuf -n 1)"
```

**Example Usage with awww:**
```bash
awww img "$(find ~/Pictures/wallpapers/wallpapers/poseidon -type f | shuf -n 1)" --transition-type none
```
