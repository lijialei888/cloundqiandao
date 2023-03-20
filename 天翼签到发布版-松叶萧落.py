# -*- coding: utf8 -*-
# 本代码与教程仅供学习交流，请勿用于其他任何用途。
# 本人也从来没有也不会接收任何打赏或广告等盈利性活动。
# 如有违规或对他人权益造成损害， 请联系我立即删除。


import requests
import json
import time
from DecryptLogin import login



for i in range(1,5):
    if i==1:
        c = 'apm_ct=20200815154033048; apm_uid=F2C222EECC916CE53B5A4952970589C2; apm_ip=0A0D407F79465768C87C54F9ACF48F86; apm_ua=AE7A02CAD8F8489E2A3B5D3F321CEF4B; shareId_169771614=yu35; shareId_169940353=smk3; shareId_170056700=f7cz; shareId_170180137=r8cw; shareId_170332976=avp4; shareId_170217744=bau0; shareId_170398254=qmu6; shareId_170077327=5vnm; shareId_170559700=ikv6; shareId_169800657=d2gc; shareId_170368076=d5ta; shareId_170558962=zpu6; shareId_170838082=5lmf; shareId_170499908=fqg2; shareId_170974777=s6ee; shareId_171026619=7nzd; shareId_169403420=rgc2; shareId_171436891=7i7v; shareId_169864497=pam4; shareId_171513661=x5ws; shareId_171584834=3eh6; shareId_171594561=3rub; shareId_114321131372=xky4; share_BnuEZzzIVbme=8zg6; apm_sid=32C35CBD589AA707A25C650EF428FA8B; JSESSIONID=A4EEFCB2D34505621CEEDA9705F6C8CF; COOKIE_LOGIN_USER=3476244C18779DCCEDB7F9ADFCDABF6E5709015EB1325B1E20F4AD96506D81111F742790059FD07795A8CEE1B11B317713760FBF1F98DB3B'
        na='王'
        username='15259328233'
        password='Luis19841015'
    elif i==2:
        c = 'apm_ct=20200815154033048; apm_uid=F2C222EECC916CE53B5A4952970589C2; apm_ip=0A0D407F79465768C87C54F9ACF48F86; apm_ua=AE7A02CAD8F8489E2A3B5D3F321CEF4B; shareId_169771614=yu35; shareId_169940353=smk3; shareId_170056700=f7cz; shareId_170180137=r8cw; shareId_170332976=avp4; shareId_170217744=bau0; shareId_170398254=qmu6; shareId_170077327=5vnm; shareId_170559700=ikv6; shareId_169800657=d2gc; shareId_170368076=d5ta; shareId_170558962=zpu6; shareId_170838082=5lmf; shareId_170499908=fqg2; shareId_170974777=s6ee; shareId_171026619=7nzd; shareId_169403420=rgc2; shareId_171436891=7i7v; shareId_169864497=pam4; shareId_171513661=x5ws; shareId_171584834=3eh6; shareId_171594561=3rub; shareId_114321131372=xky4; share_BnuEZzzIVbme=8zg6; apm_sid=563B781064062D808B9EB9670D932733; JSESSIONID=54F6DDC6E213E3D1BBF4C2E1072F5A89; COOKIE_LOGIN_USER=73A43765203A830F9E95822F00AE55AC55FFDB498AC485AB111B342BEA7F5D81A0F0BD77D1CFDA4E10CE198AEB56AF34DB7A3D992AB061EA'
        na='秋'
        username='15059278837'
        password='Luis19841015'
    elif i==3:
        c = 'apm_ct=20200815154033048; apm_uid=F2C222EECC916CE53B5A4952970589C2; apm_ip=0A0D407F79465768C87C54F9ACF48F86; apm_ua=AE7A02CAD8F8489E2A3B5D3F321CEF4B; shareId_169771614=yu35; shareId_169940353=smk3; shareId_170056700=f7cz; shareId_170180137=r8cw; shareId_170332976=avp4; shareId_170217744=bau0; shareId_170398254=qmu6; shareId_170077327=5vnm; shareId_170559700=ikv6; shareId_169800657=d2gc; shareId_170368076=d5ta; shareId_170558962=zpu6; shareId_170838082=5lmf; shareId_170499908=fqg2; shareId_170974777=s6ee; shareId_171026619=7nzd; shareId_169403420=rgc2; shareId_171436891=7i7v; shareId_169864497=pam4; shareId_171513661=x5ws; shareId_171584834=3eh6; shareId_171594561=3rub; shareId_114321131372=xky4; share_BnuEZzzIVbme=8zg6; apm_sid=563B781064062D808B9EB9670D932733; JSESSIONID=3C52756B3339358F846B45599BD38AAD; COOKIE_LOGIN_USER=8313333FF516B31564DC692A0979C659959DE93FC4FF7E850E5288BDE84080325DDA9BBF5B12B85665D2B8B0AFCAC364E1C476480FCCE34E'
        na='娘'
        username='15159382914'
        password='Luis19841015'
    elif i==4:
        c='apm_ct=20200815154033048; apm_uid=F2C222EECC916CE53B5A4952970589C2; apm_ip=0A0D407F79465768C87C54F9ACF48F86; apm_ua=AE7A02CAD8F8489E2A3B5D3F321CEF4B; shareId_169771614=yu35; shareId_169940353=smk3; shareId_170056700=f7cz; shareId_170180137=r8cw; shareId_170332976=avp4; shareId_170217744=bau0; shareId_170398254=qmu6; shareId_170077327=5vnm; shareId_170559700=ikv6; shareId_169800657=d2gc; shareId_170368076=d5ta; shareId_170558962=zpu6; shareId_170838082=5lmf; shareId_170499908=fqg2; shareId_170974777=s6ee; shareId_171026619=7nzd; shareId_169403420=rgc2; shareId_171436891=7i7v; shareId_169864497=pam4; shareId_171513661=x5ws; shareId_171584834=3eh6; shareId_171594561=3rub; shareId_114321131372=xky4; share_BnuEZzzIVbme=8zg6; apm_sid=563B781064062D808B9EB9670D932733; JSESSIONID=3C52756B3339358F846B45599BD38AAD; COOKIE_LOGIN_USER=6D87EA97EEE3A0E69AC51025F39984AB043EC5244929032C71C77CEEF8E517B1E2BEC99AECD2808F40BE3ECF7DFD2F1C253B370D80D9DEB1'
        na='爹'
        username='13950561412'
        password='Luis19841015'
    print('*************************************************\n')

    print(na+',第一次拆红包领空间\n')

