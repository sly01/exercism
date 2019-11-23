import re

def parse(markdown):
    text = markdown

    # Parse bold
    text = re.sub(r'__([^\n]+)__', r'<strong>\1</strong>', text)

    # Parse italic
    text = re.sub(r'_([^\n]+)_', r'<em>\1</em>', text)
    
    # Parse paragraph
    text = re.sub(r'([^\n]+)', r'<p>\1</p>', text)
    return text

# def parse(markdown):
#     s = markdown
#     s = re.sub(r'__([^\n]+?)__', r'<strong>\1</strong>', s)
#     s = re.sub(r'_([^\n]+?)_', r'<em>\1</em>', s)
#     s = re.sub(r'^\* (.*?$)', r'<li>\1</li>', s, flags=re.M)
#     s = re.sub(r'(<li>.*</li>)', r'<ul>\1</ul>', s, flags=re.S)
#     for i in range(6, 0, -1):
#         s = re.sub(r'^{} (.*?$)'.format('#' * i), r'<h{0}>\1</h{0}>'.format(i), s, flags=re.M)
#     s = re.sub(r'^(?!<[hlu])(.*?$)', r'<p>\1</p>', s, flags=re.M)
#     s = re.sub(r'\n', '', s)
#     return s


print(parse("This will _be_ __mixed__"))

# def parse(markdown):
#     lines = markdown.split('\n')
#     res = ''
#     in_list = False
#     in_list_append = False
#     for i in lines:
#         if re.match('###### (.*)', i) is not None:
#             i = '<h6>' + i[7:] + '</h6>'
#         elif re.match('## (.*)', i) is not None:
#             i = '<h2>' + i[3:] + '</h2>'
#         elif re.match('# (.*)', i) is not None:
#             i = '<h1>' + i[2:] + '</h1>'
#         m = re.match(r'\* (.*)', i)
#         if m:
#             if not in_list:
#                 in_list = True
#                 is_bold = False
#                 is_italic = False
#                 curr = m.group(1)
#                 m1 = re.match('(.*)__(.*)__(.*)', curr)
#                 if m1:
#                     curr = m1.group(1) + '<strong>' + \
#                         m1.group(2) + '</strong>' + m1.group(3)
#                     is_bold = True
#                 m1 = re.match('(.*)_(.*)_(.*)', curr)
#                 if m1:
#                     curr = m1.group(1) + '<em>' + m1.group(2) + \
#                         '</em>' + m1.group(3)
#                     is_italic = True
#                 i = '<ul><li>' + curr + '</li>'
#             else:
#                 is_bold = False
#                 is_italic = False
#                 curr = m.group(1)
#                 m1 = re.match('(.*)__(.*)__(.*)', curr)
#                 if m1:
#                     is_bold = True
#                 m1 = re.match('(.*)_(.*)_(.*)', curr)
#                 if m1:
#                     is_italic = True
#                 if is_bold:
#                     curr = m1.group(1) + '<strong>' + \
#                         m1.group(2) + '</strong>' + m1.group(3)
#                 if is_italic:
#                     curr = m1.group(1) + '<em>' + m1.group(2) + \
#                         '</em>' + m1.group(3)
#                 i = '<li>' + curr + '</li>'
#         else:
#             if in_list:
#                 in_list_append = True
#                 in_list = False

#         m = re.match('<h|<ul|<p|<li', i)
#         if not m:
#             i = '<p>' + i + '</p>'
#         m = re.match('(.*)__(.*)__(.*)', i)
#         if m:
#             i = m.group(1) + '<strong>' + m.group(2) + '</strong>' + m.group(3)
#         m = re.match('(.*)_(.*)_(.*)', i)
#         if m:
#             i = m.group(1) + '<em>' + m.group(2) + '</em>' + m.group(3)
#         if in_list_append:
#             i = '</ul>' + i
#             in_list_append = False
#         res += i
#     if in_list:
#         res += '</ul>'
#     return res
