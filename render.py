#! /usr/bin/python

banner = 'banner-3-military'
love_banner = 'banner-4-knight'

sublogo = 'sublogo-3-awak'
rddtlogo = 'rddtlogo-3-awak'

flairs = ['sinballoon', 'eunballoon', 'sourcelogo', 'sourcemusic', 'seasonofglass', 'flowerbud', 'snowflake', 'lol', 'eunha', 'umji', 'sinb', 'yuju', 'sowon', 'yerin', 'mandurin', 'manduwon']
flair_custom_widths = {
        'sourcemusic': 160
}
flair_size = 40
offset = 0

sidebar = ['sidebar-mar-awak' + str(i) for i in range(1, 8)]

colors = {
# white
    'color0': '#fef9f1',
    # 'color0': '#a5c4d7',
# grey
    'color1': '#2f1c0b',
    'color1hl': '#d7ccc2',
    'color1light': '#d7ccc2',
    'color1dk': '#1e1207',
# pale
    'color2': '#d4c4a3',
    'color2hl': '#e9dec7',
    'color2light': '#fff3da',
    'color2dk': '#a8a090',
# green
    'color3': '#616238',
    'color3hl': '#eef089',
    'color3dk': '#2c2d19',
    'color3light': '#e3e4ce',

    'tabmenubg': 'rgba(157,186,106, 0.4)',
    'tabmenubghl': 'rgba(119,146,72, 0.6)',
# light brown
    'color4': '#86632a',
    'color4hl': '#fadfb2',
    'color4light': '#f8e2be',
    'color4dk': '#5e5443',
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
    'love_color0': '#ffffff',
# pink  #42acec
    'love_color1': '#0e021b',
    'love_color1hl': '#c7c3dc',
    'love_color1dk': '#010103',
    'love_color1light': '#dedde1',
# pink
    'love_color2': '#0e021b',
    'love_color2hl': '#c7c3dc',
    'love_color2dk': '#010103',
    'love_color2light': '#dedde1',
# green
    'love_color3': '#0e021b',
    'love_color3hl': '#c7c3dc',
    'love_color3dk': '#010103',
    'love_color3light': '#dedde1',

    'love_tabmenubg': 'rgba(14,2,27, 0.3)',
    'love_tabmenubghl': 'rgba(14,2,27, 0.5)'
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

sidebar_pics = []
i = 0
while len(sidebar_pics) < 36:
    sidebar_pics.append(sidebar[i])
    i += 1
    if i >= len(sidebar):
        i = 0


with open('style.css') as f:
    style = f.read()

style = style.replace('/*BANNER_NAME*/', '%%' + banner + '%%')
style = style.replace('/*LOVE_BANNER_NAME*/', '%%' + love_banner + '%%')
style = style.replace('/*RDDTLOGO_NAME*/', '%%' + rddtlogo + '%%')
style = style.replace('/*LOVE_RDDTLOGO_NAME*/', '%%' + rddtlogo + '%%')
style = style.replace('/*SUBLOGO_NAME*/', '%%' + sublogo + '%%')
style = style.replace('/*LOVE_SUBLOGO_NAME*/', '%%' + sublogo + '%%')
style = style.replace('/*FLAIRS DATA*/', flairs_style)
for color_name, color_value in colors.items():
    style = style.replace('/*' + color_name.upper() + '*/', color_value)
for i, sidebar_pic in enumerate(sidebar_pics):
    style = style.replace('/*SIDEBAR_PIC_' + str(i) + '*/', '%%' + sidebar_pic + '%%')
style = style.replace('/*LOVE_BANNER_NAME*/', '%%' + love_banner + '%%')

print(style)
