# pure ishikki's hardwork
# i hope you guys wont kang it


def get_formatted_names(names):
    line_length = 26
    lines = []
    current_line = ""
    
    for name in names:
        if len(current_line) + len(name) + 1 > line_length:
            lines.append(current_line)
            current_line = name.ljust(line_length)
        else:
            current_line += name.ljust(line_length - len(current_line))
    
    if current_line:
        lines.append(current_line)
    
    formatted_text = ""
    
    for i in range(0, len(lines), 2):
        if i + 1 < len(lines):
            formatted_text += lines[i] + lines[i + 1] + '\n'
        else:
            formatted_text += lines[i] + '\n'
    
    return formatted_text