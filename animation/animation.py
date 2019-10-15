from IPython.core.display import display, HTML

css = open('./animation/custom.css', "r").read()

def generate_matrix(file_id, data_matrix):
    matrix = '<div class="array array-5"><div class=elem></div>'
    for i in range(len(data_matrix[0])):
        matrix += '<div class="elem">{}</div>'.format(i)
    
    for i in range(len(data_matrix)):
        matrix += '<div class="elem">{}</div>'.format(i)
        for j in range(len(data_matrix[0])):
            element = data_matrix[i][j]
            element_id = file_id + 'a' + str(i) + str(j)
            matrix += '<div id="{}" class="elem box">{}</div>'.format(element_id, element)
    
    return matrix + '</div>'

def generate_html(file_id, data_list):
    html = '<div class="array array-9">'
    for data in data_list:
        html = add_html(file_id, html, data)
    return html + '</div>'

def add_html(file_id, html, data):
    for i in range(len(data)):
        array_type, label, numbers = data[i] 
        html += '<div class="elem">{}</div>'.format(label)
        for j in range(8):
            if j < len(numbers):
                element_id = file_id + array_type + str(j)
                html += '<div id="{}" class="elem box">{}</div>'.format(element_id, numbers[j])
            elif i == len(data) - 1:
                html += '<div class="elem extra-vertical-space"></div>'
            else:
                html += '<div class="elem"></div>'
    return html

def generate_javascript(file_id, labels, instructions):
    javascript = '<script>'
    
    for i in range(len(labels)):
        element_id = file_id + labels[i];
        instruction = instructions[i];
        javascript += 'document.getElementById("{}").onmouseover = \
                       function() {{mouse("{}", "{}", "{}", "#0cf")}};'.format(element_id, file_id, element_id, instruction)
        javascript += 'document.getElementById("{}").onmouseout = \
                       function() {{mouse("{}", "{}", "{}", "#fff")}};'.format(element_id, file_id, element_id, instruction)

    with open('./animation/javascript.txt', 'r') as file:
        javascript += file.read() + '</script>'
    
    return javascript

def display_animation(file_id, data_matrix, data_list, labels, instructions): 
    matrix = generate_matrix(file_id, data_matrix)
    html = generate_html(file_id, data_list)
    javascript = generate_javascript(file_id, labels, instructions)
    display(HTML(css + matrix + html + javascript))