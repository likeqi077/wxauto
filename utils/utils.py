prompt = """
### 任务
下面有一段聊天记录，你要作为{user}补全他的回复，记住，要有跟网友聊天的感觉，说话尽量轻松随意一些，不要让人觉得你是一个AI助手，不需要有礼貌。

注意：
-只需要补全回复，不要有任何其他多余的内容
-尽量回复的简短一些，记住，这是网上聊天，大家通常不会长篇大论

###聊天记录
{chat_hist}
"""

def remove_suffix(string, suffix):
    # remove a certain suffix in a string if it has it, do nothing if it does not
    if string.endswith(suffix):
        return string[:-len(suffix)]
    return string

def convertToLlmMsg(msgs, self_name, self_true_name, hist_len=8):
    print(msgs)
    sys_msgs = []
    for i in range(len(msgs)):
        if msgs[i][0] == "Time" or msgs[i][0] == "Recall":
            sys_msgs.append(i)
    sys_msgs.sort(reverse=True)
    for i in sys_msgs:
        msgs.pop(i)
    if len(msgs) > hist_len:
        msgs = msgs[-hist_len:]
    msgToLlm = []
    msgHist = ''
    for msg in msgs:
        if msg[0] == self_name:
            msgHist += self_true_name + '：' + msg[1] + '\n'
        else:
            msgHist += msg[0] + '：' + msg[1] + '\n'
    msgHist += self_true_name + '：'
    formatted_prompt = prompt.format(user=self_true_name, chat_hist=msgHist)
    msgToLlm.append({'role': 'system',
                     'content': '记住，你的名字是' + self_true_name +'，请作为他/她完成聊天'})
    msgToLlm.append({'role': 'user', 'content': formatted_prompt})
    print(msgToLlm)
    return msgToLlm


