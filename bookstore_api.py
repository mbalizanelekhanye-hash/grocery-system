import requests
import truststore

# Use the operating system's trusted certificate store (helpful on managed
# Windows devices that add their own trusted HTTPS certificate).
truststore.inject_into_ssl()

# MockAPI endpoint for the Bookstore project's `books` resource.
API_URL = "https://6af5c837f6270fa08d689c3c.mockapi.io/books"
TIMEOUT_SECONDS = 15


def get_books():
    """Fetch all books and print the JSON response and HTTP status."""
    try:
        response = requests.get(API_URL, timeout=TIMEOUT_SECONDS)
        response.raise_for_status()
    except requests.exceptions.HTTPError as error:
        print(f"GET failed: {error}")
        if error.response is not None:
            print("Status code:", error.response.status_code)
            print("Response:", error.response.text)
        return None

    books = response.json()
    print("GET books:", books)
    print("Status code:", response.status_code)
    return books


def add_book(book):
    """Create a book with POST and return the created record."""
    response = requests.post(API_URL, json=book, timeout=TIMEOUT_SECONDS)
    response.raise_for_status()
    created_book = response.json()
    print("POST response:", created_book)
    print("Status code:", response.status_code)
    return created_book


def update_book(book_id, book):
    """Replace one book with PUT; the id is a URL path segment."""
    url = f"{API_URL.rstrip('/')}/{book_id}"
    response = requests.put(url, json=book, timeout=TIMEOUT_SECONDS)
    response.raise_for_status()
    updated_book = response.json()
    print("PUT response:", updated_book)
    print("Status code:", response.status_code)
    return updated_book


def delete_book(book_id):
    """Delete a book, then confirm a GET for that id returns an HTTP error."""
    url = f"{API_URL.rstrip('/')}/{book_id}"
    response = requests.delete(url, timeout=TIMEOUT_SECONDS)
    response.raise_for_status()
    print("DELETE status code:", response.status_code)

    check_response = requests.get(url, timeout=TIMEOUT_SECONDS)
    try:
        check_response.raise_for_status()
    except requests.exceptions.HTTPError as error:
        print(f"Confirmed deleted: GET {url} returned HTTP {check_response.status_code} ({error})")
        return check_response.status_code

    raise RuntimeError(
        f"Expected GET {url} to fail after deletion, but it returned HTTP {check_response.status_code}."
    )


def run_all_operations():
    """Run GET, POST, PUT, and DELETE in sequence against the demo data."""
    if API_URL == "PASTE_BOOKS_RESOURCE_API_URL_HERE":
        raise ValueError("Set API_URL to your MockAPI books resource URL before running this script.")

    get_books()
    add_book({"id": "6", "title": "The Hobbit", "author": "J.R.R. Tolkien", "rating": "9"})
    update_book(
        "2",
        {"id": "2", "title": "The Four Agreements", "author": "Don Miguel Ruiz", "rating": "8"},
    )
    delete_book("5")


if __name__ == "__main__":
    run_all_operations()
