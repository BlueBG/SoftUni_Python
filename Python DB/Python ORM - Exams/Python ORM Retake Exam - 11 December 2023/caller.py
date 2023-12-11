import os

import django
from django.db.models import Count

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import TennisPlayer, Tournament, Match


def get_tennis_players(search_name=None, search_country=None):
    if search_name is not None and search_country is not None:
        players = TennisPlayer.objects.filter(
            full_name__icontains=search_name,
            country__icontains=search_country
        ).order_by('ranking')
    elif search_name is not None:
        players = TennisPlayer.objects.filter(
            full_name__icontains=search_name
        ).order_by('ranking')
    elif search_country is not None:
        players = TennisPlayer.objects.filter(
            country__icontains=search_country
        ).order_by('ranking')
    else:
        return ""

    if players.exists():
        result = "\n".join([
            f"Tennis Player: {player.full_name}, country: {player.country}, ranking: {player.ranking}"
            for player in players
        ])
        return result
    else:
        return ""


def get_top_tennis_player():
    top_player = TennisPlayer.objects.annotate(num_of_wins=Count('matches_won')).order_by('-num_of_wins',
                                                                                          'full_name').first()

    if top_player:
        return f"Top Tennis Player: {top_player.full_name} with {top_player.num_of_wins} wins."
    else:
        return ""


def get_tennis_player_by_matches_count():
    player = TennisPlayer.objects.annotate(num_of_matches=Count('matches_participated')).order_by('-num_of_matches',
                                                                                                  'ranking').first()

    if player and player.num_of_matches > 0:
        return f"Tennis Player: {player.full_name} with {player.num_of_matches} matches played."
    else:
        return ""


def get_tournaments_by_surface_type(surface=None):
    if surface is None:
        return ""

    tournaments = Tournament.objects.filter(surface_type__icontains=surface).order_by('-start_date')

    if tournaments.exists():
        tournament_info = "\n".join([
            f"Tournament: {tournament.name}, start date: {tournament.start_date}, matches: {tournament.matches.count()}"
            for tournament in tournaments
        ])
        return tournament_info
    else:
        return ""


def get_latest_match_info():
    try:
        last_match = Match.objects.all().order_by('-date_played', '-id').first()
    except Match.DoesNotExist:
        return ""

    # player_one = last_match.players.all().first().full_name
    # player_two = last_match.players.all().last().full_name

    match_players = last_match.players.all().order_by('full_name')
    player_one = match_players.all().first().full_name
    player_two = match_players.all().last().full_name

    return (f"Latest match played on: {last_match.date_played}, tournament: {last_match.tournament.name}, score: "
            f"{last_match.score}, players: "
            f"{player_one} vs {player_two}, winner: "
            f"{'TBA' if last_match.winner is None else last_match.winner.full_name}, "
            f"summary: {last_match.summary}")


def get_matches_by_tournament(tournament_name=None):
    if tournament_name is None:
        return "No matches found."
    try:
        tournament = Tournament.objects.get(name=tournament_name)
    except Tournament.DoesNotExist:
        return "No matches found."

    matches = Match.objects.filter(tournament=tournament).order_by('-date_played')

    if not matches.exists():
        return "No matches found."

    result = "\n".join([
        f"Match played on: {match.date_played}, score: {match.score}, "
        f"winner: {'TBA' if match.winner is None else match.winner.full_name}"
        for match in matches
    ])

    return result



