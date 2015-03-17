import sys

if __name__ == '__main__':
    files = []
    for i, a in enumerate(sys.argv):
        if i != 0:
            files.append(a)
    with open('header', 'r') as h:
        html_header = h.read()
        h.close()
    with open('footer', 'r') as f:
        html_footer = f.read()
        f.close()
    for f in files:
        lines_in = []
        lines_out = []
        lines_out.append(html_header)
        filename_html = f.split('.')[0] + ".html"
        with open(f, 'r') as log:
            lines_in = log.read().split('\n')
            log.close()
        for l in lines_in:
            l = '<p>' + l + '</p>'
            lines_out.append(l)
        lines_out.append(html_footer)
        charbuf = '\n'.join(lines_out)
        with open(filename_html, 'w') as out:
            out.write(charbuf)
            out.close()
