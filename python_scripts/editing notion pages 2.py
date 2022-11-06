import re

file_path = input('Enter file path: ')
file_path = file_path.replace('\u005C', '\\')
if ('"' in file_path):
    file_path = file_path.replace('"', '')

file = open(file_path, 'r', encoding='utf-8')

txt = file.read()
file.close()

new_txt = re.sub(r'<td class="cell-title"><a href="[^">]*">Untitled</a></td>', '', txt)
new_txt = re.sub(r'<th><span class="icon property-icon"><svg viewBox="[^"]*" style="[^"]*" class="typesTitle"><path d="[^">]*"></path></svg></span>Name</th>', '', new_txt)
new_txt = re.sub(r'<table class="properties">.*</table>', '', new_txt)
new_txt = re.sub(r'<a href=".*?">', '', new_txt)
new_txt = re.sub(r'</a>', '', new_txt)

new_file_path = file_path.replace('.html', ' _ new.html')

new_file = open(new_file_path, 'w', encoding='utf-8')



new_file.write(new_txt)
new_file.close()
print('Done!')