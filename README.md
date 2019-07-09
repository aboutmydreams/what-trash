# what-trash

为了更好的垃圾分类，编写了一个智能回答小助手，数据来源于上海市垃圾查询爬取 与 福州第一技师学院的生活垃圾分类知识汇总

![trash](https://cdn.nlark.com/yuque/0/2019/png/164272/1562229745215-b636afd3-b1ed-4826-9a11-fa972e22c40f.png)

## Data格式与添加方法
可在 [ansdata/good_data.json](https://github.com/aboutmydreams/what-trash/tree/master/ansdata/good_data.json) 中查看，部分数据截取，已有500+数据，有待整理与添加。开源项目 望提交 pull request 支持。
```json
  {
    "碎陶瓷": "干垃圾",
    "毛毯": "可回收物",
    "口香糖": "干垃圾",
  },
```
项目结构中，get_more_data.py 是我拓展更多数据时
使用的py文件，用于将更多的数据写入 json 当中，在
项目部署中无需求。其中的sort_list函数可传入未知
垃圾列表，自动抓取数据写入txt。run.py是 flask 的
部署py。trash.py 是主函数所在文件，包括爬取函数，
写入txt，返回有趣的答案，您可以在其中添加"你是什么
垃圾"等 的有趣回答，望贡献文案～。


## 后端部署

后端使用简单的 flask app run部署，默认 1028 端口，可在 run.py 中修改

```bash
git clone https://github.com/aboutmydreams/what-trash.git
cd what-trash
python run.py
```

### url: /trash

#### `method: GET`

#### `param`

```json
{
  "name": "陶瓷"
}
```

### `response`:

```json
{
  "status": 1,
  "content": "陶瓷属于干垃圾哦~"
}
```

#### api 说明

```bash
status = 1, 返回已知解答

status = 0, 返回猜测解答
```

#### 测试接口

http://118.25.236.82:1028/trash?name=%E9%99%B6%E7%93%B7



## 前端部署

前端部署地址：[http://what-trash.flura.cn](http://what-trash.flura.cn/)



前端部署效果图：

![1562209292444](http://img.flura.cn/what-trash.png)

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.<br>
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.<br>
You will also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.<br>
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.<br>
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.<br>
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (Webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.



### 开源许可

本项目使用 [AGPLv3](https://github.com/aboutmydreams/what-trash/blob/master/LICENSE) 许可证，这意味着你可以使用本项目向你的用户提供服务，但如果你需要对项目的源码进行修改，则必须将你修改后的版本对你的用户开源。
