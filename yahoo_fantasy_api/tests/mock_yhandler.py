#!/bin/python

import json
import os


class YHandler:
    """A mocking class to return pre-canned JSON response for the various APIs

    This is used for testing purposes as we can avoid calling out to the Yahoo!
    service.
    """

    def get_teams_raw(self):
        """Return the raw JSON when requesting the logged in players teams.

        :return: JSON document of the request.
        """
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(dir_path + "/sample.league_teams.json", "r") as f:
            return json.load(f)

    def get_standings_raw(self, league_id):
        """Return the raw JSON when requesting standings for a league.

        :param league_id: League ID to get the standings for
        :type league_id: str
        :return: JSON document of the request.
        """
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(dir_path + "/sample.standings.json", "r") as f:
            return json.load(f)

    def get_settings_raw(self, league_id):
        """Return the raw JSON when requesting settings for a league.

        :param league_id: League ID to get the standings for
        :type league_id: str
        :return: JSON document of the request.
        """
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(dir_path + "/sample.league_settings.json", "r") as f:
            return json.load(f)

    def get_matchup_raw(self, team_key, week):
        """Return the raw JSON when requesting match-ups for a team

        :param team_key: Team key identifier to find the matchups for
        :type team_key: str
        :param week: What week number to request the matchup for?
        :type week: int
        :return: JSON of the request
        """
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(dir_path + "/sample.matchup.json", "r") as f:
            return json.load(f)

    def get_roster_raw(self, team_key, week):
        """Return the raw JSON when requesting a team's roster

        :param team_key: Team key identifier to find the matchups for
        :type team_key: str
        :param week: What week number to request the matchup for?
        :type week: int
        :return: JSON of the request
        """
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(dir_path + "/sample.team_roster.json", "r") as f:
            return json.load(f)
