<a href="https://makc.co">
    <img src="https://makccr.github.io/images/github-header.svg" alt="MAKC lgoo" title="MAKC" align="right" height="50" />
</a>

# Wallpapers
This repository contains all of the Wallpapers that I regularly use on all of my systems (and phones). These wallpapers are usually actively in use in videos from my [YouTube Channel](https://www.youtube.com/user/mackenziegcriswell), so if you're visiting this repo from there, thanks for watching, and I hope you can find what you're looking for. If you are not a viewer of my channel, and just stumbled upon this repository, you will find an image below in which I attempt to provide a descent sample of the type of wallpapers that I store in this repo (it's mostly photos of the natural world, Russia & Romantic art, and some portraits of people I think are dope).

![Sample of Wallpapers](https://raw.githubusercontent.com/makccr/wallpapers/master/thumb.jpg)

## Installation & Usage
The reason these wallpapers are in a Git Repo, rather than a zip file on my website, is so that they can be easily downloaded as part of an installation script, or quickly on the command line -- to that end, a simple ``git clone https://github.com/makccr/wallpapers``, will do the trick. But as the years go on, and I'm committing more changes to the repo, that will become increasingly unfeasible. Every commit in this repo, is not, a few lines of code, but a multi-megabyte image. As such, my recommendation is to instead use: 

```
git clone --depth 1 https://github.com/makccr/wallpapers
```

This will download only the most recent branch of wallpapers, giving you access to all the images that can be browsed on the current version of this repo; but will not download the entire history of wallpapers. 

Additionally the structure of this folder might seem odd. After cloning, the folder structure will be something like: ``~/XMediaFolder/wallpapers/wallpapers/Xcollection/``. This seems stupid, I know, but it's important when using this repo with a wallpaper setter like [``feh``](https://www.bristolwatch.com/debian/feh.htm), or [``wal``](https://github.com/dylanaraps/pywal). Here we can run something like ``feh -r`` to recursively search the folder, and pick a random background from any of the collections. However, the standard ``/wallpapers`` folder also contains the ``.git`` directory, leaving ``feh`` trying to set git files as wallpapers. Therefore we have to bury our wallpapers one layer deeper: ``wallpapers/wallpapers/Xcollection``.

## Attributions
You can also view the [wiki page](https://github.com/makccr/wallpapers/wiki/Attributions) for links to the original artworks (at least where I found them), and attribution information. 

**Note:** The above mentioned is still very much in the; work in progress stage. As it turns out, it's much harder (more time consuming) to track down the source for random images than one might think.