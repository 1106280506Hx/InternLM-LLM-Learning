先下载依赖包
然后运行download.py
再运行download_hf.py

下载 NLTK 相关资源
cd /root
git clone https://gitee.com/yzy0612/nltk_data.git  --branch gh-pages
cd nltk_data
mv packages/*  ./
cd tokenizers
unzip punkt.zip
cd ../taggers
unzip averaged_perceptron_tagger.zip

下载本项目代码
cd /root/data
git clone https://github.com/InternLM/tutorial