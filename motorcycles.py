motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
motorcycles.append('Honda')
motorcycles.append('Yamaha')
motorcycles.append('Suzuki')
print(motorcycles)

motorcycles.insert(0,'Ducati')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

del motorcycles[2]
print(motorcycles)

del motorcycles[-1]
print(motorcycles)



motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

last_owned = motorcycles.pop()
first_owned = motorcycles.pop(0)
print(motorcycles)
print(last_owned)
print(first_owned)
print(f"The Last Motorcycle that I owned was a {last_owned.title()}!")
print(f"The first motorcycle that I owed was a {first_owned.title()}!")



motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)


motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nThe {too_expensive.title()} is too expensive for me.")