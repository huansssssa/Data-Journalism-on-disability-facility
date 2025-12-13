import re
import json
from dashscope import Generation

def build_prompt(text: str) -> str:
    return f"""
请从以下政策或统计公报中提取无障碍设施相关量化指标。
仅返回文本中明确或可合理推断的数据，不要编造。

指标：
1. 市县无障碍建设覆盖率（%）
2. 公共交通线路无障碍覆盖率（%）
3. 无障碍或适老化出行服务覆盖率（%）

返回 JSON：
{{
  "city_rate": 数值或null,
  "line_rate": 数值或null,
  "service_rate": 数值或null
}}

文本：
{text}
"""

def extract_with_qwen(text: str) -> dict:
    """
    使用 Qwen 大模型（qwen-max）从政策文本中抽取无障碍设施覆盖率指标。
    通过 DashScope SDK 调用阿里云 Qwen API。
    """
    try:
        response = Generation.call(
            model="qwen-max",               # 明确指定使用 Qwen 最强推理版本
            prompt=build_prompt(text),
            temperature=0.0,                # 确保结果确定性
            result_format="message"         # 返回标准 message 格式
        )

        if response.status_code != 200:
            raise RuntimeError(f"Qwen API error: {response.code} - {response.message}")

        content = response.output.choices[0].message.content

        # 提取 JSON 块（兼容可能的前后缀）
        match = re.search(r"\{.*\}", content, re.DOTALL)
        if not match:
            raise ValueError("No valid JSON found in Qwen response")

        parsed = json.loads(match.group())
        # 确保字段存在且为数字或 null
        for key in ["city_rate", "line_rate", "service_rate"]:
            val = parsed.get(key)
            if val is not None and not isinstance(val, (int, float)):
                parsed[key] = None
        return parsed

    except Exception as e:
        print(f"⚠️ Qwen extraction failed for text snippet: {text[:100]}... | Error: {e}")
        return {"city_rate": None, "line_rate": None, "service_rate": None}