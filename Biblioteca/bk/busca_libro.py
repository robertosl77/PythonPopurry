import requests

def get_book_info(isbn):
    url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "items" in data:
            book_info = data["items"][0]["volumeInfo"]
            title = book_info.get("title", "N/A")
            authors = ", ".join(book_info.get("authors", ["N/A"]))
            published_date = book_info.get("publishedDate", "N/A")
            description = book_info.get("description", "N/A")
            return {
                "Title": title,
                "Authors": authors,
                "Published Date": published_date,
                "Description": description
            }
        else:
            return {"Error": "No book found with this ISBN"}
    else:
        return {"Error": "Failed to fetch data"}

isbn = input("Enter ISBN: ")
book_info = get_book_info(isbn)
for key, value in book_info.items():
    print(f"{key}: {value}")
