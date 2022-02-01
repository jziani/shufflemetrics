def make_hues(n):
    """Make a spectrum of n hues."""
    hues = [0]

    # 315 instead of 360 so the end doesn't look same as beginning
    step_size = 315 // n 
    for _ in range(n):
        hues.append(hues[-1] + step_size)

    return hues

header = '''<!DOCTYPE html>
    <html>
    <head>
    <style>
.rectangle {
  height: 3em;
  width: 2em;
  border: solid;
  border-color: black;
  border-width: thick;
  display: table;
  margin: 0.25em;
  float: left;
}
</style></head><body>'''

footer = '</body></html>'

def html_out(hues):
    out = []

    block_template = '<div class="rectangle" style="background-color: hsl({}, 100%, 50%);"></div>'

    for hue in hues:
        out.append(block_template.format(hue))

    return ''.join(out)

