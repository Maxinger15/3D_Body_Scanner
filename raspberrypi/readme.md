These are the scripts you have to install on your raspis.
Change the folders in the script like you need it.

### How they work
1. Connect to mqtt broker
2. take a picture when notified
3. chache pictures local
4. copy pictures do folder (in my case a samba share) and delete local chached pictures


### Run pythonscript on startup as a service
1. sudo nano /lib/systemd/system/scanner.service
2. Copy and Paste:
```
[Unit]
Description=ScannerPythonScript
After=syslog.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 /fotos/listen_os.py
Restart=always
RestartSec=2
SyslogIdentifier=scannerListener

[Install]
WantedBy=multi-user.target

```

3. Save and close the file
4. sudo systemctl daemon-reload
5. sudo systemctl start scanner
6. sudo systemctl enable scanner
7. sudo systemctl daemon-reload

### Install pillow
```
sudo apt-get update && sudo apt-get install libjpeg-dev -y && sudo apt-get install zlib1g-dev -y && sudo apt-get install libfreetype6-dev -y && sudo apt-get install liblcms1-dev -y && sudo apt-get install libopenjp2-7 -y && sudo apt-get install libtiff5 -y && sudo pip3 install pillow
```

webp:
```
python3 -m pip install --upgrade Pillow --no-cache-dir
sudo apt install libwebp-dev

```


