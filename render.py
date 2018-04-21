#! /usr/bin/python

banner = 'banner-5-parallel'
love_banner = 'banner-5-parallel'

sublogo = 'sublogo-4-parallel'
rddtlogo = 'rddtlogo-4-parallel'

flairs = ['sinballoon', 'eunballoon', 'sourcelogo', 'sourcemusic', 'seasonofglass', 'flowerbud', 'snowflake', 'lol', 'eunha', 'umji', 'sinb', 'yuju', 'sowon', 'yerin', 'mandurin', 'manduwon']
flair_custom_widths = {
        'sourcemusic': 160
}
flair_size = 40
offset = 0

sidebar = ['sidebar-mar-awak' + str(i) for i in range(1, 8)]

colors = {
# white
    'color0': '#edfaf9',
# turquoise
    'color1': '#8ceee9',
    'color1hl': '#e1eeed',
    'color1light': '#61bab5',
    'color1dk': '#90c9c6',
# turquoise
    'color4': '#8ceee9',
    'color4hl': '#e1eeed',
    'color4light': '#61bab5',
    'color4dk': '#90c9c6',
# green
    'color3': '#308b68',
    'color3hl': '#50bc93',
    'color3dk': '#1e664a',
    'color3light': '#a3e9ce',

    'tabmenubg': 'rgba(118,196,191, 0.4)',
    'tabmenubghl': 'rgba(156,238,233, 0.6)',
# green
    'color2': '#308b68',
    'color2hl': '#50bc93',
    'color2light': '#a3e9ce',
    'color2dk': '#1e664a',

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
