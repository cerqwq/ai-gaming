"""
AI Gaming - AI游戏工具
支持游戏设计、关卡生成、NPC对话
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AIGamingTools:
    """
    AI游戏工具
    支持：设计、关卡、NPC
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def design_game_mechanic(self, genre: str, concept: str) -> Dict:
        """设计游戏机制"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请为{genre}游戏设计核心机制：

概念：{concept}

请返回JSON格式：
{{
    "core_mechanic": "核心机制",
    "rules": ["规则1", "规则2"],
    "progression": "进度系统",
    "feedback_loops": ["反馈循环"],
    "monetization": "变现建议"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"design": content}

    def generate_level(self, game_type: str, difficulty: str, theme: str) -> Dict:
        """生成关卡"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请为{game_type}游戏生成{difficulty}难度的关卡：

主题：{theme}

请返回JSON格式：
{{
    "name": "关卡名",
    "objective": "目标",
    "layout": "布局描述",
    "enemies": [{{"type": "敌人类型", "count": 数量, "behavior": "行为"}}],
    "items": [{{"type": "道具", "location": "位置"}}],
    "traps": [{{"type": "陷阱", "location": "位置"}}],
    "boss": {{}}
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"level": content}

    def generate_npc_dialogue(self, npc_name: str, personality: str, context: str) -> Dict:
        """生成NPC对话"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请为{npc_name}生成对话：

性格：{personality}
情境：{context}

请返回JSON格式：
{{
    "greetings": ["问候语"],
    "quest_dialogue": ["任务对话"],
    "casual_chat": ["闲聊"],
    "farewell": ["告别语"],
    "lore": ["背景故事"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"dialogue": content}

    def generate_quest(self, game_world: str, quest_type: str) -> Dict:
        """生成任务"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请为{game_world}生成{quest_type}任务：

请返回JSON格式：
{{
    "name": "任务名",
    "description": "描述",
    "objectives": ["目标"],
    "steps": [{{"step": "步骤", "description": "描述"}}],
    "rewards": ["奖励"],
    "difficulty": "难度",
    "estimated_time": "预估时间"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"quest": content}

    def balance_game_economy(self, economy_data: Dict) -> Dict:
        """平衡游戏经济"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        data_text = json.dumps(economy_data, ensure_ascii=False)

        prompt = f"""请分析并平衡以下游戏经济数据：

{data_text}

请返回JSON格式：
{{
    "issues": ["问题"],
    "adjustments": [
        {{"item": "物品", "current": "当前值", "suggested": "建议值", "reason": "原因"}}
    ],
    "new_mechanics": ["建议新机制"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"balance": content}

    def generate_game_story(self, genre: str, setting: str) -> str:
        """生成游戏故事"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请为{genre}游戏生成故事：

背景：{setting}

要求：
1. 引人入胜的开头
2. 多条故事线
3. 分支选择
4. 多种结局"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        return response.choices[0].message.content


def create_tools(**kwargs) -> AIGamingTools:
    """创建游戏工具"""
    return AIGamingTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI Gaming Tools")
    print()

    # 测试
    mechanic = tools.design_game_mechanic("RPG", "技能树系统")
    print(json.dumps(mechanic, ensure_ascii=False, indent=2))
