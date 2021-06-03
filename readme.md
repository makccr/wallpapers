<a href="https://makc.co">
    <img src="https://makccr.github.io/images/github-header.svg" alt="MAKC lgoo" title="MAKC" align="right" height="60" />
</a>

# Wallpapers
This repository contains all of the Wallpapers that I regularly use on all of my systems (and phones). These wallpapers are usually actively in use in videos from my [YouTube Channel](https://www.youtube.com/user/mackenziegcriswell), so if you're visiting this repo from there, thanks for watching, and I hope you can find what you're looking for. 

![Sample of Wallpapers](https://raw.githubusercontent.com/makccr/wallpapers/master/thumb.jpg)

# Installation & Usage
The reason these wallpapers are in a Git Repo, rather than a zip file on my website, is so that they can be easily downloaded as part of an installation script, or just quickly on the command line -- to that end, a dimple ``git clone https://github.com/makccr/wallpapers``, will do the trick. But as the years go on, and I'm committing more and more changes to the repo, that will become increasingly unfeasible (and already is a pain in the ass) Every commit in this repo, is not, a few lines of code, but a multi-megabyte image. As such, my recommendation is to instead use: 

```
git clone --depth 1 https://github.com/makccr/wallpapers
```

This will download only the most recent branch of wallpapers, giving you access to all the images that can be browsed on the current version of this repo; but will not download the entire history of wallpapers. 

Additionally the structure of this folder might seem odd. After cloning, the folder structure will be something like: ``~/XMediaFolder/wallpapers/wallpapers/Xcollection/``. This seems stupid I know, but it's important, when using this repo with a wallpaper setter like [``feh``](https://www.bristolwatch.com/debian/feh.htm), or [``wal``](https://github.com/dylanaraps/pywal). Here we can run something like ``feh -r`` to recursively search the folder, and pick a random background from any of the collections. However, the standard ``/wallpapers`` folder also contains the ``.git`` directory, leaving ``feh`` trying to set git files as wallpapers. Therefore we have to bury our wallpapers one layer deeper: ``wallpapers/wallpapers/Xcollection``.

### Tech Specs
All of these images use the JPG format, spelled as ``.jpg``, not ``.jpeg`` for consistency. This is just to save on the file size. I find that I don't usually notice the difference between a JPG and a PNG or other higher quality image format (in the context of a wallpaper), and JPG files have significantly smaller file size; so I hope you see what I'm getting at. 

All of the wallpapers also have a minimum resolution of 1080p; and I'm slowly replacing the lower resolution wallpapers with 4K equivalents, or removing them entirely. But, for the time being, if you're using a display with a resolution higher than 1080p you might be careful just picking any image at random. 

### Devices
It also may be relevant to note that this library includes wallpapers intended for use on mobile (portrait) & desktop (landscape) layouts. These images aren't organized in any specific way, but the largest majority of images should also be of a high enough resolution that they can be used with either type of layout without any noticeable degradation. That being said, I do primarily work on a desktop or a laptop; so the majority of the images are collected with that in mind. There are some images that were collected specifically for use on a phone, and are in the proper orientation, but those are few and far between. This is a collection of images for use primarily on old school, you know... computers!
