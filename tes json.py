import json
via = {'nama': 'via', 'nim': '71220871'}
van = {'nama': 'vania', 'nim': '2414010'}
data = [via,van]
with open ('mahasiswa.json','w') as datafile: 
    json.dump(data,datafile)

#baca
with open ('mahasiswa.json','r') as datafile: 
    data = json.load(datafile)
    for item in data: 
        print('Nama: ',item['nama'],', Nim: ', item['nim'])