#以下是模拟天翼网盘登陆程序
    lg = login.Login()
    self.infos_return, self.session = lg.cloud189(username, password, 'mobile')

    # 构造url
    params = {
        'rand': str(time.time() * 1000),
        'clientType': 'TELEANDROID',
        'version': '8.9.0',
        'model': 'Mi MIX3',
    }
    url1 = f'https://api.cloud.189.cn/mkt/userSign.action?{parse.urlencode(params)}'

    # 日期转换
    date = self.cst2gmt(int(float(params['rand'])))
    # 必要的信息
    infos = json.dumps(xmltodict.parse(self.infos_return['merge_info']))
    infos = json.loads(infos)
    # 签名
    sign = f'SessionKey={infos["userSession"]["sessionKey"]}&Operate=GET&RequestURI=/mkt/userSign.action&Date={date}'
    # 请求头
    headers = {
        'sessionkey': infos['userSession']['sessionKey'],
        'date': date,
        'signature': self.getsignhex(sign, infos['userSession']['sessionSecret']),
        'user-agent': 'Ecloud/8.9.0 (Mi MIX3; ; uc) Android/10',
        'host': parse.urlparse(url).hostname
    }
    # 开始请求
    response = self.session.get(url1, headers=headers)
    response_json = json.dumps(xmltodict.parse(response.text))

    # 判断签到是否成功
    if response_json.get('userSignResult', {}).get('result') == 1:
        print(f"[INFO]: 签到成功, {response_json['userSignResult']['resultTip']}")
    else:
        print(
            f"[INFO]: 签到失败, 错误码为{response_json['userSignResult']['result']}, {response_json['userSignResult']['resultTip']}")

#以下是抽奖
    url = 'https://m.cloud.189.cn/v2/drawPrizeMarketDetails.action?taskId=TASK_SIGNIN&activityId=ACT_SIGNIN&noCache=0.5703163731957983'
    headers = {
        'cookie': c
    }

    s = requests.get(url, headers=headers)

    xy = s.text
    if "User_Not_Chance" in xy:
        print(na+'，今天已经领取过第一次拆红包了哦。')
    elif "空间" in xy:
        print(na+'，第一次领取拆红包空间成功')
    else:
        print('遇到未知错误，请检查返回信息或联系代码维护者处理，联系地址：https://b23.tv/tlQFYe')
    print('*************************************************\n')
    print(na+',第二次拆红包领空间\n')
    url = 'https://m.cloud.189.cn/v2/drawPrizeMarketDetails.action?taskId=TASK_SIGNIN_PHOTOS&activityId=ACT_SIGNIN&noCache=0.6995822705887422'

    headers = {'cookie': c}
    s = requests.get(url, headers=headers)

    xy = s.text
    if "User_Not_Chance" in xy:
        print(na+'，今天已经领取过第二次拆红包了哦。')
    elif "空间" in xy:
        print(na+'，第二次领取拆红包空间成功')
    else:
        print('遇到未知错误，请检查返回信息或联系代码维护者处理，https://b23.tv/tlQFYe')


    def main_handler(event, context):
        print("Received event: " + json.dumps(event, indent=2))
        print("Received context: " + str(context))
        print("Hello world")
        return "主人，执行完毕了，详情请查看日志信息哦。"
    time.sleep(3)