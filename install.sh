#!/bin/bash

set -e
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

error() {
    printf "ERROR: %s\n" "$*" >&2;
    exit 1
}

# Find location of symbol file
candidates="
    /usr/share/X11/symbols/ua
    /usr/share/X11/xkb/symbols/ua
"
for f in $candidates; do
    if [ -f $f ]; then
        symbol_file=$f
        break
    fi
done
if [ -z $symbol_file ]; then
    error "Could not find a symbol file to modify"
fi

# Location of evdev file
evdev_file=/usr/share/X11/xkb/rules/evdev.xml


# Add layout to symbol file
if grep -Pq "^xkb_symbols\s+\"homophonic_altgr\"" "$symbol_file"; then
    echo "Layout is already installed in symbol file. Skipping."
else
    echo "Installing 'homophonic_altgr' keyboard layout to symbols file."
    cat $DIR/ua-homophonic-altgr >> $symbol_file
fi

# Add variant entry to evdev.xml file
python3 $DIR/edit_evdev.py $evdev_file

# Enable right-alt as lvl3 key
python3 $DIR/edit_dconf.py
