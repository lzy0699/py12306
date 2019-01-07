# coding=utf-8
# 查询余票
import time

BASE_URL_OF_12306 = 'https://kyfw.12306.cn'

LEFT_TICKETS = {
    "url": BASE_URL_OF_12306 + "/otn/{type}?leftTicketDTO.train_date={left_date}&leftTicketDTO.from_station={left_station}&leftTicketDTO.to_station={arrive_station}&purpose_codes=ADULT",
    "re_try": 10,
    "re_time": 0.01,
    "s_time": 0.01,
    "is_logger": False,
    "is_json": True,
    "is_cdn": True,
}

API_BASE_LOGIN = {
    "url": BASE_URL_OF_12306 + '/passport/web/login',
    "method": "post",
    "is_cdn": True,
}

API_USER_CHECK = {
    "url": BASE_URL_OF_12306 + '/otn/login/checkUser',
    "method": "post",
    "is_cdn": True,
}

API_AUTH_CODE_DOWNLOAD = {
    'url': BASE_URL_OF_12306 + '/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&_={random}'
}
API_AUTH_CODE_CHECK = {
    'url': BASE_URL_OF_12306 + '/passport/captcha/captcha-check?answer={answer}&rand=sjrand&login_site=E&_={random}'
}
API_AUTH_UAMTK = {
    'url': BASE_URL_OF_12306 + '/passport/web/auth/uamtk'
}
API_AUTH_UAMAUTHCLIENT = {
    'url': BASE_URL_OF_12306 + '/otn/uamauthclient'
}

API_USER_INFO = {
    'url': BASE_URL_OF_12306 + '/otn/modifyUser/initQueryUserInfoApi'
}
API_USER_PASSENGERS = BASE_URL_OF_12306 + '/otn/confirmPassenger/getPassengerDTOs'
API_SUBMIT_ORDER_REQUEST = BASE_URL_OF_12306 + '/otn/leftTicket/submitOrderRequest'
API_CHECK_ORDER_INFO = BASE_URL_OF_12306 + '/otn/confirmPassenger/checkOrderInfo'
API_INITDC_URL = BASE_URL_OF_12306 + '/otn/confirmPassenger/initDc'  # 生成订单时需要先请求这个页面
API_GET_QUEUE_COUNT = BASE_URL_OF_12306 + '/otn/confirmPassenger/getQueueCount'
API_CONFIRM_SINGLE_FOR_QUEUE = BASE_URL_OF_12306 + '/otn/confirmPassenger/confirmSingleForQueue'
API_QUERY_ORDER_WAIT_TIME = BASE_URL_OF_12306 + '/otn/confirmPassenger/queryOrderWaitTime?{}'  # 排队查询

API_NOTIFICATION_BY_VOICE_CODE = 'http://ali-voice.showapi.com/sendVoice?'

