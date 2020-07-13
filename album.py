def make_album(album_name, album_band, album_release, album_songs=None):
	album = {'Name': album_name, 'Band': album_band, 'Release': album_release}
	if album_songs:
		album['Songs'] = album_songs

	return album


album_made = make_album('korn','korn',1996, album_songs=10)
print(album_made)

album_made = make_album('Papa Roach','Papa Roach',1998)
print(album_made)

album_made = make_album('Staind','Staind',1990, album_songs=11)
print(album_made)
