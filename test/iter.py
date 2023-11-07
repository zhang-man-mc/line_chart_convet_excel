import os

from github import Github

repo_user = "zhang-man-mcm"  # 改为你的GitHub用户名
repo_name = "day_cache4"  # 改为你的仓库名称
access_token = "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"  # 改为你的个人访问令牌

# 指定要上传的文件夹路径
folder_path = r"C:\Users\19125\Desktop\10月-天钥桥-简报-11.6做好"  # 改为你要上传的文件夹路径

# 创建GitHub实例
g = Github(access_token)

# 获取用户
user = g.get_user()

# 在GitHub上创建一个新的仓库
repo = user.create_repo(repo_name)

# 将当前文件夹设置为Git仓库
base_path = os.path.abspath(folder_path)
os.chdir(base_path)
os.system("git init")

# 遍历文件夹下的文件
for root, dirs, files in os.walk(base_path):
    for file in files:
        file_path = os.path.join(root, file)

        # 添加文件至Git仓库
        os.system(f'git add "{file_path}"')

# 首次提交并将仓库与远程关联
os.system('git commit -m "Initial commit"')
os.system(f"git remote add origin git@github.com:/{repo_user}/{repo_name}.git")
os.system("git push -u origin master")

print("文件上传完成！")
print("文件上传完成！")
print("文件上传完成！")
print("文件上传完成！")
