from bs4 import BeautifulSoup

html_doc = """
<html>
<head>
    <title>Test Page</title>
<head>
<body>
    <h1>This is a sample page.</p>
    <p class="content">Hello, BeautifulSoup</p>
    <ul>
        <li>Item 1</li>
        <li>Item 2</li>
        <li>Item 3</li>
    <ul>
    <div class="container">
        <h1>Title</h1>
        <p>Paragraph content</p>
    </div>

    <div id="main">
        <p class="info">Info Paragraph 1</p>
        <p class="info">Info Paragraph 2</p>
    </div>
<body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.title)

header = soup.find('h1')
print(header.text)

items = soup.find_all('li')
for item in items:
    print(item.text)

container = soup.find('div', class_='container')
print("parent tag:", container.parent.name)

elements = soup.select('div#main p.info')
for element in elements:
    print(element.get_text())