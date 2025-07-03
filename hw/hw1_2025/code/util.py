from typing import Dict, List

class ResponseData:
    data_list: List[object]
    total: int

    def __init__(self, data_list=None, total: int = 0):
        if data_list is None:
            data_list = []
        self.data_list = data_list
        self.total = total


def fetch_data(input_file_path: str,
               sort_key: str = None, sort_order: str = 'asc',
               filter_dict: Dict = None) -> ResponseData:
    # read data from file
    # TODO: open the file and retrieve the content
    member_list: List[Dict] = []  # 储存读取的球员信息
    try:
        datafile=open(input_file_path, 'r',encoding='utf-8')
    except FileNotFoundError:  #找不到文件的异常处理
        return ResponseData([], 0)
    read_data = datafile.readlines()
    if len(read_data) < 2 :
        datafile.close()
        return ResponseData([], 0)  #文件没有有效信息的异常处理
    data_name: str=read_data[0].strip()
    data_name_list=data_name.split(',')  #球员信息属性名称集合
    name_number: int=len(data_name_list)
    for data in read_data[1:]:
        datafile_temp:str=data.strip() #遍历读取球员信息
        if datafile_temp:
            temp_data_list=datafile_temp.split(',')
            if len(temp_data_list)==name_number:  #拥有所有属性的球员才读取
                parsed_values: List[object] = []
                for temp_data in temp_data_list:  #解析数值类型
                    if temp_data == '':
                        parsed_values.append(None)  #如果为空字符串，解析为None
                        continue  # 继续下一个值
                    try :
                        parsed_values.append(int(temp_data))
                    except ValueError :
                        try:
                            parsed_values.append(float(temp_data))
                        except ValueError :
                            parsed_values.append(temp_data)
                member:Dict={k:v for k,v in zip(data_name_list, parsed_values)}
                member_list.append(member) #Dict创建时如果同一个键被赋值两次，后一个值会被记住
    if  datafile:
        datafile.close()
    # process logic
    # TODO: achieve filter/sort... logic according to the augments
    #筛选逻辑
    data_list:List[object]=[]
    if filter_dict:  #若不存在筛选条件
        for member in member_list:
            flag = 0
            for key, value in filter_dict.items():
                if key in member and value is not None:  #检查筛选条件是否合理
                    if type(value) is str:
                        if not value in member[key]:
                            flag = 1
                    elif type(value) is int or type(value) is float :
                        if  value != member[key]:
                            flag = 1
            if not flag:
                data_list.append(member)  #满足条件的留下
    else:
        data_list=member_list
    # 排序
    reverse_sort = (sort_order == 'desc')
    if sort_key in data_name_list:  #判断排序条件
        data_list.sort(key=lambda item: (item.get(sort_key) is None, item.get(sort_key)), reverse=reverse_sort)  #优先判断是否为None，然后实际值

    total=len(data_list)

    # return
    response_data = ResponseData(data_list, total)
    return response_data