# 接口自动化测试框架（个人练习）

Python + pytest + requests 接口自动化框架，分层设计。

## 目录结构
- config/      多环境配置（yaml：base_url / timeout / 账号）
- common/      请求封装（Session + 统一超时 + 日志）、日志、配置读取
- api/         接口封装层（一个接口一个方法，不写断言）
- data/        测试数据（yaml）
- testcases/   测试用例（正向 + 反向 + 鉴权）
- conftest.py  全局 fixture：session 级登录态复用

## 运行方式
pip install -r requirements.txt
python -m pytest testcases -v --html=reports/report.html --self-contained-html

## 设计要点
- 分层解耦：改环境只改 config，改接口只改 api，加用例只改 testcases/yaml
- 登录态复用：session 作用域 fixture，全流程只登录一次
- 数据驱动：pytest.mark.parametrize + ids，报告可读
- 日志留痕：logging 双输出（文件 + 控制台）
