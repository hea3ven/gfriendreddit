#! /usr/bin/python

data = {}

flairs_style = ''

flairs = ['sinballoon', 'eunballoon', 'sourcelogo', 'sourcemusic', 'seasonofglass', 'flowerbud', 'snowflake']
flair_custom_widths = {
        'sourcemusic': 160
}
flair_size = 40
offset = 0

for flair in flairs:
    flairs_style += '.flair-%s {\n' % flair
    flairs_style += '    height: %dpx;\n' % flair_size
    if flair not in flair_custom_widths:
        flairs_style += '	width: %dpx;\n' % flair_size
    else:
        flairs_style += '	width: %dpx;\n' % flair_custom_widths[flair]
    flairs_style += '    background-position: -0px -%dpx;\n' % offset
    flairs_style += '    }\n'

    flairs_style += 'a[href$="%s"] {\n' % flair
    if flair not in flair_custom_widths:
        flairs_style += '	width: %dpx;\n' % flair_size
    else:
        flairs_style += '	width: %dpx;\n' % flair_custom_widths[flair]
    flairs_style += '	height: %dpx;\n' % flair_size
    flairs_style += '	content:"";\n'
    flairs_style += '	background-image:url(%%flairspritesheet2%%);\n'
    flairs_style += '   background-position: -0px -%dpx;\n' % offset
    flairs_style += '	position:relative;\n'
    flairs_style += '	display:inline-block;\n'
    flairs_style += '	cursor:default;\n'
    flairs_style += '}\n'

    offset += flair_size

data['flairs'] = flairs_style

with open('style.css') as f:
    style = f.read()

print(style.replace('/*FLAIRS DATA*/', flairs_style))
