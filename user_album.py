def make_album(album_name, album_band, album_release, album_songs=None):
	album = {'Name': album_name, 'Band': album_band, 'Release': album_release}
	if album_songs:
		album['Songs'] = album_songs

	return album

print("\nPlease enter info about your favorite albums.")
print("(Please type in 'q' to quite at any time.)")

while True:
	a_name = input("Album Name: ")
	if a_name == 'q':
		break
	a_band = input("Band Name: ")
	if a_band == 'q':
			break
	a_release = input("Release Date: ")
	if a_release == 'q':
		break
	a_songs = input("Number of Songs: ")
	if a_songs == 'q':
		break

	album_made = make_album(a_name, a_band, a_release, a_songs)	
	print(album_made)

