# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop.

def make_album(artist, title, songs = None):
    album = {"artist": artist, "title": title}
    
    if songs:
        album["songs"] = songs
    
    return album

while True:
    artist = input("Enter the artist name: ")
    if artist.lower() == "quit":
        break
    
    title = input("Enter the album title: ")
    if title.lower() == "quit":
        break

    album = make_album(artist, title)
    print(f"Album created: {album}")