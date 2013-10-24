import facebook
from auth import oauth_access_token 

def get_oauth_access_token(client_id,client_secret):
    payload={'client_id':client_id,'client_secret':client_secret,'grant_type':'client_credentials'}
    r=requests.post('https://graph.facebook.com/oauth/access_token', params=payload)
    return r.text

def init_graph_api(oauth_access_token):
    return facebook.GraphAPI(oauth_access_token)

def get_friends_network(): 
    graph=init_graph_api(oauth_access_token)
    friends = graph.get_connections("me", "friends")['data']
    for friend in friends:
        mutualfriends=graph.get_connections("me/mutualfriends",friend['id'])['data']
        friend['mutual']=mutualfriends
    return friends
