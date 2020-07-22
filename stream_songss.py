import requests
import json
import vlc
import sys

data_url = "http://beatsapi.media.jio.com/v2_1/beats-api/jio/src/response/search2/"

def song_search(query):
    new_query = query.replace(' ', '+') + '/'
    raw_data = requests.get(data_url+new_query).json()
    if(raw_data.get('messageCode')==200):
        data_of_best_match = raw_data.get('result').get('data').get('Best Match')
        data_of_other_similar_matches = raw_data.get('result').get('data').get('Songs')
        final_id_of_songs=''
    
        print("'"+data_of_best_match[0].get('title')+"'","by",data_of_best_match[0].get('artist'))
        i=0
        if(int(input("Enter integer 1 if this is the correct song. Else enter any integer "))==1):
            final_id_of_songs=data_of_best_match[0].get('id')
            final_title_of_song = data_of_best_match[0].get('title')
            final_artist_of_song= data_of_best_match[0].get('artist')
        
        else: 
            def other_function_for_other_matches(i):
                if(i<len(data_of_other_similar_matches)):
                    print(" ")
                    print("'"+data_of_other_similar_matches[i].get('title')+"'","by",data_of_other_similar_matches[i].get('artist'))
                    if(int(input("Enter integer 1 if this is the correct song. Else enter any integer "))==1):
                        final_id_of_songs= data_of_other_similar_matches[i].get('id')
                        final_title_of_song = data_of_other_similar_matches[i].get('title')
                        final_artist_of_song= data_of_other_similar_matches[i].get('artist')
                    else:
                        other_function_for_other_matches(i+1)
                else:
                    print("Sorry!! We are not able to process your song. Try searching it again more precisely or maybe there is an error in JIO servers.")
                    sys.exit()
                    
                    
            other_function_for_other_matches(0)
            
        

        return final_id_of_songs
    
    else:
        print("There is some error. Maybe you can try mentioning song more precisely in query")
        sys.exit()

    
    
def streaming_url_of_song(id):
    a = int(input("What quality do you prefer? Enter 1 for HD quality. 2 for good quality and 3 for low quality. If any other entry, song will be played on HD quality by default:"))
    song_bitrate = 320
    if a==1:
        None
    elif a==2:
        song_bitrate = 128
    elif a==3:
        song_bitrate = 64
    else:
        None
    id_elements = id.split('_')
    result_of_stream= "http://jiobeats.cdn.jio.com/mod/_definst_/mp4:hdindiamusic/audiofiles/"+id_elements[0]+"/"+id_elements[1]+"/"+id+"_"+str(song_bitrate)+".mp4/playlist.m3u8"
    return result_of_stream   
       
def final_jio_songs_player():
    a = str(input("Search for the song which you want to play by writing it here: "))

    id_of_a = song_search(a)

    player = vlc.MediaPlayer(streaming_url_of_song(id_of_a))
    print("Playing your desired song.... :)")
    player.play()
    while(True):
        player_by_vlc=str(input("Type 'PAUSE' to pause it or 'PLAY' to resume again or STOP to stop the song or type anything else for a new song: "))
        if(player_by_vlc=='PAUSE'):
            player.pause()
        elif(player_by_vlc=='PLAY'):
            player.play()
        elif(player_by_vlc=='STOP'):
            player.pause()
            player.stop
            print('Use Ctrl+c to stop the player or player will continue to ask for song searches')
            final_jio_songs_player()
        else:
            player.pause()
            player.stop
            final_jio_songs_player()

final_jio_songs_player()
            

    


        
    
