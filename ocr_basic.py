from PIL import Image
import pyocr

tools = pyocr.get_available_tools()
# パソコンに入っているcorをやってくれる部品を取ってくる

tool = tools[0]
# 一番優先順位が高い tesseractが入っっている

# print(tool)
# print(tool.get_name())

img = Image.open("sparta_camp_en.png") # pillowで画像を読み込む
# img.show() # 画像を表示

text = tool.image_to_string( # tesseractを使って
    img, # 画像
    lang="eng+jpn", # 言語  eng+jpn 英語でも日本語でもOK
    builder=pyocr.builders.TextBuilder() #どんな文字が入っているのか
)

print(text)
