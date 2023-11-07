# coding:utf-8
# author:LegendNoTitle
    
import os
from bs4 import BeautifulSoup
from glob import glob

print("欢迎使用HTML样式提取工具！")
print("本工具将帮助你从HTML文件中提取内联样式，")
print("并生成一个外部CSS文件，同时更新原HTML文件以引用新的CSS文件。")
print("将自动搜索本工具目录下的HTML文件。\n")

# 获取当前目录下所有的 HTML 文件
html_files = glob('*.html')

# 定义 HTML 和 CSS 文件名
html_file = ''
css_file_name = 'styles.css'  # 仅定义CSS文件名，不是路径

# 根据找到的HTML文件数量来决定如何获取HTML文件路径
if len(html_files) == 1:
    html_file = html_files[0]
elif len(html_files) == 0:
    html_file = input("当前程序目录下未找到 HTML 文件，请输入文件路径: ")
else:
    print("当前程序目录下找到多个 HTML 文件，请指定要转换的文件:")
    for idx, f in enumerate(html_files, start=1):
        print(f"{idx}. {f}")
    file_index = int(input("输入文件编号选择: ")) - 1
    html_file = html_files[file_index]

# 确保提供的是有效文件路径
if not os.path.isfile(html_file):
    print("提供的文件路径不正确，请重新运行程序并提供有效的HTML文件路径。")
    exit()
# 获取HTML文件所在的目录
html_dir = os.path.dirname(html_file)

# 如果html_dir是空的，意味着HTML文件在当前目录下，我们将CSS文件也保存在当前目录下
if not html_dir:
    css_file = css_file_name
else:
    css_file = os.path.join(html_dir, css_file_name)

# 读取 HTML 文件内容
with open(html_file, 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')
css_content = ""

# 从HTML的style标签中提取CSS内容
for style in soup.find_all("style"):
    css_content += style.text
    style.decompose()

# 处理每个带有 style 属性的元素
for index, element in enumerate(soup.find_all(style=True), start=1):
    class_name = f"inline-style-{index}"
    existing_classes = element.get('class', [])
    existing_classes.append(class_name)
    element['class'] = existing_classes
    css_content += f".{class_name} {{{element['style']}}}\n"
    del element['style']

# 在 HTML 文件中引用 CSS 文件
head = soup.head
if head:
    new_link_tag = soup.new_tag("link", rel="stylesheet", href=css_file)
    head.append(new_link_tag)
else:
    # 如果 HTML 文件中没有 head 标签，添加一个
    head = soup.new_tag('head')
    soup.html.insert(0, head)
    new_link_tag = soup.new_tag("link", rel="stylesheet", href=css_file)
    head.append(new_link_tag)

# 保存修改后的 HTML 文件
file_dir, file_name = os.path.split(html_file)
updated_html_file = os.path.join(file_dir, 'updated_' + file_name)

# with open(updated_html_file, 'w', encoding='utf-8') as file:
#     file.write(soup.prettify())
with open(updated_html_file, 'w', encoding='utf-8') as file:
    file.write(str(soup))  # 直接将soup对象转换成字符串而不是使用prettify()
# 保存 CSS 文件
if css_content:  # 确保不创建空的CSS文件
# 保存CSS文件到HTML文件相同的目录
    with open(css_file, 'w', encoding='utf-8') as file:
        file.write(css_content)


print(f"转换完成！已更新的 HTML 保存在 '{updated_html_file}'，CSS 保存在 '{css_file}'。")
