__all__ = (
'extend',
'clean_up',
)

import itertools
import dis
import sys



flags = {
      'hasconst'    # This list is equal to [100].
                    # So only the opcode 100 (its opname is LOAD_CONST) is in the category of hasconst.
                    # The oparg of this opcode gives the index of an element in the co_consts tuple

    , 'hasname'     # The oparg for the opcodes in this list, is the index of an element in co_names

    , 'haslocal'    # The oparg for the opcodes in this list, is the index of an element in co_varnames

    , 'hasfree'     # The oparg for the opcodes in this list, is the index of an element in co_cellvars + co_freevars

    , 'hascompare'  # The oparg for the opcode in this list, is the index of an element of the tuple dis.cmp_op.
                    # This tuple contains the comparison and membership operators like < or ==

    , 'hasjrel'     # The oparg for the opcodes in this list, should be replaced with offset + 2 + oparg
                    # where offset is the index of the byte in the bytecode sequence which represents the opcode.

    , 'hasjabs'     # Sequence of bytecodes that has an absolute jump target.
}


flag_to_pointed_name = {
      'hasconst': 'co_consts'
    , 'hasname': 'co_names'
    , 'haslocal': 'co_varnames'
    , 'hasfree': '(co_cellvars + co_freevars)'
    , 'hascompare': 'dis.cmp_op'
}

# check for the absence of multiple flags per opcode
assert len(codes := tuple(itertools.chain.from_iterable(getattr(dis, flag) for flag in flags))) == len(set(codes))


opcode_to_flag = dict(itertools.chain.from_iterable(
    ((code, attr) for code in getattr(dis, attr)) for attr in flags))


class missing(str):
    __str__ = __repr__ = lambda self: ''
    __bool__ = lambda self: False

missing = missing()


class Instruction(dis.Instruction):
    @property
    def line_number(self):
        return self.starts_line

    @property
    def jump_target_mark(self):
        return '>>' if self.is_jump_target else None

    @property
    def flag(self):
        return opcode_to_flag.get(self.opcode, missing)

    @property
    def pointsto(self):
        return f'{flag_to_pointed_name[self.flag]}[{self.arg}]' if self.flag in flag_to_pointed_name else missing

    @property
    def arg(self):
        return super().arg if self.hasarg else missing

    @property
    def argval(self):
        return super().argval if self.argrepr else missing

    @property
    def argrepr(self):
        return super().argrepr if super().argrepr else missing

    @property
    def argtype(self):
        return type(self.argval).__name__ if self.argval is not missing else missing

    @property
    def hasarg(self):
        return self.opcode >= dis.HAVE_ARGUMENT

    def aligned(self, columns, col_name_to_max_line_len):
        return ''.join(map(lambda col: ('{:{}{}}' + ' ' * col.min_col_space).format(col.fmt(getattr(self, col.name)), col.align, col_name_to_max_line_len[col.name]), columns))


def extend():
    dis.Instruction = Instruction

def clean_up():
    del sys.modules['dis']