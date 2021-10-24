import pandas as pd
from sklearn.metrics import *
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity



#pragma dataset init DATASET_NAME --size 1Gb

# TODO: fill dataset here
# Dataset will be created in /home/jupyter/mnt/datasets/DATASET_NAME

import os

def get_relatife_file_name(name_file):
    script_dir = os.path.dirname(__file__)
    return os.path.join(script_dir, name_file)



categ_1 = pd.read_csv(get_relatife_file_name('cat_1.csv'), sep=';',encoding='windows-1251')
# categ_2 = pd.read_csv('cat_2.csv', sep=';',encoding='windows-1251')
# categ_3 = pd.read_csv('cat_3.csv', sep=';',encoding='windows-1251')

categs_combined = pd.concat([categ_1])#,categ_2,categ_3])

categs_combined['aut'] = categs_combined['aut'].fillna('Неизвестен')
categs_combined['title'] = categs_combined['title'].fillna('Неизестно')
categs_combined['place'] = categs_combined['place'].fillna('Неизестно')
categs_combined['publ'] = categs_combined['publ'].fillna('Неизвестен')
categs_combined['yea'] = categs_combined['yea'].fillna('Неизвестен')
categs_combined['lan'] = categs_combined['lan'].fillna('Неизвестен')
categs_combined['rubrics'] = categs_combined['rubrics'].fillna('Неизвестны')
categs_combined['person'] = categs_combined['person'].fillna('Неизвестен')
categs_combined['serial'] = categs_combined['serial'].fillna('Неизвестен')
categs_combined['ager'] = categs_combined['ager'].fillna('Неизвестен')

fund_1 = pd.read_csv(get_relatife_file_name('fund_1.csv'), sep=';',encoding='windows-1251')

# fund_2 = pd.read_csv('fund_2.csv', sep=';',encoding='windows-1251')
#
# fund_3 = pd.read_csv('fund_3.csv', sep=';',encoding='windows-1251')
#
# fund_4 = pd.read_csv('fund_4.csv', sep=';',encoding='windows-1251')
#
# fund_5 = pd.read_csv('fund_5.csv', sep=';',encoding='windows-1251')
#
# fund_6 = pd.read_csv('fund_6.csv', sep=';',encoding='windows-1251')
#
# fund_7 = pd.read_csv('fund_7.csv', sep=';',encoding='windows-1251')
#
# fund_8 = pd.read_csv('fund_8.csv', sep=';',encoding='windows-1251')
#
# fund_9 = pd.read_csv('fund_9.csv', sep=';',encoding='windows-1251')
#
# fund_10 = pd.read_csv('fund_10_fix.csv', sep=';',encoding='windows-1251')
# fund_10 = fund_10.drop(['Unnamed: 8','Unnamed: 9'],axis=1)
#
# fund_11 = pd.read_csv('fund_11_fix.csv', sep=';',encoding='windows-1251')
# fund_11 = fund_11.drop(['Unnamed: 8','Unnamed: 9'],axis=1)
#
# fund_12 = pd.read_csv('fund_12_fix.csv', sep=';',encoding='windows-1251')
# fund_12 = fund_12.drop(['Unnamed: 8','Unnamed: 9'],axis=1)
#
# fund_13 = pd.read_csv('fund_13_fix.csv', sep=';',encoding='windows-1251')
# fund_13 = fund_13.drop(['Unnamed: 8','Unnamed: 9'],axis=1)
#
# fund_14 = pd.read_csv('fund_14.csv', sep=';',encoding='windows-1251')
#
# fund_15 = pd.read_csv('fund_15.csv', sep=';',encoding='windows-1251')
#
# fund_16 = pd.read_csv('fund_16.csv', sep=';',encoding='windows-1251')

funds_combined = pd.concat(
    [fund_1,
     # fund_2,
     # fund_3,
     # fund_4,
     # fund_5,
     # fund_6,
     # fund_7,
     # fund_8,
     # fund_9,
     # fund_10,
     # fund_11,
     # fund_12,
     # fund_13,
     # fund_14,
     # fund_15,
     # fund_16
     ])

funds_combined = funds_combined.rename(columns={'Unnamed: 6':'siglaID_2',
                               'Unnamed: 7':'inventoryNumber_2',
                               'Unnamed: 8':'barCode_2',
                               'Unnamed: 9':'trackIndex_2'})

funds_combined['trackIndex'] = funds_combined['trackIndex'].fillna('Неизвестен')
funds_combined['siglaID_2'] = funds_combined['siglaID_2'].fillna('Нет')
funds_combined['inventoryNumber_2'] = funds_combined['inventoryNumber_2'].fillna('Нет')
#funds_combined['barCode_2'] = funds_combined['barCode_2'].fillna('Нет')
#funds_combined['trackIndex_2'] = funds_combined['trackIndex_2'].fillna('Нет')


