# Time Recorder
一个记录日常时间开销的小工具，在程序内通过命令行控制。  
输入 task 和 notes（可选）自动录入一条数据，`date` 和 `start` 为当下日期时间，`end` 为待定（None）。输入下一条数据时自动将当下时间作为上一条数据的 `end` 。  
e.g. `运动 羽毛球` , `学习 看论文` 等
## 命令列表
`<task>( <notes>)` 输入 task 和 notes（可选）  
`end` 将当下时间作为最新一条数据的结束时间，即结束该 `task`  
`end -f` 用当下时间强行覆盖最后一条数据的 `end`，用于最新一条数据已有结束时间、无法使用 `end` 命令时。  
`dd` 删除上一条记录  
`rd <num>` 进入编辑模式
- `rd 1` 编辑上一条数据的 `date`
- `rd 2` 编辑上一条数据的 `start`
- `rd 3` 编辑上一条数据的 `end`
- `rd 4` 编辑上一条数据的 `task` 和 `notes`

`sum <task>( <notes>)` 统计总时长
- `sum <task>` 统计 `task` 所花费的总时间
- `sum <task> <notes>` 统计 `task notes` 所花费的总时间  

`-1` 用本地默认软件打开数据文件（如 Excel）  