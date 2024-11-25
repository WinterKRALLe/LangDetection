def get_patterns():
    return {
        'python': [
            r'def\s+\w+\s*\([^)]*\)\s*:',      # definice funkcí
            r'class\s+\w+(\s*\([^)]*\))?\s*:',  # definice tříd
            r'import\s+[\w.]+',                # importy
            r'from\s+[\w.]+\s+import',         # from importy
            r'^\s*@\w+',                       # dekorátory
            r'with\s+.+\s+as\s+\w+:',         # with statement
        ],
        'javascript': [
            r'function\s+\w+\s*\([^)]*\)',    # funkce
            r'const\s+\w+\s*=',               # const deklarace
            r'let\s+\w+\s*=',                 # let deklarace
            r'class\s+\w+\s*{',               # třídy
            r'export\s+default',              # export
            r'=>',                            # arrow funkce
        ],
        'java': [
            r'public\s+class\s+\w+',          # definice tříd
            r'public\s+static\s+void\s+main',  # main metoda
            r'@Override',                     # anotace
            r'System\.out\.println',          # print
            r'new\s+\w+\(',                   # instance
            r'private\s+\w+\s+\w+;',          # private proměnné
        ],
        'cpp': [
            r'#include\s*<[^>]+>',            # includy
            r'std::\w+',                      # std namespace
            r'->\w+',                         # pointer access
            r'::\w+',                         # scope resolution
            r'template\s*<',                  # templates
            r'delete\s+\w+',                  # delete
        ]
    }
