
def youngestFellah(data, year):
	try:
		f_age = data[(data["Year"] == year) & (data["Sex"] == "F")].sort_values("Age")["Age"].iloc[0]
		m_age = data[(data["Year"] == year) & (data["Sex"] == "M")].sort_values("Age")["Age"].iloc[0]
	except IndexError:
		print(f"AH. {year} is probably not an olympic year")
		return (None)
	return ({'f': f_age, 'm': m_age})
