# import fungsi fari tfidf
from tfidf import tf
from tfidf import idf
 
# variable
n_term = 3
total_term = 100
n_docs = 10000000
total_docs = 1000

# memanggil fungsi tf untuk menghitung term frequency
# variabel tf_value akan menampung file dari hasil komparasi fungsi tf 
tf_value = tf(n_term, total_term)
idf_value = idf(n_docs, total_docs)


# print tf_value
print("Term frequency : {0}".format(tf_value))
print("IDF : {0}".format(idf_value))


# Bobot
bobot = tf_value * idf_value
print("Weight : {0}".format(bobot))