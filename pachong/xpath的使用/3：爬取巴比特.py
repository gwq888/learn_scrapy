import json
a = [{"name":"张三"},{"afe":12},{"这些":"42"}]

a = json.dumps(a,ensure_ascii=False)
print(a)


