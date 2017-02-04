Setup systemd

(Be sure to check if you need SUDO access to make thease commands)

1. Enter this at the command prompt to copy the file from the repository to the systemd folder

    sudo cp sparc_htm.service /lib/systemd/system/

2. Enable the service

    sudo systemctl enable sparc_htm.service

3. Reload the systemctl daemon

    sudo systemctl daemon-reload

4. Start the service
    
    sudo systemctl start sparc_htm.service

5. Check status

    sudo systemctl status sparc_htm.service
