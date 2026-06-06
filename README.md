# 🎮 AI Gaming

AI游戏工具，支持游戏设计、关卡生成、NPC对话。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 🎯 游戏机制设计
- 🗺️ 关卡生成
- 💬 NPC对话生成
- 📜 任务生成
- 💰 经济平衡
- 📖 游戏故事生成

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_gaming import create_tools

tools = create_tools()

# 游戏机制
mechanic = tools.design_game_mechanic("RPG", "技能树系统")

# 关卡生成
level = tools.generate_level("平台跳跃", "medium", "森林")

# NPC对话
dialogue = tools.generate_npc_dialogue("商人", "友好", "玩家首次进入商店")

# 任务生成
quest = tools.generate_quest("奇幻世界", "主线")

# 经济平衡
balance = tools.balance_game_economy(economy_data)

# 游戏故事
story = tools.generate_game_story("RPG", "中世纪奇幻")
```

## 📁 项目结构

```
ai-gaming/
├── tools.py       # 游戏工具核心
└── README.md
```

## 📄 许可证

MIT License
