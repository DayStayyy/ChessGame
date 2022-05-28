#!/bin/bash
# To create gdrive you must do rclone config first
/user/bin/rclone copy --update --verbose --transfers 30 --checkers 8 --contimeout 60s --timeout 300s --retries 3 --low-level-retries 10 --stats 1s "var/ProjetInfra/chessgame" "gdrive:backup"