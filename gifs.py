import giphy_client
from giphy_client.rest import ApiException
from pprint import pprint
import random
from bot import read_token
#api instance

api_instance = giphy_client.DefaultApi()
giphyTokenKey = read_token(1)

async def search_gif(query):
    try:
        response = api_instance.gifs_search_get(giphyTokenKey, query, limit=3, rating='g')
        lst = list(response.data)
        gif = random.choices(lst)
        
        return gif[0].url

    except ApiException as e:
        return "Exception when calling DefaultApi->gifs_search_get: %s\n" % e