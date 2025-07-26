# 🖼️ Wallpapers
This repository contains the wallpapers I use across all my devices—desktop, laptop, and phone. A few were designed by me and originally released on my [personal website](https://makc.co/downloads), but most were discovered (or commandeered) from far more talented artists and photographers online. Many of them also appear in videos on my [YouTube channel](https://www.youtube.com/@makc)—so if you’re here from there, thanks for watching!

If you’ve stumbled across this repo by chance—Welcome! Inside, you’ll find a curated collection of wallpapers mostly featuring:

- Nature & landscapes  
- Romantic, Russian, and Religious art (plus a few other types that break the alliteration)  
- Abstract visuals and subtle backgrounds that look good without stealing focus  
- Oceans, boats, and coastlines

## 📚 Attributions
Sources and credits for the images are listed on the [Wiki page](https://github.com/makccr/wallpapers/wiki), and can be located by clicking on ```📚 Wallpaper Attributions```.

## 🚀 Installation & Usage
This repo is structured for convenience—especially for scripts or terminal-based setups. To clone the latest version of the wallpapers **without the full git history**, run:
```bash
git clone --depth 1 https://github.com/makccr/wallpapers
```
⚠️ Each commit includes full-resolution image files. Git actually handles this surprisingly well, as the full size of the repository (as of July 2025) is just a bit over 1gb. However I would still reccommend using ```--depth 1``` unless you have a reason not to. This flag simply tells git to only pull the most recent commit, as opposed to the entire history of the repository. 

### 📁 Folder Structure
After cloning, the structure will look like: ```📁 ~/XMediaFolder/wallpapers/wallpapers/Xcollection/``` Yes, there’s a duplicated ```📁 /wallpapers/``` folder. This is intentional. Tools like [feh](https://wiki.archlinux.org/title/Feh), [nitrogen](https://wiki.archlinux.org/title/Nitrogen) or [pywal](https://github.com/dylanaraps/pywal) rely on recursive file discovery. Keeping image files one level deeper avoids issues with ```📁 .git/``` files & directories being mistaken for images.

**Example usage with feh:**
```
feh -r ~/photos/wallpapers/wallpapers/people --bg-scale
```

## Categories
### 🎨 [Abstract](https://github.com/makccr/wallpapers/tree/master/wallpapers/abstract)
A curated collection of tech-inspired and nature-driven abstract wallpapers—designed to look dope without demanding attention. These backgrounds blend form and function, keeping your desktop clean, focused, and ready for work. No distractions. Just vibes.
### 🐾 [Animals](https://github.com/makccr/wallpapers/tree/master/wallpapers/animals)
A curated collection of high-quality animal wallpapers—featuring everything from deep-sea creatures to majestic African wildlife. These photos are vivid and natural, striking without being overwhelming. Perfect for keeping your desktop wild—but still calm, clean, and focused.
### 🏛️ [Architecture](https://github.com/makccr/wallpapers/tree/master/wallpapers/architecture)
This section features a mix of monumental structures from across history—primarily Greek, Roman, and ancient European architecture. You’ll also find standout examples of modern design and a touch of 18th- and 19th-century American architecture. From crumbling columns to sleek steel, these images capture form, symmetry, and human ambition in built form.
### 🖼️ [Art](https://github.com/makccr/wallpapers/tree/master/wallpapers/art)
This section features a carefully selected collection of Romantic, Russian, and Religious artwork—rich in atmosphere, emotion, and symbolism. Expect dramatic lighting, sacred iconography, and sweeping historical scenes. These wallpapers carry weight and mood, often blurring the line between reverence and rebellion.
### 🌄 [Landscapes](https://github.com/makccr/wallpapers/tree/master/wallpapers/landscape)
A diverse collection of landscapes spanning American, European, and Mediterranean scenes. From rolling hills and dense forests to sun-drenched coasts and rugged mountains, these wallpapers capture the natural beauty and varied moods of these regions.
### 💡 [Light](https://github.com/makccr/wallpapers/tree/master/wallpapers/light)
A collection of bright, vibrant wallpapers that might break dark mode—but in the best way. These backgrounds bring energy and contrast, perfect if you want your desktop to pop with bold, eye-catching visuals.
### 🅼 [Makc](https://github.com/makccr/wallpapers/tree/master/wallpapers/makc)
A collection of wallpapers inspired by nerdy tech culture—featuring Linux distro wallpapers, yin-yang motifs, retro tech brands, and even logos for classic command-line tools like Vim. If you're as big of a tech nerd as me you might be into this collection, but most can probably just float right over this category. If you're looking for my [Paper Collection(https://youtu.be/HE8LJBw2oCI) specifically, you'll have to pull that from my [personal site](https://makc.co/downloads), it's absolutely massive and I don't want to drop it in here.
### 🎨 [Maller](https://github.com/makccr/wallpapers/tree/master/wallpapers/maller)
The entire collection is just art from [Justin Maller](https://justinmaller.com/), featuring mainly his abstract, unbranded wallpapers—all in sharp 1080p resolution (sorry about that, you can run it through one of those AI upscale tools if you want). Expect bold shapes, vivid colors, and dynamic compositions perfect for making your desktop pop.
### 👥 [People](https://github.com/makccr/wallpapers/tree/master/wallpapers/people)
A curated gallery of portraits featuring influential authors, iconic figures like Audrey Hepburn, historic presidents, and select modern personalities. These wallpapers celebrate individuals who have left a mark on culture, history, and inspiration.
### 🌊 [Poseidon](https://github.com/makccr/wallpapers/tree/master/wallpapers/poseidon)
A collection dedicated to the sea—featuring breathtaking coastlines, serene oceans, and boats that evoke a sense of adventure and calm. Perfect for those who find inspiration in salt air and endless horizons-or those of us who just really like Rum.
### 🌈 [Psychedelic](https://github.com/makccr/wallpapers/tree/master/wallpapers/psychedelic)
A wild ride of visuals inspired by psychedelic art—think vivid colors, swirling patterns, and mind-bending designs. Perfect for fans of DMT-inspired creativity and surreal, trippy vibes.
### 🚀 [Space](https://github.com/makccr/wallpapers/tree/master/wallpapers/space)
In case the seas wasn't for you: explore the cosmos with wallpapers featuring stars, planets, galaxies, and the vast mysteries of the universe. Perfect for those inspired by the infinite and the unknown.
### 💻 [Windows & MacOS](https://github.com/makccr/wallpapers/tree/master/wallpapers/win-mac)
The classic default wallpapers from Windows and MacOS—those iconic images we all grew up with. Don't be a linux snob. Windows and MacOS suck, but they have managed to source some talented artists over the years of development. 
