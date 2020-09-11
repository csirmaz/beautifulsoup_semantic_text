# beautifulsoup_semantic_text
Replacement for BeautifulSoup's get_text() that takes into account block-level elements (Python)

`get_text()` in BeautifulSoup simply concatenates strings among the
descendants. This can create unexpected results when so-called block-level HTML
elements are used, which are expected to semantically separate portions of
the text.

For example, for the following HTML:
```
<ul><li><strong>V</strong>ery interesting</li><li>Thing it is</li></ul>
```

`get_text()` returns "Very interestingThing it is" instead of the expected
"Very interesting Thing it is" as it disregards the block-level nature of
`<li>`.

`beautifulsoup_semantic_text.bs_semantic_text()` overcomes this problem by
adding a space in front of each block-level element when constructing the
string.

Note that block-level and inline is a historical categorisation of HTML
elements and is not defined everywhere.
See https://developer.mozilla.org/en-US/docs/Web/HTML/Block-level_elements
for more. The distinction is still useful to approximate the
expected presentation of the HTML in a string.

Also note that the code specifies more elements as block-level than would be
strictly accurate (e.g. `<td>`), again to approximate the expected rendering
of the HTML.
