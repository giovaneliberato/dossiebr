#coding: utf-8
from base import GAETestCase
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
        article = mommy.save_one(models.Article)
        tags = ['#communism_rules', '#SP']
        mentions = ['@Eneas', 'Plínio']

        core.tag_article(article, [tags[0]], [])
        self.assertEquals(1, models.Tag.query().count())
        self.assertEquals(1, models.ArticleTag.query().count())

        core.tag_article(article, tags, [])
        self.assertEquals(2, models.Tag.query().count())
        self.assertEquals(3, models.ArticleTag.query().count())

        core.tag_article(article, [], [mentions[0]])
        self.assertEquals(1, models.Mention.query().count())
        self.assertEquals(1, models.ArticleMention.query().count())

        core.tag_article(article, [], mentions)
        self.assertEquals(2, models.Mention.query().count())
        self.assertEquals(3, models.ArticleMention.query().count())
