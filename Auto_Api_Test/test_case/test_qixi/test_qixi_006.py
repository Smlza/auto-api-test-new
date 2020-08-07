# -*- coding: utf-8 -*-
# @Time : 2020/8/7 16:58
# @Author : turing
# @File : test_qixi_006.py
import time
import unittest
import requests
from google.protobuf import json_format
import NewBaoAdmin_Activity_pb2
class post_request(unittest.TestCase):
    def setUp(self):
        print('运营管理台七夕活动积分记录查询接口开始')
        pass

    def api_time(self,a,b):
        return str((a - b) * 1000)

    # 正常传参
    def test_01(self):
        url='https://baogotest.turingsenseai.com/admin/doubleSeventhScore'
        headers={'content-type': 'application/x-protobuf'}
        info=NewBaoAdmin_Activity_pb2.TSAdminDoubleSeventhScoreRequest()
        info.phoneNum = '15850782959' #数据库查询
        info.pageNum = 1
        info.pageSize = 10
        # info.lotteryStatus = '1'  # 抽奖状态  1已抽奖  2未抽奖
        # info.status = '3'  # 生效状态  1待生效、2生效中、3已失效、4停用
        data = info.SerializeToString()
        info_datatime_before = time.time()
        r=requests.post(url,headers,data)
        info_datatime_after=time.time()
        print('接口耗时：%s ms' % self.api_time(info_datatime_after, info_datatime_before))
        if r.status_code is 200:
            rep=NewBaoAdmin_Activity_pb2.TSAdminDoubleSeventhScoreResponse()
            rep.ParseFromString(r.content)
            dic=json_format.MessageToDict(rep)
            for k ,v in dic.items():
                print([k,v])

        elif r.status_code is 401 or 404:
            print(r.status_code)
        else:
            print("接口异常")

    #传入的phoneNum不存在
    def test_02(self):
        url='https://baogotest.turingsenseai.com/admin/doubleSeventhScore'
        headers={'content-type': 'application/x-protobuf'}
        info=NewBaoAdmin_Activity_pb2.TSAdminDoubleSeventhScoreRequest()
        info.phoneNum = '11111111111' #数据库查询
        info.pageNum = 1
        info.pageSize = 10
        # info.lotteryStatus = '1'  # 抽奖状态  1已抽奖  2未抽奖
        # info.status = '3'  # 生效状态  1待生效、2生效中、3已失效、4停用
        data = info.SerializeToString()
        info_datatime_before = time.time()
        r=requests.post(url,headers,data)
        info_datatime_after=time.time()
        print('接口耗时：%s ms' % self.api_time(info_datatime_after, info_datatime_before))
        if r.status_code is 200:
            rep=NewBaoAdmin_Activity_pb2.TSAdminDoubleSeventhScoreResponse()
            rep.ParseFromString(r.content)
            dic=json_format.MessageToDict(rep)
            for k ,v in dic.items():
                print([k,v])

        elif r.status_code is 401 or 404:
            print(r.status_code)
        else:
            print("接口异常")

    #传入的phoneNum为空
    def test_03(self):
        url='https://baogotest.turingsenseai.com/admin/doubleSeventhScore'
        headers={'content-type': 'application/x-protobuf'}
        info=NewBaoAdmin_Activity_pb2.TSAdminDoubleSeventhScoreRequest()
        info.phoneNum = '' #数据库查询
        info.pageNum = 1
        info.pageSize = 10
        # info.lotteryStatus = '1'  # 抽奖状态  1已抽奖  2未抽奖
        # info.status = '3'  # 生效状态  1待生效、2生效中、3已失效、4停用
        data = info.SerializeToString()
        info_datatime_before = time.time()
        r=requests.post(url,headers,data)
        info_datatime_after=time.time()
        print('接口耗时：%s ms' % self.api_time(info_datatime_after, info_datatime_before))
        if r.status_code is 200:
            rep=NewBaoAdmin_Activity_pb2.TSAdminDoubleSeventhScoreResponse()
            rep.ParseFromString(r.content)
            dic=json_format.MessageToDict(rep)
            for k ,v in dic.items():
                print([k,v])

        elif r.status_code is 401 or 404:
            print(r.status_code)
        else:
            print("接口异常")

    #传入的pageNum超过最大页数
    def test_04(self):
        url = 'https://baogotest.turingsenseai.com/admin/doubleSeventhScore'
        headers = {'content-type': 'application/x-protobuf'}
        info = NewBaoAdmin_Activity_pb2.TSAdminDoubleSeventhScoreRequest()
        info.phoneNum = '15850782959'  # 数据库查询
        info.pageNum = 1000000
        info.pageSize = 10
        # info.lotteryStatus = '1'  # 抽奖状态  1已抽奖  2未抽奖
        # info.status = '3'  # 生效状态  1待生效、2生效中、3已失效、4停用
        data = info.SerializeToString()
        info_datatime_before = time.time()
        r = requests.post(url, headers, data)
        info_datatime_after = time.time()
        print('接口耗时：%s ms' % self.api_time(info_datatime_after, info_datatime_before))
        if r.status_code is 200:
            rep = NewBaoAdmin_Activity_pb2.TSAdminDoubleSeventhScoreResponse()
            rep.ParseFromString(r.content)
            dic = json_format.MessageToDict(rep)
            for k, v in dic.items():
                print([k, v])

        elif r.status_code is 401 or 404:
            print(r.status_code)
        else:
            print("接口异常")

    #传入的pageNum为负
    def test_05(self):
        url = 'https://baogotest.turingsenseai.com/admin/doubleSeventhScore'
        headers = {'content-type': 'application/x-protobuf'}
        info = NewBaoAdmin_Activity_pb2.TSAdminDoubleSeventhScoreRequest()
        info.phoneNum = '15850782959'  # 数据库查询
        info.pageNum = -1
        info.pageSize = 10
        # info.lotteryStatus = '1'  # 抽奖状态  1已抽奖  2未抽奖
        # info.status = '3'  # 生效状态  1待生效、2生效中、3已失效、4停用
        data = info.SerializeToString()
        info_datatime_before = time.time()
        r = requests.post(url, headers, data)
        info_datatime_after = time.time()
        print('接口耗时：%s ms' % self.api_time(info_datatime_after, info_datatime_before))
        if r.status_code is 200:
            rep = NewBaoAdmin_Activity_pb2.TSAdminDoubleSeventhScoreResponse()
            rep.ParseFromString(r.content)
            dic = json_format.MessageToDict(rep)
            for k, v in dic.items():
                print([k, v])

        elif r.status_code is 401 or 404:
            print(r.status_code)
        else:
            print("接口异常")

    #传入的pageNum为空
    def test_06(self):
        url = 'https://baogotest.turingsenseai.com/admin/doubleSeventhScore'
        headers = {'content-type': 'application/x-protobuf'}
        info = NewBaoAdmin_Activity_pb2.TSAdminDoubleSeventhScoreRequest()
        info.phoneNum = '15850782959'  # 数据库查询
        # info.pageNum = -1
        info.pageSize = 10
        # info.lotteryStatus = '1'  # 抽奖状态  1已抽奖  2未抽奖
        # info.status = '3'  # 生效状态  1待生效、2生效中、3已失效、4停用
        data = info.SerializeToString()
        info_datatime_before = time.time()
        r = requests.post(url, headers, data)
        info_datatime_after = time.time()
        print('接口耗时：%s ms' % self.api_time(info_datatime_after, info_datatime_before))
        if r.status_code is 200:
            rep = NewBaoAdmin_Activity_pb2.TSAdminDoubleSeventhScoreResponse()
            rep.ParseFromString(r.content)
            dic = json_format.MessageToDict(rep)
            for k, v in dic.items():
                print([k, v])

        elif r.status_code is 401 or 404:
            print(r.status_code)
        else:
            print("接口异常")

    #传入的pageSize为负
    def test_07(self):
        url = 'https://baogotest.turingsenseai.com/admin/doubleSeventhScore'
        headers = {'content-type': 'application/x-protobuf'}
        info = NewBaoAdmin_Activity_pb2.TSAdminDoubleSeventhScoreRequest()
        info.phoneNum = '15850782959'  # 数据库查询
        info.pageNum = 1
        info.pageSize = -10
        # info.lotteryStatus = '1'  # 抽奖状态  1已抽奖  2未抽奖
        # info.status = '3'  # 生效状态  1待生效、2生效中、3已失效、4停用
        data = info.SerializeToString()
        info_datatime_before = time.time()
        r = requests.post(url, headers, data)
        info_datatime_after = time.time()
        print('接口耗时：%s ms' % self.api_time(info_datatime_after, info_datatime_before))
        if r.status_code is 200:
            rep = NewBaoAdmin_Activity_pb2.TSAdminDoubleSeventhScoreResponse()
            rep.ParseFromString(r.content)
            dic = json_format.MessageToDict(rep)
            for k, v in dic.items():
                print([k, v])

        elif r.status_code is 401 or 404:
            print(r.status_code)
        else:
            print("接口异常")

    #传入的pageSize为空
    def test_08(self):
        url = 'https://baogotest.turingsenseai.com/admin/doubleSeventhScore'
        headers = {'content-type': 'application/x-protobuf'}
        info = NewBaoAdmin_Activity_pb2.TSAdminDoubleSeventhScoreRequest()
        info.phoneNum = '15850782959'  # 数据库查询
        info.pageNum = 1
        # info.pageSize = 10
        # info.lotteryStatus = '1'  # 抽奖状态  1已抽奖  2未抽奖
        # info.status = '3'  # 生效状态  1待生效、2生效中、3已失效、4停用
        data = info.SerializeToString()
        info_datatime_before = time.time()
        r = requests.post(url, headers, data)
        info_datatime_after = time.time()
        print('接口耗时：%s ms' % self.api_time(info_datatime_after, info_datatime_before))
        if r.status_code is 200:
            rep = NewBaoAdmin_Activity_pb2.TSAdminDoubleSeventhScoreResponse()
            rep.ParseFromString(r.content)
            dic = json_format.MessageToDict(rep)
            for k, v in dic.items():
                print([k, v])

        elif r.status_code is 401 or 404:
            print(r.status_code)
        else:
            print("接口异常")

    def tearDown(self):
        print('==============================================')
        print('运营管理台七夕活动积分记录查询接口结束')
        pass