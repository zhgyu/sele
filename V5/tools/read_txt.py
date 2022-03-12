def read_txt(filename):
    pth="../data/"+filename
    with open(pth,'r',encoding="utf-8") as f:
        return f.readlines()

if __name__ == '__main__':
    datas = read_txt('data.txt')
    print(datas)
    arrs=[]
    for data in datas:
        arrs.append(tuple(data.strip().split(",")))
    print(arrs)