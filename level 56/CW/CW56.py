#დავალება 1
def nugzar_chubinidze(sadgerdzelo, limit):
    if sadgerdzelo > limit:
        return "ლუიზა: ნუგზარი აღარ დალიო მეტი!"
    else:
        return "მოდი ახლა მართლა, დამილოცნინე!"


#დავალება 2
def yuri_gagarini():
    გულის_წნევას = int(input("შეიყვანეთ თქვენი გულის წნევა:"))
    პულსი = int(input("შეიყვანეთ თქვენი პულსი:"))
    if (გულის_წნევას == 120 and პულსი == 80):
        return True
    return False 
print(yuri_gagarini())


#დავალება 3
def captianjack(cois):
    if coins == 0:
        return "ვირთხის დღეში ხარ! ეკიპაჯის აჯანყება"
    elif coins ==150:
        return "დაბალი კლასისი გემი"
    elif coins ==250:
        return "საშვალო კლასისი გემი"
    elif coins ==350:
        return "საუკეთესო კლასისი გემი"
    elif coins > 350:
        return "ზედმეტი არის თანხა ხურდა გეკუთნის"
    else:
        return "ვირთხის დღეში ხარ! ეკიპაჯის აჯანყება"
print() 


#დავალება 4
apples = ["პანტა", "პანტა", "გორული"]
apple = list(set(appleს))
print(apple)

#დავალება 5
