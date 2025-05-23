# class FaceBook:
#     def sharing_post(self):
#         print('Sharing Post from FaceBook')

# class Instagram:
#     def sharing_post(self):
#         print('Sharing Post from Instagram')

# class Twitter:
#     def sharing_post(self):
#         print('Sharing Post from Twitter')

# fc = FaceBook()

# Insta = Instagram()

# x = Twitter()

# social_media = [fc,Insta,x]

# for  media in social_media:
#     media.sharing_post()



class Facebook:
    def share_post(self):
        print("Sharing post on Facebook...")


class Instagram:
    def share_post(self):
        print("Sharing post on Instagram...")


class Twitter:
    def share_post(self):
        print("Sharing post on Twitter...")


# Creating objects of each class
fb = Facebook()
insta = Instagram()
tw = Twitter()

# Putting all objects into a list
social_media = [fb, insta, tw]

# Looping through each and calling the method
for app in social_media:
    app.share_post()
