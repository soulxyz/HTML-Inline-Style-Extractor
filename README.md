
# HTML内联样式提取工具 / HTML Inline Style Extractor

本工具从HTML文档中提取内联样式，并将其释放到外联CSS文件中，减少原HTML体积。
This tool extracts inline styles from an HTML document and creates an external CSS file, then updates the HTML file to link to the newly created CSS file.

## 功能特点 / Features

- 自动在当前目录寻找HTML文件。
- 将内联样式转换为CSS类并将它们添加到外部CSS文件中。
- 更新HTML文件，移除内联样式并链接到外部CSS文件。
- 
- Converts inline styles to CSS classes and adds them to an external CSS file.
- Automatically finds HTML files in the current directory.
- Updates the HTML file by removing inline styles and linking to the external CSS file.

## 条件 / Prerequisites

在运行此工具之前，请确保你的计算机上已设置了Python环境。(或下载我的打包版本)
Ensure you have a Python environment set up on your computer before running this tool.

## 使用说明 / Usage

1. 将你的HTML文件放置于工具相同的目录下。（不在也没有关系，手动输入路径即可ヾ(≧▽≦*)o）
2. 从命令行运行脚本。
1. Place your HTML file in the same directory as the tool.
2. Run the script from the command line.

## 如何运行 / How to Run
**直接下载的exe直接就可以使用了**

如果下载了源码，在终端中执行以下命令：
Execute the following command in the terminal:

```bash
python style_extractor.py
```

如果在当前目录中找到多个HTML文件，脚本会提示你选择一个进行处理。
The script will automatically search for an HTML file in the current directory. If it finds multiple HTML files, it will prompt you to choose one to process.

## 结果 / Results

运行脚本后，你将得到两个文件：
After running the script, you will obtain two files:

- 一个添加了`updated_`前缀的更新过的HTML文件。
- An updated HTML file with the `updated_` prefix added to the filename.
- 一个默认命名为`styles.css`的新CSS文件。
- A new CSS file, named `styles.css` by default.

这两个文件将被保存在原HTML文件的相同目录中。
Both files will be saved in the same directory as the original HTML file.

## 注意事项 / Notes

- 确保目录中没有名为`styles.css`的重要文件，因为它将被覆盖。
- Ensure there is no important file named `styles.css` in the directory, as it will be overwritten.
- HTML文件中手动添加的`<link>`引用CSS将保持不变。
- Manual `<link>` references to CSS in the HTML file will remain unchanged.

## 贡献 / Contributing

如果你有任何改进意见或对额外功能的请求，请开一个问题或提交一个拉取请求。
If you have any suggestions for improvement or requests for additional features, please open an issue or submit a pull request.

## 许可证 / License

此项目根据[MIT许可证](LICENSE)授权。
This project is licensed under the [MIT License](LICENSE).