circ_1 = pd.read_csv(get_relatife_file_name('circulaton_1.csv'), sep=';',encoding='windows-1251')
# circ_2 = pd.read_csv('circulaton_2.csv', sep=';',encoding='windows-1251')
# circ_3 = pd.read_csv('circulaton_3.csv', sep=';',encoding='windows-1251')
# circ_4 = pd.read_csv('circulaton_4.csv', sep=';',encoding='windows-1251')
# circ_5 = pd.read_csv('circulaton_5.csv', sep=';',encoding='windows-1251')
# circ_6 = pd.read_csv('circulaton_6.csv', sep=';',encoding='windows-1251')
# circ_7 = pd.read_csv('circulaton_7.csv', sep=';',encoding='windows-1251')
# circ_8 = pd.read_csv('circulaton_8.csv', sep=';',encoding='windows-1251')
# circ_9 = pd.read_csv('circulaton_9.csv', sep=';',encoding='windows-1251')
# circ_10 = pd.read_csv('circulaton_10.csv', sep=';',encoding='windows-1251')
# circ_11 = pd.read_csv('circulaton_11.csv', sep=';',encoding='windows-1251')
# circ_12 = pd.read_csv('circulaton_12.csv', sep=';',encoding='windows-1251')
# circ_13 = pd.read_csv('circulaton_13.csv', sep=';',encoding='windows-1251')
# circ_14 = pd.read_csv('circulaton_14.csv', sep=';',encoding='windows-1251')
# circ_15 = pd.read_csv('circulaton_15.csv', sep=';',encoding='windows-1251')
# circ_16 = pd.read_csv('circulaton_16.csv', sep=';',encoding='windows-1251')

circs_combined = pd.concat(
    [circ_1,
     # circ_2,
     # circ_3,
     # circ_4,
     # circ_5,
     # circ_6,
     # circ_7,
     # circ_8,
     # circ_9,
     # circ_10,
     # circ_11,
     # circ_12,
     # circ_13,
     # circ_14,
     # circ_15,
     # circ_16
     ])

circs_combined = circs_combined.drop(['Unnamed: 8'],axis=1)
combiner = circs_combined['catalogueRecordID'].value_counts().to_dict()


occurences = []

for c in categs_combined['recId']:
    #print(c)
    try:
        occurences.append(combiner[c])
    except:
        occurences.append(0)

categs_combined['booking'] = occurences

years = []

for y in categs_combined['yea']:
    if y != 'Неизвестен':
        new_y = y[0:3]
        new_y = new_y + '0'
    years.append(new_y)

categs_combined['decade'] = years

needed_set = categs_combined[['aut','title','rubrics','decade','booking']]

def clean_data(x):
    if isinstance(x, list):
        return [str.lower(i.replace(" ", "").replace(":", "").replace(".", "")) for i in x]
    else:
        #Check if director exists. If not, return empty string
        if isinstance(x, str):
            return str.lower(x.replace(" ", "").replace(":", "").replace(".", ""))
        else:
            return ''

features = ['aut','title','rubrics','decade']

for f in features:
    needed_set[f] = needed_set[f].apply(clean_data)

needed_set = needed_set.replace(['неизвестно','неизвестен'],'')


def create_soup(x):
    return ''.join(x['aut']) + ' ' + ''.join(x['title']) + ' ' + x['rubrics'] + ' ' + ''.join(x['decade'])

needed_set['soup'] = needed_set.apply(create_soup, axis=1)

#needed_set = needed_set[:20000] # можно подкрутить или убрать ограничитель

count = CountVectorizer()
count_matrix = count.fit_transform(needed_set['soup'])

count_matrix = count_matrix.astype(np.float32)

cosine_sim2 = cosine_similarity(count_matrix, count_matrix)

indices = pd.Series(categs_combined.index, index=categs_combined['title']).drop_duplicates()

def search(user_id):
    result_json = {}
    history_set = circs_combined[circs_combined['readerID'] == user_id]
    barcodes = history_set['barcode']
    catalogue_info = {}

    for index, row in funds_combined.iterrows():
        if row['barCode'] in list(barcodes):
            catalogue_info[row['fundID']] = row['catalogueRecordID']

    res = dict((v, k) for k, v in catalogue_info.items())

    list_of_history = []
    list_of_recommendations = []
    list_of_titles = []

    for index, row in categs_combined.iterrows():
        if row['recId'] in catalogue_info.values():
            hist = {}
            hist['id'] = res[row['recId']]
            hist['title'] = row['title']
            hist['author'] = row['aut']

            list_of_history.append(hist)
            list_of_titles.append(row['title'])

    def get_recommendations(title, cosine_sim):
        idx = indices[title]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1]
        book_indices = [i[0] for i in sim_scores]
        return categs_combined[['recId', 'title', 'aut']].iloc[book_indices]

    recomms = []

    if len(list_of_titles) < 5:
        if len(list_of_titles) == 0:
            return "Рекомендаций нет"
        else:
            for l in list_of_titles:
                result = get_recommendations(l, cosine_sim2).to_dict()
                new_res = {}
                for index, row in funds_combined.iterrows():
                    if result['recId'] == row['catalogueRecordID']:
                        new_res['id'] = row['catalogueRecordID']
                        break
                new_res['title'] = result['title']
                new_res['author'] = result['aut']
                recomms.append(new_res)

    result_json['recommendations'] = recomms
    result_json['history'] = list_of_history
    return result_json
