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

        core.tag_article(article, tags, [])
        self.assertEquals(2, models.Tag.query().count())
        self.assertEquals(2, models.ArticleTag.query().count())

        core.tag_article(article, [], mentions)

    def test_get_tag_or_mention_by_prefix(self):
        mommy.save_one(models.Tag, name='#tag1')
        mommy.save_one(models.Tag, name='#tag2')

        found_tags = core.find_tags_by_prefix('#tag')
        self.assertEquals(2, found_tags.count())

        found_tags = core.find_tags_by_prefix('#tag1')
        self.assertEquals(1, found_tags.count())
