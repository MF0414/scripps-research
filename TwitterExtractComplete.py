from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import time
import json

#Graph Class------------------------------------------------------------------#

class Graph(object):
   def __init__(self, graph_dict = None):
      if graph_dict == None:
         graph_dict = {}
      self.__graph_dict = graph_dict
    
   def dictionary(self):
      return self.__graph_dict

   def vertices(self):
      return list(self.__graph_dict.keys())

   def edges(self):
      return self.processEdges()
      
   def processEdges(self):
      edges = []
      for vertex in self.__graph_dict:
         for neighbor in self.__graph_dict[vertex]:
            if {neighbor, vertex} not in edges:
               edges.append({vertex,neighbor})
      return edges

   def degrees(self):
      degrees=[]
      vertices = self.vertices()
      for i in range(len(vertices)):
         degree = 0
         for edge in self.edges():
            if vertices[i] == list(edge)[0] or vertices[i] == list(edge)[1]:
               degree = degree + 1
         degrees.append(degree)
      return degrees

   def isConnected(self):
      this_graph = self.__graph_dict
      vertices = self.vertices()
      first_vertex = vertices[0]
      check = {vertex: 'no' for vertex in vertices}
      checkList = [first_vertex]
      while len(checkList) != 0:
         viewed_vertex = checkList.pop()
         for vertex in this_graph[viewed_vertex]:
            if check[vertex] == 'no':
               check[vertex] = 'yes'
               checkList.append(vertex)
         check[viewed_vertex] = 'flag' 

      return list(check.values()).count('flag') == len(this_graph)


#Methods for File Creation-----------------------------------------------#

def createJS(id_list):
   #Create JS Array of IDS
   JS_FILE = open('ids.js', "w")
   #print(len(ids))
   JS_FILE.write("var ids = [")

   for i in range(len(ids)):
      user = str(ids[i])
      if (i == 0):
         JS_FILE.write(user)
      else:
         JS_FILE.write("," + user)
   JS_FILE.write("];")
   JS_FILE.close()

def createJSON(dictionary):
   return 0

def extract_friendship(friend_object):
   if "followed_by=True" in str(friend_object[1]):
      return True
   else:
      return False



#MAIN-------------------------------------------------------------------#

if __name__ == '__main__':
   
   #API Setup
   access_token = "1666122888-uSWuz7YnSKiLmnBZ0ccglCColQJzufxaMhAPSU4"
   access_token_secret = "37eLiYE2Zv1KJ386ZSHWZhXSyTpqtyfDKAtzxcklnJjui"
   consumer_key = "cekJqEoqofOPKs3R5jVegGNlJ"
   consumer_secret = "MRSHPhwEf30Y9pKkwIE7eYMuPk3bK6UqaaFCvVR5V8PBVeDvC6"

   auth = OAuthHandler(consumer_key, consumer_secret )
   auth.set_access_token(access_token, access_token_secret)

   api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=3, retry_delay=60)

   #Grab GVSU Followers
   u = api.get_user(screen_name = 'GVSU')
   GVSU_ID = u.id
   i = 0
   ids = []
   page = tweepy.Cursor(api.followers_ids, screen_name='@GVSU').pages()

   run = True
   while run == True:
      try:
    
         #process followers
         ids.extend(page)
         print(str(i))
         if i == 100:  #Comment out after sample.
            run = False
         i = i + 1
      except tweepy.TweepError:
         #pause to avoid rate limit
         time.sleep(60 * 15)
         continue
      except StopIteration:
         break 

   #Create Javascript Array for Visualization
   createJS(ids)

   # Check for friendships    
   g = {}
   for firstID in ids:
      for nextID in ids:
         friends = []
         if extract_friendship(api.show_friendship(target_id=firstID, source_id=nextID)):
            friends.append(nextID)
      g[str(firstID)] = friends

   # Create Network Object
   network = Graph(g)

   #Export to JSON for visualization 
   createJSON(network.dictionary)  
         

