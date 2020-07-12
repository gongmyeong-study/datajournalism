from corona import Corona

crawler = Corona()

japan_confirmed = crawler.get_confirmed_by_country("Japan")
world_confirmed = crawler.get_confirmed_globally()

print(japan_confirmed)
print(world_confirmed)
