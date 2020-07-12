class Mood:
    def decision(self, events):
        self.country_cases = events.country_cases
        self.world_cases = events.world_cases
        self.country_name = events.country_name

        if self.country_name in ["Japan", "Brazil"]:
            self._make_world_mood(150000, 200000)
            self._make_country_mood(300)
        else:
            self._make_world_mood(100000, 150000)
            self._make_country_mood(100)

    def _make_world_mood(self, low, high):
        if self.world_cases >= high:
            self.covid_mood_globally = "Highly Dangerous"
        elif self.world_cases >= low:
            self.covid_mood_globally = "Dangerous"
        else:
            self.covid_mood_globally = "Safe"

    def _make_country_mood(self, high):
        if self.country_cases >= high:
            self.covid_mood_in_country = "Dangerous"
        else:
            self.covid_mood_in_country = "Safe"
