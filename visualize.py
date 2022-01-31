def make_hues(n):
    """Make a spectrum of n hues."""
    hues = [0]

    # 315 instead of 360 so the end doesn't look same as beginning
    step_size = 315 // n 
    for _ in range(n):
        hues.append(hues[-1] + step_size)

    return hues

def html_out(hues):
    block_template = '<font style="color:hsl({}, 100%, 50%)">█</font>'
    out = []

    for hue in hues:
        out.append(block_template.format(hue))

    return ''.join(out)
