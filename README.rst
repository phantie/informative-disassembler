.. code:: python
    from idis import idis
    from dis import dis

    def foo():
        a = 1
        b = 2
        def f(x):
            global b
            b = 3
            y = x + 1
            return y 
        f(4)
        print(a)

    idis(foo)


::
    Disassembly of <code object foo at 0x0000024F84413240, file "c:\Users\phant1e\Desktop\auto\test.py", line 56>:
        hasconst -> (None, 1, 2, <code object f at 0x0000024F8430FC90, file "c:\Users\phant1e\Desktop\auto\test.py", line 59>, 'foo.<locals>.f', 4)
        hasname -> ('print',)
        haslocal -> ('a', 'b', 'f')
    
                    opname          opcode   flag       arg   pointsto         argval            argtype    hasarg
                    ¯¯¯¯¯¯          ¯¯¯¯¯¯   ¯¯¯¯       ¯¯¯   ¯¯¯¯¯¯¯¯         ¯¯¯¯¯¯            ¯¯¯¯¯¯¯    ¯¯¯¯¯¯
    57            0 LOAD_CONST      100      hasconst     1   co_consts[1]     1                 int        ✔
                  2 STORE_FAST      125      haslocal     0   co_varnames[0]   a                 str        ✔
    
    58            4 LOAD_CONST      100      hasconst     2   co_consts[2]     2                 int        ✔
                  6 STORE_FAST      125      haslocal     1   co_varnames[1]   b                 str        ✔
    
    59            8 LOAD_CONST      100      hasconst     3   co_consts[3]     <code object f>   code       ✔
                 10 LOAD_CONST      100      hasconst     4   co_consts[4]     foo.<locals>.f    str        ✔
                 12 MAKE_FUNCTION   132                   0                                                 ✔
                 14 STORE_FAST      125      haslocal     2   co_varnames[2]   f                 str        ✔
    
    64           16 LOAD_FAST       124      haslocal     2   co_varnames[2]   f                 str        ✔
                 18 LOAD_CONST      100      hasconst     5   co_consts[5]     4                 int        ✔
                 20 CALL_FUNCTION   131                   1                                                 ✔
                 22 POP_TOP         1                                                                         ✖
    
    65           24 LOAD_GLOBAL     116      hasname      0   co_names[0]      print             str        ✔
                 26 LOAD_FAST       124      haslocal     0   co_varnames[0]   a                 str        ✔
                 28 CALL_FUNCTION   131                   1                                                 ✔
                 30 POP_TOP         1                                                                         ✖
                 32 LOAD_CONST      100      hasconst     0   co_consts[0]     None              NoneType   ✔
                 34 RETURN_VALUE    83                                                                        ✖
    
    Disassembly of <code object f at 0x0000024F8430FC90, file "c:\Users\phant1e\Desktop\auto\test.py", line 59>:
        hasconst -> (None, 3, 1)
        hasname -> ('b',)
        haslocal -> ('x', 'y')
    
                    opname          opcode   flag       arg   pointsto         argval            argtype    hasarg
                    ¯¯¯¯¯¯          ¯¯¯¯¯¯   ¯¯¯¯       ¯¯¯   ¯¯¯¯¯¯¯¯         ¯¯¯¯¯¯            ¯¯¯¯¯¯¯    ¯¯¯¯¯¯
    61            0 LOAD_CONST      100      hasconst     1   co_consts[1]     3                 int        ✔
                  2 STORE_GLOBAL    97       hasname      0   co_names[0]      b                 str        ✔
    
    62            4 LOAD_FAST       124      haslocal     0   co_varnames[0]   x                 str        ✔
                  6 LOAD_CONST      100      hasconst     2   co_consts[2]     1                 int        ✔
                  8 BINARY_ADD      23                                                                        ✖
                 10 STORE_FAST      125      haslocal     1   co_varnames[1]   y                 str        ✔
    
    63           12 LOAD_FAST       124      haslocal     1   co_varnames[1]   y                 str        ✔
                 14 RETURN_VALUE    83                                                                        ✖


    dis(foo)

    
     57           0 LOAD_CONST               1 (1)
                  2 STORE_FAST               0 (a)
    
     58           4 LOAD_CONST               2 (2)
                  6 STORE_FAST               1 (b)
    
     59           8 LOAD_CONST               3 (<code object f at 0x000002C93C94FC90, file "c:\Users\phant1e\Desktop\auto\test.py", line 59>)
                 10 LOAD_CONST               4 ('foo.<locals>.f')
                 12 MAKE_FUNCTION            0
                 14 STORE_FAST               2 (f)
    
     64          16 LOAD_FAST                2 (f)
                 18 LOAD_CONST               5 (4)
                 20 CALL_FUNCTION            1
                 22 POP_TOP
    
     65          24 LOAD_GLOBAL              0 (print)
                 26 LOAD_FAST                0 (a)
                 28 CALL_FUNCTION            1
                 30 POP_TOP
                 32 LOAD_CONST               0 (None)
                 34 RETURN_VALUE
    
    Disassembly of <code object f at 0x000002C93C94FC90, file "c:\Users\phant1e\Desktop\auto\test.py", line 59>:
     61           0 LOAD_CONST               1 (3)
                  2 STORE_GLOBAL             0 (b)
    
     62           4 LOAD_FAST                0 (x)
                  6 LOAD_CONST               2 (1)
                  8 BINARY_ADD
                 10 STORE_FAST               1 (y)
    
     63          12 LOAD_FAST                1 (y)
                 14 RETURN_VALUE