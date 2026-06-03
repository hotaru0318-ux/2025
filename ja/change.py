import json

input_file = "ch09.ipynb"
output_file = "ch09_fixed.ipynb"

# ノートブックの読み込み
with open(input_file, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

# エラーの原因となっている widgets メタデータを削除
if "metadata" in notebook and "widgets" in notebook["metadata"]:
    del notebook["metadata"]["widgets"]
    print("metadataからwidgetsを削除しました。")

# 修正したノートブックを保存
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, ensure_ascii=False, indent=2)

print(f"修正版を {output_file} として保存しました。")
