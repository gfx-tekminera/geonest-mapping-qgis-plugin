from qgis.utils import qgsfunction

@qgsfunction(args='auto', group='Geonest Mapping')
def geomaplib_to_hex(val, length=0, feature=None, parent=None):
    """
    Converts a decimal integer to hexadecimal, padding to the left if necessary.
    Usage in the QGIS expression: to_hex(255) or to_hex(255, 4)
    """
    h = format(int(val), "x")  # hex conversion
    if length > 0:
        h = h.rjust(length, "0")  # left padding
    return h
