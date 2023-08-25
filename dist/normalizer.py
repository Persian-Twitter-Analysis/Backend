from user.models import User as UserModel

b = UserModel.objects.filter()
for i in b:
    s1 = []
    num_sum = 0
    for j in i.tweets_sentiments.split("#"):
        s1.append(float(j))
        num_sum+= float(j)
    print(s1)
    for j in range(len(s1)):
        s1[j] /= num_sum
        s1[j] = round(s1[j]*100)
        s1[j] = str(s1[j])
    ts = '#'.join(s1)
    UserModel.objects.filter(id=i.id).update(tweets_sentiments=ts)
    print(s1)
    
    s1 = []
    num_sum = 0
    for j in i.images_sentiments.split("#"):
        s1.append(float(j))
        num_sum += float(j)
    print(s1)
    for j in range(len(s1)):
        s1[j] /= num_sum
        s1[j] = round(s1[j]*100)
        s1[j] = str(s1[j])
    ims = '#'.join(s1)
    UserModel.objects.filter(id=i.id).update(images_sentiments=ims)
    print(s1)

    s1 = []
    num_sum = 0
    for j in i.friends_sentiments.split("#"):
        s1.append(float(j))
        num_sum += float(j)
    print(s1)
    for j in range(len(s1)):
        s1[j] /= num_sum
        s1[j] = round(s1[j]*100)
        s1[j] = str(s1[j])
    fs = '#'.join(s1)
    UserModel.objects.filter(id=i.id).update(friends_sentiments=fs)
    print(s1)
