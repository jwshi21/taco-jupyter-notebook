from IPython.core.display import display, HTML

css = open('./animation/custom.css', "r").read()

matrix = '<div class="array array-5">\
            <div class=elem></div>\
            <div class="elem">0</div>\
            <div class="elem">1</div>\
            <div class="elem">2</div>\
            <div class="elem">3</div>\
            <div class="elem">0</div>\
            <div id="a00" class="elem box">6</div>\
            <div class="elem box"></div>\
            <div id="a02"class="elem box">9</div>\
            <div id="a03"class="elem box">8</div>\
            <div class="elem">1</div>\
            <div class="elem box"></div>\
            <div class="elem box"></div>\
            <div class="elem box"></div>\
            <div class="elem box"></div>\
            <div class="elem">2</div>\
            <div id="a20"class="elem box">5</div>\
            <div class="elem box"></div>\
            <div class="elem box"></div>\
            <div id="a23"class="elem box">7</div></div>'

size = [('size', 'size', [3])]
data_columns = [('pos_c', 'pos', [0, 3, 3, 5]),
                ('idx_c', 'idx', [0, 2, 3, 0, 3])]  
values = [('vals', 'vals', [6, 9, 8, 5, 7])]

def pretty_display(html, data_pieces):
    html += '<div class="array array-7">'
    for piece in data_pieces:
        html = add_html(html, piece)
    return html

def add_html(html, data):
    for i in range(len(data)):
        element_id, label, numbers = data[i]   
        html += '<div class="elem">' + label + '</div>'
        for j in range(6):
            if j < len(numbers):
                html += '<div id="' + element_id + str(j) + '" class="elem box">' + str(numbers[j]) + '</div>'
            elif i == len(data) - 1:
                html += '<div class="elem extra-vertical-space"></div>'
            else:
                html += '<div class="elem"></div>'
    return html

html = pretty_display("", [size, data_columns, values]) + '</div>'

javascript = "<script>"

labels = ['"a00"', '"a02"', '"a03"', '"a20"', '"a23"']
instructions = ['"___0100"', '"___0111"', '"___0122"', '"___2333"', '"___2344"']

for i in range(len(labels)):
    label = labels[i];
    instruction = instructions[i];
    javascript += 'document.getElementById({}).onmouseover = function() {{mouse({}, "#0cf")}};\n'.format(label, instruction)
    javascript += 'document.getElementById({}).onmouseout = function() {{mouse({}, "#fff")}};'.format(label, instruction)

with open('./animation/javascript.txt', 'r') as file:
    javascript += file.read() + '</script>'

display(HTML(css + matrix + html + javascript))