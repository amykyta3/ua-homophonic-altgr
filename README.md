# Ukrainian Homophonic keyboard layout
This is an alternate Ukrainian homophonic keyboard layout that uses 3rd-level
keys to access additional Cyrillic characters.
This is unlike existing homophonic layouts that replace useful punctuation keys.

To install:
* Run install script as root: `sudo ./install.sh`
* Set right-alt to enable 3rd level keys.
* In language settings, add the new keyboard: `Ukrainian (homophonic-AltGr)`

## Enabling 3rd level AltGr
For most versions of Ubuntu, you can map a key for "3rd-level" keys
by finding the appropriate setting in the keyboard input GUI.

### Ubuntu 17.10
17.10 Does not have this setting available in the new keyboard settings GUI.

Instead, enable through `dconf-editor`:
* Navigate to: `/org/gnome/desktop/input-sources/xkb-options`
* Add the following entry to the value's list: `'lv3:ralt_switch'`

### XFCE:
Doesn't have the "3rd level option" in GUI.

```
sudo nano /usr/share/X11/xorg.conf.d.10-evdev.conf
```

In the appropriate section, add the option:
```
Option "XkbOptions" "lv3:ralt_switch"
```
    
So it looks like this:
```
Section "InputClass"
        Identifier "evdev keyboard catchall"
        MatchIsKeyboard "on"
        MatchDevicePath "/dev/input/event*"
        Driver "evdev"
        Option "XkbOptions" "lv3:ralt_switch"
EndSection
```
