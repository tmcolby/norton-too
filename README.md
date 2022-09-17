# norton-too
Catch all for Norton too

### My sigK plugins
signalk-datetime
signalk-geekworm-x728

### Virtual keyboard
https://pimylifeup.com/raspberry-pi-on-screen-keyboard/  

Install
```
sudo apt update && sudo apt install matchbox-keyboard
```

Link
```
sudo ln -s /home/tyson/dev/norton-too/toggle-keyboard.sh /usr/bin/
```

Toggle
```
sudo cp toggle-keyboard.desktop /usr/share/raspi-ui-overrides/applications/
cp /etc/xdg/lxpanel/LXDE-pi/panels/panel /home/tyson/.config/lxpanel/LXDE-pi/panels/panel
echo "Plugin {
  type=launchbar
  Config {
    Button {
      id=toggle-keyboard.desktop
    }
  }
}
" >> /home/tyson/.config/lxpanel/LXDE-pi/panels/panel
```
