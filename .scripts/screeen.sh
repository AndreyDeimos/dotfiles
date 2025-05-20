#!/bin/bash
HEADLESS=$(hyprctl -j monitors | jq -r '.[] | select(.name | test("HEADLESS-"; "i")).name')
echo $HEADLESS
if [$HEADLESS == ""];
then
  hyprctl output create headless &
  O_PID=$!
  wait $O_PID
  dunstify "created display"
else 
  hyprctl output remove "$HEADLESS"
  dunstify "removed display"
fi
