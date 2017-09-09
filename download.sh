#!/bin/bash
URL=$1;
# sed -e 's/https:\/\/classevirtuelle.ulaval.ca\/\(.*\)\/?launcher.*/\1/'

VAR=$(sed 's/https:\/\/classevirtuelle.ulaval.ca\/\(.*\)\/?launcher.*/\1/' << EOF                                                                                                                 
$URL
EOF
)
echo $VAR

xdg-open https://classevirtuelle.ulaval.ca/$VAR/output/$VAR.zip?download=zip
