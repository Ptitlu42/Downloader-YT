import locale
from pytube import Search
from pytube import YouTube  
from pytube import Channel

locale.setlocale(locale.LC_NUMERIC, 'fr_FR.UTF-8')

#https://www.youtube.com/watch?v=xo8CrpjC6t0
#https://www.youtube.com/watch?v=sLdH-S6Eubs
#https://www.youtube.com/channel/UCrQjCrWOS63rBxO15TA5CfQ

SAVE_PATH = "C:\\Users\\POEC-REN-09\\Desktop\\Downloader YT\\path"

####----REFACTOR----####
def id_to_url(element):
    print(element)
    element = str(element)
    element = element[-12:]                
    element = element[0:11]                            
    element = "http://youtube.com/watch?v=" + element
    return element

def url_to_dl(SAVE_PATH, yt, element):
    
    stream = YouTube(element)
    stream = stream.streams.filter(only_audio=True).first()
    stream.download(output_path=SAVE_PATH)

####----SCRIPT----####
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
    
    
if choice == "4":
    search = input("Recherche:\n\n")
    increm = 1
    s = Search(search)
    # resultlen = len(s.results)
    results = s.results[:20]
    
    for element in results:
        yt = element
        author = yt.author
        title = yt.title
        increm = increm + 1
        
        
        print(f"{increm}:"
               f"Auteur: {author}  "+
               f"Titre: {title}\n")
        
    choice = input ("N: Choix?\n"+
                    "0: Quitter")
            
    match choice:
            case "0":
                pass
            
            case "1":         
                choice = int(choice) - 2
                element = results[int(choice)]       
                element = id_to_url(element)
                yt = YouTube(element)
                
                url_to_dl(SAVE_PATH, yt, element)
                print(f"Téléchargement de {yt.author}"+
                      f"  {yt.title}   réussi.")
                
                
            case "2":
                
                choice = int(choice) - 2
                element = results[int(choice)]       
                element = id_to_url(element)
                yt = YouTube(element)
                
                url_to_dl(SAVE_PATH, yt, element)
                print(f"Téléchargement de {yt.author}"+
                      f"  {yt.title}   réussi.")
                
                
            case "4":
                
                choice = int(choice) - 2
                element = results[int(choice)]       
                element = id_to_url(element)
                yt = YouTube(element)
                
                url_to_dl(SAVE_PATH, yt, element)
                print(f"Téléchargement de {yt.author}"+
                      f"  {yt.title}   réussi.")
                
            case "5":
                
                choice = int(choice) - 2
                element = results[int(choice)]       
                element = id_to_url(element)
                yt = YouTube(element)
                
                url_to_dl(SAVE_PATH, yt, element)
                print(f"Téléchargement de {yt.author}"+
                      f"  {yt.title}   réussi.")
                
            case "5":
                
                choice = int(choice) - 2
                element = results[int(choice)]       
                element = id_to_url(element)
                yt = YouTube(element)
                
                url_to_dl(SAVE_PATH, yt, element)
                print(f"Téléchargement de {yt.author}"+
                      f"  {yt.title}   réussi.")
                
            case "6":
                
                choice = int(choice) - 2
                element = results[int(choice)]       
                element = id_to_url(element)
                yt = YouTube(element)
                
                url_to_dl(SAVE_PATH, yt, element)
                print(f"Téléchargement de {yt.author}"+
                      f"  {yt.title}   réussi.")
                
            case "7":
                
                choice = int(choice) - 2
                element = results[int(choice)]       
                element = id_to_url(element)
                yt = YouTube(element)
                
                url_to_dl(SAVE_PATH, yt, element)
                print(f"Téléchargement de {yt.author}"+
                      f"  {yt.title}   réussi.")
                
            case "8":
               
                choice = int(choice) - 2
                element = results[int(choice)]       
                element = id_to_url(element)
                yt = YouTube(element)
                
                url_to_dl(SAVE_PATH, yt, element)
                print(f"Téléchargement de {yt.author}"+
                      f"  {yt.title}   réussi.")
                
                
            case "9":
                
                choice = int(choice) - 2
                element = results[int(choice)]       
                element = id_to_url(element)
                yt = YouTube(element)
                
                url_to_dl(SAVE_PATH, yt, element)
                print(f"Téléchargement de {yt.author}"+
                      f"  {yt.title}   réussi.")
                
            case "11":
                
                choice = int(choice) - 2
                element = results[int(choice)]       
                element = id_to_url(element)
                yt = YouTube(element)
                
                url_to_dl(SAVE_PATH, yt, element)
                print(f"Téléchargement de {yt.author}"+
                      f"  {yt.title}   réussi.")
                
            case "12":
                
                choice = int(choice) - 2
                element = results[int(choice)]       
                element = id_to_url(element)
                yt = YouTube(element)
                
                url_to_dl(SAVE_PATH, yt, element)
                print(f"Téléchargement de {yt.author}"+
                      f"  {yt.title}   réussi.")
                
            case "13":
                
                choice = int(choice) - 2
                element = results[int(choice)]       
                element = id_to_url(element)
                yt = YouTube(element)
                
                url_to_dl(SAVE_PATH, yt, element)
                print(f"Téléchargement de {yt.author}"+
                      f"  {yt.title}   réussi.")
                
            case "14":
                
                choice = int(choice) - 2
                element = results[int(choice)]       
                element = id_to_url(element)
                yt = YouTube(element)
                
                url_to_dl(SAVE_PATH, yt, element)
                print(f"Téléchargement de {yt.author}"+
                      f"  {yt.title}   réussi.")
                
            case "15":
                
                choice = int(choice) - 2
                element = results[int(choice)]       
                element = id_to_url(element)
                yt = YouTube(element)
                
                url_to_dl(SAVE_PATH, yt, element)
                print(f"Téléchargement de {yt.author}"+
                      f"  {yt.title}   réussi.")
                
            case "16":
                
                choice = int(choice) - 2
                element = results[int(choice)]       
                element = id_to_url(element)
                yt = YouTube(element)
                
                url_to_dl(SAVE_PATH, yt, element)
                print(f"Téléchargement de {yt.author}"+
                      f"  {yt.title}   réussi.")
                
            case "17":
                
                choice = int(choice) - 2
                element = results[int(choice)]       
                element = id_to_url(element)
                yt = YouTube(element)
                
                url_to_dl(SAVE_PATH, yt, element)
                print(f"Téléchargement de {yt.author}"+
                      f"  {yt.title}   réussi.")
                
            case "18":
                
                choice = int(choice) - 2
                element = results[int(choice)]       
                element = id_to_url(element)
                yt = YouTube(element)
                
                url_to_dl(SAVE_PATH, yt, element)
                print(f"Téléchargement de {yt.author}"+
                      f"  {yt.title}   réussi.")
            
            case "19":
                
                choice = int(choice) - 2
                element = results[int(choice)]       
                element = id_to_url(element)
                yt = YouTube(element)
                
                url_to_dl(SAVE_PATH, yt, element)
                print(f"Téléchargement de {yt.author}"+
                      f"  {yt.title}   réussi.")
            
            case "20":
                
                choice = int(choice) - 2
                element = results[int(choice)]       
                element = id_to_url(element)
                yt = YouTube(element)
                
                url_to_dl(SAVE_PATH, yt, element)
                print(f"Téléchargement de {yt.author}"+
                      f"  {yt.title}   réussi.")
            

        

    
    
        
   
    
    



  

