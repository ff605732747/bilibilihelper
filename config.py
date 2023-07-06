config = {
    "multi": [
        {
            "cookie": "buvid3=8C1CB2BF-D71D-8A25-0D02-E924DDB8CA0A63561infoc; b_nut=1687924063; i-wanna-go-back=-1; _uuid=48C714F10-933A-AB1010-CE4E-D5AF34BB666B86323infoc; FEED_LIVE_VERSION=V8; header_theme_version=CLOSE; home_feed_column=5; rpdid=|(u|JJ~|k~|Y0J'uY)~mkY)Ym; fingerprint=bc1eff8756b7daf68216f06a2837f92a; buvid_fp_plain=undefined; SESSDATA=015f9683%2C1703478919%2C92143%2A62w44T-eWFOjDcD7tXJs50XhKPV9-UberzGxdLDrTTKBQFrgYg1TguGuFIfh2AiVP5eZDdcwAAMgA; bili_jct=61f94d72522fe8741af78c39ec9413b6; DedeUserID=353750; DedeUserID__ckMd5=128b462ca7f1237c; sid=54x04c80; bp_t_offset_353750=812100650047373385; b_ut=5; buvid4=395239AE-C3B8-426F-9716-5A2435EF358463561-023062811-7CPQ%2BUOUPgS8hGoVy%2F9ijw%3D%3D; nostalgia_conf=-1; share_source_origin=QQ; bsource=search_bing; b_lsid=D5F108B58_1890653BD60; innersign=0; browser_resolution=2505-682; CURRENT_BLACKGAP=0; CURRENT_FNVAL=16; bp_video_offset_353750=812579680379994100; buvid_fp=95EED967-DAF9-F2D4-691B-0522D72C97D143423infoc",
            "options": {
                "watch": True,  # 每日观看视频
                "coins": 1,  # 投币个数
                "share": True,  # 视频分享
                "comics": True,  # 漫画签到
                "lb": True,  # 直播签到
                "threshold": 100,  # 仅剩多少币时不再投币(不写默认100)
                "toCoin": False,  # 银瓜子兑换硬币
            },
            # "push": {
            #     "type": "pushplus",
            #     "key": "xxx",
            # },
        },
        {
            "cookie": "buvid3=8C1CB2BF-D71D-8A25-0D02-E924DDB8CA0A63561infoc; b_nut=1687924063; i-wanna-go-back=-1; _uuid=48C714F10-933A-AB1010-CE4E-D5AF34BB666B86323infoc; FEED_LIVE_VERSION=V8; header_theme_version=CLOSE; home_feed_column=5; rpdid=|(u|JJ~|k~|Y0J'uY)~mkY)Ym; fingerprint=bc1eff8756b7daf68216f06a2837f92a; buvid_fp_plain=undefined; SESSDATA=015f9683%2C1703478919%2C92143%2A62w44T-eWFOjDcD7tXJs50XhKPV9-UberzGxdLDrTTKBQFrgYg1TguGuFIfh2AiVP5eZDdcwAAMgA; bili_jct=61f94d72522fe8741af78c39ec9413b6; DedeUserID=353750; DedeUserID__ckMd5=128b462ca7f1237c; sid=54x04c80; bp_t_offset_353750=812100650047373385; b_ut=5; buvid4=395239AE-C3B8-426F-9716-5A2435EF358463561-023062811-7CPQ%2BUOUPgS8hGoVy%2F9ijw%3D%3D; nostalgia_conf=-1; share_source_origin=QQ; bsource=search_bing; b_lsid=D5F108B58_1890653BD60; innersign=0; browser_resolution=2505-682; CURRENT_BLACKGAP=0; CURRENT_FNVAL=16; bp_video_offset_353750=812579680379994100; buvid_fp=95EED967-DAF9-F2D4-691B-0522D72C97D143423infoc",
            "options": {
                "watch": True,  # 每日观看视频
                "coins": 2,  # 投币个数
                "share": True,  # 视频分享
                "comics": True,  # 漫画签到
                "lb": True,  # 直播签到
                "toCoin": False,  # 银瓜子兑换硬币
            },
            # "push": [
            #     # 以数组的形式填写, 则会向多个服务推送消息
            #     {
            #         "type": "pushplus",
            #         "key": "xxx",
            #     },
            #     {
            #         "type": "workWechat",
            #         "key": {
            #             "agentid": 1000002,
            #             "corpSecret": "xxx",
            #             "corpid": "xxx",
            #         },
            #     },
            # ],
        },
    ],
    "push": {
        # 合并发送消息, 只合并未单独配置 push 的账号
        "type": "pushplus",
        "key": "xxx",
    },
}
