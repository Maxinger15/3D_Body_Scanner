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

### Mount Samba Share
[Link](https://support.zadarastorage.com/hc/en-us/articles/213024986-How-to-Mount-a-SMB-Share-in-Ubuntu)
