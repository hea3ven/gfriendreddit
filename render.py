#! /usr/bin/python

banner = 'banner-lol'
love_banner = 'banner-love'

flairs = ['sinballoon', 'eunballoon', 'sourcelogo', 'sourcemusic', 'seasonofglass', 'flowerbud', 'snowflake']
flair_custom_widths = {
        'sourcemusic': 160
}
flair_size = 40
offset = 0

colors = {
# white
    'color0': '#F5FFF5',
# blue  #42acec
    'color1': '#0099EE',
    'color1hl': '#48B3EE',
    'color1dk': '#0099EE',
    'color1light': '#D9E7EE',
# yellow
    'color2': '#FFDD00',
    'color2light': '#FFFADC',
    'color2dk': '#C9AE00',
# green
    'color3': '#00DDBB',
    'color3hl': '#3CDDC4',
    'color3light': '#BDDDD8',
    'color3dk': '#0CAD94',

    'tabmenubg': 'rgba(12,173,148, 0.4)',
    'tabmenubghl': 'rgba(12,173,148, 0.6)',

# white
    # 'love_color0': '#FFF8FD',
    'love_color0': '#FFFFFF',
# pink  #42acec
    'love_color1': '#BA99AF',
    'love_color1hl': '#48B3EE',
    'love_color1dk': '#BA99AF',
    'love_color1light': '#D9E7EE',
# pink
    'love_color2': '#BA99AF',
    'love_color2light': '#FFFADC',
    'love_color2dk': '#BA99AF',
# green
    'love_color3': '#a0ae97',
    'love_color3hl': '#3CDDC4',
    'love_color3light': '#BDDDD8',
    'love_color3dk': '#ff7183',
    # 'love_color3dk': '#BA99AF',

    'love_tabmenubg': 'rgba(186,153,175, 0.4)',
    'love_tabmenubghl': 'rgba(186,153,175, 0.6)'
}

flairs_style = ''
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

with open('style.css') as f:
    style = f.read()

style = style.replace('/*BANNER_NAME*/', '%%' + banner + '%%')
style = style.replace('/*LOVE_BANNER_NAME*/', '%%' + love_banner + '%%')
style = style.replace('/*FLAIRS DATA*/', flairs_style)
for color_name, color_value in colors.items():
    style = style.replace('/*' + color_name.upper() + '*/', color_value)
print(style)
