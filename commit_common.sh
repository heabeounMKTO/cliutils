#!/bin/bash

if [ -z "$(git status -s -uno | grep -v '^ ' | awk '{print $2}')" ]; then
    gum confirm "Stage all?" && git add .
fi
echo "$(gum style --foreground 255 --background 65 'WHAT KIND OF COMMIT IS THIS')"
TYPE=$(gum choose "")
