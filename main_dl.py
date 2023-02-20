import locale
from pytube import Search
from pytube import YouTube  
from pytube import Channel

locale.setlocale(locale.LC_NUMERIC, 'fr_FR.UTF-8')

#https://www.youtube.com/watch?v=xo8CrpjC6t0
#https://www.youtube.com/watch?v=sLdH-S6Eubs
#https://www.youtube.com/channel/UCrQjCrWOS63rBxO15TA5CfQ

SAVE_PATH = "C:\\Users\\POEC-REN-09\\Desktop\\Downloader YT\\path"

print("[[YOUTUBE DOWNLOADER]]\n")

choice = input("1: Télécharger une video.\n"+
               "2: Télécharger seulement l'audio\n"+
               "3: Télécharger toute une chaine\n"+
               "4: Chercher une video\n")


####----1----####
if choice == "1":
    link = input("Lien de la vidéo:\n\n")

    yt = YouTube(link)
    vue = "{:n}".format(yt.views)
    print(f"\nAuteur: {yt.author}\n"
          f"Titre: {yt.title}\n"+
          f"Longueur: {yt.length} secondes\n"+
          f"Publiée le: {yt.publish_date}\n"+
          f"Vues : {vue}\n")
    
    
    choice2 = input("\n1: Valider\n"+
                    "2: Quitter\n\n")
    ####----1----####
    if choice2 == "1":
        stream = yt.streams.filter(progressive=True).first()
        stream.download(output_path=SAVE_PATH)
        
        print("Teléchargement effectué.")
    ####----2----####
    if choice2 == "2":
        print("Téléchargement annulé.")
        
        

####----2----####
if choice == "2":
    link = input("Lien de la vidéo:\n")
    
    yt = YouTube(link)
    print(f"\nAuteur: {yt.author}\n"
          f"Titre: {yt.title}\n"+
          f"Longueur: {yt.length} secondes\n"+
          f"Publiée le: {yt.publish_date}")
    
    choice2 = input("\n1: Valider\n"+
                    "2: Quitter\n\n")
    ####----1----####
    if choice2 == "1":
        stream = yt.streams.filter(only_audio=True).first()
        stream.download(output_path=SAVE_PATH)
        
        print("Teléchargement effectué.")
    ####----2----####
    if choice2 == "2":
        print("Téléchargement annulé.")
        
        
####----3----###
if choice == "3":
    increm = 1
    chan = input("Lien de la chaine:\n")
    chanvid = chan + "/videos"
    
    c = Channel(chan)
    print(f"Downloading videos by: {c.channel_name}\n"+
          f"On URL: {c.channel_id}"+
          f"Video: {c.videos_url}")
    
    
    for videos in c.videos:
        print(increm)
        increm = increm + 1
    # for video in c.videos:
    #     print(increm)
    #     increm = increm + 1
        
    
    
    # link = input("Lien de la chaine:\n") 
    # channel = Channel(link)
    # print(increm)
    # for videos in channel:
    #     print(increm)
    #     increm = increm + 1
    
if choice == "4":
    search = input("Recherche:")
    increm = 1
    s = Search(search)
    # resultlen = len(s.results)
    s.results[:19]
    
    for element in s.results:
        yt = element
        author = yt.author
        title = yt.title
        increm = increm + 1
        
        
        print(f"{increm}:"
               f"Auteur: {author}  "+
               f"Titre: {title}\n")
        
    choice = input ("Choix?\n"+
                    "0: Quitter")
            
    match choice:
            case "0":
                pass
            
            case "1":            
                element = s.results[1]  
                stream = element.id
                
                stream.download(SAVE_PATH)
                
            case "2":
                pass
                
            case "4":
                pass
                
            case "5":
                pass
                
            case "5":
                pass
                
            case "6":
                pass
                
            case "7":
                pass
                
            case "8":
                pass
                
            case "9":
                pass
                
            case "11":
                pass
                
            case "12":
                pass
                
            case "13":
                pass
                
            case "14":
                pass
                
            case "15":
                pass
                
            case "16":
                pass
                
            case "17":
              pass
                
            case "18":
                pass
            
            case "19":
                pass
            
            case "20":
                pass
        
        
    
    
        
   
    
    



  

