# 天翼云自动签到
天翼云盘每日签到一次，抽奖2次  
使用方法  
1.测试环境为python3.7.6,自行安装python3  
2.requirements.txt 是所需第三方模块，执行 `pip install -r requirements.txt` 安装模块  
3.可在脚本内直接填写账号密码  
4.Python 和需要模块都装好了直接在目录 cmd 运行所要运行的脚本。  


# Github Actions说明
## 一、Fork此仓库
![](http://tu.yaohuo.me/imgs/2020/06/f059fe73afb4ef5f.png)
## 二、设置账号密码
添加名为**USER**、**PWD**的变量  
值分别为**账号**、**密码**  
支持多账号，账号之间与密码之间用**半角逗号**分隔，账号于密码的个数要对应  
示例：**USER:123456,24678**，**PWD:cxkjntm,jntmcxk**
![](http://tu.yaohuo.me/imgs/2020/06/748bf9c0ca6143cd.png)

## 三、启用Action
1 点击**Action**，再点击**I understand my workflows, go ahead and enable them**  
2 修改任意文件后提交一次  
![](http://tu.yaohuo.me/imgs/2020/06/34ca160c972b9927.png)

## 四、查看运行结果
Actions > Cloud189Checkin > build  
能看到如下所示:
```shell
Run user='***'
共有 1 个账号，即将开始签到
登录成功
已经签到过了，签到获得73M空间
```

此后，将会在每天10:00和22:00各签到一次  
若有需求，可以在[.github/workflows/check-in.yml]中自行修改
