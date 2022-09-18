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

### i2c map
`i2cdetect -y 1`  
```
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- 36 -- -- -- -- -- -- -- -- -- 
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- UU -- -- -- -- 6d 6e 6f 
70: -- -- -- -- -- -- -- 77
```
0x36 Geekworm UPS x728 
0x77 BME280 environment sensor
0x6d Button 1
0x6e Button 2
0x6f Button 3
