#!/usr/bin/env bash

LATEST=$(curl -s https://api.github.com/repos/apex/apex/tags | grep -Eo '"name":.*?[^\\]",'  | head -n 1 | sed 's/[," ]//g' | cut -d ':' -f 2)
URL="https://github.com/apex/apex/releases/download/$LATEST/apex_linux_amd64"
DEST=~/.local/bin/apex

curl -sL ${URL} -o ${DEST}
chmod +x ${DEST}
