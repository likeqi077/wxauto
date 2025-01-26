from zhipuai import ZhipuAI

from utils.configs import default_user_name, default_wechat_name, default_model_name, zhipu_api_key
from utils.msg import prompt_template, character_description


class ZhipuModel:
    def __init__(self, user_name=default_user_name, wechat_name=default_wechat_name, model_name=default_model_name,
                 api_key=zhipu_api_key):
        self.user_name = user_name
        self.wechat_name = wechat_name
        self.model_name = model_name
        self.client = ZhipuAI(api_key=api_key)

    def format_prompt_from_msgs(self, msgs):
        chat_hist = ''
        for msg in msgs:
            if msg['user'] == "Self":
                chat_hist += f"{self.user_name}: {msg['content']}\n"
            else:
                chat_hist += f"{msg['user']}: {msg['content']}\n"
        formatted_prompt = prompt_template.format(user=self.user_name, chat_hist=chat_hist,
                                                  char_desc=character_description)
        formatted_msgs = [{'role': 'system',
                           'content': '记住，你的名字是' + self.user_name + '，请作为他/她完成聊天'},
                          {'role': 'user', 'content': formatted_prompt}]
        return formatted_msgs

    def chat(self, msgs):
        formatted_msgs = self.format_prompt_from_msgs(msgs)
        print(f"prompt")
        for msg in formatted_msgs:
            print(f"{msg['role']}: {msg['content']}")
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=formatted_msgs,
        )
        return response.choices[0].message.content

