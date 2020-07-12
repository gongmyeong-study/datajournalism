from corona import Corona
from events import Events
from mood import Mood
from article import Article

crawler = Corona()
japan_data = crawler.get_confirmed_by_country("Japan")[-1]
world_data = crawler.get_confirmed_globally()

events = Events()
events.event_process(japan_data, world_data)

mood = Mood()
mood.decision(events)

article = Article(events, mood)
today_covid_article = article.generate()
print(today_covid_article)
