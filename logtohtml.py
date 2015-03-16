import sys

if __name__ == '__main__':
    files = []
    lines_in = []
    lines_out = []
    html_header = open('header', 'r').read()
    lines_out.append(html_header)
    html_footer = open('footer', 'r').read()
    for i, a in enumerate(sys.argv):
        if i != 0:
            files.append(a)
    for f in files:
        filename_html = '.'.join([f.split('.')[0], 'html'])
        with open(f, 'r') as log:
            lines_in = log.read().split('\n')
            log.close()
        for l in lines_in:
            l = '<p>' + l + '</p>\n'
            lines_out.append(l)
        lines_out.append(html_footer)
        charbuf = ''.join(lines_out)
        with open(filename_html, 'w') as out:
            out.write(charbuf)
            out.close()
