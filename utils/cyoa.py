from zhipuai import ZhipuAI

start_user_prompt_1 = """
Ignore all previous instructions.\n\nWrite all output in Chinese.\n\nImagine you are a Choose Your Own Adventure book. \n\nStart by suggesting the user 9 random CYOA books to choose from, or, option 10, where you prompt the user for a custom story.\n\nAfter the story is determined, you respond as if it's a page from the CYOA book, complete with choices I have to pick from. \n\nUser will enter their choice. Then you continue showing the user stories from the CYOA pages, and so on, until you decide to end the game with a good or bad ending.\n\nMake the plot of the story very interesting and exciting, so introduce plot twists every now and then.\n\n I'll send you the story theme later. If you understand, reply“明白”
"""
start_user_prompt_2 = """
请给出九个故事，它们应该尽量适合多人一起游玩
"""

start_system_prompt = """
明白
"""

AI_mark = "9876543210qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"

messages = [
    {"role": "user", "content": start_user_prompt_1},
    {'role': 'assistant', 'content': start_system_prompt},
    {'role': 'user', 'content': start_user_prompt_2},
]

client = ZhipuAI(api_key="")  # 填写您自己的APIKey

def start_game():
    response = client.chat.completions.create(
        model="glm-3-turbo",  # 填写需要调用的模型名称
        messages=messages
    )
    reply = response.choices[0].message.content
    messages.append({'role': 'assistant', 'content': reply})
    print(messages)
    return reply

def story_choice(user_input):
    messages.append({'role': 'user', 'content': user_input})
    response = client.chat.completions.create(
        model="glm-3-turbo",  # 填写需要调用的模型名称
        messages=messages
    )
    reply = response.choices[0].message.content
    messages.append({'role': 'assistant', 'content': reply})
    print(messages)
    return reply

def run_story(input):
    messages.append({'role': 'user', 'content': input})
    response = client.chat.completions.create(
        model="glm-3-turbo",  # 填写需要调用的模型名称
        messages=messages
    )
    reply = response.choices[0].message.content
    messages.append({'role': 'assistant', 'content': reply})
    print(messages)
    return reply

if __name__ == "__main__":
    print(start_game())
    print(story_choice("3"))
    print(run_story("""
张三：1
谭sir：3
赵构：2
"""))

