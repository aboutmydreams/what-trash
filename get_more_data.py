import re, json

from trash import *

# https://www.yuque.com/zhiwa/ideas/gty6wa
# https://zh.speaklanguages.com/英语/词汇/厨房


def to_word_list(words: str) -> list:
    s = words.replace("	"," ").replace('\n', ' ').replace('/', ' ').split(' ')
    res = re.findall("\d+|[a-zA-Z]+", fruit)  # ['not', '404', 'found', '99']
    things_list = [item for item in s if not item in res]
    return list(things_list)


fruit = """Almond 杏仁
Apple 苹果
Apricot 杏子
Arbutus 杨梅
Avocado 南美梨
Bagasse 甘蔗渣
Banana 香蕉
Bennet 水杨梅
Bergamot 佛手柑
Berry 桨果
Betelnut 槟榔
Bilberry 野桑果
Bitter orange 苦酸橙
Blackberry 刺梅
Black brin 黑布林
 黑布林 
Blueberry 越桔，蓝莓
Bryony 野葡萄
Bullace 野李子
Bush fruit 丛生果
Cantaloupe 美国甜瓜
Carambola 杨桃
Casaba 冬季甜瓜
Cascara 鼠李
Cherry 樱桃
Cherry tomato 圣女果
Chestnut 栗子
Coconut 椰子
Cocoa 可可果
Codlin 未熟苹果
Core 果心
Cranberry 曼越桔
Cucumber 黄瓜
Cumquat 金桔
Custard apple 番荔枝
Damson 洋李子
Date 枣子
Date palm 枣椰子
Dew 果露
Durian 榴莲
Fig 无花果
Filbert 榛子
榛子filbert的图片
Flat peach 蕃桃
Foxnut 鸡头果
Ginkgo 银杏
Gooseberry 醋栗
Grape 葡萄
Grapefruit 葡萄柚子
Guava 番石榴
Haw 山楂
Herbaceous fruit 草本果
Hickory 山胡桃
Honey-dew melon 哈蜜瓜
Juicy peach 水蜜桃
Kernel fruit 仁果
Kiwifruit 奇异果 猕猴桃
Lemon 柠檬
Lichee 荔枝
Longan 龙眼 桂圆
Loquat 枇杷
Lotus 莲子
Mandarin 中国柑桔
Mango 芒果
Mangosteen 山竹果
Marc 果渣
Melon 黄香瓜
Mini watermelon 小西瓜
Nectarine 油桃
Newton pippin 香蕉苹果
Nucleus 核仁
Olive 橄榄
Orange 橙子
Papaya 木瓜
Peach 桃子
Peanut 花生
Pear 梨
Persimmon 柿子
Phoenix eye nut 凤眼果
Pistachio 开心果
Pitaya 火龙果
Plum 梅子，李子
Pomegranate 石榴
Pomelo 柚子
Quarenden 大红苹果
Rambutan 红毛丹
Raspberry 覆盆子
Sapodilla 人参果
人参果 
Sapodilla plum 芝果
Seedless watermelon 无籽西瓜
Segment 片囊
Shaddock 文旦
Sorgo 芦栗
Sorosis 桑果
Strawberry 草莓
Sugarcane 甘蔗
Sultana 苏丹葡萄
Sweet acorn 甜栎子
Syrup shaddock 汁柚
Tangerine 蜜柑桔
Tangor 广柑
Teazle fruit 刺果
Tough pear 木梨
Vermillion orange 朱砂桔
Walnut 核桃
 山核桃 凤梨 菠萝
Warden 冬梨
Water Caltrop 菱角
Waterchestnut 马蹄 荸荠
Watermelon 西瓜
White shaddock 白柚
Wild peach 毛桃"""

# 水果类
# s = fruit.replace('\n',' ').split(' ')
# res = re.findall("\d+|[a-zA-Z]+", fruit)          # ['not', '404', 'found', '99']
# fruit_list = [item for item in s if not item in res]
# sort_list(fruit_list)

daily_use = """
battery	电池
candle	蜡烛
cotton	棉
envelopes	信封
firelighters	生火料
fuse	保险丝
glue	胶水
light bulb	灯泡
lighter	打火机
matches	火柴
needle	针
safety pin	安全别针
scissors	剪刀
sellotape	胶带
stamps	邮票
pen	钢笔
pencil	铅笔
tissues	纸巾
toilet paper  toilet roll	厕纸
toothpaste	牙膏
tube of toothpaste	一管牙膏
writing paper	写字纸
清洗用具
bin bag  bin liner	垃圾袋
bleach	漂白水
detergent	洗涤剂
disinfectant	消毒水
dustbin bag	垃圾袋
duster	抹尘布
fabric softener	柔顺剂
floorcloth	擦地布
furniture polish	家俱油
hoover bag	吸尘袋
shoe polish	鞋油
soap	肥皂
washing powder	洗衣粉
"""
# 生活用品类
# s = daily_use.replace('\n',' ').split(' ')
# res = re.findall("\d+|[a-zA-Z]+", fruit)          # ['not', '404', 'found', '99']
# fruit_list = [item for item in s if not item in res]
# sort_list(fruit_list)


