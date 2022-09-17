from main import the

def isfloat(string):
    """Check and convert string to float if possible"""
    try:
        float(string)
        return True
    except ValueError:
        return False

def coerce(string):
    """Parse 'the' config settings from 'help'"""
    if isfloat(string):
        return float(string)
    elif string == "true":
            return True
    elif string == "false":
        return False
    else:
        return string

def csv(src, fn):
    """Call function 'fn' on each row. Row cells are divided in 'the.separator'"""
    sep = the['seperator']
    with open(src, "r") as f:
        for line in f.readlines():
            table = []
            for value in line.split(sep):
                table.append(coerce(value.strip()))
            fn(table)

def push(table, row):
    """Adds 'row' to table and returns the last row"""
    table.append(row)
    return row
