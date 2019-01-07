from py12306.log.base import BaseLog
from py12306.config import *
from py12306.helpers.func import *


@singleton
class CommonLog(BaseLog):
    # 这里如果不声明，会出现重复打印，目前不知道什么原因
    logs = []
    thread_logs = {}
    quick_log = []

    MESSAGE_12306_IS_CLOSED = '当前时间: {}     |       12306 休息时间，程序将在明天早上 6 点自动运行'
    MESSAGE_RETRY_AUTH_CODE = '{} 秒后重新获取验证码'

    MESSAGE_EMPTY_APP_CODE = '无法发送语音消息，未填写验证码接口 appcode'
    MESSAGE_VOICE_API_FORBID = '语音消息发送失败，请检查 appcode 是否填写正确或 套餐余额是否充足'
    MESSAGE_VOICE_API_SEND_FAIL = '语音消息发送失败，错误原因 {}'
    MESSAGE_VOICE_API_SEND_SUCCESS = '语音消息发送成功! 接口返回信息 {} '

    MESSAGE_CHECK_AUTO_CODE_FAIL = '请配置打码账号的账号密码'
    MESSAGE_CHECK_EMPTY_USER_ACCOUNT = '请配置 12306 账号密码'

    MESSAGE_TEST_SEND_VOICE_CODE = '正在测试发送语音验证码...'

    def __init__(self):
        super().__init__()
        self.init_data()

    def init_data(self):
        pass

    @classmethod
    def print_welcome(cls):
        self = cls()
        self.add_quick_log('######## py12306 购票助手，本程序为开源工具，请勿用于商业用途 ########')
        if Const.IS_TEST:
            self.add_quick_log()
            self.add_quick_log('当前为测试模式，程序运行完成后自动结束')
        self.add_quick_log()
        self.flush()
        return self

    @classmethod
    def print_configs(cls):
        # 打印配置
        self = cls()
        enable = '已开启'
        disable = '未开启'
        self.add_quick_log('**** 当前配置 ****')
        self.add_quick_log('多线程查询: {}'.format(get_true_false_text(config.QUERY_JOB_THREAD_ENABLED, enable, disable)))
        self.add_quick_log('语音验证码: {}'.format(get_true_false_text(config.QUERY_JOB_THREAD_ENABLED, enable, disable)))
        self.add_quick_log('查询间隔: {} 秒'.format(config.QUERY_INTERVAL))
        self.add_quick_log('用户心跳检测间隔: {} 秒'.format(config.USER_HEARTBEAT_INTERVAL))
        self.add_quick_log()
        self.flush()
        return self

    @classmethod
    def test_complete(cls):
        self = cls()
        self.add_quick_log('# 测试完成，请检查输出是否正确 #')
        self.flush()
        return self

    @classmethod
    def print_auto_code_fail(cls, reason):
        self = cls()
        self.add_quick_log('打码失败: 错误原因 {reason}'.format(reason=reason))
        self.flush()
        return self
