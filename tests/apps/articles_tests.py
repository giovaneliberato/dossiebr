#coding: utf-8
from base import GAETestCase
from gaepermission.model import MainUser
from mommygae import mommy

from articles import core, models


class CoreTest(GAETestCase):
    def test_find_or_create_article(self):
        """
        Asserts that there's only one DB registry for each url.
        """
        article_url = 'http://www.exemple.com/1'
        core.find_or_create_article(article_url)
        self.assertEquals(1, models.Article.query().count())

        core.find_or_create_article(article_url)
        self.assertEquals(1, models.Article.query().count())

        core.find_or_create_article(article_url + "/2")
        self.assertEquals(2, models.Article.query().count())

    def test_tag_article(self):
        user = mommy.save_one(MainUser)
        article = mommy.save_one(models.Article)
        tags = ['#communism_rules', '#SP']
        mentions = ['@Eneas', 'Plínio']

        core.tag_article(user, article, tags, [])
        self.assertEquals(2, models.Tag.query().count())

        core.tag_article(user, article, [], mentions)
        self.assertEquals(2, models.Mention.query().count())

        self.assertTrue(2, article.find_tags().count())
        self.assertTrue(2, article.find_mentions().count())

    def test_get_tag_or_mention_by_prefix(self):
        mommy.save_one(models.Tag, name='#tag1')
        mommy.save_one(models.Tag, name='#tag2')

        found_tags = core.find_tags_by_prefix('#tag')
        self.assertEquals(2, found_tags.count())

        found_tags = core.find_tags_by_prefix('#tag1')
        self.assertEquals(1, found_tags.count())

    def test_search_articles(self):
        user = mommy.save_one(MainUser)
        article1 = mommy.save_one(models.Article, url="www.articles.com/1")
        article2 = mommy.save_one(models.Article, url="www.articles.com/2")

        models.Tag(name="#tag1", origin=user, destination=article1).put()
        models.Tag(name="#tag2", origin=user, destination=article2).put()
        models.Mention(name="@ghandi", origin=user, destination=article1).put()
        models.Mention(name="@ghandi", origin=user, destination=article2).put()

        articles = core.search_articles("#tag")
        self.assertEquals(2, len(articles))

        articles = core.search_articles("#tag1")
        self.assertEquals(1, len(articles))

        articles = core.search_articles("#tag2")
        self.assertEquals(1, len(articles))

        articles = core.search_articles("@ghandi")
        self.assertEquals(2, len(articles))
