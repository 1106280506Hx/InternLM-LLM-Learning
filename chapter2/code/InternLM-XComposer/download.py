import torch
from modelscope import snapshot_download, AutoModel, AutoTokenizer
import os
model_dir = snapshot_download('Shanghai_AI_Laboratory/internlm-xcomposer-7b', cache_dir='/root/model', revision='master')


### and then git clone code

# cd /root/code
# git clone https://gitee.com/internlm/InternLM-XComposer.git
# cd /root/code/InternLM-XComposer
# git checkout 3e8c79051a1356b9c388a6447867355c0634932d  # 最好保证和教程的 commit 版本一致

###  then run the code

# cd /root/code/InternLM-XComposer
# python examples/web_demo.py  \
#     --folder /root/model/Shanghai_AI_Laboratory/internlm-xcomposer-7b \
#     --num_gpus 1 \
#     --port 6006