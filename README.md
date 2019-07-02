# what-trash

为了更好的垃圾分类

## 后端运行

默认 1028 端口，可在 run.py 中修改

```bash
git clone https://github.com/aboutmydreams/what-trash.git
cd what-trash
python run.py
```

### url: /trash

#### method: GET

#### param

```json
{
  "name": "陶瓷"
}
```

### response:

```json
{
  "status": 1,
  "content": "陶瓷属于干垃圾哦~"
}
```

#### api 说明

status = 1, 返回已知解答
status = 0, 返回猜测解答

#### 测试接口

http://118.25.236.82:1028/trash?name=%E9%99%B6%E7%93%B7
