import os

imdb_dir = 'E:\\PIAIC\\PIAIC-AI\\ALL SUBJECTS\\Deep Learning\\Deep Learning Using Word Embedding\\aclImdb\\aclImdb'
train_dir = os.path.join(imdb_dir, 'train')

labels = []
texts = []

for label_type in ['neg', 'pos']:
    dir_name = os.path.join(train_dir, label_type)
    for fname in os.listdir(dir_name):
        if fname[-4:] == '.txt':
            f = open(os.path.join(dir_name, fname),encoding='utf8')
            texts.append(f.read())
            f.close()
            if label_type == 'neg':
                labels.append(0)
            else:
                labels.append(1)

for i in range(10):
    for label, text in zip(labels, texts):
        print (label)
        print ("###")
        print (text)
