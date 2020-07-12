class Events:
    def __init__(self):
        pass

    def event_process(self, country_data, world_data):
        self.country_cases = country_data["Confirmed"]
        self.country_name = country_data["Country"]
        self.world_cases = world_data["TotalConfirmed"]
