translation-agent：
[ ] 1 zhipuai跑通反射agent的translation
[ ] 2 单独添加一个术语翻译模块：
  [ ] 2.1 词典的定义 参考百度、小牛
  [ ] 2.2 词典抽取（bm25s+faiss-cpu+onnx_embed） cpu检索，轻量化
  [ ] 2.3 prompt修改 
[ ] 3 有榜单benchmark，评估效果（flores、frmt、ifly）数据集。指标：bleu还有术语词的准确性
[ ] 4 模型库，追踪新老的术语翻译方法。并且能够对llm做微调
[ ] 5 兼容性：与llama-idx兼容
[ ] 6 服务化：有fastapi或laptonai部署成api服务，有dockerfile打包，有webui翻译。

conda create -n translation_agent python=3.10
conda activate translation_agent
pip install -r requirements.txt

pip install -e .

export ZHIPUAI_API_KEY=xx

python setup.py develop --no-deps

```python
import translation_agent as ta
ta.translate(source_lang="Chinese",target_lang="English", 
            source_text="你好啊 小牛翻译", country="China")
#>>> import translation_agent as ta
#>>> 'Translating text as a single chunk'
#>>> 'Hello, Young Bull Translation.'
```