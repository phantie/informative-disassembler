__all__ = (
'comp',
'shorten_long',
'replace_obj',
'hide_none',
'replace_bool_with_symbol',
)

import inspect
import functools



def comp(f, *fs):
    """Takes a set of functions and returns a fn that is the composition
    of those fns.  The returned fn takes a variable number of args,
    applies the leftmost of fns to the args, the next
    fn (left-to-right) to the result, etc."""
    def executable(*args, **kwargs):
        return functools.reduce((lambda r, f: f(r)), (f(*args, **kwargs), *fs))        
    return executable

def shorten_long(v):
    if inspect.iscode(v):
        return f'<code object {v.co_name}>'
    return v

def replace_obj(obj, replace, v):
    return replace if v is obj else v

hide_none = functools.partial(replace_obj, None, '')

def replace_bool_with_symbol(p):
    return '✔' if p else '  ✖'