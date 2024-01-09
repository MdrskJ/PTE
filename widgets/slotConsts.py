def get_indents(a: int):
    indent_left = a // 16
    indent_left_orb = a * 13 // 16

    indent_top_num = a // 16
    indent_top_sym = a // 4
    indent_top_name = a * 9 // 16
    indent_top_mass = a * 3 // 4
    return (indent_left, indent_left_orb, indent_top_num,
            indent_top_sym, indent_top_name, indent_top_mass)
