__all__ = ['idis']

from . import instruction
instruction.extend()
from .f import idis
instruction.clean_up()