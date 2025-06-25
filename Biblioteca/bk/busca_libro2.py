import requests

def get_book_info_openlibrary(isbn):
    url = f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if f"ISBN:{isbn}" in data:
            book_info = data[f"ISBN:{isbn}"]
            title = book_info.get("title", "N/A")
            authors = ", ".join([author["name"] for author in book_info.get("authors", [{"name": "N/A"}])])
            published_date = book_info.get("publish_date", "N/A")
            return {
                "Title": title,
                "Authors": authors,
                "Published Date": published_date
            }
        else:
            return {"Error": "No book found with this ISBN"}
    else:
        return {"Error": f"Failed to fetch data, status code: {response.status_code}"}

isbn = input("Enter ISBN: ")
book_info = get_book_info_openlibrary(isbn)
for key, value in book_info.items():
    print(f"{key}: {value}")