urls = {
    "auth": {  # 登录接口
        "req_url": "/passport/web/auth/uamtk",
        "req_type": "post",
        "Referer": "https://kyfw.12306.cn/otn/passport?redirect=/otn/login/userLogin",
        "Host": "kyfw.12306.cn",
        "Content-Type": 1,
        "re_try": 10,
        "re_time": 0.1,
        "s_time": 0.1,
        "is_logger": True,
        "is_json": True,
    },
    "login": {  # 登录接口
        "req_url": "/passport/web/login",
        "req_type": "post",
        "Referer": "https://kyfw.12306.cn/otn/login/init",
        "Host": "kyfw.12306.cn",
        "Content-Type": 1,
        "re_try": 10,
        "re_time": 0.1,
        "s_time": 0.1,
        "is_logger": True,
        "is_json": True,

    },
    "left_ticket_init": {  # 登录接口
        "req_url": "/otn/leftTicket/init",
        "req_type": "post",
        "Referer": "https://kyfw.12306.cn/otn/login/init",
        "Host": "kyfw.12306.cn",
        "Content-Type": 1,
        "re_try": 10,
        "re_time": 0.1,
        "s_time": 0.1,
        "is_logger": False,
        "is_json": False,

    },
    "getCodeImg": {  # 登录验证码
        "req_url": "/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&{0}",
        "req_type": "get",
        "Referer": "https://kyfw.12306.cn/otn/login/init",
        "Host": "kyfw.12306.cn",
        "Content-Type": 1,
        "re_try": 10,
        "re_time": 0.1,
        "s_time": 0.1,
        "is_logger": False,
        "is_json": False,
        "not_decode": True,
    },
    "codeCheck": {  # 验证码校验
        "req_url": "/passport/captcha/captcha-check",
        "req_type": "post",
        "Referer": "https://kyfw.12306.cn/otn/login/init",
        "Host": "kyfw.12306.cn",
        "Content-Type": 1,
        "re_try": 10,
        "re_time": 0.1,
        "s_time": 0.1,
        "is_logger": True,
        "is_json": True,
    },
    "loginInit": {  # 登录页面
        "req_url": "/otn/login/init",
        "req_type": "get",
        "Referer": "https://kyfw.12306.cn/otn/index/init",
        "Host": "kyfw.12306.cn",
        "re_try": 1,
        "re_time": 0.1,
        "s_time": 0.1,
        "is_logger": False,
        "is_json": False,
    },
    "loginInitCdn": {  # 登录页面
        "req_url": "/otn/login/init",
        "req_type": "get",
        "Referer": "https://kyfw.12306.cn/otn/index/init",
        "Host": "kyfw.12306.cn",
        "re_try": 1,
        "re_time": 0.1,
        "s_time": 0.1,
        "is_logger": False,
        "is_test_cdn": True,
        "is_json": False,
    },
    "getUserInfo": {  # 获取用户信息
        "req_url": "/otn/index/initMy12306",
        "req_type": "get",
        "Referer": "https://kyfw.12306.cn/otn/passport?redirect=/otn/login/userLogin",
        "Host": "kyfw.12306.cn",
        "re_try": 10,
        "re_time": 0.1,
        "s_time": 0.01,
        "is_logger": False,
        "is_json": False,
    },
    "userLogin": {  # 用户登录
        "req_url": "/otn/login/userLogin",
        "req_type": "get",
        "Referer": "https://kyfw.12306.cn/otn/passport?redirect=/otn/login/userLogin",
        "Host": "kyfw.12306.cn",
        "re_try": 10,
        "re_time": 0.1,
        "s_time": 0.1,
        "is_logger": True,
        "is_json": True,
    },
    "uamauthclient": {  # 登录
        "req_url": "/otn/uamauthclient",
        "req_type": "post",
        "Referer": "https://kyfw.12306.cn/otn/passport?redirect=/otn/login/userLogin",
        "Host": "kyfw.12306.cn",
        "Content-Type": 1,
        "re_try": 10,
        "re_time": 0.1,
        "s_time": 0.1,
        "is_logger": True,
        "is_json": True,
    },
    "initdc_url": {  # 生成订单页面
        "req_url": "/otn/confirmPassenger/initDc",
        "req_type": "get",
        "Referer": "https://kyfw.12306.cn/otn/leftTicket/init",
        "Host": "kyfw.12306.cn",
        "re_try": 10,
        "re_time": 0.1,
        "s_time": 1,
        "is_logger": False,
        "is_json": False,
    },
    "GetJS": {  # 订单页面js
        "req_url": "/otn/HttpZF/GetJS",
        "req_type": "get",
        "Referer": "https://kyfw.12306.cn/otn/confirmPassenger/initDc",
        "Host": "kyfw.12306.cn",
        "re_try": 10,
        "re_time": 0.1,
        "s_time": 0.1,
        "is_logger": False,
        "is_json": False,
    },
    "odxmfwg": {  # 订单页面js
        "req_url": "/otn/dynamicJs/odxmfwg",
        "req_type": "get",
        "Referer": "https://kyfw.12306.cn/otn/confirmPassenger/initDc",
        "Host": "kyfw.12306.cn",
        "re_try": 10,
        "re_time": 0.1,
        "s_time": 0.1,
        "is_logger": False,
        "is_json": False,
    },
    "get_passengerDTOs": {  # 获取乘车人
        "req_url": "/otn/confirmPassenger/getPassengerDTOs",
        "req_type": "post",
        "Referer": "https://kyfw.12306.cn/otn/confirmPassenger/initDc",
        "Host": "kyfw.12306.cn",
        "re_try": 10,
        "re_time": 0.1,
        "s_time": 0.1,
        "is_logger": True,
        "is_json": True,
    },
    "select_url": {  # 查询余票
        "req_url": "/otn/{3}?leftTicketDTO.train_date={0}&leftTicketDTO.from_station={1}&leftTicketDTO.to_station={2}&purpose_codes=ADULT",
        "req_type": "get",
        "Referer": "https://kyfw.12306.cn/otn/leftTicket/init",
        "Host": "kyfw.12306.cn",
        "re_try": 10,
        "re_time": 0.01,
        "s_time": 0.01,
        "is_logger": False,
        "is_json": True,
        "is_cdn": True,
    },
    "check_user_url": {  # 检查用户登录
        "req_url": "/otn/login/checkUser",
        "req_type": "post",
        "Referer": "https://kyfw.12306.cn/otn/leftTicket/init",
        "Host": "kyfw.12306.cn",
        "re_try": 10,
        "re_time": 0.3,
        "s_time": 0.1,
        "is_logger": True,
        "is_json": True,
    },
    "submit_station_url": {  # 提交订单
        "req_url": "/otn/leftTicket/submitOrderRequest",
        "req_type": "post",
        "Referer": "https://kyfw.12306.cn/otn/leftTicket/init",
        "Host": "kyfw.12306.cn",
        "re_try": 10,
        "re_time": 0.01,
        "s_time": 0.1,
        "is_logger": True,
        "is_json": True,
    },
    "checkOrderInfoUrl": {  # 检查订单信息规范
        "req_url": "/otn/confirmPassenger/checkOrderInfo",
        "req_type": "post",
        "Referer": "https://kyfw.12306.cn/otn/confirmPassenger/initDc",
        "Host": "kyfw.12306.cn",
        "re_try": 10,
        "re_time": 0.01,
        "s_time": 0.1,
        "is_logger": True,
        "is_json": True,
    },
    "getQueueCountUrl": {  # 剩余余票数
        "req_url": "/otn/confirmPassenger/getQueueCount",
        "req_type": "post",
        "Referer": "https://kyfw.12306.cn/otn/confirmPassenger/initDc",
        "Host": "kyfw.12306.cn",
        "re_try": 10,
        "re_time": 0.01,
        "s_time": 0.1,
        "is_logger": True,
        "is_json": True,
    },
    "checkQueueOrderUrl": {  # 订单队列排队
        "req_url": "/otn/confirmPassenger/confirmSingleForQueue",
        "req_type": "post",
        "Referer": "https://kyfw.12306.cn/otn/confirmPassenger/initDc",
        "Host": "kyfw.12306.cn",
        "re_try": 10,
        "re_time": 0.01,
        "s_time": 0.1,
        "is_logger": True,
        "is_json": True,
    },
    "checkRandCodeAnsyn": {  # 暂时没用到
        "req_url": "/otn/passcodeNew/checkRandCodeAnsyn",
        "req_type": "post",
        "Referer": "https://kyfw.12306.cn/otn/confirmPassenger/initDc",
        "Host": "kyfw.12306.cn",
        "re_try": 10,
        "re_time": 0.01,
        "s_time": 0.1,
        "is_logger": True,
        "is_json": True,
    },
    "codeImgByOrder": {  # 订单页面验证码
        "req_url": "/otn/passcodeNew/getPassCodeNew?module=passenger&rand=randp&{}",
        "req_type": "post",
        "Referer": "https://kyfw.12306.cn/otn/confirmPassenger/initDc",
        "Host": "kyfw.12306.cn",
        "re_try": 10,
        "re_time": 0.01,
        "s_time": 0.1,
        "is_logger": False,
        "is_json": False,
    },
    "queryOrderWaitTimeUrl": {  # 订单等待页面
        "req_url": "/otn/confirmPassenger/queryOrderWaitTime?random={0}&tourFlag=dc&_json_att=",
        "req_type": "get",
        "Referer": "https://kyfw.12306.cn/otn/confirmPassenger/initDc",
        "Host": "kyfw.12306.cn",
        "re_try": 10,
        "re_time": 0.01,
        "s_time": 0.1,
        "is_logger": True,
        "is_json": True,
    },
    "queryMyOrderNoCompleteUrl": {  # 订单查询页面
        "req_url": "/otn/queryOrder/queryMyOrderNoComplete",
        "req_type": "post",
        "Referer": "https://kyfw.12306.cn/otn/queryOrder/initNoComplete",
        "Host": "kyfw.12306.cn",
        "re_try": 10,
        "re_time": 0.01,
        "s_time": 0.1,
        "is_logger": True,
        "is_json": True,
    },
    "initNoCompleteUrl": {  # 获取订单列表
        "req_url": "/otn/queryOrder/initNoComplete",
        "req_type": "post",
        "Referer": "https://kyfw.12306.cn/otn/queryOrder/initNoComplete",
        "Host": "kyfw.12306.cn",
        "re_try": 10,
        "re_time": 0.01,
        "s_time": 0.1,
        "is_logger": False,
        "is_json": False,
    },
    "cancelNoCompleteMyOrder": {  # 取消订单
        "req_url": "/otn/queryOrder/cancelNoCompleteMyOrder",
        "req_type": "post",
        "Referer": "https://kyfw.12306.cn/otn/queryOrder/initNoComplete",
        "Host": "kyfw.12306.cn",
        "re_try": 10,
        "re_time": 0.01,
        "s_time": 0.1,
        "is_logger": True,
        "is_json": True,
    },
    "autoSubmitOrderRequest": {  # 快速自动提交订单
        "req_url": "/otn/confirmPassenger/autoSubmitOrderRequest",
        "req_type": "post",
        "Referer": "https://kyfw.12306.cn/otn/leftTicket/init",
        "Host": "kyfw.12306.cn",
        "Content-Type": 1,
        "re_try": 10,
        "re_time": 0.01,
        "s_time": 0.1,
        "is_logger": True,
        "is_json": True,
    },
    "getQueueCountAsync": {  # 快速获取订单数据
        "req_url": "/otn/confirmPassenger/getQueueCountAsync",
        "req_type": "post",
        "Referer": "https://kyfw.12306.cn/otn/leftTicket/init",
        "Host": "kyfw.12306.cn",
        "Content-Type": 1,
        "re_try": 10,
        "re_time": 0.01,
        "s_time": 0.1,
        "is_logger": True,
        "is_json": True,
    },
    "confirmSingleForQueueAsys": {  # 快速订单排队
        "req_url": "/otn/confirmPassenger/confirmSingleForQueueAsys",
        "req_type": "post",
        "Referer": "https://kyfw.12306.cn/otn/leftTicket/init",
        "Content-Type": 1,
        "Host": "kyfw.12306.cn",
        "re_try": 10,
        "re_time": 0.01,
        "s_time": 0.1,
        "is_logger": True,
        "is_json": True,
    },
    "cdn_host": {
        "req_url": "http://ping.chinaz.com/kyfw.12306.cn",
        "req_type": "post"
    },
    "cdn_list": {
        "req_url": "http://ping.chinaz.com/iframe.ashx?t=ping&callback=jQuery111304824429956769827_{}".format(
            int(round(time.time() * 1000))),
        "req_type": "post"
    }
}
