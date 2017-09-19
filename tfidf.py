import math 

def tf(n_term, total_term):
	tf = n_term / total_term
	return tf

def idf(n_term, total_term):
	idf = math.log10(n_term / total_term)
	return idf
