import bs4

block_level_elements = ['p', 'ul', 'ol', 'li', 'div', 'dd', 'dt', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'table', 'tr', 'td', 'br']

block_level_elements_dict = {x: 1 for x in block_level_elements}

def bs_semantic_text(soup):
    """Replacement for BeautifulSoup's get_text() that takes into account block-level elements"""
    out = ''
    for e in soup.descendants:
        if isinstance(e, bs4.element.Tag):
            if e.name in block_level_elements_dict:
                out += ' '
        if isinstance(e, bs4.element.NavigableString):
            out += e
    return out.strip()

# Test code
if __name__ == "__main__":
    from bs4 import BeautifulSoup
    soup = BeautifulSoup('<ul><li><strong>V</strong>ery interesting</li><li>Thing it is</li></ul>', 'html5lib')
    print(soup.get_text())
    print(bs_semantic_text(soup))
