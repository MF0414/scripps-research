import json
import codecs




if __name__ == '__main__':



#ID Extraction
   id_tuples = []

   with open("follower_ids.txt") as f:
      content = f.readlines()
   content = [x.strip() for x in content]

   for item in content:
      id_tuples.append(item.split(','))

#Build Friendship Adjacency List
    
   id_tuples.remove(["user","id"]) #Remove header
   n = len(id_tuples)
   followers = []
   new_net = {}
   
   for item in id_tuples:
      followers.append(item[0])
      

   files = ['A1','A','B','C','D','E','F','G','H','I','J','L']
#Store Network Adjacency Dictionary into File

   for f in files:
      print("Getting Dictionary " + f + '\n')
      input_file = file(f+'.json','r')
      network = json.loads(input_file.read().decode('utf-8-sig'))
      for user in network:
         #print("next user")
         temp = []
         for follower in network[user]:
            if str(follower) in followers:
               temp.append(follower)
         new_net[user] = temp
         

   with open('GVSU_Twitter_Network.json','w') as o:
      json.dump(new_net,o)

   

   


   
