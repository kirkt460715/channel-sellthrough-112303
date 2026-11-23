# 经销商动销与跨区串货的补货返利

原箱每箱 12 袋，拆箱和销售按袋计。movements 的日期是离开发货点或拟加工点的日期，received 为明确签收日期；同一运单只去一个候选目的地。已发未签的属于在途，未发运的不减现货。同一批次的终端证据中，零售扫描可认定售出，出库未注明终端不作确定动销；找不到应有的营业日上报记录计为缺报。已关联红冲扣相应原交易及当时认定的实际市场。单店确认的月底盘点可纳入实际日的平衡，待复盘的数只作提示。L04 在 6 月 30 日已有一轮签收和营业，inventory 中当日期末盘点是后续核算起点。 数据为合成资料。交换说明见 [数据约定](data-contract.md)。

使用 Python 3.11。当前可读取和抽查原始业务资料。
如使用业务分析依赖，可从项目根目录运行 `python3 -m pip install -r requirements.txt`。

```sh
python3 inspect_data.py
python3 inspect_data.py movements --limit 2
python3 -m unittest discover -s tests -v
```

测试检查交换资料的关联和原始凭据的可读性。命令可离线使用。
