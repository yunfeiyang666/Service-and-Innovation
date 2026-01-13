# GitHub 小组协作指南

本指南帮助团队成员从零开始学习 GitHub 协作流程。

---

## 一、前置准备（只做一次）

### 1. 安装 Git

1. 去 [Git 官方网站](https://git-scm.com/) 下载安装包（搜索 "Git for Windows"）。
2. 安装过程中一直「下一步」即可，默认设置就行。

**安装时几个关键选项的推荐：**

- **Choosing the default editor**：推荐选 **VS Code** 或 **Notepad**，不要选 Vim（对新手不友好）。
- **Adjusting your PATH environment**：选 **"Git from the command line and also from 3rd-party software"**。
- **Choosing the HTTPS transport backend**：保持默认 **"Use the OpenSSL library"**。
- **Configuring the line ending conversions**：选默认 **"Checkout Windows-style, commit Unix-style line endings"**。
- 其他选项保持默认即可。

### 2. 验证安装

安装完成后，打开 PowerShell 或 CMD，输入：

```bash
git --version
```

看到类似 `git version 2.xx.x` 就表示安装成功。

### 3. 配置你的 Git 身份（只需配置一次）

```bash
git config --global user.name "你的名字"
git config --global user.email "你的邮箱@example.com"
```

检查是否配置成功：

```bash
git config --global --list
```

---

## 二、在 GitHub 上创建公共仓库

1. 登录 [github.com](https://github.com)。
2. 右上角点 `+`，选择 **New repository**。
3. 填写：
   - **Repository name**：比如 `team-demo`。
   - 选择 **Public**。
   - 勾选 `Add a README file`。
4. 点击 **Create repository**。

### 邀请组员协作

1. 打开仓库页面，点上方的 **Settings**。
2. 左侧菜单选择 **Collaborators**（或 "Manage access"）。
3. 点 **Add people**，输入队友的 GitHub 用户名，发送邀请。
4. 队友在 GitHub 通知里接受邀请后，就能推送代码了。

---

## 三、把仓库克隆到本地

在 GitHub 仓库页面上：

1. 点击绿色按钮 **Code**。
2. 选择 HTTPS，复制仓库地址。

在本地终端运行：

```bash
git clone https://github.com/用户名/仓库名.git
cd 仓库名
```

---

## 四、日常协作流程（命令行版）

### 整体流程

1. **先拉取最新代码**：`git pull`
2. **在本地修改代码/文件**
3. **查看改动**：`git status` / `git diff`
4. **提交到本地仓库**：`git add` + `git commit`
5. **推送到 GitHub**：`git push`

### 具体命令

```bash
# 拉取团队最新代码（每次开始写代码前先执行）
git pull

# 查看当前改动状态
git status

# 把所有改动加入暂存区
git add .

# 提交到本地仓库
git commit -m "描述本次修改的内容"

# 推送到 GitHub
git push
```

---

## 五、使用分支进行协作（推荐）

多人协作时，建议：
- `main` 分支只放稳定、已审核的代码。
- 每个人为新功能**新建一个分支**。
- 改完代码 → 提交推送 → 发起 Pull Request → 审核后合并到 `main`。

### 分支操作命令

```bash
# 确保在 main 分支且是最新
git checkout main
git pull

# 创建并切换到新分支
git checkout -b feature-login

# 在分支上开发、提交
git add .
git commit -m "实现登录页面"

# 第一次推送新分支
git push --set-upstream origin feature-login

# 之后再推送同一分支
git push
```

### 发起 Pull Request（PR）

1. 打开 GitHub 仓库页面。
2. 看到 "Compare & pull request" 提示，点进去。
3. 确认 base 分支是 `main`，compare 分支是你的功能分支。
4. 填写标题和说明，点 **Create pull request**。
5. 队友审核后，点 **Merge pull request** 合并。

---

## 六、处理冲突

冲突发生在 `git pull` 或合并时，如果你和队友修改了同一行代码。

### 解决方法

1. 打开有冲突的文件，会看到类似：

   ```
   <<<<<<< HEAD
   你的修改
   =======
   队友的修改
   >>>>>>> origin/main
   ```

2. 手动编辑，保留最终想要的内容，删除冲突标记。
3. 解决后：

   ```bash
   git add 有冲突的文件名
   git commit -m "解决冲突"
   git push
   ```

---

## 七、常用命令速查表

```bash
# 克隆远程仓库
git clone 仓库地址

# 查看当前状态
git status

# 查看当前分支
git branch

# 切换到某分支
git checkout 分支名

# 新建分支并切换
git checkout -b 新分支名

# 拉取远程最新代码
git pull

# 暂存所有改动
git add .

# 暂存某个文件
git add 文件名

# 提交到本地
git commit -m "提交说明"

# 推送到远程
git push

# 推送并设置上游分支（第一次推送新分支用）
git push --set-upstream origin 分支名

# 查看提交历史
git log --oneline
```

---

## 八、GitHub Desktop 使用方法（图形界面）

如果不想用命令行，可以使用 GitHub Desktop。

### 基本操作

1. **克隆仓库**：`File → Clone repository`
2. **查看改动**：左侧 Changes 栏会显示修改的文件
3. **提交**：左下角填 Summary，点 `Commit to main`
4. **推送**：右上角点 `Push origin`
5. **拉取**：右上角点 `Pull origin`（如果有更新）

### 新建分支

1. 顶部 `Current branch` 处点击。
2. 点 `New branch`，输入分支名。
3. 点 `Create branch`。

### Preview Pull Request

在分支上完成开发后，点 **Preview Pull Request** 可以：
- 预览你的分支和 main 分支的差异
- 跳转到 GitHub 网页发起正式的 Pull Request

---

## 九、协作最佳实践

1. **每次开始写代码前先 `git pull`**，保持本地代码最新。
2. **频繁提交**，每完成一个小功能就 commit 一次，说明写清楚。
3. **使用分支开发**，不要直接在 main 上改代码。
4. **发起 PR 让队友审核**，减少 bug。
5. **遇到冲突不要慌**，仔细看冲突内容，手动合并后再提交。

---

祝协作愉快！🎉
