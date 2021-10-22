import dis
import itertools
import inspect
from .fmt import *
from .column import Column



flag_to_pointed = {
      'hasconst': lambda code: code.co_consts
    , 'hasname': lambda code: code.co_names
    , 'haslocal': lambda code: code.co_varnames
    , 'hasfree': lambda code: code.co_cellvars + code.co_freevars
    , 'hascompare': lambda code: dis.cmp_op
}


def idis(f, *,
    columns: list[Column] = (
        Column('starts_line', fmt = comp(hide_none, str), min_col_space = 4, hide_name = True),
        Column('jump_target_mark', fmt = hide_none, hide_name = True),
        Column('offset', align_left = False, hide_name = True, min_col_space = 1),
        Column('opname'),
        Column('opcode'),
        Column('flag'),
        Column('arg', align_left = False),
        Column('pointsto'),
        Column('argval', fmt = comp(shorten_long, str)),
        # Column('argrepr', fmt = comp(shorten_long, repr)),
        Column('argtype'),
        Column('hasarg', fmt = replace_bool_with_symbol),
        # Column('starts_line', fmt = comp(hide_none, str)),
        # Column('is_jump_target', fmt = replace_bool_with_symbol)
), ifilter = lambda i: True):
    if inspect.isfunction(f):
        f = f.__code__

    def iter_closures(f):
        for c1 in f.co_consts:
            if inspect.iscode(c1):
                yield c1
                for c2 in iter_closures(c1):
                    yield c2

    closures = (f, *iter_closures(f))

    col_name_to_max_line_len = {col.name: max(max(({col.name: 0 for col in columns},
        *({col.name: len(col.fmt(getattr(inst, col.name))) for col in columns}
        for inst in filter(ifilter, itertools.chain.from_iterable(map(dis.get_instructions, closures))))),
        key = lambda x: x[col.name])[col.name], len(col.public_name)) for col in columns}

    for closure in closures:
        instructions = tuple(filter(ifilter, dis.get_instructions(closure)))

        print(f'Disassembly of {closure!r}:')
        for flag in {inst.flag for inst in instructions if inst.flag}:
            if flag in flag_to_pointed:
                print(f'    {flag} -> {flag_to_pointed[flag](closure)}')
        print()
        print(''.join(map(lambda col: col.aligned(col_name_to_max_line_len), columns)))
        print(''.join(map(lambda col: col.aligned_underline(col_name_to_max_line_len), columns)))

        near_header = True

        for instruction in instructions:
            if instruction.line_number is not None:
                if near_header:
                    near_header = not near_header
                else:
                    print()
            print(instruction.aligned(columns, col_name_to_max_line_len))
        print()
