infos = [
    {
        'sno': '32306300085',         # 学号
        'pwd': '050624HJH.',         # 密码
        'devName': '4c-096',   # 预约的座位号（不足3位数的要补零）
        'name': '猪猪侠',        # 随便起个名字
        'periods': (            # 预约时间段（每段时间不能超过4小时）
            ('8:30:00', '12:30:00'),
            ('13:30:00', '17:30:00'),
            ('18:15:00', '22:15:00')
        ),
        'pushplus': '',         # pushplus 的 token（用于推送消息到微信）
    },

    # 如果只是一个人预约座位，不需要帮别人预约签到，则可把下面三个字典注释/删除
    {
        'sno': '32206200066',
        'pwd': '3220620066#Deng',  
        'devName': '4c-095',
        'name': '皮卡丘',
        'periods': (
            ('8:30:00', '12:30:00'),
            ('13:30:00', '17:30:00'),
            ('18:15:00', '22:15:00')
        ),
        'pushplus': '',
    },
]
