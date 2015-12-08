# xueer_be

    the backend of xueer::学而后台
  
## 0. build
### virtual environment

    $ virtual venv
    $ source venv/bin/activate
    
### install extensions

    $ pip install -r requirement.txt (--no-cache-dir)
    
### test database
#### create Role

    $ chmod 777 data.sh
    $ ./data.sh
    >> Role.insert_roles()

#### fake data

    >> User.generate_fake()
    >> Courses.generate_fake()
    >> quit()

    $ password:
    $ confirm:

### run

    python manage.py run (--help)


## 1. 参与人员

  朱承浩、王怡凡、黄刘胤

## 2. 提交流程

	fork这个仓库, 每一个新功能checkout一个新分支，向这个仓库的主分支提交
	朱承浩(@neo1218)负责合并和维护这个仓库

	ps: 请每次工作前务必git pull一下

## 3. 进度

	151102: 任务安排1+提交流程
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	151106: 任务安排2
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	151109: 任务安排3 + 提交数据库修正
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	151125: 任务安排4
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	151126: 本地可以运行(无语法错误)
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	151126: 完成清理工作(删除不必要的模版, 导航栏及其他)
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	151127: 完成mysql远程数据库部署
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	151129: fix ISSUE #2, 依据文档部分完成API编写
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    151201: 添加虚拟数据、修复API部分bug
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	151201: 基础API review完毕， 有部分问题见 milestone(Basic API)
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	151204: 首页、登录页、点赞、取消点赞API的编写
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	151204: 完成基础资源(老师、课程、用户、评论、标签)的CRUD编写,
	        完成部分相互调用API的编写
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	151208: 基础API除了首页tips外全部搞定

## 4. ToDo
~~0. clean~~ <br/>
~~1. token可以请求~~ <br/>
~~3. mysql 数据库测试成功~~ <br/>
~~4. 数据库分页编写~~ <br/>
~~5. 测试基础数据库API~~ <br/>
~~6. 首页、登录页、点赞、取消点赞API~~ <br/>

    1. API 测试
        done!
    2. API 编写
~~7. 首页、课程信息页、登录页、注册页 API 编写~~
~~8. 点赞API,~~

    首页tips API
    权限管理
    错误与异常处理
    
    搜索
    优化(服务器性能优化配置、浏览器首页静态化。。。)
    