kitchen_ele = """fridge (refrigerator的缩写)	冰箱
coffee pot	咖啡壶
cooker	厨具
dishwasher	洗碗机
freezer	冰柜
kettle	水壶
oven	烤炉
stove	炉子
toaster	吐司机
washing	machine	洗衣机
厨房器具
bottle opener	啤酒开瓶器（金属盖）
chopping board	案板
colander	漏勺
corkscrew	红酒开瓶器（软木塞盖）
frying pan	煎锅
grater  cheese grater	刨丝器，奶酪刨丝器
juicer	榨汁器
kitchen foil	锡纸
kitchen scales	厨房秤
ladle	长柄勺
mixing bowl	搅拌碗
oven cloth	烤炉巾
oven gloves	烤炉用手套
rolling pin	擀面杖
saucepan	煮锅
scouring pad / scourer	百洁布
sieve	筛子
tin opener	开罐器
tongs	夹子
tray	盘子
whisk	打蛋器
wooden spoon	木勺
餐具
knife	刀子
fork	叉子
spoon	匙子
dessert spoon	点心匙
soup spoon	汤匙
tablespoon	大汤匙
teaspoon	茶匙
carving knife	切肉用的餐刀
chopsticks	筷子
陶器和玻璃制品
cup		杯子
bowl	碗
crockery	陶器
glass	玻璃杯
jar	罐子
jug	瓶
mug	茶杯
plate	碟子
saucer	茶碟
sugar bowl	糖碗
teapot	茶壶
wine glass	酒杯

bin	垃圾桶
cling film	保鲜膜
cookery book	食谱
dishcloth	洗碗布
draining board	滴水板
grill	烤架
kitchen roll	厨房纸巾
plug	插头
tea towel	茶巾
shelf	架子
sink	洗涤槽
tablecloth	桌布
washing-up liquid	洗洁精""".replace("	"," ")

# # 厨房电器
# s = kitchen_ele.replace('\n',' ').split(' ')
# res = re.findall("\d+|[a-zA-Z]+", fruit)          # ['not', '404', 'found', '99']
# fruit_list = [item for item in s if not item in res]
# sort_list(fruit_list)

pets = """cat	猫
dog	狗
goldfish (复数形式：goldfish)	金鱼
guinea pig	豚鼠
hamster	仓鼠
horse	马
kitten	小猫
mouse	老鼠
parrot	鹦鹉
pony	小马
puppy	小狗
rabbit	白兔
snake	蛇
tropical fish (复数形式：tropical fish)	热带鱼
turtle	乌龟
其他单词
to bark	叫
to bite	咬
to keep a pet	养宠物
to ride a horse	骑马
to ride a pony	骑小马
to train	训练
to walk the dog / to take the dog a walk	遛狗
lead	狗绳"""


# pet_list = to_word_list(about_car)
# sort_list(pet_list)

about_car = """accelerator	油门踏板
brake pedal	刹车踏板
clutch pedal	离合器踏板
fuel gauge	油表
gear stick	变速杆
handbrake	手刹
speedometer	速度表
steering wheel	方向盘
temperature gauge	温度表
warning light	警示灯
机械部分
battery	蓄电池
brakes	刹车
clutch	离合器
engine	引擎
fan belt	风扇皮带
exhaust	排气
exhaust pipe	排气管
gear box	齿轮箱
ignition	点火开关
radiator	散热器
spark plug	火花塞
windscreen wiper	雨刮
windscreen wipers	雨刮器
其他单词
air conditioning	空调
automatic	自动的
central locking	中央门锁
manual	手动的
tax disc	汽车路税圆形纳税证
sat nav (satellite navigation的缩写)	卫星导航
灯光和视镜
brake light	刹车灯
hazard lights	双闪灯
headlamp	前灯
headlamps	前照灯
headlights	前照灯
indicator	指示灯
indicators	指示灯
rear view mirror	后视镜
sidelights	示宽灯
wing mirror	侧视镜
其他部件
aerial	天线
back seat	后排座位
bonnet	引擎罩
boot	行李箱
bumper	保险杠
child seat	儿童座椅
cigarette lighter	打火机
dashboard	仪表板
front seat	前排座位
fuel tank	油箱
glove compartment	副驾驶前面的小柜子
glovebox	手套箱，副驾驶前面的小柜子
heater	暖气
number plate	车牌
passenger seat	乘客座位
petrol tank	油箱
roof	车顶
roof rack	车顶行李架
seatbelt	安全带
spare wheel	备胎
tow bar	牵引杆
tyre	轮胎
wheel	车轮
window	车窗
windscreen	挡风玻璃"""



# car_list = to_word_list(about_car)
# sort_list(car_list)


# sort_list("纸、废塑料、废金属、废包装物、废旧纺织物、废弃电器电子产品、废玻璃、废纸塑铝复合包装")


def name_to_json():
    name_list_f = open("ansdata/name_list.txt","r")
    name_list = list(set(eval("["+name_list_f.read().replace("}","},")+"]")))
    name_list_f.close()
    with open('ansdata/name_list.json', "w", encoding='utf-8') as write_name_list_json:
        json.dump(name_list, write_name_list_json,ensure_ascii=False)


def json_data_to_answer():
    with open('ansdata/name_list.json', "r", encoding='utf-8') as name_list_f:
        name_list = json.load(name_list_f)
        sort_list(name_list)


def answer_to_json():
    ans_list_f = open("ansdata/answer_data.txt", "r")
    ans_list = eval(json.dumps('['+str(ans_list_f.read()).replace(",", "").replace("}", "},")+']').encode('utf-8'))
    print(ans_list,type(ans_list))
    # ans_list = list(set(ans_list))
    print(len(ans_list))
    ans_list_f.close()
    with open('ansdata/answer_data.json', "w", encoding='utf-8') as ans_list_json:
        json.dump(ans_list, ans_list_json, ensure_ascii=False)

answer_to_json()
# ans_data = open("ansdata/answer_data.txt","r")

