csv = "John,25,Engineer;Mary,30,Doctor;Sam,22,Designer"
data = [row.split(",") for row in csv.split(";")]
print(data)
