class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = title
        
        author._articles.append(self)
        magazine._articles.append(self)
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) and 5 <= len(value) <= 50:
            raise TypeError("title must be of type str between 5 and 50 characters")
    
        if hasattr(self, 'title'):
            raise AttributeError('Cannot modify title')
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError('Author must be an instance of the Author class')
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise TypeError('Magazine must be an instance of the Magazine class')
        self._magazine = value
        
class Author:
    all = []

    def __init__(self, name):
        self.name = name
        self._articles = []
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError('Name must be a non-empty string')
        if hasattr(self, '_name'):
            raise Exception('Cannot modify name')
        self._name = value
    
    def articles(self):
        return self._articles

    def magazines(self):
        return list(set([article.magazine for article in self._articles]))
   
    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self._articles: 
            return None
        return list(set([article.magazine.category for article in self._articles]))

class Magazine:
    all = []

    def __init__(self, name, category):
        self._name = name
        self.category = category
        self._articles = []
        self._contributors = []
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) and 2 <= len(value) <= 16:
            raise TypeError("name must be a string between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise TypeError('Category must be a string')
        if hasattr(self, '_category'):
            raise Exception('Cannot modify category')
        self._category = value

    def articles(self):
        if not self._articles:
            return None
        else:
            return self._articles

    def contributors(self, author):
        if not self._articles:
            return None
        return [article.author for article in self._articles if article.author == author]
    
    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self, author):
        if not self._contributors:
            return None
        self._contributors.append(author)
        return [contributor for contributor in self._contributors if contributor == author]
