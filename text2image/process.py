import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from PIL import Image
import matplotlib.pyplot as plt
import text2image.preprocess
import shutil
import os

'''This code load the dataset and convert the attributes matrix
to a matrix of image id and vectorized texts
, calculate the similarity, and show higher-similrity pictures'''

def load_data():

    # Load the dataset to a dataframe
    dir = "./data/styleGAN_project_split_data_train_data_attr.csv" #to be modifid to load it from GCP!
    df = pd.read_csv(dir, low_memory = False)

    # Combine attributes at every row
    df=df.replace(-1, 0)
    columns_list=df.columns.values[1:].tolist()

    df['combined'] = df.iloc[:, 1:].dot(df.columns[1:] + ' ').str[:-1]
    df.combined = df.combined.str.replace("_"," ")

    df_new = df[["image_id","combined"]]

    return df_new

def vectorization(df_new):

    # Vectorize the attributes at every row
    ds = df_new["combined"]

    # Call a vocaburary dictionary
    vocab = call_vocaburary_dict()

    ## TfidfVectorizer with a vocaburary option, ngram(1,3)
    vec_tfidf = TfidfVectorizer(vocabulary=vocab, ngram_range = (1,3))

    ## vectorize
    tfidf_matrix = vec_tfidf.fit_transform(ds)

    ## Print the properties, shape of tfidf_matrix
    print('Vocabulary size: {}'.format(len(vec_tfidf.vocabulary_)))
    print('Vocabulary content: {}'.format(vec_tfidf.vocabulary_))
    print(tfidf_matrix.shape)
    matrix_tfidf=pd.DataFrame(tfidf_matrix.todense())
    matrix_tfidf.head()

    return ds, tfidf_matrix, vec_tfidf

def text_audience_input(query, ds, tfidf_matrix, vec_tfidf):

    # Input a query from audience <-- Streamlit input
    #query = 'A young male, bald, wavy hair, attractive'
    #query = 'An attractive young female, wavy hair, blond hair, no beard, bangs, earrings, lipsticks'
    print(f"The input text is {query}")

    query_preprocessed = np.array([text2image.preprocessing(query)])

    # vectorize
    tfidf_matrix_query = vec_tfidf.transform(query_preprocessed)

    # Print the shape of tfidf_matrix
    print(tfidf_matrix_query.shape)
    return tfidf_matrix_query

def calc_cosine_similarity(tfidf_matrix, tfidf_matrix_query):
    # colc cosine similarity
    cosine_sim = cosine_similarity(tfidf_matrix[0:], tfidf_matrix_query)
    cosine_sim

    df2 = pd.DataFrame(cosine_sim, columns=["cos_sim"])

    df2.cos_sim.sort_values(ascending=False)

    index_highsimilarity=df2.cos_sim.sort_values(ascending=False).index
    print(index_highsimilarity)
    return index_highsimilarity

def show_pics(df_new, index_highsimilarity):

    # A path to the picture directory
    path = "./data/raw_data/img_align_celeba/"
    # A path to the directory to save selected pictures
    path_save = "./data/save/"

    plt.close("all")
    shutil.rmtree(path_save)
    os.mkdir(path_save)

    for i in range(1): # change the top N
        print(i)
        img_filename = df_new.iloc[index_highsimilarity[i]].image_id
        filename = path + img_filename
        print(filename)
        img = Image.open(filename)
        plt.figure(figsize=(2,2))
        plt.imshow(img)
        img.save(f"{path_save}matched_{img_filename}.png", format='PNG')
        plt.show()
    return filename

def call_vocaburary_dict():
#you can choose either of the following vocaburary dicts#
    vocab = {"5 o'clock shadow":0,"arched eyebrows":1,"attractive":2,"bags under eyes":3,
            "bald":4,"bangs":5,"big lips":6,"big nose":7,"black hair":8,"blond hair":9,
            "blurry":10,"brown hair":11,"bushy eyebrows":12,"chubby":13,"double chin":14,
            "eyeglasses":15,"goatee":16,"gray hair":17,"heavy makeup":18,"high cheekbones":19,
            "male":20,"mouth slightly open":21,"mustache":22,"narrow eyes":23,"no beard":24,
            "oval face":25,"pale skin":26,"pointy nose":27,"receding hairline":28,
            "rosy cheeks":29,"sideburns":30,"smiling":31,"straight hair":32,"wavy hair":33,
            "wearing earrings":34,"wearing hat":35,"wearing lipstick":36,"wearing necklace":37,
            "wearing necktie":38,"young":39}

    vocab_arranged = {"5 o'clock":0,"arched":1,"attractive":2,"bags under eyes":3,
            "bald":4,"bangs":5,"big lips":6,"big nose":7,"black":8,"blond":9,
            "blurry":10,"brown":11,"bushy":12,"chubby":13,"double chin":14,
            "eyeglasses":15,"goatee":16,"gray":17,"heavy makeup":18,"high cheekbones":19,
            "male":20,"mouth slightly open":21,"mustache":22,"narrow eyes":23,"no beard":24,
            "oval":25,"pale":26,"pointy":27,"receding hairline":28,
            "rosy":29,"sideburns":30,"smiling":31,"straight":32,"wavy":33,
            "earrings":34,"hat":35,"lipstick":36,"necklace":37,
            "necktie":38,"young":39}
    return vocab



#df_new = load_data()
#ds, tfidf_matrix, vec_tfidf = vectorization(df_new)
#tfidf_matrix_query = text_audience_input(ds, tfidf_matrix, vec_tfidf)
#index_highsimilarity = calc_cosine_similarity(tfidf_matrix, tfidf_matrix_query)
#show_pics(df_new, index_highsimilarity)
