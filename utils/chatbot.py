import time

from utils.configs import default_wechat_name, default_user_name
from utils.msg import format_raw_msgs


class Chatbot:
    def __init__(self, wx_client, llm, wechat_name=default_wechat_name, user_name=default_user_name):
        self.wx = wx_client
        self.llm = llm
        self.friend_list = []
        self.wechat_name = wechat_name
        self.user_name=user_name

    def add_friend(self, friend_name):
        if friend_name not in self.friend_list:
            self.friend_list.append(friend_name)
        else:
            print(f"friend {friend_name} already in the friend list")

    def chat_with(self, user_name):
        self.wx.ChatWith(user_name)
        raw_msgs = self.wx.GetAllMessage()
        msgs = format_raw_msgs(raw_msgs)
        if msgs[-1]['user'] != self.wechat_name and msgs[-1]['user'] != "Self":
            try:
                response = self.llm.chat(msgs)
                if response.startswith(f"{self.user_name}: "):
                    response = response[len(f"{self.user_name}: "):]
            except Exception as e:
                response = f"Error: {e}"
            print(f"response: {response}")
            self.wx.SendMsg(response, user_name)

    def run(self):
        while True:
            for friend in self.friend_list:
                self.chat_with(friend)
                time.sleep(3)
