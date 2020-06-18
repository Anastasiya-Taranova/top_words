from func import top_words, url_from_file, text_from_url

urls = url_from_file()
number_of_top_words = 5

for url in urls:
    text = text_from_url(url)
    top = top_words(text, number_of_top_words)
