from pages.Searchpage import SearchPage



def test_search(logged_in_page):
    search = SearchPage(logged_in_page)
    search.search_amazon("Laptop")
    search.click_first_result()
    