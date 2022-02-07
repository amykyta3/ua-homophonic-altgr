import subprocess

def dconf_read(key):
    result = subprocess.run(['dconf', 'read', key], stdout=subprocess.PIPE)
    if(result.returncode):
        return(None)
    else:
        return(result.stdout.decode('utf-8'))

def dconf_write(key, value):
    subprocess.run(['dconf', 'write', key, value])


KEY="/org/gnome/desktop/input-sources/xkb-options"

opt_str = dconf_read(KEY)
try:
    options = eval(opt_str)
except SyntaxError:
    options = []

if('lv3:ralt_switch' not in options):
    options.append('lv3:ralt_switch')
    dconf_write(KEY, str(options))
    print("Enabled 'lv3:ralt_switch' in dconf")
else:
    print("'lv3:ralt_switch' is already enabled. Skipping")
