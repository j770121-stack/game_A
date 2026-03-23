import os

app_path = 'c:/Users/jay20/Desktop/game_A/App.js'
html_path = 'c:/Users/jay20/Desktop/game_A/index.html'

with open(app_path, 'r', encoding='utf-8') as f:
    app_js = f.read()

# remove React imports at top
lines = app_js.split('\n')
new_app_js = []
for line in lines:
    if line.startswith("import React"): continue
    if line.startswith("import './styles.css'"): continue
    if line.startswith("export default App;"): continue
    new_app_js.append(line)
app_js = '\n'.join(new_app_js)

with open(html_path, 'r', encoding='utf-8') as f:
    index_html = f.read()

start_marker = '<script type="text/babel">'
end_marker = "        const root = ReactDOM.createRoot(document.getElementById('root'));"

start_idx = index_html.find(start_marker)
end_idx = index_html.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print("Markers not found")
    exit(1)

prefix = index_html[:start_idx + len(start_marker) + 1]
suffix = index_html[end_idx:]

new_babel = """        const { useState, useEffect, useRef } = React;
        const { motion } = window.Motion || { motion: { div: "div" } };

""" + app_js + "\n\n"

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(prefix + new_babel + suffix)

print("Successfully synced App.js to index.html!")
