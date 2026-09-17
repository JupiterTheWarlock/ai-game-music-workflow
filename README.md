# AI Game Music Workflow

一个面向独立游戏开发者的 Agent Skill：先做一段短小、容易识别的原创旋律，再用 AI 把它改编成多个场景的游戏音乐。

它适合这些情况：

- 不会系统作曲，但希望不同场景的 BGM 听起来属于同一款游戏；
- 已经有一段 WAV，想围绕它做不同编曲；
- AI 生成的音乐逐渐偏离了上传的旋律；
- 想把提示词、结果和每次修改记录下来，方便继续迭代。

## 方法概览

1. 明确游戏需要怎样的音乐身份。
2. 生成或导入一段简短的核心旋律。
3. 用统一音色试听、编号并选出核心旋律。
4. 选择几个差异明显的场景做压力测试。
5. 上传核心旋律，让音乐模型重新编曲。
6. 判断问题属于旋律、气质、音色、节奏低频还是结构，再逐项修改。
7. 保存提示词、结果和判断，整理成可继续使用的音乐素材。

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
使用 $ai-game-music-workflow，帮我先做一组短旋律候选，再把选中的旋律改编成几个场景版本。
```

## 仓库内容

- `SKILL.md`：完整工作方法与处理边界。
- `references/prompt-template.md`：场景卡片、提示词模板和常见问题的修改方法。
- `references/iteration-log-template.md`：每轮生成结果的记录模板。
- `agents/openai.yaml`：Codex 中显示的 Skill 信息。

## License

MIT
