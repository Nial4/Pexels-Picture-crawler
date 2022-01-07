# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
import os
import urllib.request


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+8 to toggle the breakpoint.
    # curl - H
    # "Authorization: 563492ad6f91700001000001c32842f1900c415e98fc7fce9b734525" \
    # "https://api.pexels.com/v1/search?query=nature&per_page=110" - o
    # test2.json
    print("=======start part "+str(name)+"=======")
    with open("summer"+str(name)+".json", 'r', encoding='utf8') as fp:
        json_data = json.load(fp)
        #print('json：', json_data)
        print('json Type：', type(json_data))

        images=json_data['photos']
        imageList= []
        for id in images:
            imageList.append(id['src']['medium'])
        #print(imageList)

        for i in range(len(imageList)):
            print("download:" + str(i))
            save_name = str(i) + '.jpg'
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
            with open('snow' + str(i) + '.jpg', 'wb') as wf:
                req = urllib.request.Request(url=imageList[i], headers=headers)
                context = urllib.request.urlopen(req).read()
                wf.write(context)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for i in range(1,101):
        print_hi(i)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
