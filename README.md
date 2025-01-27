# 适用PC微信3.9.8.15版本

基于wxauto项目(https://github.com/cluic/wxauto) 的Windows版本微信客户端自动化及智谱AI，可实现使用AI进行自动聊天

**3.9.8.15版本微信安装包下载**：
[点击下载](https://github.com/tom-snow/wechat-windows-versions/releases/download/v3.9.8.15/WeChatSetup-3.9.8.15.exe)


|  环境  | 版本 |
| :----: | :--: |
|   OS   | [![Windows](https://img.shields.io/badge/Windows-10\|11\|Server2016+-white?logo=windows&logoColor=white)](https://www.microsoft.com/)  |
|  微信  | [![Wechat](https://img.shields.io/badge/%E5%BE%AE%E4%BF%A1-3.9.8.X-07c160?logo=wechat&logoColor=white)](https://pan.baidu.com/s/1FvSw0Fk54GGvmQq8xSrNjA?pwd=vsmj) **(3.9.9疑似容易掉线)** |
| Python | [![Python](https://img.shields.io/badge/Python-3.X-blue?logo=python&logoColor=white)](https://www.python.org/) **(不支持3.7.6和3.8.1)**|


## 基于智谱AI的自动聊天机器人
在utils/configs.py中，配置以下变量：
- whiteList: 自动聊天的好友/群名
- zhipu_api_key: 智谱AI的api
- default_user_name: 想要AI扮演的角色名
- default_wechat_name: 账号的微信名
- default_model_name: 调用的智谱AI模型名，如glm-4-plus、glm-4-air-0111、glm-4-airx、glm-4-long 、glm-4-flashx 、glm-4-flash等

配置完成后运行auto_chat.py即可


## 免责声明
代码仅供交流学习使用，请勿用于非法用途和商业用途！如因此产生任何法律纠纷，均与作者无关！



