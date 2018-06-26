

#重命名
import datetime


def get_new_file_name(old_name):
    # .png
    # 获取客服端图片的后缀名
    suffix_name = '.' + old_name.split('.')[-1]
    #把时间类型转化为指定格式的字符串输出
    #IMG2018062525262545
    # new_name = 'IMG_%s' %(datetime.datetime.now().strftime('%Y%m%%d%H%M%S'))
    new_name = 'IMG_{}'.format(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
    return new_name + suffix_name