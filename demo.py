import yaml

code="""



"""

with open("gitlab-ci.yml",'r') as f:
    data1=yaml.safe_load(f)


print(data1)