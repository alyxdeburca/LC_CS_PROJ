def save(data):
	with open("savefile.dat", "w") as f:
		f.write(str(data))
		f.close()
