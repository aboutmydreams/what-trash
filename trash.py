import requests,re
import random
from bs4 import BeautifulSoup


def trash(trash_name):
    trash_name = trash_name.replace("是什么垃圾","").replace("是什么垃圾","").replace("?","").replace("？","").replace(' ','')


    trash_name = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])","",trash_name)
    str_name = re.sub('[a-zA-Z0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~\s]+', "", trash_name)
    if str_name == '':
        unknow_answer = [
            '我现在还不太明白这种垃圾呢！',
            '我有点看不懂你的意思呀，可以跟我聊些简单的话题嘛',
            '其实我不太明白你的意思……',
            '抱歉哦，我现在的能力还不能够明白你在说什么，但我会加油的～'
        ]
        return random.choice(unknow_answer)

    if trash_name in ["你","浩浩","你们","那你"]:
        inter_answer = [
            '我这么聪明，怎么会是垃圾呢？',
            '我这么机智，要说是也是高智商垃圾吧'
        ]
        return random.choice(inter_answer)
    if trash_name in ["我","我们","那我","楼上"]:
        inter_answer = [
            '你这么聪明，怎么会是垃圾呢？',
            '你看起来不像来自地球，不会是太空垃圾吧？',
            '你这么机智，要说是也是高智商垃圾吧'
        ]
        return random.choice(inter_answer)

    if trash_name in ["群主","楼上","欣芝"]:
        inter_answer = [
            '{}这么聪明，怎么会是垃圾呢？'.format(trash_name),
            '{}看起来不像来自地球，不会是太空垃圾吧？'.format(trash_name),
            '{}这么机智，要说是也是高智商垃圾吧'.format(trash_name)
        ]
        return random.choice(inter_answer)

    if trash_name in ["老汪头","郑宇杰"]:
        inter_answer = [
            '{}这么笨，被归属于垃圾，垃圾家族应该不会满意吧！！'.format(trash_name),
            '{}看起来不像来自地球，不会是太空垃圾吧？'.format(trash_name),
            '{}这么搞笑，或许是娱乐垃圾吧'.format(trash_name)
        ]
        return random.choice(inter_answer)

    try:
        url = 'http://trash.lhsr.cn/sites/feiguan/trashTypes_2/TrashQuery.aspx?kw={}'.format(trash_name)
        res = requests.get(url).text
        soup = BeautifulSoup(res,'lxml')
        trash_is = soup.select('#form1 > div.main > div.con > div.info > p > span')[0].get_text()
        ans = '{}属于{}哦~'.format(trash_name,str(trash_is))
        return ans
    except IndexError or requests.exceptions.ConnectionError:
        random_sentence = (
            '我现在还不太明白{}是什么呢，但没关系，你可以问点别的呢！'.format(trash_name),
            '我有点看不懂你的意思呀，可以跟我聊些简单的话题嘛',
            '其实我不太明白{}的意思……'.format(trash_name),
            '这个我不知道呢...或许是厨余垃圾？',
            '这个我不知道呢...{}可能是厨余垃圾？'.format(trash_name),
            '不知道哦...看样子含水量挺多的？可能是湿垃圾吧',
            '看起来挺酷的...{}难道是电子垃圾？'.format(trash_name),
            '这个我不确定呢，难不成是太空垃圾？'
        )
        other_name = cut_find_more_word(trash_name)
        if other_name == []:
            other_name = ''
        else:
            print(other_name)
            other_name = '或许你想问的是'+ '、'.join(list(set(other_name))) + '?'
        return random.choice(random_sentence) + other_name
# print(res)

def other_trash(name):
    url = 'http://trash.lhsr.cn/sites/feiguan/trashTypes/dyn/Handler/Handler.ashx'
    datas = {
        'a': 'Keywords_Get',
        's_kw': name
    }
    try:
        res = requests.post(url,data=datas,timeout=3).text
        if res == "":
            return []
        else:
            res = eval(requests.post(url,data=datas,timeout=3).text)
            #["502胶水","504胶水","504胶水废包装"]
            return res
    except:
        return []


def cut_find_more_word(word):
    url_list= ['http://114.67.84.223/get.php?source=', 'http://120.26.6.172/get.php?source=','http://116.196.101.207/get.php?source=']
    url = random.choice(url_list) + word + "&param1=0&param2=1&json=1"
    # print(url)
    res = eval(requests.get(url).text)
    word_list = []
    for i in res:
        if float(i["p"]) > 0.9:
            word_list.append(i["t"])

    more_word = []
    if word_list is not []:
        for w in word_list:
            others = other_trash(w)
            if others!=[] and others not in more_word:
                more_word.extend(others)
    return more_word


# a = trash("邓文浩是什么垃圾")
# print(a)
# other_trash("人")
