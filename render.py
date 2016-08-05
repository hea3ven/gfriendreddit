#! /usr/bin/python

banner = 'banner-laugh'
love_banner = 'banner-love'

flairs = ['sinballoon', 'eunballoon', 'sourcelogo', 'sourcemusic', 'seasonofglass', 'flowerbud', 'snowflake', 'lol', 'eunha', 'umji', 'sinb', 'yuju', 'sowon', 'yerin', 'mandurin', 'manduwon']
flair_custom_widths = {
        'sourcemusic': 160
}
flair_size = 40
offset = 0

colors = {
# white
    'color0': '#e4f0f8',
    # 'color0': '#a5c4d7',
# green
    'color1': '#27d09c',
    'color1hl': '#7ef0cd',
    'color1dk': '#127c5b',
    'color1light': '#c5e1d9',
# yellow
    'color2': '#eb9b1a',
    'color2light': '#f3e1c6',
    'color2dk': '#886328',
# blue
    'color3': '#3d9dd7',
    'color3hl': '#7fc4ee',
    'color3light': '#BDDDD8',
    'color3dk': '#246d99',

    'tabmenubg': 'rgba(61,157,215, 0.4)',
    'tabmenubghl': 'rgba(61,157,215, 0.6)',
# red
    'color4': '#db3d3f',
    'color4hl': '#e67f81',
    'color4dk': '#9e393a',
    'color4light': '#e1c7c7',
# # white
#     'color0': '#F5FFF5',
# # blue  #42acec
#     'color1': '#0099EE',
#     'color1hl': '#48B3EE',
#     'color1dk': '#0099EE',
#     'color1light': '#D9E7EE',
# # yellow
#     'color2': '#FFDD00',
#     'color2light': '#FFFADC',
#     'color2dk': '#C9AE00',
# # green
#     'color3': '#00DDBB',
#     'color3hl': '#3CDDC4',
#     'color3light': '#BDDDD8',
#     'color3dk': '#0CAD94',
#
#     'tabmenubg': 'rgba(12,173,148, 0.4)',
#     'tabmenubghl': 'rgba(12,173,148, 0.6)',

# white
    # 'love_color0': '#FFF8FD',
    'love_color0': '#faf4e7',
# pink  #42acec
    'love_color1': '#dc9d12',
    'love_color1hl': '#e6b850',
    'love_color1dk': '#88610b',
    'love_color1light': '#dccfb1',
# pink
    'love_color1': '#dc9d12',
    'love_color1hl': '#e6b850',
    'love_color1dk': '#88610b',
    'love_color1light': '#dccfb1',
# green
    'love_color3': '#dc9d12',
    # 'love_color3': '#3d293a',
    'love_color3hl': '#e6b850',
    'love_color3light': '#88610b',
    'love_color3dk': '#dccfb1',
    # 'love_color3dk': '#BA99AF',

    'love_tabmenubg': 'rgba(220,157,18, 0.4)',
    'love_tabmenubghl': 'rgba(220,157,18, 0.6)'
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

    flairs_style += 'a[href$="#%s"] {\n' % flair
    if flair not in flair_custom_widths:
        flairs_style += '	width: %dpx;\n' % flair_size
    else:
        flairs_style += '	width: %dpx;\n' % flair_custom_widths[flair]
    flairs_style += '	height: %dpx;\n' % flair_size
    flairs_style += '	content:"";\n'
    flairs_style += '	background-image:url(%%flairspritesheet%%);\n'
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
