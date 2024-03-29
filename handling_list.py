def main():
    top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey", "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]
    for i, artist in enumerate(top_artists):
        print(i, artist)
    replaceArtist(top_artists)
    for i, artist in enumerate(top_artists):
        print(i, artist)
    replaceArtist(top_artists)

def replaceArtist (top_artists):
    try:
        #error handling for index
        index = int(input("Enter the index of the artist you want to replace: "))
        if index < 0 or index >= len(top_artists):
            raise IndexError
        #asking for new artist
        new_artist = input("Enter the name of the new artist: ")
        top_artists[index] = new_artist
        print("Artist has been replaced.")
    except (ValueError, IndexError):
        print("An input error has occurred.")


main()