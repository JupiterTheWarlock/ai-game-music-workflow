# AI Game Music Workflow

一个面向零基础独立游戏开发者的 Agent Skill，用三步完成一套可以继续迭代的游戏音乐：

1. 生成编号的核心短旋律候选，并打开离线试听页。
2. 根据场景、风格和用户需求生成提示词。
3. 使用 Suno Cover 生成音乐，再根据试听结果逐项调整。

## 使用

### 一句话安装

```text
请安装这个 Skill：https://github.com/JupiterTheWarlock/ai-game-music-workflow
```

也可以直接使用命令：

```bash
npx skills add JupiterTheWarlock/ai-game-music-workflow
```

### 一句话开始

```text
使用 ai-game-music-workflow，帮我先做一组短旋律候选，再把选中的旋律改编成几个场景版本。
```

如果客户端支持显式 Skill 语法，也可以使用 `$ai-game-music-workflow`；其他客户端直接发送上面的自然语言即可。

## 三步会得到什么

### 1. 核心短旋律

- 默认生成 12 段同音色、相近时长的 WAV；
- 自动编号；
- 自动生成并打开离线试听页；
- 用户按编号选出核心旋律。

### 2. 场景提示词

- 先用普通语言确认各场景想要的感觉；
- 再整理成可以直接粘贴到音乐模型里的提示词；
- 不要求用户掌握乐理或制作术语。

### 3. Suno Cover

- 上传选中的 WAV；
- 使用 Cover 生成不同场景版本；
- 根据听感判断主要问题；
- 每轮尽量只修改一类问题，并保留旧结果。

## 仓库内容

- `SKILL.md`：三步主流程、边界和完成标准。
- `scripts/generate_candidates.py`：生成编号 WAV，并构建试听页。
- `scripts/build_review_page.py`：把已有 WAV 整理成试听页。
- `assets/review-page.html`：与音频内容分离的通用试听页框架。
- `references/motif-generation-and-review.md`：候选旋律和试听页说明。
- `references/suno-cover.md`：Suno 上传、Cover、生成和验证流程。
- `references/prompt-template.md`：场景提示词与常见问题调整表。
- `references/iteration-log-template.md`：每轮结果的记录模板。

## 运行要求

- Python 3.8 或更高版本；
- 生成候选和试听页不需要第三方 Python 包；
- Suno 阶段需要用户自己的账号及可用权限。

## License

MIT
