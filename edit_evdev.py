import sys
import xml.etree.ElementTree as ET


# Find "ua" layout
def find_layout_node(root, layout_name):
    for layout in root.findall("./layoutList/layout"):
        for ci_name in layout.findall("./configItem/name"):
            if(ci_name.text == layout_name):
                return(layout)
    return(None)

class TElement(ET.Element):
    def __init__(self, tag, parent=None, text=None, attrib={}, **extra):
        super().__init__(tag, attrib, **extra)
        if(text):
            self.text = text
        if(parent is not None):
            parent.append(self)

tree = ET.parse(sys.argv[1])
root = tree.getroot()

layout = find_layout_node(root, "ua")
variant_list = layout.find("./variantList")

# Check if variant is already installed
for variant_name in variant_list.findall("./variant/configItem/name"):
    if(variant_name.text == "homophonic_altgr"):
        print("Variant is already installed in evdev.xml. Skipping")
        sys.exit(0)

# Install new variant
print("Installing 'homophonic_altgr' keyboard layout to evdev.xml.")
new_variant = TElement("variant", variant_list)
new_ci = TElement("configItem", new_variant)
TElement("name", new_ci, "homophonic_altgr")
TElement("description", new_ci, "Ukrainian (homophonic-AltGr)")

# Write out
with open(sys.argv[1], 'wb') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n'.encode('utf-8'))
    f.write('<!DOCTYPE xkbConfigRegistry SYSTEM "xkb.dtd">\n'.encode('utf-8'))
    tree.write(f, encoding="UTF-8", xml_declaration=False)
