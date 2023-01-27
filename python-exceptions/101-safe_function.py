#!/usr/bin/python3
def safe_function(fct, *args):
    """
    executes a function safely.
    """

    import sys
    try:
        return fct(*args)
    except (Exception) as nano:
        print(f"Exception: {nano}", file=sys.stderr)
        return None
