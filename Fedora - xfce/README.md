# dotfiles

## Fedora 32 (xfce)
![fedora-32-desktop](https://i.imgur.com/ZtkFzdJ.png)

After installing:
1. In terminal:
   ```
   $ sudo dnf update
   $ sudo rpm -Uvh http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm
   $ sudo rpm -Uvh http://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
   $ sudo hostnamectl set-hostname zen
   $ sudo dnf install gimp vlc gcolor3 inkscape geany hugo htop plank dconf-editor git slick-greeter spacefm rofi isoimagewriter clementine xed google-noto-sans-mono-fonts.noarch
   ```
2. Install [chrome](https://www.google.com/chrome/)
3. Install [Visual Studio Code](https://code.visualstudio.com/docs/setup/linux#_rhel-fedora-and-centos-based-distributions)
4. Install plank themes from Eric Dubois github [repository](https://github.com/erikdubois/plankthemes). Place in .local/share/plank/themes.  Plank theme in above image is 'shade'
   ```
   $ git clone https://github.com/erikdubois/plankthemes.git
   ```
   Plank settings (i.e. placement of icons) should be placed in .config folder

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
7. Rofi:  see rofi folder.  Script to go into ```.config/rofi/config.rasi```.  Keyboard shortcut is ```rofi -combi-modi window,drun -show combi -modi combi```

8. [Wallpapers](https://drive.google.com/drive/folders/1pYbUg8BJSaZeqtZjX1ehHKiqr3IuTfLu?usp=sharing)
   
9. Installing virtualbox using these [instructions](https://computingforgeeks.com/how-to-install-vagrant-and-virtualbox-on-fedora/):
    ```
    $ sudo dnf -y install wget
    $ wget http://download.virtualbox.org/virtualbox/rpm/fedora/virtualbox.repo
    $ sudo mv virtualbox.repo /etc/yum.repos.d/virtualbox.repo
    $ sudo dnf install -y gcc binutils make glibc-devel patch libgomp glibc-headers  kernel-headers kernel-devel-`uname -r` dkms
    $ sudo dnf install -y VirtualBox-6.1
    $ sudo usermod -a -G vboxusers ${USER}
    $ sudo /usr/lib/virtualbox/vboxdrv.sh setup

10. Remove some default applications:
    ```
    $ sudo dnf remove pidgin parole
