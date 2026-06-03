import json
import os

def extract_notebook_content(notebook_path, output_path):
    """
    Jupyter Notebookから内容を抽出してMarkdownファイルとして保存
    """
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    markdown_content = []
    
    for i, cell in enumerate(notebook['cells']):
        cell_type = cell.get('cell_type', 'unknown')
        
        if cell_type == 'markdown':
            # マークダウンセル
            source = ''.join(cell.get('source', []))
            markdown_content.append(source)
            markdown_content.append('\n\n')
        
        elif cell_type == 'code':
            # コードセル
            source = ''.join(cell.get('source', []))
            markdown_content.append('```python\n')
            markdown_content.append(source)
            markdown_content.append('\n```\n\n')
            
            # 出力を追加
            outputs = cell.get('outputs', [])
            if outputs:
                markdown_content.append('**出力結果:**\n\n')
                for output in outputs:
                    if output.get('output_type') == 'stream':
                        text = ''.join(output.get('text', []))
                        markdown_content.append('```\n')
                        markdown_content.append(text)
                        markdown_content.append('\n```\n\n')
                    elif output.get('output_type') == 'execute_result':
                        text = ''.join(output.get('data', {}).get('text/plain', []))
                        markdown_content.append('```\n')
                        markdown_content.append(text)
                        markdown_content.append('\n```\n\n')
    
    # ファイルに保存
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(''.join(markdown_content))
    
    print(f"✓ 保存完了: {output_path}")

# 実行
extract_notebook_content('ja/ch09.ipynb', 'ch09_output.md')
