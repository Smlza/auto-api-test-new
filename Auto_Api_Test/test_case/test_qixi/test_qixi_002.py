# -*- coding: utf-8 -*-
# @Time : 2020/8/7 16:08
# @Author : turing
# @File : test_qixi_002.py
import time
import unittest
import requests
from google.protobuf import json_format
import NewBao_Activity_pb2
class post_request(unittest.TestCase):
    def setUp(self):
        print('七夕活动-用户积分页面数据接口开始')
        pass

    def api_time(self,a,b):
        return str((a - b) * 1000)

    # 正常传参数
    def test_01(self):
        url='https://baogotest.turingsenseai.com/activity/doubleSeventhScorePage'
        headers={'Authorization': "tokenmaolin",'content-type': 'application/x-protobuf'}
        info=NewBao_Activity_pb2.TSDoubleSeventhScorePageRequest()
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
            rep=NewBao_Activity_pb2.TSDoubleSeventhScorePageResponse()
            rep.ParseFromString(r.content)
            dic=json_format.MessageToDict(rep)
            for k ,v in dic.items():
                print([k,v])

        elif r.status_code is 401 or 404:
            print(r.status_code)
        else:
            print("接口异常")

#传入的pageNum超过最大页数
    def test_02(self):
        url = 'https://baogotest.turingsenseai.com/activity/doubleSeventhScorePage'
        headers = {'Authorization': "tokenmaolin", 'content-type': 'application/x-protobuf'}
        info = NewBao_Activity_pb2.TSDoubleSeventhScorePageRequest()
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
            rep = NewBao_Activity_pb2.TSDoubleSeventhScorePageResponse()
            rep.ParseFromString(r.content)
            dic = json_format.MessageToDict(rep)
            for k, v in dic.items():
                print([k, v])

        elif r.status_code is 401 or 404:
            print(r.status_code)
        else:
            print("接口异常")

#传入的pageNum为负
    def test_03(self):
        url = 'https://baogotest.turingsenseai.com/activity/doubleSeventhScorePage'
        headers = {'Authorization': "tokenmaolin", 'content-type': 'application/x-protobuf'}
        info = NewBao_Activity_pb2.TSDoubleSeventhScorePageRequest()
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
            rep = NewBao_Activity_pb2.TSDoubleSeventhScorePageResponse()
            rep.ParseFromString(r.content)
            dic = json_format.MessageToDict(rep)
            for k, v in dic.items():
                print([k, v])

        elif r.status_code is 401 or 404:
            print(r.status_code)
        else:
            print("接口异常")

#传入的pageNum为空
    def test_04(self):
        url = 'https://baogotest.turingsenseai.com/activity/doubleSeventhScorePage'
        headers = {'Authorization': "tokenmaolin", 'content-type': 'application/x-protobuf'}
        info = NewBao_Activity_pb2.TSDoubleSeventhScorePageRequest()
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
            rep = NewBao_Activity_pb2.TSDoubleSeventhScorePageResponse()
            rep.ParseFromString(r.content)
            dic = json_format.MessageToDict(rep)
            for k, v in dic.items():
                print([k, v])

        elif r.status_code is 401 or 404:
            print(r.status_code)
        else:
            print("接口异常")

#传入的pageSize为负
    def test_05(self):
        url = 'https://baogotest.turingsenseai.com/activity/doubleSeventhScorePage'
        headers = {'Authorization': "tokenmaolin", 'content-type': 'application/x-protobuf'}
        info = NewBao_Activity_pb2.TSDoubleSeventhScorePageRequest()
        info.pageNum = 1
        info.pageSize = -1
        # info.lotteryStatus = '1'  # 抽奖状态  1已抽奖  2未抽奖
        # info.status = '3'  # 生效状态  1待生效、2生效中、3已失效、4停用
        data = info.SerializeToString()
        info_datatime_before = time.time()
        r = requests.post(url, headers, data)
        info_datatime_after = time.time()
        print('接口耗时：%s ms' % self.api_time(info_datatime_after, info_datatime_before))
        if r.status_code is 200:
            rep = NewBao_Activity_pb2.TSDoubleSeventhScorePageResponse()
            rep.ParseFromString(r.content)
            dic = json_format.MessageToDict(rep)
            for k, v in dic.items():
                print([k, v])

        elif r.status_code is 401 or 404:
            print(r.status_code)
        else:
            print("接口异常")

#传入的pageSize为空
    def test_06(self):
        url = 'https://baogotest.turingsenseai.com/activity/doubleSeventhScorePage'
        headers = {'Authorization': "tokenmaolin", 'content-type': 'application/x-protobuf'}
        info = NewBao_Activity_pb2.TSDoubleSeventhScorePageRequest()
        info.pageNum = 1
        # info.pageSize = -1
        # info.lotteryStatus = '1'  # 抽奖状态  1已抽奖  2未抽奖
        # info.status = '3'  # 生效状态  1待生效、2生效中、3已失效、4停用
        data = info.SerializeToString()
        info_datatime_before = time.time()
        r = requests.post(url, headers, data)
        info_datatime_after = time.time()
        print('接口耗时：%s ms' % self.api_time(info_datatime_after, info_datatime_before))
        if r.status_code is 200:
            rep = NewBao_Activity_pb2.TSDoubleSeventhScorePageResponse()
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
        print('七夕活动-用户积分页面数据接口结束')
        pass