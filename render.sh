#/bin/sh -e

ID=$$
cat map.html.template | sed s/SPECIES/"$1"/g > tmp/map.$ID.html
python python-webkit2png/webkit2png/scripts.py http://localhost/maprender/tmp/map.$ID.html -x 900 900 -W --output=tmp/map.$ID.png -F javascript
rm tmp/map.$ID.html
echo $ID

