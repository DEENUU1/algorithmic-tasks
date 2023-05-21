def rgb(r, g, b):
    r = max(0, min(255, round(r)))
    g = max(0, min(255, round(g)))
    b = max(0, min(255, round(b)))
    
    rgb_code = (r, g, b)
    convert = '%02x%02x%02x' % rgb_code
    return convert.upper()