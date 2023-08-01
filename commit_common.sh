#!/bin/bash

if [ -z "$(git status -s -uno | grep -v '^ ' | awk '{print $2}')" ]; then
    gum confirm "are we staging all the changes?" && git add .
fi

echo "$(gum style --foreground 212 'what kind of commit would you like to make, sir?')"
TYPE=$(gum choose "fix" "feat" "docs" "refactor" "test" "chore" "revert" "penis" "custom" "nevermind")

if [ $TYPE = "custom" ]; then
  clear;
  TYPE=$(gum input --placeholder "your custom commit type please sir")
elif [ $TYPE = "nevermind" ]; then
  clear;
  echo "$(gum style --foreground 212 'exiting then...')"
  exit 0
fi
clear;
echo "$(gum style --foreground 212 --background 62 'Summary of your changes sir')"
SUMMARY=$(gum input --value "$TYPE :" --placeholder "")
DESCRIPTION=$(gum write --placeholder "Details, if you care to elaborate")

gum confirm "Commit changes right now sir?" && git commit -m "$SUMMARY" -m "$DESCRIPTION"
gum confirm "Do you want to push to remote?" && git push
