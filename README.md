# dotfiles
## Fedora 32 (xfce)
![fedora-32-dsektop](https://i.imgur.com/ZtkFzdJ.png)

After install:
1. In terminal:
```
$ sudo dnf update
$ sudo rpm -Uvh http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm
$ sudo rpm -Uvh http://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
$ sudo hostnamectl set-hostname zen
$ sudo dnf install gimp vlc gcolor3 inkscape geany hugo htop plank dconf-editor git
```
2. Install [chrome](https://www.google.com/chrome/)
3. Install [Visual Studio Code](https://code.visualstudio.com/docs/setup/linux#_rhel-fedora-and-centos-based-distributions)
4. Install plank themes from Eric Dubois github [repository](https://github.com/erikdubois/plankthemes). Place in .local/share/plank/themes.  Plank theme in image is 'shade'
```
$ git clone https://github.com/erikdubois/plankthemes.git
```
