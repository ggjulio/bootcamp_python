class Evaluator:
	@staticmethod
	def __check_error(coefs, words):
		if len(coefs) != len(words):
			raise ValueError("coef and words should have the same lenght")
		if type(coefs) is not list:
			raise TypeError("coefs should be a list")
		if type(words) is not list:
			raise TypeError("words should be a list")
		if not all(isinstance(n, (int, float)) for n in coefs):
			raise TypeError("coefs should contain only int or float values.")
		if not all(isinstance(w, (str)) for w in words):
			raise TypeError("words should contain only str values.")

	@staticmethod
	def zip_evaluate(coefs, words):
		Evaluator.__check_error(coefs,words)
		return (sum([coef * len(word) for coef, word in zip(coefs, words)]))

	@staticmethod
	def enumerate_evaluate(coefs, words):
		Evaluator.__check_error(coefs,words)
		return (sum([coef * len(word) for coef, word in zip(coefs, words)]))
	


