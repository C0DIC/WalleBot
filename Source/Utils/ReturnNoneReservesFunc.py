def returnNoneReserved(var: str):
    new_var = var.replace('_', '\\_').replace('*', '\\*').replace('[', '\\[').replace(']', '\\]').replace('(', '\\(')
    new_var = new_var.replace(')', '\\)').replace('~', '\\~').replace('`', '\\`').replace('>', '\\>')
    new_var = new_var.replace('#', '\\#').replace('+', '\\+').replace('-', '\\-').replace('=', '\\=')
    new_var = new_var.replace('|', '\\|').replace('{', '\\{').replace('}', '\\}').replace('.', '\\.').replace('!', '\\!')

    return new_var
