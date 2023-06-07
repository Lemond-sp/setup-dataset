import os
import tensorflow_datasets as tfds

# データセットの取得
def get_wiki(wiki_lang = 'wiki40b/ja',mode='test'):
  ds = tfds.load(wiki_lang, split=mode)

  # 0番目の記事の確認
  wiki = list(ds.as_numpy_iterator())[0]
  print('text:', wiki['text'].decode())
  print('version_id:',wiki['version_id'].decode())
  print('wikidata_id:',wiki['wikidata_id'].decode())

  '''
  前処理済みのテキストに，以下のマークアップが埋め込まれている．
  ・_START_ARTICLE_ : ページタイトル
  ・_START_SECTION_ : 節のタイトル
  ・_START_PARAGRAPH_ : 説明文
  ・_NEWLINE_ : 改行
  '''
def wiki_text()
def main():
  get_wiki()

if __name__ == "__main__":
  main()