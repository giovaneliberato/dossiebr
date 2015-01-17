from models import Article, Tag, Mention, ArticleTag


def tag_article(article, tags, mentions):
    tags_to_save = []
    for tag_name in tags:
        tags_to_save.append(Tag.find_or_create(tag_name))
    
