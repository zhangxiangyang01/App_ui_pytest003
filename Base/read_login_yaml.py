import yaml, sys, os

def get_yaml():
    with open(os.getcwd()+os.sep+"Data"+os.sep+"login_data.yaml", 'r', encoding='utf-8') as f:
        return yaml.load(f, Loader=yaml.FullLoader)

# def get_yaml22():
#     with open("../Data/login_data.yaml", 'r', encoding='utf-8') as f:
#         return yaml.load(f, Loader=yaml.FullLoader)

if __name__ == '__main__':
    # print(get_yaml())
    # print(get_yaml().values())
    arrs = []
    for i in get_yaml().values():
        arrs.append((i.get("username"), i.get("pwd"), i.get("expect_toast")))
    print(arrs)

