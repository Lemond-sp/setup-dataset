lang=ja
path=/home/kajikawa_r/datasets/wiki40b

for i in 'train' 'test' 'validation'
do 
  python src/wiki.py \
        --outfile ${path}/${i}-${lang}.txt \
        --mode ${i} \
        --lang ${lang}
done