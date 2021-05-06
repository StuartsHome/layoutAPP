from newspaper import Article

def main():
    url = 'https://www.bbc.co.uk/news/uk-57011376'
    article = Article(url)
    # print(article)
    article.download()
    print(article.html)
if __name__ == '__main__':
    main()