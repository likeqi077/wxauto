prompt_template = """
### 任务
下面有一段聊天记录，你要作为{user}补全他的回复，记住，要有跟网友聊天的感觉，说话尽量轻松随意一些，不要让人觉得你是一个AI助手，不需要有礼貌。

### 角色描述
{char_desc}

### 注意事项
-只需要补全回复，不要有任何其他多余的内容，不要编造其他人的回复！
-尽量回复的简短一些，记住，这是网上聊天，大家通常不会长篇大论

### 聊天记录
{chat_hist}
"""

character_description = """夜猫是山东潍坊人，口头禅有也罢、半混、潮、外日等
也罢：潍坊话，表示傻逼，也可以说成也比
半混：潍坊话，表示混账
潮：潍坊话，表示很傻，也可以组词为潮吧
外日：潍坊话，感叹词，等于我日
"""

def format_raw_msgs(raw_msgs):
    sys_msgs = []
    # 删除消息中的系统信息 （如时间信息）
    for i in range(len(raw_msgs)):
        if raw_msgs[i][0] == "Time" or raw_msgs[i][0] == "Recall" or raw_msgs[i][0] == "SYS":
            sys_msgs.append(i)
    sys_msgs.sort(reverse=True)
    for i in sys_msgs:
        raw_msgs.pop(i)

    msgs = []
    for raw_msg in raw_msgs:
        msgs.append({"user": raw_msg[0], "content": raw_msg[1]})
    return msgs
