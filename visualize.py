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
  height: 2.5vw;
  width: 1.25vw;
  border: solid;
  border-color: black;
  border-width: medium;
  display: inline-block;
  margin: 0.25vw;
}
</style></head><body>'''

footer = '</body></html>'

def hues2html(hues):
    out = []

    block_template = '<div class="rectangle" style="background-color: hsl({}, 100%, 50%);"></div>'

    for hue in hues:
        out.append(block_template.format(hue))

    return ''.join(out)

