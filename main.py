from text2image import preprocess, process
#import text2image

def main():
    df_new = process.load_data()
    ds, tfidf_matrix, vec_tfidf = process.vectorization(df_new)
    tfidf_matrix_query = process.text_audience_input(ds, tfidf_matrix, vec_tfidf)
    index_highsimilarity = process.calc_cosine_similarity(tfidf_matrix, tfidf_matrix_query)
    process.show_pics(df_new, index_highsimilarity)


if __name__ == '__main__':
    main()
