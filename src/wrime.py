'''
・テキストファイルに「テキスト」「主観・客観のラベル」を保存
・それぞれ別ファイルに保存
'''

import pandas as pd

df = pd.read_csv('/home/kajikawa_r/datasets/wrime/wrime-ver2.tsv','\t')


# object型を改行する際には、regexが必要
df['Sentence'] = df['Sentence'].replace('\n','',regex=True)

train_text = df[df['Train/Dev/Test'] == 'train']['Sentence']
dev_text = df[df['Train/Dev/Test'] == 'dev']['Sentence']
test_text = df[df['Train/Dev/Test'] == 'test']['Sentence']

train_writer = df[df['Train/Dev/Test'] == 'train']['Writer_Sentiment']
train_reader = df[df['Train/Dev/Test'] == 'train']['Avg. Readers_Sentiment']
dev_writer = df[df['Train/Dev/Test'] == 'dev']['Writer_Sentiment']
dev_reader = df[df['Train/Dev/Test'] == 'dev']['Avg. Readers_Sentiment']
test_writer = df[df['Train/Dev/Test'] == 'test']['Writer_Sentiment']
test_reader = df[df['Train/Dev/Test'] == 'test']['Avg. Readers_Sentiment']

# text
train_text.to_csv('/home/kajikawa_r/datasets/wrime/train-text.txt',header=False,index=False)
dev_text.to_csv('/home/kajikawa_r/datasets/wrime/dev-text.txt',header=False,index=False)
test_text.to_csv('/home/kajikawa_r/datasets/wrime/test-text.txt',header=False,index=False)

# label（主観と客観）
train_writer.to_csv('/home/kajikawa_r/datasets/wrime/train-writer.txt',header=False,index=False)
train_reader.to_csv('/home/kajikawa_r/datasets/wrime/train-reader.txt',header=False,index=False)
dev_writer.to_csv('/home/kajikawa_r/datasets/wrime/dev-writer.txt',header=False,index=False)
dev_reader.to_csv('/home/kajikawa_r/datasets/wrime/dev-reader.txt',header=False,index=False)
test_writer.to_csv('/home/kajikawa_r/datasets/wrime/test-writer.txt',header=False,index=False)
test_reader.to_csv('/home/kajikawa_r/datasets/wrime/test-reader.txt',header=False,index=False)

# output
# wrime-ver2
# print(df.columns)
# Index(['Sentence', 'UserID', 'Datetime', 'Train/Dev/Test', 'Writer_Joy',
#        'Writer_Sadness', 'Writer_Anticipation', 'Writer_Surprise',
#        'Writer_Anger', 'Writer_Fear', 'Writer_Disgust', 'Writer_Trust',
#        'Writer_Sentiment', 'Reader1_Joy', 'Reader1_Sadness',
#        'Reader1_Anticipation', 'Reader1_Surprise', 'Reader1_Anger',
#        'Reader1_Fear', 'Reader1_Disgust', 'Reader1_Trust', 'Reader1_Sentiment',
#        'Reader2_Joy', 'Reader2_Sadness', 'Reader2_Anticipation',
#        'Reader2_Surprise', 'Reader2_Anger', 'Reader2_Fear', 'Reader2_Disgust',
#        'Reader2_Trust', 'Reader2_Sentiment', 'Reader3_Joy', 'Reader3_Sadness',
#        'Reader3_Anticipation', 'Reader3_Surprise', 'Reader3_Anger',
#        'Reader3_Fear', 'Reader3_Disgust', 'Reader3_Trust', 'Reader3_Sentiment',
#        'Avg. Readers_Joy', 'Avg. Readers_Sadness', 'Avg. Readers_Anticipation',
#        'Avg. Readers_Surprise', 'Avg. Readers_Anger', 'Avg. Readers_Fear',
#        'Avg. Readers_Disgust', 'Avg. Readers_Trust', 'Avg. Readers_Sentiment'],
#       dtype='object')