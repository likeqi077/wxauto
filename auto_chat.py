import time
from wxauto import WeChat
from utils.utils import remove_suffix, convertToLlmMsg
from utils.configs import whiteList, zhipu_api_key, user_name, user_true_name

from zhipuai import ZhipuAI

if __name__ == '__main__':
    wx = WeChat()
    client = ZhipuAI(api_key=zhipu_api_key)
    print(whiteList)
    while True:
        print("ONE LOOP")
        new_msgs = wx.GetNextNewMessage()
        while new_msgs is not None:
            for user, msgs in new_msgs.items():
                print(user)
                user = remove_suffix(user, "已置顶")
                if user not in whiteList:
                    continue
                all_msgs = wx.GetAllMessage()
                wx.ChatWith('文件传输助手')
                msgToLlm = convertToLlmMsg(all_msgs, user_name, user_true_name)
                for msg in msgs:
                    print(msg[0] + '说了：' + msg[1])
                print(msgToLlm)
                try:
                    response = client.chat.completions.create(
                        model="glm-4",  # 填写需要调用的模型名称
                        messages=msgToLlm,
                        max_tokens=32*4
                    )
                    reply = response.choices[0].message.content
                    if reply.startswith(user_true_name + "："):
                        reply = reply[3:]
                except Exception as e:
                    reply = '你的输入有问题，请换个问题'
                    print(e)
                wx.SendMsg(reply, user)
                print("我： " + reply)
            new_msgs = wx.GetNextNewMessage()
        wx.ChatWith('文件传输助手')
        time.sleep(10)
