from users_manager import UsersManager

SHEETY_POST_ENDPOINT = 'https://api.sheety.co/760117026c88bf95a4871f82d651707f/flightDeals/users'
SHEETY_BEARER_TOKEN = 'si74rmcsfhnov82dynovc7sy4fc893oy487fny7'

UM = UsersManager(endpoint=SHEETY_POST_ENDPOINT, token=SHEETY_BEARER_TOKEN)
UM.signup_user()
