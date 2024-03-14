import os
from plemmy import LemmyHttp
from plemmy.responses import GetCommunityResponse
from plemmy.responses import GetPostsResponse
from dotenv import load_dotenv

load_dotenv()
# create object for Lemmy.ml, log in
srv = LemmyHttp("https://lemmy.world")
srv.login(os.getenv("LEMMY_USERNAME"), os.getenv("LEMMY_PASSWORD"))


# obtain community, parse JSON
api_response = srv.get_community(name="politics")
response = GetCommunityResponse(api_response)

# community info
community = response.community_view.community
print(community.name)
print(community.actor_id)
print(community.id)

# list community moderators
for person in response.moderators:
    print(person.moderator.name, person.community.name)

# get top 10 posts from the community
posts_response = srv.get_posts(community_name="politics", limit=10, sort="TopAll")

# parse JSON response
posts = GetPostsResponse(posts_response)

# print the content of the posts
for post in posts.posts:
    print(post.post.name)
    print(post.post.body)