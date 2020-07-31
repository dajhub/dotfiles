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
$ sudo dnf install gimp vlc gcolor3 inkscape geany hugo htop plank dconf-editor git slick-greeter spacefm rofi
```
2. Install [chrome](https://www.google.com/chrome/)
3. Install [Visual Studio Code](https://code.visualstudio.com/docs/setup/linux#_rhel-fedora-and-centos-based-distributions)
4. Install plank themes from Eric Dubois github [repository](https://github.com/erikdubois/plankthemes). Place in .local/share/plank/themes.  Plank theme in above image is 'shade'
```
$ git clone https://github.com/erikdubois/plankthemes.git
```
5. Themes and icons to install from xfce themes site:
   - [qogir light](https://www.xfce-look.org/p/1230631/)
   - [tela blue](https://www.xfce-look.org/p/1279924/)
   - [dots theme](https://www.xfce-look.org/p/1151531/)

6. Procedure for installing light-locker and then replacing the default 'xscreensaver'
   ```
   $ sudo dnf install light-locker
   $ sudo dnf remove xscreensaver-base
   $ xfconf-query -c xfce4-session -p /general/LockCommand -s "light-locker-command -l" --create -t string
   ```
7. Rofi - see rofi folder.  Script to go into ```.config/rofi/config.rasi```.  Keyboard shortcut is ```rofi -combi-modi window,drun -show combi -modi combi```