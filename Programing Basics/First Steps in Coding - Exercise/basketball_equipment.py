trainin_price_per_year = int(input())

shoes_coast = trainin_price_per_year - (trainin_price_per_year * 0.40)
sport_kit_coast = shoes_coast - (shoes_coast * 0.20)
basketball_ball_coast = sport_kit_coast / 4
accessories_coast = basketball_ball_coast / 5
total_equpment_amaunt = shoes_coast + sport_kit_coast + basketball_ball_coast + \
                        accessories_coast + trainin_price_per_year

print(total_equpment_amaunt)
