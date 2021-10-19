class Column:
    def __init__(self, name, *, min_col_space = 3, fmt = str, align_left = True, hide_name = False):
        self.name = name
        self.min_col_space = min_col_space
        self.fmt = fmt
        self.align = '<' if align_left else '>'
        self.hide_name = hide_name

    def aligned(self, col_name_to_max_line_len):
        return ('{:{}{}}' + ' ' * self.min_col_space).format(self.public_name, self.align, col_name_to_max_line_len[self.name])

    def aligned_underline(self, col_name_to_max_line_len):
        return ('{:{}{}}' + ' ' * self.min_col_space).format(chr(175) * len(self.public_name), self.align, col_name_to_max_line_len[self.name])

    @property
    def public_name(self):
        return self.name if not self.hide_name else ''
