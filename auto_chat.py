from utils.chatbot import Chatbot
from utils.configs import whiteList
from utils.zhipu import ZhipuModel
from wxauto import WeChat


if __name__ == '__main__':
    wx = WeChat()
    llm = ZhipuModel()
    chatbot = Chatbot(wx, llm)
    for friend in whiteList:
        chatbot.add_friend(friend)
    chatbot.run()
