import requests, re, json
import random

unknow_answer = [
    '我现在还不太明白这种垃圾呢！',
    '我有点看不懂你的意思呀，或许你可以问问小家园？',
    '其实我不太明白你的意思……',
    '抱歉哦，我现在的能力还不能够明白你在说什么垃圾，但我会加油的～'
]

with open('ansdata/good_data.json', "r", encoding='utf-8') as ans_list_json:
    all_datas = json.load(ans_list_json)

def trash(trash_name):

    if not trash_name:
        return random.choice(unknow_answer)

    trash_name1 = trash_name.replace("是什么垃圾", "").replace("是什么垃圾", "").replace("?", "").replace("？", "").replace(' ', '')

    trash_name2 = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", trash_name1)
    str_name = re.sub('[a-zA-Z0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~\s]+', "", trash_name2)
    if str_name == '':
        return random.choice(unknow_answer)

    if trash_name in ["你", "浩浩", "你们", "那你"]:
        inter_answer = [
            '我这么聪明，怎么会是垃圾呢？',
            '我就是除了尬聊什么都不会的小垃圾，唉。',
            '好了，那你又是什么垃圾？',
            '你都这样问了，我无可奉告',
            '为啥又有人问我这个问题...',
            '我还能和你聊天，看来我也不是一无是处qwq',
            '嗯？我是垃圾？嘿嘿 那你装得下我嘛？',
            '我是不可回收垃圾呜呜呜，不要卖了我',
            '我这么机智，要说是也是高智商垃圾吧'
        ]
        return random.choice(inter_answer)
    if trash_name2 in ["我", "我们", "那我"]:
        inter_answer = [
            '你这么聪明，怎么会是垃圾呢？',
            '你看起来不像来自地球，不会是太空垃圾吧？',
            '你这么机智，要说是也是高智商垃圾吧',
            '你这么瘦，看起来被啃过一样~ 不会是厨余垃圾八~',
            '没想到这个世界上居然会有人像我一样承认自己是垃圾',
            '我不想告诉你真相，怕你伤心'
        ]
        return random.choice(inter_answer)
    if trash_name2 in ["群主", "楼上", "欣芝"]:
        inter_answer = [
            '{}这么聪明，怎么会是垃圾呢？'.format(trash_name),
            '{}看起来不像来自地球，不会是太空垃圾吧？'.format(trash_name),
            '{}这么机智，要说是也是高智商垃圾吧'.format(trash_name)
        ]
        return random.choice(inter_answer)
    if trash_name2 in ["老汪头", "郑宇杰"]:
        inter_answer = [
            '为啥又有人问我这个问题...',
            '{}这么笨，被归属于垃圾，垃圾家族应该不会满意吧！！'.format(trash_name),
            '{}看起来不像来自地球，不会是太空垃圾吧？'.format(trash_name),
            '{}这么搞笑，或许是娱乐垃圾吧'.format(trash_name)
        ]
        return random.choice(inter_answer)

    if trash_name2 in all_datas:
        # print('='*100)
        trash_is = all_datas[trash_name2]
        ans = '{}属于{}{}'.format(trash_name, str(trash_is), random.choice(['哦~', '呢！', '的啦！', '哟~']))
        return ans

    try:
        url = 'http://trash.lhsr.cn/sites/feiguan/trashTypes_3/Handler/Handler.ashx?a=GET_KEYWORDS&kw={}'.format(trash_name2)
        res = requests.get(url, headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3962.2 Safari/537.36'
        })
        data = json.loads(res.text)
        if data['kw_list']:
            list = data['kw_list']
            if (trash_name2 in list):
                trash_is = data['kw_arr'][list.index(trash_name2)]['TypeKey']
                ans = '{}属于{}{}'.format(trash_name, str(trash_is), random.choice(['哦~', '呢！', '的啦！', '哟~']))
            else:
                trash_is = '、'.join(list)
                ans = '你问的是{}中的哪一个呢？请输入全名哦~'.format(trash_is)
            return ans
        else: raise IndexError
        # ans_data_f = open("ansdata/answer_data.txt","a")
        # ans_data = {trash_name2: trash_is}
        # ans_data_f.write(str(ans_data))
    except IndexError or requests.exceptions.ConnectionError:
        random_sentence = (
            '我现在还不太明白{}是什么垃圾呢，但没关系，你可以问点别的呢！比如我是什么垃圾'.format(trash_name),
            '我有点看不懂你的意思呀，或许你可以问问小家园？',
            '其实我不太明白{}的意思……'.format(trash_name),
            '这个我不知道呢...或许是厨余垃圾？',
            '为啥又有人问我这个问题...',
            '这个我不知道呢...{}可能是厨余垃圾？'.format(trash_name),
            '不知道哦...看样子含水量挺多的？可能是湿垃圾吧',
            '看起来挺酷的...{}难道是电子垃圾？'.format(trash_name),
            '不知道...但愿Ta是无毒无害垃圾吧',
            '这个我不确定呢，难不成是太空垃圾？'
        )
        other_name = cut_find_more_word(trash_name2)
        if other_name == []:
            other_name = ''
        else:
            # print(other_name)
            name_list = list(set(other_name))
            ans_data_f = open("ansdata/name_list.txt", "a")
            ans_data_f.write(str(name_list)[1:-1] + ',')
            other_name = '或许你想问的是' + '、'.join(name_list) + '?'

        return random.choice(random_sentence) + other_name


# print(res)

def other_trash(name):
    url = 'http://trash.lhsr.cn/sites/feiguan/trashTypes/dyn/Handler/Handler.ashx'
    datas = {
        'a': 'Keywords_Get',
        's_kw': name
    }
    try:
        res = requests.post(url, data=datas, timeout=3).text
        if res == "":
            return []
        else:
            res = eval(requests.post(url, data=datas, timeout=3).text)
            # ["502胶水","504胶水","504胶水废包装"]
            return res
    except:
        return []


def cut_find_more_word(word):
    url_list = ['http://114.67.84.223/get.php?source=', 'http://120.26.6.172/get.php?source=',
                'http://116.196.101.207/get.php?source=']

    # print(url)
    try:
        url = random.choice(url_list) + word + "&param1=0&param2=1&json=1"
        res = eval(requests.get(url).text)
    except requests.exceptions.ConnectionError:
        url = random.choice(url_list) + word + "&param1=0&param2=1&json=1"
        res = eval(requests.get(url).text)
    word_list = []
    for i in res:
        if float(i["p"]) > 0.9:
            word_list.append(i["t"])

    more_word = []
    if word_list is not []:
        for w in word_list:
            others = other_trash(w)
            if others != [] and others not in more_word:
                more_word.extend(others)
    return more_word


def sort_list(trash_list_str: str or list) -> str:
    if type(trash_list_str) is list:
        trash_list = list(set(trash_list_str))
    else:
        trash_list = trash_list_str.replace('，','、').replace('等','').split('、')
    # print(trash_list)
    for i in trash_list:
        ans = trash(i)
        print(ans)

# sort_list("榴莲壳、椰子壳、柚子皮")

# a = trash("行李箱")
print("run!!!")
# other_trash("人")
