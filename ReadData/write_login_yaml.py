import yaml
data = {"name": "张三", "age": 18}
with open("../Data/write_login.yaml", "w", encoding='utf-8')as f:
    yaml.dump(data, f, allow_unicode=True)